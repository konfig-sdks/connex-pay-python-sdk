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


class SaleUpdateDelayedActivationRequest(BaseModel):
    # Device's Guid provided by ConnexPay.
    device_guid: str = Field(alias='DeviceGuid')

    # Sales's Guid that was provided by ConnexPay upon initial creation of the delayed activation sale.
    sale_guid: str = Field(alias='SaleGuid')

    # Amount of the transaction that will be processed. Note: this value is submitted multiple times (in different formats) within the integration to support different purposes i.e. risk analysis, merchant processing, etc.  The minimun amount is: $0.50.
    amount: typing.Union[int, float] = Field(alias='Amount')

    # Set a future date on which to run this sale, at least one day from creation date and within 600 days.
    activation_date: typing.Optional[date] = Field(None, alias='ActivationDate')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
