"""A package that provides functionality to parse and process the page
https://scalable.capital/transactions. """

__all__ = (
    "parse_html_transactions",
    "sort_transactions_by_type",
    "Transaction",
    "value_per_transaction_type",
)

from ._parse import Transaction, parse_html_transactions
from ._process import sort_transactions_by_type, value_per_transaction_type
