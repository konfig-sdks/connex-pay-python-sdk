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


class RequiredCardCancelVirtualCardResponseCard(TypedDict):
    pass

class OptionalCardCancelVirtualCardResponseCard(TypedDict, total=False):
    cardGuid: str

    amountLimit: typing.Union[int, float]

    usageLimit: int

    limitWindow: str

    expirationDate: str

    expiration: str

    firstSix: str

    lastFour: str

    nameLine1: str

    nameLine2: str

    status: str

    cardType: str

class CardCancelVirtualCardResponseCard(RequiredCardCancelVirtualCardResponseCard, OptionalCardCancelVirtualCardResponseCard):
    pass
