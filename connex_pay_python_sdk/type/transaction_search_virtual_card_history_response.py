# coding: utf-8

"""
    ConnexPay Reporting API

    REST API for retrieving reporting data. Currently Daily Accounting data only.

    The version of the OpenAPI document: v1
    Created by: https://docs.connexpay.com
"""

from datetime import datetime, date
import typing
from enum import Enum
from typing_extensions import TypedDict, Literal, TYPE_CHECKING

from connex_pay_python_sdk.type.transaction_search_virtual_card_history_response_transactions import TransactionSearchVirtualCardHistoryResponseTransactions

class RequiredTransactionSearchVirtualCardHistoryResponse(TypedDict):
    pass

class OptionalTransactionSearchVirtualCardHistoryResponse(TypedDict, total=False):
    transactions: TransactionSearchVirtualCardHistoryResponseTransactions

class TransactionSearchVirtualCardHistoryResponse(RequiredTransactionSearchVirtualCardHistoryResponse, OptionalTransactionSearchVirtualCardHistoryResponse):
    pass
