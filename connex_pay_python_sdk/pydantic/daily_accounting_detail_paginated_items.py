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

from connex_pay_python_sdk.pydantic.daily_accounting_detail import DailyAccountingDetail

class DailyAccountingDetailPaginatedItems(BaseModel):
    # Count of all items available in the day's accounting detail.
    total_item_count: typing.Optional[int] = Field(None, alias='totalItemCount')

    # Count of pages available in the day's accounting detail.
    page_count: typing.Optional[int] = Field(None, alias='pageCount')

    # Count of items in the current page.
    page_item_count: typing.Optional[int] = Field(None, alias='pageItemCount')

    # Sequence number of the current page.
    page_number: typing.Optional[int] = Field(None, alias='pageNumber')

    # Collection of accounting detail items for the current page.
    items: typing.Optional[typing.Optional[typing.List[DailyAccountingDetail]]] = Field(None, alias='items')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
