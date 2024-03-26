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

from connex_pay_python_sdk.type.merchant_payee_dto import MerchantPayeeDto

class RequiredMerchantPayeePaginatedResponse(TypedDict):
    pass

class OptionalMerchantPayeePaginatedResponse(TypedDict, total=False):
    totalCount: int

    totalPageCount: int

    pageSize: int

    currentPage: int

    searchResults: typing.List[MerchantPayeeDto]

class MerchantPayeePaginatedResponse(RequiredMerchantPayeePaginatedResponse, OptionalMerchantPayeePaginatedResponse):
    pass
