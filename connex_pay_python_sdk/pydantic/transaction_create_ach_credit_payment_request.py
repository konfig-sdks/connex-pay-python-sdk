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

from connex_pay_python_sdk.pydantic.transaction_create_ach_credit_payment_request_account_holder import TransactionCreateAchCreditPaymentRequestAccountHolder

class TransactionCreateAchCreditPaymentRequest(BaseModel):
    # Merchant's guid. Application level value that indicates the ACH payment is being requested for clients account. Value provided by ConnexPay.
    merchant_guid: str = Field(alias='MerchantGuid')

    # Payment amount. Minimum amount > 0.5.
    amount: typing.Union[int, float] = Field(alias='Amount')

    # Payee name up to 100 characters.
    payee_name: str = Field(alias='PayeeName')

    # ITC for short Application level setting to associate the ACH payment request with an original sale or sale group. The value is provided in the sale response of the original sale transaction, or in the Group Sale response of the group sale. All ACH payment requests must be associated with an original sale or group transaction.
    incoming_transaction_code: str = Field(alias='IncomingTransactionCode')

    account_holder: TransactionCreateAchCreditPaymentRequestAccountHolder = Field(alias='AccountHolder')

    # Company Name to display Bank Statement. The first 16 characters will display on the bank account holders statement.
    statement_company_name: typing.Optional[str] = Field(None, alias='StatementCompanyName')

    # For banks who accept statement descriptors, the first 10 characters will display on the bank account holders statement.
    description: typing.Optional[str] = Field(None, alias='Description')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
