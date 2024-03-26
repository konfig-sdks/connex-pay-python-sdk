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

from connex_pay_python_sdk.pydantic.card_update_lodged_card_response_card_mid_blacklist import CardUpdateLodgedCardResponseCardMidBlacklist
from connex_pay_python_sdk.pydantic.card_update_lodged_card_response_card_mid_whitelist import CardUpdateLodgedCardResponseCardMidWhitelist

class CardUpdateLodgedCardResponseCard(BaseModel):
    card_guid: typing.Optional[str] = Field(None, alias='cardGuid')

    amount_limit: typing.Optional[int] = Field(None, alias='amountLimit')

    usage_limit: typing.Optional[int] = Field(None, alias='usageLimit')

    limit_window: typing.Optional[str] = Field(None, alias='limitWindow')

    expiration_date: typing.Optional[str] = Field(None, alias='expirationDate')

    expiration: typing.Optional[str] = Field(None, alias='expiration')

    first_six: typing.Optional[str] = Field(None, alias='firstSix')

    last_four: typing.Optional[str] = Field(None, alias='lastFour')

    name_line1: typing.Optional[str] = Field(None, alias='nameLine1')

    name_line2: typing.Optional[str] = Field(None, alias='nameLine2')

    status: typing.Optional[str] = Field(None, alias='status')

    card_type: typing.Optional[str] = Field(None, alias='cardType')

    mid_whitelist: typing.Optional[CardUpdateLodgedCardResponseCardMidWhitelist] = Field(None, alias='midWhitelist')

    mid_blacklist: typing.Optional[CardUpdateLodgedCardResponseCardMidBlacklist] = Field(None, alias='midBlacklist')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
