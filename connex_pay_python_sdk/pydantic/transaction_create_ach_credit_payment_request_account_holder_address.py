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


class TransactionCreateAchCreditPaymentRequestAccountHolderAddress(BaseModel):
    # Address 1 up to 50 characters
    address1: typing.Optional[str] = Field(None, alias='Address1')

    # Address 2 up to 50 characters
    address2: typing.Optional[str] = Field(None, alias='Address2')

    # City up to 50 characters
    city: typing.Optional[str] = Field(None, alias='City')

    # US State up to 2 characters
    state: typing.Optional[str] = Field(None, alias='State')

    # Country. 'US' only as of now
    country: typing.Optional[str] = Field(None, alias='Country')

    # ZipCode up to 10 characters
    zip_code: typing.Optional[str] = Field(None, alias='ZipCode')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
