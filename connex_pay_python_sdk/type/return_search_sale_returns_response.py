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

from connex_pay_python_sdk.type.return_search_sale_returns_response_search_result_dto import ReturnSearchSaleReturnsResponseSearchResultDto

class RequiredReturnSearchSaleReturnsResponse(TypedDict):
    pass

class OptionalReturnSearchSaleReturnsResponse(TypedDict, total=False):
    pageCurrent: int

    pageCurrentResults: int

    pageTotal: int

    pageSize: int

    totalResults: int

    cardSummary: typing.Union[bool, date, datetime, dict, float, int, list, str, None]

    searchResultDTO: ReturnSearchSaleReturnsResponseSearchResultDto

class ReturnSearchSaleReturnsResponse(RequiredReturnSearchSaleReturnsResponse, OptionalReturnSearchSaleReturnsResponse):
    pass
