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


class RequiredCardGetDetailResponse(TypedDict):
    pass

class OptionalCardGetDetailResponse(TypedDict, total=False):
    cardGuid: str

    expirationDate: str

    expiration: str

    terminateDate: str

    currencyCode: str

    firstSix: str

    lastFour: str

    nameLine1: str

    nameLine2: str

    status: str

    bank: int

    issuedAmount: int

    cardType: str

    purchaseType: str

    availableBalance: int

class CardGetDetailResponse(RequiredCardGetDetailResponse, OptionalCardGetDetailResponse):
    pass
