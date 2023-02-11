"""This module contains functionality to parse the transactions from ScalableCapital."""
import datetime
from collections.abc import Sequence
from pathlib import Path
from typing import NamedTuple

from bs4 import BeautifulSoup, Tag

from scutils._utils import LINK_OR_LIST_ITEM_PATTERN, convert_number_separators, extract_date


class Transaction(NamedTuple):
    """A single transaction.

    Attributes:
        date: The date of the transaction.
        type: The type of the transaction.
        description: The description of the transaction.
        amount: The amount of the transaction, i.e. the number of shares bought/sold.
        value: The value of the transaction, i.e. the value of the shares bought/sold. Value is
          given in the currency of the account.
    """

    date: datetime.date
    type: str
    description: str
    amount: float | None
    value: float


def _get_table_root(soup: BeautifulSoup) -> Tag:
    table_root = None
    for element in soup.find_all(name="div", class_="MuiGrid-root", recursive=True):
        if element.find_all(name="div", class_="jss373"):
            for elemen in element.find_all(
                name="div", class_="infinite-scroll-component__outerdiv"
            ):
                for eleme in elemen.find_all(name="div", class_="infinite-scroll-component"):
                    table_root = eleme
                    break

    if table_root is None:
        raise RuntimeError("Could not find table root")

    return table_root


def parse_html_transactions(file_path: str | Path) -> Sequence[Transaction]:
    """Parse the html file and return a sequence of transactions.

    Args:
        file_path: The path to an html file created by saving the page
            https://scalable.capital/transactions (after scrolling down to
            load all transactions).

    Returns:
        A sequence of transactions.
    """
    soup = BeautifulSoup(Path(file_path).read_text(encoding="utf-8"), "html5lib")

    current_date: datetime.date | None = None
    transactions = []
    for child in _get_table_root(soup).children:
        if "jss376" in child.attrs["class"]:
            current_date = extract_date(next(child.children))
        elif "jss378" in child.attrs["class"]:
            type_tags = child.find_all(name="div", class_="jss383", role="listitem")
            assert len(type_tags) == 1, "Unable to parse table row"
            type_ = type_tags[0].text

            description_tags = child.find_all(
                name="div", class_="jss384", role=LINK_OR_LIST_ITEM_PATTERN
            )
            assert len(description_tags) == 1, "Unable to parse table row"
            description = description_tags[0].text

            amount_tags = child.find_all(name="div", class_="jss386", role="listitem")
            assert len(amount_tags) == 1, "Unable to parse table row"
            if not amount_tags[0].text:
                amount = None
            else:
                amount = float(
                    convert_number_separators(amount_tags[0].text.replace(" Stk.", "").strip())
                )

            value_tags = child.find_all(name="div", class_="jss387", role="listitem")
            assert len(value_tags) == 1, "Unable to parse table row"
            value = float(convert_number_separators(value_tags[0].text.replace("€", "").strip()))

            if current_date is None:
                raise RuntimeError("Don't have a date for this transaction")
            transaction = Transaction(
                date=current_date,
                type=type_,
                description=description,
                amount=amount,
                value=value,
            )
            transactions.append(transaction)

    return transactions
