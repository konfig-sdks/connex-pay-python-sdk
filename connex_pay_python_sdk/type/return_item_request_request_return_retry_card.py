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


class RequiredReturnItemRequestRequestReturnRetryCard(TypedDict):
    pass

class OptionalReturnItemRequestRequestReturnRetryCard(TypedDict, total=False):
    # Card number. Must be 16 characters.
    CardNumber: str

    # Cardholder's name
    CardHolderName: str

    # The three or four digit CVV code at the back side of the credit and debit card
    Cvv2: int

    # Card's expiry date in the YYMM format
    ExpirationDate: date

class ReturnItemRequestRequestReturnRetryCard(RequiredReturnItemRequestRequestReturnRetryCard, OptionalReturnItemRequestRequestReturnRetryCard):
    pass
