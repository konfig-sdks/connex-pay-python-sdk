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

from connex_pay_python_sdk.pydantic.dto_payments import DtoPayments
from connex_pay_python_sdk.pydantic.dto_payout_label_ids import DtoPayoutLabelIds

class DtoPayout(BaseModel):
    # Unique identifier assigned to the Payout.
    payout_guid: typing.Optional[str] = Field(None, alias='payoutGuid')

    # The Payout identifier that will be needed by our support teams to research issues.
    payout_reference_token: typing.Optional[str] = Field(None, alias='payoutReferenceToken')

    # A brief description highlighting the reason for this Payout.
    memo: typing.Optional[str] = Field(None, alias='memo')

    # The most common number used throughout the ConnexPay Portal. Transaction ID within client environment associated with the order. The value is searchable and reportable in the ConnexPay portal. This value may be sent in multiple instances of the integration for multiple purposes. The maximum length is 50 alpha-numeric characters and allows dashes ( - ).
    order_number: typing.Optional[str] = Field(None, alias='orderNumber')

    # Association ID is used to tie a Payout to a sale or sales. For example, if you have several sales and one Payout to a Payee, association ID can be added to the sales and the Payout for downstream reporting.
    association_id: typing.Optional[str] = Field(None, alias='associationId')

    # Transaction ID within the client environment associated with the customer. This value acts as a secondary identifier in conjunction with OrderNumber. The value is searchable and reportable in the ConnexPay portal. This value may be sent in multiple times within the integration for multiple purposes. The maximum length is 100 characters and is alpha-numeric.
    customer_id: typing.Optional[str] = Field(None, alias='customerId')

    created_date: typing.Optional[datetime] = Field(None, alias='createdDate')

    created_by: typing.Optional[str] = Field(None, alias='createdBy')

    label_ids: typing.Optional[DtoPayoutLabelIds] = Field(None, alias='labelIds')

    payments: typing.Optional[typing.List[DtoPayments]] = Field(None, alias='payments')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
