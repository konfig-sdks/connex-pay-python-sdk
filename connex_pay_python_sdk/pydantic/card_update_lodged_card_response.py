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

from connex_pay_python_sdk.pydantic.card_update_lodged_card_response_card import CardUpdateLodgedCardResponseCard

class CardUpdateLodgedCardResponse(BaseModel):
    card: typing.Optional[CardUpdateLodgedCardResponseCard] = Field(None, alias='card')

    mcc_group_name: typing.Optional[str] = Field(None, alias='mccGroupName')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
