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


class CardSearchIssuedVirtualCardsRequest(BaseModel):
    # Your assigned Merchant GUID.
    merchant_guid: str = Field(alias='MerchantGuid')

    # Sale GUID linked to the card you are searching.
    sale_guid: typing.Optional[str] = Field(None, alias='SaleGuid')

    # Incoming Transaction Code linked to the card you are searching.
    incoming_transaction_code: typing.Optional[str] = Field(None, alias='IncomingTransactionCode')

    # Order Number linked to the card you are searching.
    order_number: typing.Optional[str] = Field(None, alias='OrderNumber')

    # Order Number linked to the card you are searching.
    customer_i_d: typing.Optional[str] = Field(None, alias='CustomerID')

    # Starting Issued Date linked to the card(s) you are searching.
    time_stamp_from: typing.Optional[date] = Field(None, alias='TimeStampFrom')

    # Ending Issued Date linked to the card(s) you are searching.
    time_stamp_to: typing.Optional[date] = Field(None, alias='TimeStampTo')

    # Start of Issued Amount range linked to the card(s) you are searching.
    issued_amount_from: typing.Optional[typing.Union[int, float]] = Field(None, alias='IssuedAmountFrom')

    # End of Issued Amount range linked to the card(s) you are searching.
    issued_amount_to: typing.Optional[typing.Union[int, float]] = Field(None, alias='IssuedAmountTo')

    # Outgoing Transaction Code linked to the card(s) you are searching.
    outgoing_transaction_code: typing.Optional[str] = Field(None, alias='OutgoingTransactionCode')

    # Start of Settled Amount range linked to the card(s) you are searching.
    settled_amount_from: typing.Optional[int] = Field(None, alias='SettledAmountFrom')

    # End of Settled Amount range linked to the card(s) you are searching.
    settled_amount_to: typing.Optional[int] = Field(None, alias='SettledAmountTo')

    # Start of Settled Returned Amount range linked to the card(s) you are searching.
    returned_amount_from: typing.Optional[int] = Field(None, alias='ReturnedAmountFrom')

    # End of Settled Returned Amount range linked to the card(s) you are searching.
    returned_amount_to: typing.Optional[int] = Field(None, alias='ReturnedAmountTo')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
