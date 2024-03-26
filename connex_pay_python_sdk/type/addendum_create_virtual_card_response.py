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


class RequiredAddendumCreateVirtualCardResponse(TypedDict):
    pass

class OptionalAddendumCreateVirtualCardResponse(TypedDict, total=False):
    guid: str

    itemGuid: str

    value: str

    category: str

    idExternal: str

    note: str

    sequence: str

class AddendumCreateVirtualCardResponse(RequiredAddendumCreateVirtualCardResponse, OptionalAddendumCreateVirtualCardResponse):
    pass
