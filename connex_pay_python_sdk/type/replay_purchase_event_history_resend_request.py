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


class RequiredReplayPurchaseEventHistoryResendRequest(TypedDict):
    pass

class OptionalReplayPurchaseEventHistoryResendRequest(TypedDict, total=False):
    # The unique GUID for a particular purchase.  This would be the Guid returned on your virtual card, lodged card, physical card or ACH issue call.
    SourceGuid: str

    # Include your Merchant Guid instead of the Source Guid if you want to see all events for a given date range (you must also include the date range parameters)
    MerchantGuid: str

    # Transaction ID as displayed in Bridge
    EventGuid: str

    # From date
    FromDateTime: date

    # To date
    ToDateTime: date

class ReplayPurchaseEventHistoryResendRequest(RequiredReplayPurchaseEventHistoryResendRequest, OptionalReplayPurchaseEventHistoryResendRequest):
    pass
