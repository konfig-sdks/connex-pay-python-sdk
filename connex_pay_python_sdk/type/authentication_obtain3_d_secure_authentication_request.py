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

from connex_pay_python_sdk.type.authentication_obtain3_d_secure_authentication_request_browser_data import AuthenticationObtain3DSecureAuthenticationRequestBrowserData
from connex_pay_python_sdk.type.authentication_obtain3_d_secure_authentication_request_card import AuthenticationObtain3DSecureAuthenticationRequestCard

class RequiredAuthenticationObtain3DSecureAuthenticationRequest(TypedDict):
    Card: AuthenticationObtain3DSecureAuthenticationRequestCard

    # Device's Guid as assigned by ConnexPay.
    DeviceGuid: str

    BrowserData: AuthenticationObtain3DSecureAuthenticationRequestBrowserData

    # Amount of the transaction being 3DS authenticated
    Amount: typing.Union[int, float]

class OptionalAuthenticationObtain3DSecureAuthenticationRequest(TypedDict, total=False):
    pass

class AuthenticationObtain3DSecureAuthenticationRequest(RequiredAuthenticationObtain3DSecureAuthenticationRequest, OptionalAuthenticationObtain3DSecureAuthenticationRequest):
    pass
