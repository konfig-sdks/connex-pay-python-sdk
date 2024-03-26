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

from connex_pay_python_sdk.pydantic.return_search_sale_returns_response_search_result_dto_item import ReturnSearchSaleReturnsResponseSearchResultDtoItem

ReturnSearchSaleReturnsResponseSearchResultDto = typing.List[ReturnSearchSaleReturnsResponseSearchResultDtoItem]
