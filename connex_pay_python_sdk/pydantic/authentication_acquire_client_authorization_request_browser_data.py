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


class AuthenticationAcquireClientAuthorizationRequestBrowserData(BaseModel):
    # Required.  Exact content of the http accept header.
    acceptance_header: str = Field(alias='AcceptanceHeader')

    # Required. Value representing the bit depth of the color palette for displaying images, in bits per pixel.
    color_depth: int = Field(alias='ColorDepth')

    # True or False response that represents ability of cardholder browser to execute Java
    java_enabled: bool = Field(alias='JavaEnabled')

    # Total height of the Cardholder's screen in pixels
    screen_height: int = Field(alias='ScreenHeight')

    # Total width of the Cardholder's screen in pixels
    screen_width: int = Field(alias='ScreenWidth')

    # Time Zone difference between browser time zone and UTC time, in hours.  Can be positive or negative.
    time_zone_offset: int = Field(alias='TimeZoneOffset')

    # Value representing the browser language as defined in IETF BCP47
    language: str = Field(alias='Language')

    # The merchant URL to which the browser should be redirected after the challenge session.
    redirect_u_r_l: str = Field(alias='RedirectURL')

    # Exact content of the HTTP user-agent header.
    user_agent_header: str = Field(alias='UserAgentHeader')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
