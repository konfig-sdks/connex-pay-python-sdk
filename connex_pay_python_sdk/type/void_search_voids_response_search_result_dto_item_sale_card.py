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


class RequiredVoidSearchVoidsResponseSearchResultDtoItemSaleCard(TypedDict):
    pass

class OptionalVoidSearchVoidsResponseSearchResultDtoItemSaleCard(TypedDict, total=False):
    cardHolderName: typing.Union[bool, date, datetime, dict, float, int, list, str, None]

    cardType: str

    last4: str

class VoidSearchVoidsResponseSearchResultDtoItemSaleCard(RequiredVoidSearchVoidsResponseSearchResultDtoItemSaleCard, OptionalVoidSearchVoidsResponseSearchResultDtoItemSaleCard):
    pass
