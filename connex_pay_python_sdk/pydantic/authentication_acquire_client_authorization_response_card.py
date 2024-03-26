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

from connex_pay_python_sdk.pydantic.authentication_acquire_client_authorization_response_card_customer import AuthenticationAcquireClientAuthorizationResponseCardCustomer

class AuthenticationAcquireClientAuthorizationResponseCard(BaseModel):
    first6: typing.Optional[str] = Field(None, alias='first6')

    first4: typing.Optional[str] = Field(None, alias='first4')

    last4: typing.Optional[str] = Field(None, alias='last4')

    card_holder_name: typing.Optional[str] = Field(None, alias='cardHolderName')

    card_type: typing.Optional[str] = Field(None, alias='cardType')

    expiration_date: typing.Optional[str] = Field(None, alias='expirationDate')

    customer: typing.Optional[AuthenticationAcquireClientAuthorizationResponseCardCustomer] = Field(None, alias='customer')

    guid: typing.Optional[str] = Field(None, alias='guid')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
