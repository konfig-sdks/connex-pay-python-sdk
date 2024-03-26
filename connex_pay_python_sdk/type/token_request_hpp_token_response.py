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


class RequiredTokenRequestHppTokenResponse(TypedDict):
    pass

class OptionalTokenRequestHppTokenResponse(TypedDict, total=False):
    description: str

    merchantName: str

    amount: int

    resultRedirectUrl: str

    tempToken: str

    expiration: str

    logoUrl: str

class TokenRequestHppTokenResponse(RequiredTokenRequestHppTokenResponse, OptionalTokenRequestHppTokenResponse):
    pass
