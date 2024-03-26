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

from connex_pay_python_sdk.pydantic.funding_merchant_cash_balance_response_bank_account import FundingMerchantCashBalanceResponseBankAccount

class FundingMerchantCashBalanceResponse(BaseModel):
    merchant_guid: typing.Optional[str] = Field(None, alias='merchantGuid')

    request_ip: typing.Optional[str] = Field(None, alias='requestIp')

    amount: typing.Optional[typing.Union[int, float]] = Field(None, alias='amount')

    is_fund_cash_balance: typing.Optional[bool] = Field(None, alias='isFundCashBalance')

    bank_account: typing.Optional[FundingMerchantCashBalanceResponseBankAccount] = Field(None, alias='bankAccount')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
