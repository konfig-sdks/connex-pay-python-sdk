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

from connex_pay_python_sdk.type.return_search_sale_returns_response_search_result_dto_item_card import ReturnSearchSaleReturnsResponseSearchResultDtoItemCard

class RequiredReturnSearchSaleReturnsResponseSearchResultDtoItem(TypedDict):
    pass

class OptionalReturnSearchSaleReturnsResponseSearchResultDtoItem(TypedDict, total=False):
    status: str

    amount: int

    card: ReturnSearchSaleReturnsResponseSearchResultDtoItemCard

    timeStamp: str

    processorStatusCode: str

    batchStatus: str

    guid: str

    relatedVoid: typing.Union[bool, date, datetime, dict, float, int, list, str, None]

    deviceGuid: str

    type: str

    cardDataSource: str

    allowCardEmv: bool

class ReturnSearchSaleReturnsResponseSearchResultDtoItem(RequiredReturnSearchSaleReturnsResponseSearchResultDtoItem, OptionalReturnSearchSaleReturnsResponseSearchResultDtoItem):
    pass
