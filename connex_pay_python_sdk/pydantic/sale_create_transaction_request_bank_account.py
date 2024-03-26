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

from connex_pay_python_sdk.pydantic.sale_create_transaction_request_bank_account_customer import SaleCreateTransactionRequestBankAccountCustomer

class SaleCreateTransactionRequestBankAccount(BaseModel):
    # Accepted account types are: Saving or Checking
    account_type: str = Field(alias='AccountType')

    # 9 Digit routing number
    routing_number: str = Field(alias='RoutingNumber')

    # Account number up to 20 characters
    account_number: str = Field(alias='AccountNumber')

    # Name on the account for ACH transfer (upto 50 characters)
    name_on_account: str = Field(alias='NameOnAccount')

    # Encrypted Token previously assigned to Bank Account. Either AccountAndRoutingNumberToken or both AccountNumber  and RoutingNumber  should be provided.
    account_and_routing_number_token: typing.Optional[str] = Field(None, alias='AccountAndRoutingNumberToken')

    customer: typing.Optional[SaleCreateTransactionRequestBankAccountCustomer] = Field(None, alias='Customer')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
