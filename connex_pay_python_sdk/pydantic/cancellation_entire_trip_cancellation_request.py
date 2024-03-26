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


class CancellationEntireTripCancellationRequest(BaseModel):
    # Device's Guid provided by ConnexPay
    device_guid: str = Field(alias='DeviceGuid')

    # Sale transaction Guid
    sale_guid: str = Field(alias='SaleGuid')

    # Transaction sequence number within client environment. Provide a unique SequenceNumber for each new request. If the same value is sent within 30 minutes it will be considered a duplicate request. Note: value is not searchable or reportable in ConnexPay portal.  Alphanumeric.
    sequence_number: typing.Optional[str] = Field(None, alias='SequenceNumber')

    # Indicates the reason the transaction was voided
    void_reason: typing.Optional[str] = Field(None, alias='VoidReason')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
