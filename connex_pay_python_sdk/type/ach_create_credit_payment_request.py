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

from connex_pay_python_sdk.type.ach_create_credit_payment_request_account_holder import AchCreateCreditPaymentRequestAccountHolder

class RequiredAchCreateCreditPaymentRequest(TypedDict):
    # Merchant's guid. Application level value that indicates the ACH payment is being requested for clients account. Value provided by ConnexPay.
    MerchantGuid: str

    # Payment amount with the minimum amount > 0.5.
    Amount: typing.Union[int, float]

    # Payee name up to 100 characters.
    PayeeName: str

    AccountHolder: AchCreateCreditPaymentRequestAccountHolder

class OptionalAchCreateCreditPaymentRequest(TypedDict, total=False):
    # Company Name to display Bank Statement. The first 16 characters will display on the bank account holders statement.
    StatementCompanyName: str

    # For banks who accept statement descriptors, the first 10 characters will display on the bank account holders statement.
    Description: str

    # This is the most common number you'll see throughout the ConnexPay Portal.  Transaction ID within client environment associated with the order. The value is searchable and reportable in the ConnexPay portal. This value may be sent in multiple instances of the integration for multiple purposes. Customers in the travel space often send the Record Locator/PNR in this field.  The maximum length is 50 alpha-numeric characters.
    OrderNumber: str

    # Transaction sequence number within client environment. Note: value is not searchable or reportable in ConnexPay portal.  Alphanumeric.
    SequenceNumber: str

    # This parameter allows you to input an up to 100 character association ID that can be used to tie this ACH Purchase to a sale (Association ID also needs to be included on the sale request). This is useful if you issue the ACH purchase prior to creating the sale that associates to it.
    AssociationId: str

class AchCreateCreditPaymentRequest(RequiredAchCreateCreditPaymentRequest, OptionalAchCreateCreditPaymentRequest):
    pass
