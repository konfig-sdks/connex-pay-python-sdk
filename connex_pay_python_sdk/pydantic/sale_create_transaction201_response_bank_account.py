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

from connex_pay_python_sdk.pydantic.sale_create_transaction201_response_bank_account_customer import SaleCreateTransaction201ResponseBankAccountCustomer

class SaleCreateTransaction201ResponseBankAccount(BaseModel):
    guid: typing.Optional[str] = Field(None, alias='guid')

    account_type: typing.Optional[str] = Field(None, alias='accountType')

    account_number_last_four: typing.Optional[str] = Field(None, alias='accountNumberLastFour')

    name_on_account: typing.Optional[str] = Field(None, alias='nameOnAccount')

    customer: typing.Optional[SaleCreateTransaction201ResponseBankAccountCustomer] = Field(None, alias='customer')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
