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


class RequiredPaymentsDto(TypedDict):
    # Unique identifier assigned to the Payee.
    payeeGuid: str

    # Amount of the Payment.
    value: typing.Union[int, float]

class OptionalPaymentsDto(TypedDict, total=False):
    # The Payee identifier used by ConnexPay support teams to research issues related to the Payee.
    payeeReferenceToken: str

    # For Payment Widget customers only. This is the identifier that used by ConnexPay support teams to research issues related to the Payment Widget.
    ridReferenceToken: str

    # Unique identifier assigned to the Payment.
    paymentGuid: str

    # Unique identifier assigned when using the Payment Widget.
    ridGuid: str

    # Payment-level description highlighting the reason for this Payment.
    memo: str

    # Additional data field that can be used to provide additional data to the Payee and for your reporting purposes.
    field2: str

    # Additional data field that can be used to provide additional data to the Payee and for your reporting purposes.
    field3: str

    # Additional data field that can be used to provide additional data to the Payee and for your reporting purposes.
    field4: str

    # Additional data field that can be used to provide additional data to the Payee and for your reporting purposes.
    field5: str

class PaymentsDto(RequiredPaymentsDto, OptionalPaymentsDto):
    pass
