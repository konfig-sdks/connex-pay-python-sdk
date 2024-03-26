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


class CardUpdateDelayedActivationRequest(BaseModel):
    # Merchant's guid. Application level value that indicates a virtual card is being requested for clients account. Value provided by ConnexPay.
    merchant_guid: str = Field(alias='MerchantGuid')

    # Provide a future date, up to 600 days, if you wish to update the virtual card's activation date. Otherwise leave blank.
    activation_date: typing.Optional[date] = Field(None, alias='ActivationDate')

    # Provide a card amount if you wish to update the amount limit for the virtual card, otherwise leave blank.
    amount_limit: typing.Optional[typing.Union[int, float]] = Field(None, alias='AmountLimit')

    # The TerminateDate (YYYY-MM-DD format) is the date the Virtual Credit Card will be terminated by ConnexPay. TerminateDate is different than ExpirationDate in that TerminateDate indicates the actual date the card will no longer be active.  ExpirationDate is the month and year that will be applied to the actual VCC. The recommendation is to set the ExpirationDate one or two years in the future and set the TerminateDate just a day or two after the VCC is expected to be processed. Note, Returns can still be processed on terminated VCCs.
    terminate_date: typing.Optional[date] = Field(None, alias='TerminateDate')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
