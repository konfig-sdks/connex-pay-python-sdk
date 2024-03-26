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

from connex_pay_python_sdk.pydantic.authentication_acquire_client_authorization_request_bank_account import AuthenticationAcquireClientAuthorizationRequestBankAccount
from connex_pay_python_sdk.pydantic.authentication_acquire_client_authorization_request_browser_data import AuthenticationAcquireClientAuthorizationRequestBrowserData
from connex_pay_python_sdk.pydantic.authentication_acquire_client_authorization_request_card import AuthenticationAcquireClientAuthorizationRequestCard
from connex_pay_python_sdk.pydantic.authentication_acquire_client_authorization_request_customer import AuthenticationAcquireClientAuthorizationRequestCustomer
from connex_pay_python_sdk.pydantic.authentication_acquire_client_authorization_request_enhanced_data import AuthenticationAcquireClientAuthorizationRequestEnhancedData
from connex_pay_python_sdk.pydantic.authentication_acquire_client_authorization_request_risk_data import AuthenticationAcquireClientAuthorizationRequestRiskData

class AuthenticationAcquireClientAuthorizationRequest(BaseModel):
    # Device's Guid provided by ConnexPay.
    device_guid: str = Field(alias='DeviceGuid')

    # Amount of the transaction that will be processed. Note: this value is submitted multiple times (in different formats) within the integration to support different purposes i.e. risk analysis, merchant processing, etc.  The minimum amount is: $0.50.
    amount: typing.Union[int, float] = Field(alias='Amount')

    risk_data: AuthenticationAcquireClientAuthorizationRequestRiskData = Field(alias='RiskData')

    # Transaction sequence number within client environment. Provide a unique SequenceNumber for each new request. If the same value is sent within 30 minutes it will be considered a duplicate request. Note: value is not searchable or reportable in ConnexPay portal.  Alphanumeric.
    sequence_number: typing.Optional[str] = Field(None, alias='SequenceNumber')

    # This is the most common number you'll see throughout the ConnexPay Portal.  Transaction ID within client environment associated with the order. The value is searchable and reportable in the ConnexPay portal. This value may be sent in multiple instances of the integration for multiple purposes. Customers in the travel space often send the Record Locator/PNR in this field.  The maximum length is 50 alpha-numeric characters.
    order_number: typing.Optional[str] = Field(None, alias='OrderNumber')

    # Value determines whether or not a customer shall be emailed a receipt from the ConnexPay platform if the email address is provided in the API customer block. The default value is TRUE. Set to FALSE so that an email receipt is not sent to the customer. Set to TRUE or leave empty if you want e-mail to be sent. If TRUE, customer's email must be included in the \"Card.Customer.email\" parameter.
    send_receipt: typing.Optional[bool] = Field(None, alias='SendReceipt')

    # US Clients only: The statement description allows a client to customize the Merchant name that appears on the cardholder statement such that the cardholder recognizes the transaction on their statement. ConnexPay recommends sending a recognizable DBA along with the PNR i.e. ABC Travel ABC123. Note: functionality not applicable for American Express OptBlue program.  The maximun length is 25 alpha-numeric characters.
    statement_description: typing.Optional[str] = Field(None, alias='StatementDescription')

    # Transaction ID within client environment associated with the customer. This value acts as a secondary identifier in conjunction with OrderNumber. The value is searchable and reportable in the ConnexPay portal. This value may be sent in multiple times within the integration for multiple purposes.  The maximum length is 100 characters and is alpha-numeric.
    customer_i_d: typing.Optional[str] = Field(None, alias='CustomerID')

    card: typing.Optional[AuthenticationAcquireClientAuthorizationRequestCard] = Field(None, alias='Card')

    bank_account: typing.Optional[AuthenticationAcquireClientAuthorizationRequestBankAccount] = Field(None, alias='BankAccount')

    customer: typing.Optional[AuthenticationAcquireClientAuthorizationRequestCustomer] = Field(None, alias='Customer')

    enhanced_data: typing.Optional[AuthenticationAcquireClientAuthorizationRequestEnhancedData] = Field(None, alias='EnhancedData')

    # Utilize the Association ID field to tie a virtual card to a sale or sales. For example, if you have several sales and one virtual card payment to a supplier, you can add association ID to the sales and the virtual card for downstream reporting.
    association_i_d: typing.Optional[str] = Field(None, alias='AssociationID')

    browser_data: typing.Optional[AuthenticationAcquireClientAuthorizationRequestBrowserData] = Field(None, alias='BrowserData')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
