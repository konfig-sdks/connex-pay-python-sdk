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

from connex_pay_python_sdk.pydantic.setting_tokenize_bank_account_info_response_account_holder_address import SettingTokenizeBankAccountInfoResponseAccountHolderAddress
from connex_pay_python_sdk.pydantic.setting_tokenize_bank_account_info_response_account_holder_bank_account import SettingTokenizeBankAccountInfoResponseAccountHolderBankAccount

class SettingTokenizeBankAccountInfoResponseAccountHolder(BaseModel):
    account_holder_guid: typing.Optional[str] = Field(None, alias='accountHolderGuid')

    first_name: typing.Optional[str] = Field(None, alias='firstName')

    last_name: typing.Optional[str] = Field(None, alias='lastName')

    _business_name: typing.Optional[str] = Field(None, alias='_businessName')

    email: typing.Optional[str] = Field(None, alias='email')

    phone: typing.Optional[str] = Field(None, alias='phone')

    address: typing.Optional[SettingTokenizeBankAccountInfoResponseAccountHolderAddress] = Field(None, alias='address')

    bank_account: typing.Optional[SettingTokenizeBankAccountInfoResponseAccountHolderBankAccount] = Field(None, alias='bankAccount')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
