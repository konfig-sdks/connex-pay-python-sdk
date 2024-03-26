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


class VoidCreateVoidRequest(BaseModel):
    # Device’s Guid provided by ConnexPay.
    device_guid: str = Field(alias='DeviceGuid')

    # Sale Transaction Guid
    sale_guid: typing.Optional[str] = Field(None, alias='SaleGuid')

    # Return's Guid
    return_guid: typing.Optional[str] = Field(None, alias='ReturnGuid')

    # Sale Reference Number
    sale_reference_number: typing.Optional[int] = Field(None, alias='SaleReferenceNumber')

    # Guid to include in request when voiding an Auth Only request.
    auth_only_guid: typing.Optional[str] = Field(None, alias='AuthOnlyGuid')

    # Indicates the reason the transaction was voided.  Allowed values:  1. POST_AUTH_USER_DECLINE 2. DEVICE_TIMEOUT 3. DEVICE_UNAVAILABLE 4. PARTIAL_REVERSAL 5. TORN_TRANSACTIONS 6. POST_AUTH_CHIP_DECLINE
    void_reason: typing.Optional[str] = Field(None, alias='VoidReason')

    # Amount to be voided.  Note: Amount is be used once only for credit card Sales and should not exceed corresponding Sale’s Amount.
    amount: typing.Optional[typing.Union[int, float]] = Field(None, alias='Amount')

    # Transaction sequence number within client environment. Provide a unique SequenceNumber for each new request. If the same value is sent within 30 minutes it will be considered a duplicate request. Note: value is not searchable or reportable in ConnexPay portal.  Alphanumeric.
    sequence_number: typing.Optional[str] = Field(None, alias='SequenceNumber')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
