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


class RequiredFundingTransferMerchantCashBalanceResponse(TypedDict):
    pass

class OptionalFundingTransferMerchantCashBalanceResponse(TypedDict, total=False):
    TransferredFrom: str

    TransferredTo: str

    Amount: int

class FundingTransferMerchantCashBalanceResponse(RequiredFundingTransferMerchantCashBalanceResponse, OptionalFundingTransferMerchantCashBalanceResponse):
    pass
