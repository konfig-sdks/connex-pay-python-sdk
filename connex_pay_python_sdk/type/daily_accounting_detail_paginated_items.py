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

from connex_pay_python_sdk.type.daily_accounting_detail import DailyAccountingDetail

class RequiredDailyAccountingDetailPaginatedItems(TypedDict):
    pass

class OptionalDailyAccountingDetailPaginatedItems(TypedDict, total=False):
    # Count of all items available in the day's accounting detail.
    totalItemCount: int

    # Count of pages available in the day's accounting detail.
    pageCount: int

    # Count of items in the current page.
    pageItemCount: int

    # Sequence number of the current page.
    pageNumber: int

    # Collection of accounting detail items for the current page.
    items: typing.Optional[typing.List[DailyAccountingDetail]]

class DailyAccountingDetailPaginatedItems(RequiredDailyAccountingDetailPaginatedItems, OptionalDailyAccountingDetailPaginatedItems):
    pass
