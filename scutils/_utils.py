"""Utility functionality used by the scutils package."""

import datetime
import re

from bs4 import Tag
from dateutil.parser import parse as dt_parse
from dateutil.parser import parserinfo


class _GermanParserInfo(parserinfo):
    """Parser info with support for German months and weekdays."""

    MONTHS = [
        ("Jan", "January", "Januar"),
        ("Feb", "February", "Februar"),
        ("Mar", "March", "März", "Mär"),
        ("Apr", "April"),
        ("May", "May", "Mai"),
        ("Jun", "June", "Juni"),
        ("Jul", "July", "Juli"),
        ("Aug", "August"),
        ("Sep", "Sept", "September"),
        ("Oct", "October", "Oktober", "Okt"),
        ("Nov", "November"),
        ("Dec", "December", "Dezember", "Dez"),
    ]

    WEEKDAYS = [
        ("Mon", "Monday", "Montag", "Mo"),
        ("Tue", "Tuesday", "Dienstag", "Di"),
        ("Wed", "Wednesday", "Mittwoch", "Mi"),
        ("Thu", "Thursday", "Donnerstag", "Do"),
        ("Fri", "Friday", "Freitag", "Fr"),
        ("Sat", "Saturday", "Samstag", "Sa"),
        ("Sun", "Sunday", "Sonntag", "So"),
    ]


GERMAN_PARSER_INFO = _GermanParserInfo()
LINK_OR_LIST_ITEM_PATTERN = re.compile(r"link|listitem")


def extract_date(tag: Tag) -> datetime.date:
    """Extract the date from a tag."""
    return dt_parse(tag.text, fuzzy=True, parserinfo=GERMAN_PARSER_INFO).date()


def convert_number_separators(text: str) -> str:
    """Convert the number separators in a string to the standard format."""
    return text.replace(".", "").replace(",", ".")
