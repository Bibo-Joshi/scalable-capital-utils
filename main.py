"""Example script that showcases how to use the `scutils` package."""

from pprint import pprint

from scutils import parse_html_transactions, sort_transactions_by_type, value_per_transaction_type

if __name__ == "__main__":
    transactions = parse_html_transactions("html_page/Broker _ Scalable Capital.html")
    pprint(sort_transactions_by_type(transactions), compact=False)
    pprint(value_per_transaction_type(transactions), compact=False)
