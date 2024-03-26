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


class ReturnItemRequestRequestReturnRetryCard(BaseModel):
    # Card number. Must be 16 characters.
    card_number: typing.Optional[str] = Field(None, alias='CardNumber')

    # Cardholder's name
    card_holder_name: typing.Optional[str] = Field(None, alias='CardHolderName')

    # The three or four digit CVV code at the back side of the credit and debit card
    cvv2: typing.Optional[int] = Field(None, alias='Cvv2')

    # Card's expiry date in the YYMM format
    expiration_date: typing.Optional[date] = Field(None, alias='ExpirationDate')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
