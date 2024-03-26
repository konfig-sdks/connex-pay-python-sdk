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


class CardIssueCreateVirtualCardLiteRequestCustomParametersItem(BaseModel):
    # The custom parameter name can be anything you want to label the field. You can include as many custom parameters as needed to provide additional data to be included for the virtual card.
    name: typing.Optional[str] = Field(None, alias='Name')

    # The value associated with this parameter. For example, if you are including an invoice number with your virtual card request, you would populate the custom parameter 'Name' as 'Invoice' and the custom parameter 'Value' as the invoice number.
    value: typing.Optional[str] = Field(None, alias='Value')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
