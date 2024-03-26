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

from connex_pay_python_sdk.type.card_update_delayed_activation_response_card import CardUpdateDelayedActivationResponseCard
from connex_pay_python_sdk.type.card_update_delayed_activation_response_card_holder import CardUpdateDelayedActivationResponseCardHolder

class RequiredCardUpdateDelayedActivationResponse(TypedDict):
    pass

class OptionalCardUpdateDelayedActivationResponse(TypedDict, total=False):
    cardHolder: CardUpdateDelayedActivationResponseCardHolder

    card: CardUpdateDelayedActivationResponseCard

class CardUpdateDelayedActivationResponse(RequiredCardUpdateDelayedActivationResponse, OptionalCardUpdateDelayedActivationResponse):
    pass
