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

from connex_pay_python_sdk.type.void_search_voids_response_search_result_dto_item_sale import VoidSearchVoidsResponseSearchResultDtoItemSale

RequiredVoidSearchVoidsResponseSearchResultDtoItem = TypedDict("RequiredVoidSearchVoidsResponseSearchResultDtoItem", {
    })

OptionalVoidSearchVoidsResponseSearchResultDtoItem = TypedDict("OptionalVoidSearchVoidsResponseSearchResultDtoItem", {
    "status": str,

    "sale": VoidSearchVoidsResponseSearchResultDtoItemSale,

    "authOnly": typing.Union[bool, date, datetime, dict, float, int, list, str, None],

    "debitSale": typing.Union[bool, date, datetime, dict, float, int, list, str, None],

    "debitReturn": typing.Union[bool, date, datetime, dict, float, int, list, str, None],

    "ebtFoodStampPurchase": typing.Union[bool, date, datetime, dict, float, int, list, str, None],

    "ebtElectronicVoucher": typing.Union[bool, date, datetime, dict, float, int, list, str, None],

    "ebtReturn": typing.Union[bool, date, datetime, dict, float, int, list, str, None],

    "ebtCashBenefitPurchase": typing.Union[bool, date, datetime, dict, float, int, list, str, None],

    "return": typing.Union[bool, date, datetime, dict, float, int, list, str, None],

    "voidReason": typing.Union[bool, date, datetime, dict, float, int, list, str, None],

    "timeStamp": str,

    "processorStatusCode": str,

    "batchStatus": str,

    "guid": str,

    "allowCardEmv": bool,
    }, total=False)

class VoidSearchVoidsResponseSearchResultDtoItem(RequiredVoidSearchVoidsResponseSearchResultDtoItem, OptionalVoidSearchVoidsResponseSearchResultDtoItem):
    pass
