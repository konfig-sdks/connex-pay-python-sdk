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


class RequiredStatusGroup3DsAuthenticationStatusResponseCard(TypedDict):
    pass

class OptionalStatusGroup3DsAuthenticationStatusResponseCard(TypedDict, total=False):
    first6: str

    first4: str

    last4: str

    cardType: str

    expirationDate: str

    guid: str

class StatusGroup3DsAuthenticationStatusResponseCard(RequiredStatusGroup3DsAuthenticationStatusResponseCard, OptionalStatusGroup3DsAuthenticationStatusResponseCard):
    pass
