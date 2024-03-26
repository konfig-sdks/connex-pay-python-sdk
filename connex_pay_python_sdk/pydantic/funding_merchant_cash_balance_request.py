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


class FundingMerchantCashBalanceRequest(BaseModel):
    # The merchant's GUID. Value provided by ConnexPay.
    merchant_g_u_i_d: str = Field(alias='merchantGUID')

    # Self-service funding amount that will be processed. Maximum transaction and daily funding limits are set by ConnexPay.
    amount: typing.Union[int, float] = Field(alias='amount')

    # true: Fund your merchant cash balance from your merchant bank account. false: Withdraw your merchant cash balance and ConnexPay will credit your merchant bank account.
    is_fund_cash_balance: bool = Field(alias='isFundCashBalance')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
