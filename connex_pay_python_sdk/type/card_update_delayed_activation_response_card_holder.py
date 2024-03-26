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


class RequiredCardUpdateDelayedActivationResponseCardHolder(TypedDict):
    pass

class OptionalCardUpdateDelayedActivationResponseCardHolder(TypedDict, total=False):
    cardHolderGuid: str

    firstName: str

    lastName: str

    phone: str

    address1: str

    address2: str

    city: str

    zipcode: str

class CardUpdateDelayedActivationResponseCardHolder(RequiredCardUpdateDelayedActivationResponseCardHolder, OptionalCardUpdateDelayedActivationResponseCardHolder):
    pass
