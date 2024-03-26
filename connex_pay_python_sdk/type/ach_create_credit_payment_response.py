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


class RequiredAchCreateCreditPaymentResponse(TypedDict):
    pass

class OptionalAchCreateCreditPaymentResponse(TypedDict, total=False):
    description: str

    merchantId: str

    incomingTransactionCode: str

    paymentId: str

    isCredit: bool

    amount: int

    payeeName: str

    paymentStatus: str

    scheduleDate: str

    receiptDate: str

    processingDate: typing.Union[bool, date, datetime, dict, float, int, list, str, None]

class AchCreateCreditPaymentResponse(RequiredAchCreateCreditPaymentResponse, OptionalAchCreateCreditPaymentResponse):
    pass
