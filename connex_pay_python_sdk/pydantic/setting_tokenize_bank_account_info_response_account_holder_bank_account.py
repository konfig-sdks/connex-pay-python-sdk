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


class SettingTokenizeBankAccountInfoResponseAccountHolderBankAccount(BaseModel):
    bank_account_guid: typing.Optional[str] = Field(None, alias='bankAccountGuid')

    account_type: typing.Optional[str] = Field(None, alias='accountType')

    account_holder_name: typing.Optional[str] = Field(None, alias='accountHolderName')

    last4_digits: typing.Optional[str] = Field(None, alias='last4Digits')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
