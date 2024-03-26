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

from connex_pay_python_sdk.pydantic.ach_create_credit_payment_request_account_holder import AchCreateCreditPaymentRequestAccountHolder

class AchCreateCreditPaymentRequest(BaseModel):
    # Merchant's guid. Application level value that indicates the ACH payment is being requested for clients account. Value provided by ConnexPay.
    merchant_guid: str = Field(alias='MerchantGuid')

    # Payment amount with the minimum amount > 0.5.
    amount: typing.Union[int, float] = Field(alias='Amount')

    # Payee name up to 100 characters.
    payee_name: str = Field(alias='PayeeName')

    account_holder: AchCreateCreditPaymentRequestAccountHolder = Field(alias='AccountHolder')

    # Company Name to display Bank Statement. The first 16 characters will display on the bank account holders statement.
    statement_company_name: typing.Optional[str] = Field(None, alias='StatementCompanyName')

    # For banks who accept statement descriptors, the first 10 characters will display on the bank account holders statement.
    description: typing.Optional[str] = Field(None, alias='Description')

    # This is the most common number you'll see throughout the ConnexPay Portal.  Transaction ID within client environment associated with the order. The value is searchable and reportable in the ConnexPay portal. This value may be sent in multiple instances of the integration for multiple purposes. Customers in the travel space often send the Record Locator/PNR in this field.  The maximum length is 50 alpha-numeric characters.
    order_number: typing.Optional[str] = Field(None, alias='OrderNumber')

    # Transaction sequence number within client environment. Note: value is not searchable or reportable in ConnexPay portal.  Alphanumeric.
    sequence_number: typing.Optional[str] = Field(None, alias='SequenceNumber')

    # This parameter allows you to input an up to 100 character association ID that can be used to tie this ACH Purchase to a sale (Association ID also needs to be included on the sale request). This is useful if you issue the ACH purchase prior to creating the sale that associates to it.
    association_id: typing.Optional[str] = Field(None, alias='AssociationId')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
