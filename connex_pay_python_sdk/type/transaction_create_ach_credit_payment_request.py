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

from connex_pay_python_sdk.type.transaction_create_ach_credit_payment_request_account_holder import TransactionCreateAchCreditPaymentRequestAccountHolder

class RequiredTransactionCreateAchCreditPaymentRequest(TypedDict):
    # Merchant's guid. Application level value that indicates the ACH payment is being requested for clients account. Value provided by ConnexPay.
    MerchantGuid: str

    # Payment amount. Minimum amount > 0.5.
    Amount: typing.Union[int, float]

    # Payee name up to 100 characters.
    PayeeName: str

    # ITC for short Application level setting to associate the ACH payment request with an original sale or sale group. The value is provided in the sale response of the original sale transaction, or in the Group Sale response of the group sale. All ACH payment requests must be associated with an original sale or group transaction.
    IncomingTransactionCode: str

    AccountHolder: TransactionCreateAchCreditPaymentRequestAccountHolder

class OptionalTransactionCreateAchCreditPaymentRequest(TypedDict, total=False):
    # Company Name to display Bank Statement. The first 16 characters will display on the bank account holders statement.
    StatementCompanyName: str

    # For banks who accept statement descriptors, the first 10 characters will display on the bank account holders statement.
    Description: str

class TransactionCreateAchCreditPaymentRequest(RequiredTransactionCreateAchCreditPaymentRequest, OptionalTransactionCreateAchCreditPaymentRequest):
    pass
