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

from connex_pay_python_sdk.pydantic.transaction_capture_authorization_request_connex_pay_transaction import TransactionCaptureAuthorizationRequestConnexPayTransaction
from connex_pay_python_sdk.pydantic.transaction_capture_authorization_request_custom_parameters import TransactionCaptureAuthorizationRequestCustomParameters

class TransactionCaptureAuthorizationRequest(BaseModel):
    # Device's Guid provided by ConnexPay.
    device_guid: str = Field(alias='DeviceGuid')

    # Guid received from the AuthOnly operation.
    auth_only_guid: str = Field(alias='AuthOnlyGuid')

    # Transaction sequence number within client environment. Provide a unique SequenceNumber for each new request. If the same value is sent within 30 minutes it will be considered a duplicate request. Note: value is not searchable or reportable in ConnexPay portal.  Alphanumeric.
    sequence_number: typing.Optional[str] = Field(None, alias='SequenceNumber')

    connex_pay_transaction: typing.Optional[TransactionCaptureAuthorizationRequestConnexPayTransaction] = Field(None, alias='ConnexPayTransaction')

    # This is the most common number you'll see throughout the ConnexPay Portal. Transaction ID within client environment associated with the order. The value is searchable and reportable in the ConnexPay portal. This value may be sent in multiple instances of the integration for multiple purposes. Customers in the travel space often send the Record Locator/PNR in this field. The maximum length is 50 alpha-numeric characters and allows dashes ( - ). If you provided an order number in the AUTH request it will be overwritten with the order number in the CAPTURE endpoint.
    order_number: typing.Optional[str] = Field(None, alias='OrderNumber')

    # Transaction ID within client environment associated with the customer. This value acts as a secondary identifier in conjunction with OrderNumber. The value is searchable and reportable in the ConnexPay portal. This value may be sent in multiple times within the integration for multiple purposes. The maximum length is 100 characters and is alpha-numeric.
    customer_i_d: typing.Optional[str] = Field(None, alias='CustomerID')

    # Utilize the Association ID field to tie a virtual card to a sale or sales. For example, if you have several sales and one virtual card payment to a supplier, you can add association ID to the sales and the virtual card for downstream reporting.
    association_i_d: typing.Optional[str] = Field(None, alias='AssociationID')

    custom_parameters: typing.Optional[TransactionCaptureAuthorizationRequestCustomParameters] = Field(None, alias='CustomParameters')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
