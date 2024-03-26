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

from connex_pay_python_sdk.pydantic.transaction_create_ach_credit_payment_request_account_holder_address import TransactionCreateAchCreditPaymentRequestAccountHolderAddress
from connex_pay_python_sdk.pydantic.transaction_create_ach_credit_payment_request_account_holder_bank_account import TransactionCreateAchCreditPaymentRequestAccountHolderBankAccount

class TransactionCreateAchCreditPaymentRequestAccountHolder(BaseModel):
    # Conditional -  Payee's First name between 2 to 40 characters. Can be left blank if BusinessName is provided
    first_name: typing.Optional[str] = Field(None, alias='FirstName')

    # Conditional - Payee's Last name between 2 to 40 characters. Can be left blank if BusinessName is provided
    last_name: typing.Optional[str] = Field(None, alias='LastName')

    # Payee's Middle name
    middle_name: typing.Optional[str] = Field(None, alias='MiddleName')

    # Conditional - Can be left blank if FirstName and LastName are provided
    business_name: typing.Optional[str] = Field(None, alias='BusinessName')

    # Email up to 100 characters
    email: typing.Optional[str] = Field(None, alias='Email')

    # Phone number up to 10 characters
    phone: typing.Optional[str] = Field(None, alias='Phone')

    address: typing.Optional[TransactionCreateAchCreditPaymentRequestAccountHolderAddress] = Field(None, alias='Address')

    bank_account: typing.Optional[TransactionCreateAchCreditPaymentRequestAccountHolderBankAccount] = Field(None, alias='BankAccount')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
