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


class RequiredCancellationEntireTripCancellationRequest(TypedDict):
    # Device's Guid provided by ConnexPay
    DeviceGuid: str

    # Sale transaction Guid
    SaleGuid: str

class OptionalCancellationEntireTripCancellationRequest(TypedDict, total=False):
    # Transaction sequence number within client environment. Provide a unique SequenceNumber for each new request. If the same value is sent within 30 minutes it will be considered a duplicate request. Note: value is not searchable or reportable in ConnexPay portal.  Alphanumeric.
    SequenceNumber: str

    # Indicates the reason the transaction was voided
    VoidReason: str

class CancellationEntireTripCancellationRequest(RequiredCancellationEntireTripCancellationRequest, OptionalCancellationEntireTripCancellationRequest):
    pass
