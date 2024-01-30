"""This module contains functionality to process the transactions parsed from ScalableCapital."""

from collections.abc import Mapping, Sequence

from scutils._parse import Transaction


def sort_transactions_by_type(
    transactions: Sequence[Transaction],
) -> Mapping[str, Sequence[Transaction]]:
    """Sort the transactions by type.

    Args:
        transactions: A sequence of transactions.

    Returns:
        A dictionary mapping transaction types to sequences of transactions.
    """
    transactions_by_type: dict[str, list[Transaction]] = {}
    for transaction in transactions:
        if transaction.type not in transactions_by_type:
            transactions_by_type[transaction.type] = []
        transactions_by_type[transaction.type].append(transaction)
    return transactions_by_type


def value_per_transaction_type(transactions: Sequence[Transaction]) -> dict[str, float]:
    """Calculate total the value per transaction type.

    Args:
        transactions: A sequence of transactions.

    Returns:
        A dictionary mapping transaction types to the total value of the
        transactions of that type.
    """
    transactions_by_type = sort_transactions_by_type(transactions)
    value_per_type = {
        transaction_type: sum(transaction.value for transaction in transactions)
        for transaction_type, transactions in transactions_by_type.items()
    }
    return value_per_type
