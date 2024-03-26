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

from connex_pay_python_sdk.type.payments_dto import PaymentsDto
from connex_pay_python_sdk.type.payout_dto_label_ids import PayoutDtoLabelIds

class RequiredPayoutDto(TypedDict):
    # Application-level value that indicates a Payout is being requested for client's account. Value provided by ConnexPay.
    merchantGuid: str

    # A brief description highlighting the reason for this Payout.
    memo: str

    payments: typing.List[PaymentsDto]

class OptionalPayoutDto(TypedDict, total=False):
    # Guid assigned to the Payout by ConnexPay upon creation of a Payout.
    payoutGuid: str

    # The Payout identifier that will be needed by ConnexPay support teams to research issues.
    payoutReferenceToken: str

    # Status of the Payout.
    status: str

    # The most common number used throughout the ConnexPay Portal. Transaction ID within client environment associated with the order. The value is searchable and reportable in the ConnexPay portal. This value may be sent in multiple instances of the integration for multiple purposes. The maximum length is 50 alpha-numeric characters and allows dashes ( - ).
    orderNumber: str

    # Transaction ID within the client environment associated with the customer. This value acts as a secondary identifier in conjunction with OrderNumber. The value is searchable and reportable in the ConnexPay portal. This value may be sent in multiple times within the integration for multiple purposes. The maximum length is 100 characters and is alpha-numeric.
    customerId: str

    # Association ID is used to tie a Payout to a sale or sales. For example, if you have several sales and one Payout to a Payee, association ID can be added to the sales and the Payout for downstream reporting.
    associationId: str

    labelIds: PayoutDtoLabelIds

class PayoutDto(RequiredPayoutDto, OptionalPayoutDto):
    pass
