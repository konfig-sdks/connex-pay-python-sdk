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

from connex_pay_python_sdk.type.authentication_obtain3_d_secure_authentication_response_card import AuthenticationObtain3DSecureAuthenticationResponseCard

class RequiredAuthenticationObtain3DSecureAuthenticationResponse(TypedDict):
    pass

class OptionalAuthenticationObtain3DSecureAuthenticationResponse(TypedDict, total=False):
    guid: str

    status: str

    timeStamp: str

    deviceGuid: str

    amount: int

    threeDSStatus: str

    SecureData: str

    Cavv: str

    Version: str

    DirectoryServerTransactionID: str

    AcsTransactionId: str

    ECI: str

    card: AuthenticationObtain3DSecureAuthenticationResponseCard

    exemptThreeDSRequest: bool

    exemptThreeDSPayment: bool

class AuthenticationObtain3DSecureAuthenticationResponse(RequiredAuthenticationObtain3DSecureAuthenticationResponse, OptionalAuthenticationObtain3DSecureAuthenticationResponse):
    pass
