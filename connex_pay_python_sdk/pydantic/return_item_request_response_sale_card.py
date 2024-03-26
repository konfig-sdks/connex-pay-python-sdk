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

from connex_pay_python_sdk.pydantic.return_item_request_response_sale_card_customer import ReturnItemRequestResponseSaleCardCustomer

class ReturnItemRequestResponseSaleCard(BaseModel):
    first4: typing.Optional[str] = Field(None, alias='first4')

    last4: typing.Optional[str] = Field(None, alias='last4')

    card_number: typing.Optional[str] = Field(None, alias='cardNumber')

    card_holder_name: typing.Optional[str] = Field(None, alias='cardHolderName')

    expiration_date: typing.Optional[str] = Field(None, alias='expirationDate')

    customer: typing.Optional[ReturnItemRequestResponseSaleCardCustomer] = Field(None, alias='customer')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
