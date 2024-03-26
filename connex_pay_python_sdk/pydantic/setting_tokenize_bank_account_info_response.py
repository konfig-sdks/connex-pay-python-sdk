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

from connex_pay_python_sdk.pydantic.setting_tokenize_bank_account_info_response_account_holder import SettingTokenizeBankAccountInfoResponseAccountHolder

class SettingTokenizeBankAccountInfoResponse(BaseModel):
    merchant_guid: typing.Optional[str] = Field(None, alias='merchantGuid')

    supplier_name: typing.Optional[str] = Field(None, alias='supplierName')

    time_stamp: typing.Optional[str] = Field(None, alias='timeStamp')

    id_user: typing.Optional[int] = Field(None, alias='idUser')

    id_merchant_supplier_settings: typing.Optional[int] = Field(None, alias='idMerchantSupplierSettings')

    account_holder: typing.Optional[SettingTokenizeBankAccountInfoResponseAccountHolder] = Field(None, alias='accountHolder')

    user_name: typing.Optional[str] = Field(None, alias='userName')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
