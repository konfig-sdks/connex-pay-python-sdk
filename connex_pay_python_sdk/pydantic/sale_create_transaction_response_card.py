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

from connex_pay_python_sdk.pydantic.sale_create_transaction_response_card_customer import SaleCreateTransactionResponseCardCustomer
from connex_pay_python_sdk.pydantic.sale_create_transaction_response_card_three_ds import SaleCreateTransactionResponseCardThreeDs

class SaleCreateTransactionResponseCard(BaseModel):
    three_d_s: typing.Optional[SaleCreateTransactionResponseCardThreeDs] = Field(None, alias='ThreeDS')

    card_number: typing.Optional[str] = Field(None, alias='CardNumber')

    card_holder_name: typing.Optional[str] = Field(None, alias='CardHolderName')

    cvv2: typing.Optional[str] = Field(None, alias='Cvv2')

    expiration_date: typing.Optional[str] = Field(None, alias='ExpirationDate')

    customer: typing.Optional[SaleCreateTransactionResponseCardCustomer] = Field(None, alias='Customer')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
