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

from connex_pay_python_sdk.pydantic.card_update_delayed_activation_response_card import CardUpdateDelayedActivationResponseCard
from connex_pay_python_sdk.pydantic.card_update_delayed_activation_response_card_holder import CardUpdateDelayedActivationResponseCardHolder

class CardUpdateDelayedActivationResponse(BaseModel):
    card_holder: typing.Optional[CardUpdateDelayedActivationResponseCardHolder] = Field(None, alias='cardHolder')

    card: typing.Optional[CardUpdateDelayedActivationResponseCard] = Field(None, alias='card')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
