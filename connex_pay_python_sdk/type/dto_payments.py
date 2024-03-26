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


class RequiredDtoPayments(TypedDict):
    pass

class OptionalDtoPayments(TypedDict, total=False):
    paymentGuid: str

    # Identifier needed by ConnexPay support teams to research Payment issues.
    paymentReferenceToken: str

    # Payee identifier needed by ConnexPay support teams to research Payee issues.
    payeeReferenceToken: str

    # For Payment Widget customers only. Identifier needed by ConnexPay support teams to research issues related to the Payment Widget.
    ridReferenceToken: str

    # Payment-level description highlighting the reason for this Payment.
    memo: str

    # Amount of the Payment.
    value: typing.Union[int, float]

    # Status of the Payment.
    status: str

    # Additional data field that can be used to provide additional data to the Payee and for your reporting purposes.
    field2: str

    # Additional data field that can be used to provide additional data to the Payee and for your reporting purposes.
    field3: str

    # Additional data field that can be used to provide additional data to the Payee and for your reporting purposes.
    field4: str

    # Additional data field that can be used to provide additional data to the Payee and for your reporting purposes.
    field5: str

    terminationDate: str

    # The Payee's name.
    payeeName: str

    # Email address the Payment was sent to for the Payee.
    email: str

    # Last four digits of the Payee's card number.
    lastFour: str

    # Postal address line 1 of the Payee. Alphanumerics and [,.-'] are allowed.
    address1: str

    # Postal address line 2 of the Payee. Alphanumerics and [,.-'] are allowed.
    address2: str

    # Postal address city of the Payee.
    city: str

    # Postal address state for the Payee.
    state: str

    # Postal code for the Payee.
    zipCode: str

    # Postal address country for the Payee.
    country: str

    createdBy: str

class DtoPayments(RequiredDtoPayments, OptionalDtoPayments):
    pass
