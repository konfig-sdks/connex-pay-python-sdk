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

from connex_pay_python_sdk.type.sale_search_sales_response_search_result_dto import SaleSearchSalesResponseSearchResultDto

class RequiredSaleSearchSalesResponse(TypedDict):
    pass

class OptionalSaleSearchSalesResponse(TypedDict, total=False):
    pageCurrent: int

    pageCurrentResults: int

    pageTotal: int

    pageSize: int

    totalResults: int

    cardSummary: typing.Union[bool, date, datetime, dict, float, int, list, str, None]

    searchResultDTO: SaleSearchSalesResponseSearchResultDto

class SaleSearchSalesResponse(RequiredSaleSearchSalesResponse, OptionalSaleSearchSalesResponse):
    pass
