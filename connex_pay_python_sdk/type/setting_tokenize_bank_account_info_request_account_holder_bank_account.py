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


class RequiredSettingTokenizeBankAccountInfoRequestAccountHolderBankAccount(TypedDict):
    # Routing number up to 9 characters
    RoutingNumber: str

    # Account number up to 17 characters
    AccountNumber: str

    # 'Checking' or 'Saving'
    AccountType: str

    # Account holder name up to 150 characters
    AccountHolderName: str

class OptionalSettingTokenizeBankAccountInfoRequestAccountHolderBankAccount(TypedDict, total=False):
    pass

class SettingTokenizeBankAccountInfoRequestAccountHolderBankAccount(RequiredSettingTokenizeBankAccountInfoRequestAccountHolderBankAccount, OptionalSettingTokenizeBankAccountInfoRequestAccountHolderBankAccount):
    pass
