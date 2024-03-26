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


class RequiredTokenGenerateReportingTokenRequest(TypedDict):
    # Assigned username for CXP Bridge
    UserName: str

    # Assigned password for CXP Bridge
    Password: str

class OptionalTokenGenerateReportingTokenRequest(TypedDict, total=False):
    pass

class TokenGenerateReportingTokenRequest(RequiredTokenGenerateReportingTokenRequest, OptionalTokenGenerateReportingTokenRequest):
    pass
