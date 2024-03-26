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


class RequiredSaleUpdateDelayedActivationRequest(TypedDict):
    # Device's Guid provided by ConnexPay.
    DeviceGuid: str

    # Sales's Guid that was provided by ConnexPay upon initial creation of the delayed activation sale.
    SaleGuid: str

    # Amount of the transaction that will be processed. Note: this value is submitted multiple times (in different formats) within the integration to support different purposes i.e. risk analysis, merchant processing, etc.  The minimun amount is: $0.50.
    Amount: typing.Union[int, float]

class OptionalSaleUpdateDelayedActivationRequest(TypedDict, total=False):
    # Set a future date on which to run this sale, at least one day from creation date and within 600 days.
    ActivationDate: date

class SaleUpdateDelayedActivationRequest(RequiredSaleUpdateDelayedActivationRequest, OptionalSaleUpdateDelayedActivationRequest):
    pass
