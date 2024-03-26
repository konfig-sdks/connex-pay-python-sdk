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


class RequiredSettingTokenizeBankAccountInfoResponseAccountHolderBankAccount(TypedDict):
    pass

class OptionalSettingTokenizeBankAccountInfoResponseAccountHolderBankAccount(TypedDict, total=False):
    bankAccountGuid: str

    accountType: str

    accountHolderName: str

    last4Digits: str

class SettingTokenizeBankAccountInfoResponseAccountHolderBankAccount(RequiredSettingTokenizeBankAccountInfoResponseAccountHolderBankAccount, OptionalSettingTokenizeBankAccountInfoResponseAccountHolderBankAccount):
    pass
