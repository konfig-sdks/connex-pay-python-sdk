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


class ReplayPurchaseEventHistoryResendRequest(BaseModel):
    # The unique GUID for a particular purchase.  This would be the Guid returned on your virtual card, lodged card, physical card or ACH issue call.
    source_guid: typing.Optional[str] = Field(None, alias='SourceGuid')

    # Include your Merchant Guid instead of the Source Guid if you want to see all events for a given date range (you must also include the date range parameters)
    merchant_guid: typing.Optional[str] = Field(None, alias='MerchantGuid')

    # Transaction ID as displayed in Bridge
    event_guid: typing.Optional[str] = Field(None, alias='EventGuid')

    # From date
    from_date_time: typing.Optional[date] = Field(None, alias='FromDateTime')

    # To date
    to_date_time: typing.Optional[date] = Field(None, alias='ToDateTime')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
