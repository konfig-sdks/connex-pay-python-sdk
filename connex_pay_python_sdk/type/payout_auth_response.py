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

from connex_pay_python_sdk.type.authentication_result import AuthenticationResult

class RequiredPayoutAuthResponse(TypedDict):
    pass

class OptionalPayoutAuthResponse(TypedDict, total=False):
    AuthenticationResult: AuthenticationResult

class PayoutAuthResponse(RequiredPayoutAuthResponse, OptionalPayoutAuthResponse):
    pass
