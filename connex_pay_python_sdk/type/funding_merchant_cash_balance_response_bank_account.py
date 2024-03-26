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

from connex_pay_python_sdk.type.funding_merchant_cash_balance_response_bank_account_customer import FundingMerchantCashBalanceResponseBankAccountCustomer

class RequiredFundingMerchantCashBalanceResponseBankAccount(TypedDict):
    pass

class OptionalFundingMerchantCashBalanceResponseBankAccount(TypedDict, total=False):
    guid: str

    accountType: str

    accountNumberLastFour: str

    nameOnAccount: str

    customer: FundingMerchantCashBalanceResponseBankAccountCustomer

class FundingMerchantCashBalanceResponseBankAccount(RequiredFundingMerchantCashBalanceResponseBankAccount, OptionalFundingMerchantCashBalanceResponseBankAccount):
    pass
