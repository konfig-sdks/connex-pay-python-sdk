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


class SettingTokenizeBankAccountInfoRequestAccountHolderBankAccount(BaseModel):
    # Routing number up to 9 characters
    routing_number: str = Field(alias='RoutingNumber')

    # Account number up to 17 characters
    account_number: str = Field(alias='AccountNumber')

    # 'Checking' or 'Saving'
    account_type: str = Field(alias='AccountType')

    # Account holder name up to 150 characters
    account_holder_name: str = Field(alias='AccountHolderName')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
