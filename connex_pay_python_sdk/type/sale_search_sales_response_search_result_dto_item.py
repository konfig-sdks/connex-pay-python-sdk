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

from connex_pay_python_sdk.type.sale_search_sales_response_search_result_dto_item_card import SaleSearchSalesResponseSearchResultDtoItemCard

class RequiredSaleSearchSalesResponseSearchResultDtoItem(TypedDict):
    pass

class OptionalSaleSearchSalesResponseSearchResultDtoItem(TypedDict, total=False):
    status: str

    amount: int

    card: SaleSearchSalesResponseSearchResultDtoItemCard

    orderNumber: typing.Union[bool, date, datetime, dict, float, int, list, str, None]

    orderDate: typing.Union[bool, date, datetime, dict, float, int, list, str, None]

    timeStamp: str

    customerID: typing.Union[bool, date, datetime, dict, float, int, list, str, None]

    processorResponseMessage: typing.Union[bool, date, datetime, dict, float, int, list, str, None]

    effectiveAmount: int

    batchStatus: str

    relatedVoid: typing.Union[bool, date, datetime, dict, float, int, list, str, None]

    relatedReturns: typing.Union[bool, date, datetime, dict, float, int, list, str, None]

    guid: str

    deviceGuid: str

    captureGuid: typing.Union[bool, date, datetime, dict, float, int, list, str, None]

    customData: typing.Union[bool, date, datetime, dict, float, int, list, str, None]

    generatedByCapture: bool

    partiallyApprovedAmount: typing.Union[bool, date, datetime, dict, float, int, list, str, None]

    type: str

    surcharge: typing.Union[bool, date, datetime, dict, float, int, list, str, None]

    surchargeType: typing.Union[bool, date, datetime, dict, float, int, list, str, None]

    serviceFee: typing.Union[bool, date, datetime, dict, float, int, list, str, None]

    tipAmount: typing.Union[bool, date, datetime, dict, float, int, list, str, None]

    cardDataSource: str

    allowCardEmv: bool

    incomingTransactionCode: str

    activationDate: str

class SaleSearchSalesResponseSearchResultDtoItem(RequiredSaleSearchSalesResponseSearchResultDtoItem, OptionalSaleSearchSalesResponseSearchResultDtoItem):
    pass
