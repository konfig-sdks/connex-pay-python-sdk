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


class TokenIssueAuthenticationTokenResponse(BaseModel):
    access_token: typing.Optional[str] = Field(None, alias='access_token')

    token_type: typing.Optional[str] = Field(None, alias='token_type')

    expires_in: typing.Optional[int] = Field(None, alias='expires_in')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
