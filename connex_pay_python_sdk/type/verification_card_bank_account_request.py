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

from connex_pay_python_sdk.type.verification_card_bank_account_request_bank_account import VerificationCardBankAccountRequestBankAccount
from connex_pay_python_sdk.type.verification_card_bank_account_request_card import VerificationCardBankAccountRequestCard

class RequiredVerificationCardBankAccountRequest(TypedDict):
    # Device's Guid provided by ConnexPay.
    DeviceGuid: str

class OptionalVerificationCardBankAccountRequest(TypedDict, total=False):
    Card: VerificationCardBankAccountRequestCard

    BankAccount: VerificationCardBankAccountRequestBankAccount

class VerificationCardBankAccountRequest(RequiredVerificationCardBankAccountRequest, OptionalVerificationCardBankAccountRequest):
    pass
