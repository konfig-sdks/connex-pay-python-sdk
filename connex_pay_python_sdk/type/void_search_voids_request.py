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


class RequiredVoidSearchVoidsRequest(TypedDict):
    pass

class OptionalVoidSearchVoidsRequest(TypedDict, total=False):
    # Merchant’s Guid.
    MerchantGuid: str

    # Indicates the reason the transaction was voided.  Allowed values:  1. POST_AUTH_USER_DECLINE 2. DEVICE_TIMEOUT 3. DEVICE_UNAVAILABLE 4. PARTIAL_REVERSAL 5. TORN_TRANSACTIONS 6. POST_AUTH_CHIP_DECLINE
    VoidReason: str

    # Void’s status.  Allowed values:  1. Transaction - Approved 2. Transaction - Declined 3. Transaction - Created - Local 4. Transaction - Created - Error: Processor not reached 5. Transaction - Processor Error 6. Transaction - Approved - Warning
    Status: str

    # Void’s TimeStamp.
    TimeStampFrom: date

    # Void’s TimeStamp.
    TimeStampTo: date

class VoidSearchVoidsRequest(RequiredVoidSearchVoidsRequest, OptionalVoidSearchVoidsRequest):
    pass
