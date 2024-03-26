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


class RequiredTokenGenerateReportingTokenResponse(TypedDict):
    pass

class OptionalTokenGenerateReportingTokenResponse(TypedDict, total=False):
    access_token: str

    expires_in: str

class TokenGenerateReportingTokenResponse(RequiredTokenGenerateReportingTokenResponse, OptionalTokenGenerateReportingTokenResponse):
    pass
