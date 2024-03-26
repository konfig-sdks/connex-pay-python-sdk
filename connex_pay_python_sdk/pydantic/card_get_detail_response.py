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


class CardGetDetailResponse(BaseModel):
    card_guid: typing.Optional[str] = Field(None, alias='cardGuid')

    expiration_date: typing.Optional[str] = Field(None, alias='expirationDate')

    expiration: typing.Optional[str] = Field(None, alias='expiration')

    terminate_date: typing.Optional[str] = Field(None, alias='terminateDate')

    currency_code: typing.Optional[str] = Field(None, alias='currencyCode')

    first_six: typing.Optional[str] = Field(None, alias='firstSix')

    last_four: typing.Optional[str] = Field(None, alias='lastFour')

    name_line1: typing.Optional[str] = Field(None, alias='nameLine1')

    name_line2: typing.Optional[str] = Field(None, alias='nameLine2')

    status: typing.Optional[str] = Field(None, alias='status')

    bank: typing.Optional[int] = Field(None, alias='bank')

    issued_amount: typing.Optional[int] = Field(None, alias='issuedAmount')

    card_type: typing.Optional[str] = Field(None, alias='cardType')

    purchase_type: typing.Optional[str] = Field(None, alias='purchaseType')

    available_balance: typing.Optional[int] = Field(None, alias='availableBalance')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
