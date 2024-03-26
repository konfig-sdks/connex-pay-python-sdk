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

from connex_pay_python_sdk.type.setting_tokenize_bank_account_info_request_account_holder import SettingTokenizeBankAccountInfoRequestAccountHolder

class RequiredSettingTokenizeBankAccountInfoRequest(TypedDict):
    # Merchant's guid. Application level value that indicates the ACH payment is being requested for clients account. Value provided by ConnexPay.
    MerchantGuid: str

    # Name of supplier to whom payment will be made
    SupplierName: str

    AccountHolder: SettingTokenizeBankAccountInfoRequestAccountHolder

class OptionalSettingTokenizeBankAccountInfoRequest(TypedDict, total=False):
    pass

class SettingTokenizeBankAccountInfoRequest(RequiredSettingTokenizeBankAccountInfoRequest, OptionalSettingTokenizeBankAccountInfoRequest):
    pass
