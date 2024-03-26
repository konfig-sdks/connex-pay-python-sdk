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


class SettlementSearchVirtualCardSettlementsRequest(BaseModel):
    # Merchant's Guid.
    merchant_guid: str = Field(alias='MerchantGuid')

    # Card's Issued Date.
    date_from: typing.Optional[date] = Field(None, alias='DateFrom')

    # Card's Issued Date.
    date_to: typing.Optional[date] = Field(None, alias='DateTo')

    # Card settlement post date.
    posted_date_from: typing.Optional[date] = Field(None, alias='PostedDateFrom')

    # Card settlement post date.
    posted_date_to: typing.Optional[date] = Field(None, alias='PostedDateTo')

    # Order Number. Max. Length = 50.
    order_number: typing.Optional[str] = Field(None, alias='OrderNumber')

    # Issued Amount of the Card.
    issued_amount_from: typing.Optional[int] = Field(None, alias='IssuedAmountFrom')

    # Issued Amount of the Card.
    issued_amount_to: typing.Optional[int] = Field(None, alias='IssuedAmountTo')

    # Card last four number.
    issued_card_last_four: typing.Optional[str] = Field(None, alias='IssuedCardLastFour')

    # Posted Amount of the Card.
    posted_amount_from: typing.Optional[typing.Union[int, float]] = Field(None, alias='PostedAmountFrom')

    # Posted Amount of the Card.
    posted_amount_to: typing.Optional[typing.Union[int, float]] = Field(None, alias='PostedAmountTo')

    # Card's expiration date.
    expiration_date_from: typing.Optional[date] = Field(None, alias='ExpirationDateFrom')

    # Card's expiration date.
    expiration_date_to: typing.Optional[date] = Field(None, alias='ExpirationDateTo')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
