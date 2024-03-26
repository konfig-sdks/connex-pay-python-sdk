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

from connex_pay_python_sdk.pydantic.void_search_voids_response_search_result_dto_item_sale import VoidSearchVoidsResponseSearchResultDtoItemSale

class VoidSearchVoidsResponseSearchResultDtoItem(BaseModel):
    status: typing.Optional[str] = Field(None, alias='status')

    sale: typing.Optional[VoidSearchVoidsResponseSearchResultDtoItemSale] = Field(None, alias='sale')

    auth_only: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = Field(None, alias='authOnly')

    debit_sale: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = Field(None, alias='debitSale')

    debit_return: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = Field(None, alias='debitReturn')

    ebt_food_stamp_purchase: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = Field(None, alias='ebtFoodStampPurchase')

    ebt_electronic_voucher: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = Field(None, alias='ebtElectronicVoucher')

    ebt_return: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = Field(None, alias='ebtReturn')

    ebt_cash_benefit_purchase: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = Field(None, alias='ebtCashBenefitPurchase')

    return_: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = Field(None, alias='return')

    void_reason: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = Field(None, alias='voidReason')

    time_stamp: typing.Optional[str] = Field(None, alias='timeStamp')

    processor_status_code: typing.Optional[str] = Field(None, alias='processorStatusCode')

    batch_status: typing.Optional[str] = Field(None, alias='batchStatus')

    guid: typing.Optional[str] = Field(None, alias='guid')

    allow_card_emv: typing.Optional[bool] = Field(None, alias='allowCardEmv')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
