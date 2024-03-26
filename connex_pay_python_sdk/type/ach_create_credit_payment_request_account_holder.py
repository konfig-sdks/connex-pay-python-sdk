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

from connex_pay_python_sdk.type.ach_create_credit_payment_request_account_holder_address import AchCreateCreditPaymentRequestAccountHolderAddress
from connex_pay_python_sdk.type.ach_create_credit_payment_request_account_holder_bank_account import AchCreateCreditPaymentRequestAccountHolderBankAccount

class RequiredAchCreateCreditPaymentRequestAccountHolder(TypedDict):
    pass

class OptionalAchCreateCreditPaymentRequestAccountHolder(TypedDict, total=False):
    # Conditional -  Payee's First name between 2 to 40 characters. Can be left blank if BusinessName is provided
    FirstName: str

    # Conditional - Payee's Last name between 2 to 40 characters. Can be left blank if BusinessName is provided
    LastName: str

    # Payee's Middle name
    MiddleName: str

    # Conditional - Can be left blank if FirstName and LastName are provided
    BusinessName: str

    # Email up to 100 characters
    Email: str

    # Phone number up to 10 characters
    Phone: str

    Address: AchCreateCreditPaymentRequestAccountHolderAddress

    BankAccount: AchCreateCreditPaymentRequestAccountHolderBankAccount

class AchCreateCreditPaymentRequestAccountHolder(RequiredAchCreateCreditPaymentRequestAccountHolder, OptionalAchCreateCreditPaymentRequestAccountHolder):
    pass
