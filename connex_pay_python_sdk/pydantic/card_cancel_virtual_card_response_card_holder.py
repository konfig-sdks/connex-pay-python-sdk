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


class CardCancelVirtualCardResponseCardHolder(BaseModel):
    card_holder_guid: typing.Optional[str] = Field(None, alias='cardHolderGuid')

    first_name: typing.Optional[str] = Field(None, alias='firstName')

    last_name: typing.Optional[str] = Field(None, alias='lastName')

    phone: typing.Optional[str] = Field(None, alias='phone')

    address1: typing.Optional[str] = Field(None, alias='address1')

    address2: typing.Optional[str] = Field(None, alias='address2')

    city: typing.Optional[str] = Field(None, alias='city')

    zipcode: typing.Optional[str] = Field(None, alias='zipcode')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
