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
from pydantic import BaseModel, Field, RootModel, ConfigDict

from connex_pay_python_sdk.pydantic.authentication_obtain3_d_secure_authentication_request_browser_data import AuthenticationObtain3DSecureAuthenticationRequestBrowserData
from connex_pay_python_sdk.pydantic.authentication_obtain3_d_secure_authentication_request_card import AuthenticationObtain3DSecureAuthenticationRequestCard

class AuthenticationObtain3DSecureAuthenticationRequest(BaseModel):
    card: AuthenticationObtain3DSecureAuthenticationRequestCard = Field(alias='Card')

    # Device's Guid as assigned by ConnexPay.
    device_guid: str = Field(alias='DeviceGuid')

    browser_data: AuthenticationObtain3DSecureAuthenticationRequestBrowserData = Field(alias='BrowserData')

    # Amount of the transaction being 3DS authenticated
    amount: typing.Union[int, float] = Field(alias='Amount')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
