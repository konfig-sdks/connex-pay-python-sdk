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


class RequiredCardSearchIssuedVirtualCardsRequest(TypedDict):
    # Your assigned Merchant GUID.
    MerchantGuid: str

class OptionalCardSearchIssuedVirtualCardsRequest(TypedDict, total=False):
    # Sale GUID linked to the card you are searching.
    SaleGuid: str

    # Incoming Transaction Code linked to the card you are searching.
    IncomingTransactionCode: str

    # Order Number linked to the card you are searching.
    OrderNumber: str

    # Order Number linked to the card you are searching.
    CustomerID: str

    # Starting Issued Date linked to the card(s) you are searching.
    TimeStampFrom: date

    # Ending Issued Date linked to the card(s) you are searching.
    TimeStampTo: date

    # Start of Issued Amount range linked to the card(s) you are searching.
    IssuedAmountFrom: typing.Union[int, float]

    # End of Issued Amount range linked to the card(s) you are searching.
    IssuedAmountTo: typing.Union[int, float]

    # Outgoing Transaction Code linked to the card(s) you are searching.
    OutgoingTransactionCode: str

    # Start of Settled Amount range linked to the card(s) you are searching.
    SettledAmountFrom: int

    # End of Settled Amount range linked to the card(s) you are searching.
    SettledAmountTo: int

    # Start of Settled Returned Amount range linked to the card(s) you are searching.
    ReturnedAmountFrom: int

    # End of Settled Returned Amount range linked to the card(s) you are searching.
    ReturnedAmountTo: int

class CardSearchIssuedVirtualCardsRequest(RequiredCardSearchIssuedVirtualCardsRequest, OptionalCardSearchIssuedVirtualCardsRequest):
    pass
