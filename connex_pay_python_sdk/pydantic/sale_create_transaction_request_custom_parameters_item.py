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


class SaleCreateTransactionRequestCustomParametersItem(BaseModel):
    # Custom Parameter's Name, up to a maximum of 100 alphanumeric characters allowed.
    name: typing.Optional[str] = Field(None, alias='Name')

    # Custom Parameter's Value, up to a maximum of 100 alphanumeric characters allowed.
    value: typing.Optional[str] = Field(None, alias='Value')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
