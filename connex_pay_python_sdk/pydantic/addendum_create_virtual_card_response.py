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


class AddendumCreateVirtualCardResponse(BaseModel):
    guid: typing.Optional[str] = Field(None, alias='guid')

    item_guid: typing.Optional[str] = Field(None, alias='itemGuid')

    value: typing.Optional[str] = Field(None, alias='value')

    category: typing.Optional[str] = Field(None, alias='category')

    id_external: typing.Optional[str] = Field(None, alias='idExternal')

    note: typing.Optional[str] = Field(None, alias='note')

    sequence: typing.Optional[str] = Field(None, alias='sequence')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
