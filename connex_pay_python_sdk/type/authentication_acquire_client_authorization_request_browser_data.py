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


class RequiredAuthenticationAcquireClientAuthorizationRequestBrowserData(TypedDict):
    # Required.  Exact content of the http accept header.
    AcceptanceHeader: str

    # Required. Value representing the bit depth of the color palette for displaying images, in bits per pixel.
    ColorDepth: int

    # True or False response that represents ability of cardholder browser to execute Java
    JavaEnabled: bool

    # Total height of the Cardholder's screen in pixels
    ScreenHeight: int

    # Total width of the Cardholder's screen in pixels
    ScreenWidth: int

    # Time Zone difference between browser time zone and UTC time, in hours.  Can be positive or negative.
    TimeZoneOffset: int

    # Value representing the browser language as defined in IETF BCP47
    Language: str

    # The merchant URL to which the browser should be redirected after the challenge session.
    RedirectURL: str

    # Exact content of the HTTP user-agent header.
    UserAgentHeader: str

class OptionalAuthenticationAcquireClientAuthorizationRequestBrowserData(TypedDict, total=False):
    pass

class AuthenticationAcquireClientAuthorizationRequestBrowserData(RequiredAuthenticationAcquireClientAuthorizationRequestBrowserData, OptionalAuthenticationAcquireClientAuthorizationRequestBrowserData):
    pass
