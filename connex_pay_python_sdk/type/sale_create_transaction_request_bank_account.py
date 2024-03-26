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

from connex_pay_python_sdk.type.sale_create_transaction_request_bank_account_customer import SaleCreateTransactionRequestBankAccountCustomer

class RequiredSaleCreateTransactionRequestBankAccount(TypedDict):
    # Accepted account types are: Saving or Checking
    AccountType: str

    # 9 Digit routing number
    RoutingNumber: str

    # Account number up to 20 characters
    AccountNumber: str

    # Name on the account for ACH transfer (upto 50 characters)
    NameOnAccount: str

class OptionalSaleCreateTransactionRequestBankAccount(TypedDict, total=False):
    # Encrypted Token previously assigned to Bank Account. Either AccountAndRoutingNumberToken or both AccountNumber  and RoutingNumber  should be provided.
    AccountAndRoutingNumberToken: str

    Customer: SaleCreateTransactionRequestBankAccountCustomer

class SaleCreateTransactionRequestBankAccount(RequiredSaleCreateTransactionRequestBankAccount, OptionalSaleCreateTransactionRequestBankAccount):
    pass
