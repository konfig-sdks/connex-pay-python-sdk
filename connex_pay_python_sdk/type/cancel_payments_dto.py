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

from connex_pay_python_sdk.type.cancel_payments_dto_payments import CancelPaymentsDtoPayments

class RequiredCancelPaymentsDto(TypedDict):
    # Application-level value that indicates a Payout is being requested for client's account. Value provided by ConnexPay.
    merchantGuid: str

    payments: CancelPaymentsDtoPayments

class OptionalCancelPaymentsDto(TypedDict, total=False):
    pass

class CancelPaymentsDto(RequiredCancelPaymentsDto, OptionalCancelPaymentsDto):
    pass
