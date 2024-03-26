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


class VoidSearchVoidsRequest(BaseModel):
    # Merchant’s Guid.
    merchant_guid: typing.Optional[str] = Field(None, alias='MerchantGuid')

    # Indicates the reason the transaction was voided.  Allowed values:  1. POST_AUTH_USER_DECLINE 2. DEVICE_TIMEOUT 3. DEVICE_UNAVAILABLE 4. PARTIAL_REVERSAL 5. TORN_TRANSACTIONS 6. POST_AUTH_CHIP_DECLINE
    void_reason: typing.Optional[str] = Field(None, alias='VoidReason')

    # Void’s status.  Allowed values:  1. Transaction - Approved 2. Transaction - Declined 3. Transaction - Created - Local 4. Transaction - Created - Error: Processor not reached 5. Transaction - Processor Error 6. Transaction - Approved - Warning
    status: typing.Optional[str] = Field(None, alias='Status')

    # Void’s TimeStamp.
    time_stamp_from: typing.Optional[date] = Field(None, alias='TimeStampFrom')

    # Void’s TimeStamp.
    time_stamp_to: typing.Optional[date] = Field(None, alias='TimeStampTo')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
