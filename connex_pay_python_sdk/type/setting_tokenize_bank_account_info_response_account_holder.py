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

from connex_pay_python_sdk.type.setting_tokenize_bank_account_info_response_account_holder_address import SettingTokenizeBankAccountInfoResponseAccountHolderAddress
from connex_pay_python_sdk.type.setting_tokenize_bank_account_info_response_account_holder_bank_account import SettingTokenizeBankAccountInfoResponseAccountHolderBankAccount

class RequiredSettingTokenizeBankAccountInfoResponseAccountHolder(TypedDict):
    pass

class OptionalSettingTokenizeBankAccountInfoResponseAccountHolder(TypedDict, total=False):
    accountHolderGuid: str

    firstName: str

    lastName: str

    _businessName: str

    email: str

    phone: str

    address: SettingTokenizeBankAccountInfoResponseAccountHolderAddress

    bankAccount: SettingTokenizeBankAccountInfoResponseAccountHolderBankAccount

class SettingTokenizeBankAccountInfoResponseAccountHolder(RequiredSettingTokenizeBankAccountInfoResponseAccountHolder, OptionalSettingTokenizeBankAccountInfoResponseAccountHolder):
    pass
