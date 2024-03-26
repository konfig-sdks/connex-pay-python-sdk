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


class RequiredCardUpdateDelayedActivationResponseCard(TypedDict):
    pass

class OptionalCardUpdateDelayedActivationResponseCard(TypedDict, total=False):
    cardGuid: str

    amountLimit: int

    usageLimit: int

    limitWindow: str

    expirationDate: str

    expiration: str

    firstSix: str

    lastFour: str

    nameLine1: str

    nameLine2: str

    status: str

    activationDate: str

    cardType: str

class CardUpdateDelayedActivationResponseCard(RequiredCardUpdateDelayedActivationResponseCard, OptionalCardUpdateDelayedActivationResponseCard):
    pass
