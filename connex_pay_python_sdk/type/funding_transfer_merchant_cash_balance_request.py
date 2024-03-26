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


class RequiredFundingTransferMerchantCashBalanceRequest(TypedDict):
    # The merchant's GUID of the withdrawn account. Value provided by ConnexPay.
    TransferredFrom: str

    # The merchant's GUID of the deposited account. Value provided by ConnexPay.
    TransferredTo: str

    # Transferred funding amount that will be processed. Maximum transaction and daily funding limits are set by ConnexPay.
    Amount: typing.Union[int, float]

class OptionalFundingTransferMerchantCashBalanceRequest(TypedDict, total=False):
    pass

class FundingTransferMerchantCashBalanceRequest(RequiredFundingTransferMerchantCashBalanceRequest, OptionalFundingTransferMerchantCashBalanceRequest):
    pass
