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

from connex_pay_python_sdk.pydantic.verification_card_bank_account_request_bank_account import VerificationCardBankAccountRequestBankAccount
from connex_pay_python_sdk.pydantic.verification_card_bank_account_request_card import VerificationCardBankAccountRequestCard

class VerificationCardBankAccountRequest(BaseModel):
    # Device's Guid provided by ConnexPay.
    device_guid: str = Field(alias='DeviceGuid')

    card: typing.Optional[VerificationCardBankAccountRequestCard] = Field(None, alias='Card')

    bank_account: typing.Optional[VerificationCardBankAccountRequestBankAccount] = Field(None, alias='BankAccount')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
