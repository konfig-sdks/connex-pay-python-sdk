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

from connex_pay_python_sdk.type.setting_tokenize_bank_account_info_response_account_holder import SettingTokenizeBankAccountInfoResponseAccountHolder

class RequiredSettingTokenizeBankAccountInfoResponse(TypedDict):
    pass

class OptionalSettingTokenizeBankAccountInfoResponse(TypedDict, total=False):
    merchantGuid: str

    supplierName: str

    timeStamp: str

    idUser: int

    idMerchantSupplierSettings: int

    accountHolder: SettingTokenizeBankAccountInfoResponseAccountHolder

    userName: str

class SettingTokenizeBankAccountInfoResponse(RequiredSettingTokenizeBankAccountInfoResponse, OptionalSettingTokenizeBankAccountInfoResponse):
    pass
