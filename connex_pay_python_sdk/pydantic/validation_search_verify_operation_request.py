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


class ValidationSearchVerifyOperationRequest(BaseModel):
    # Merchant’s Guid.
    merchant_guid: typing.Optional[str] = Field(None, alias='MerchantGuid')

    # Card last four number.
    card_last_four: typing.Optional[str] = Field(None, alias='CardLastFour')

    # Cardholder’s name. Providing information in this field allows a user of the ConnexPay portal to search for a transaction using the cardholder name.
    card_holder_name: typing.Optional[str] = Field(None, alias='CardHolderName')

    # Card Type.
    card_type: typing.Optional[str] = Field(None, alias='CardType')

    # Verify’s TimeStamp From.
    time_stamp_from: typing.Optional[date] = Field(None, alias='TimeStampFrom')

    # Verify’s TimeStamp To.
    time_stamp_to: typing.Optional[date] = Field(None, alias='TimeStampTo')

    # Verify’s status.  Allowed values:  1. Transaction - Approved 2. Transaction - Declined 3. Transaction - Created - Local 4. Transaction - Created - Error: Processor not reached 5. Transaction - Processor Error 6. Transaction - Approved - Warning
    status: typing.Optional[str] = Field(None, alias='Status')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
