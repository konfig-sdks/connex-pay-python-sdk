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

from connex_pay_python_sdk.pydantic.return_item_request_request_return_retry_card import ReturnItemRequestRequestReturnRetryCard

class ReturnItemRequestRequest(BaseModel):
    # Device's Guid
    device_guid: str = Field(alias='DeviceGuid')

    # Transaction’s amount. Min. amt.: $0.50
    amount: typing.Union[int, float] = Field(alias='Amount')

    # Mandatory when SaleReferenceNumber field is not sent. Sale's Guid.
    sale_guid: typing.Optional[str] = Field(None, alias='SaleGuid')

    # Mandatory when SaleGuid field is not sent. Sale's Reference Number
    sale_reference_number: typing.Optional[int] = Field(None, alias='SaleReferenceNumber')

    # Transaction sequence number within client environment. Provide a unique SequenceNumber for each new request. If the same value is sent within 30 minutes it will be considered a duplicate request. Note: value is not searchable or reportable in ConnexPay portal.  Alphanumeric.
    sequence_number: typing.Optional[str] = Field(None, alias='SequenceNumber')

    return_retry_card: typing.Optional[ReturnItemRequestRequestReturnRetryCard] = Field(None, alias='ReturnRetryCard')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
