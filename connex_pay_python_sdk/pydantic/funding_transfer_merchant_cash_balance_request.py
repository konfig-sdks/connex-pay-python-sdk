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


class FundingTransferMerchantCashBalanceRequest(BaseModel):
    # The merchant's GUID of the withdrawn account. Value provided by ConnexPay.
    transferred_from: str = Field(alias='TransferredFrom')

    # The merchant's GUID of the deposited account. Value provided by ConnexPay.
    transferred_to: str = Field(alias='TransferredTo')

    # Transferred funding amount that will be processed. Maximum transaction and daily funding limits are set by ConnexPay.
    amount: typing.Union[int, float] = Field(alias='Amount')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
