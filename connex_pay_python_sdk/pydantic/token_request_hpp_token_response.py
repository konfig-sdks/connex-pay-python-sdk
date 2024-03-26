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


class TokenRequestHppTokenResponse(BaseModel):
    description: typing.Optional[str] = Field(None, alias='description')

    merchant_name: typing.Optional[str] = Field(None, alias='merchantName')

    amount: typing.Optional[int] = Field(None, alias='amount')

    result_redirect_url: typing.Optional[str] = Field(None, alias='resultRedirectUrl')

    temp_token: typing.Optional[str] = Field(None, alias='tempToken')

    expiration: typing.Optional[str] = Field(None, alias='expiration')

    logo_url: typing.Optional[str] = Field(None, alias='logoUrl')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
