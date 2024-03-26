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

from connex_pay_python_sdk.type.return_item_request_request_return_retry_card import ReturnItemRequestRequestReturnRetryCard

class RequiredReturnItemRequestRequest(TypedDict):
    # Device's Guid
    DeviceGuid: str

    # Transaction’s amount. Min. amt.: $0.50
    Amount: typing.Union[int, float]

class OptionalReturnItemRequestRequest(TypedDict, total=False):
    # Mandatory when SaleReferenceNumber field is not sent. Sale's Guid.
    SaleGuid: str

    # Mandatory when SaleGuid field is not sent. Sale's Reference Number
    SaleReferenceNumber: int

    # Transaction sequence number within client environment. Provide a unique SequenceNumber for each new request. If the same value is sent within 30 minutes it will be considered a duplicate request. Note: value is not searchable or reportable in ConnexPay portal.  Alphanumeric.
    SequenceNumber: str

    ReturnRetryCard: ReturnItemRequestRequestReturnRetryCard

class ReturnItemRequestRequest(RequiredReturnItemRequestRequest, OptionalReturnItemRequestRequest):
    pass
