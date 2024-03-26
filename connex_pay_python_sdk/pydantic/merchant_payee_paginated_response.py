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

from connex_pay_python_sdk.pydantic.merchant_payee_dto import MerchantPayeeDto

class MerchantPayeePaginatedResponse(BaseModel):
    total_count: typing.Optional[int] = Field(None, alias='totalCount')

    total_page_count: typing.Optional[int] = Field(None, alias='totalPageCount')

    page_size: typing.Optional[int] = Field(None, alias='pageSize')

    current_page: typing.Optional[int] = Field(None, alias='currentPage')

    search_results: typing.Optional[typing.List[MerchantPayeeDto]] = Field(None, alias='searchResults')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
