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

from connex_pay_python_sdk.type.sale_create_transaction201_response_bank_account_customer import SaleCreateTransaction201ResponseBankAccountCustomer

class RequiredSaleCreateTransaction201ResponseBankAccount(TypedDict):
    pass

class OptionalSaleCreateTransaction201ResponseBankAccount(TypedDict, total=False):
    guid: str

    accountType: str

    accountNumberLastFour: str

    nameOnAccount: str

    customer: SaleCreateTransaction201ResponseBankAccountCustomer

class SaleCreateTransaction201ResponseBankAccount(RequiredSaleCreateTransaction201ResponseBankAccount, OptionalSaleCreateTransaction201ResponseBankAccount):
    pass
