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

from connex_pay_python_sdk.pydantic.payments_dto import PaymentsDto
from connex_pay_python_sdk.pydantic.payout_dto_label_ids import PayoutDtoLabelIds

class PayoutDto(BaseModel):
    # Application-level value that indicates a Payout is being requested for client's account. Value provided by ConnexPay.
    merchant_guid: str = Field(alias='merchantGuid')

    # A brief description highlighting the reason for this Payout.
    memo: str = Field(alias='memo')

    payments: typing.List[PaymentsDto] = Field(alias='payments')

    # Guid assigned to the Payout by ConnexPay upon creation of a Payout.
    payout_guid: typing.Optional[str] = Field(None, alias='payoutGuid')

    # The Payout identifier that will be needed by ConnexPay support teams to research issues.
    payout_reference_token: typing.Optional[str] = Field(None, alias='payoutReferenceToken')

    # Status of the Payout.
    status: typing.Optional[str] = Field(None, alias='status')

    # The most common number used throughout the ConnexPay Portal. Transaction ID within client environment associated with the order. The value is searchable and reportable in the ConnexPay portal. This value may be sent in multiple instances of the integration for multiple purposes. The maximum length is 50 alpha-numeric characters and allows dashes ( - ).
    order_number: typing.Optional[str] = Field(None, alias='orderNumber')

    # Transaction ID within the client environment associated with the customer. This value acts as a secondary identifier in conjunction with OrderNumber. The value is searchable and reportable in the ConnexPay portal. This value may be sent in multiple times within the integration for multiple purposes. The maximum length is 100 characters and is alpha-numeric.
    customer_id: typing.Optional[str] = Field(None, alias='customerId')

    # Association ID is used to tie a Payout to a sale or sales. For example, if you have several sales and one Payout to a Payee, association ID can be added to the sales and the Payout for downstream reporting.
    association_id: typing.Optional[str] = Field(None, alias='associationId')

    label_ids: typing.Optional[PayoutDtoLabelIds] = Field(None, alias='labelIds')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
