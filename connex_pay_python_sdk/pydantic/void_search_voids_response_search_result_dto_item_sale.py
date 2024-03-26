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

from connex_pay_python_sdk.pydantic.void_search_voids_response_search_result_dto_item_sale_card import VoidSearchVoidsResponseSearchResultDtoItemSaleCard

class VoidSearchVoidsResponseSearchResultDtoItemSale(BaseModel):
    amount: typing.Optional[int] = Field(None, alias='amount')

    card: typing.Optional[VoidSearchVoidsResponseSearchResultDtoItemSaleCard] = Field(None, alias='card')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
