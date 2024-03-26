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


class RequiredVoidCreateVoidRequest(TypedDict):
    # Device’s Guid provided by ConnexPay.
    DeviceGuid: str

class OptionalVoidCreateVoidRequest(TypedDict, total=False):
    # Sale Transaction Guid
    SaleGuid: str

    # Return's Guid
    ReturnGuid: str

    # Sale Reference Number
    SaleReferenceNumber: int

    # Guid to include in request when voiding an Auth Only request.
    AuthOnlyGuid: str

    # Indicates the reason the transaction was voided.  Allowed values:  1. POST_AUTH_USER_DECLINE 2. DEVICE_TIMEOUT 3. DEVICE_UNAVAILABLE 4. PARTIAL_REVERSAL 5. TORN_TRANSACTIONS 6. POST_AUTH_CHIP_DECLINE
    VoidReason: str

    # Amount to be voided.  Note: Amount is be used once only for credit card Sales and should not exceed corresponding Sale’s Amount.
    Amount: typing.Union[int, float]

    # Transaction sequence number within client environment. Provide a unique SequenceNumber for each new request. If the same value is sent within 30 minutes it will be considered a duplicate request. Note: value is not searchable or reportable in ConnexPay portal.  Alphanumeric.
    SequenceNumber: str

class VoidCreateVoidRequest(RequiredVoidCreateVoidRequest, OptionalVoidCreateVoidRequest):
    pass
