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

from connex_pay_python_sdk.type.transaction_capture_authorization_response_sale_card_customer import TransactionCaptureAuthorizationResponseSaleCardCustomer

class RequiredTransactionCaptureAuthorizationResponseSaleCard(TypedDict):
    pass

class OptionalTransactionCaptureAuthorizationResponseSaleCard(TypedDict, total=False):
    first6: str

    first4: str

    last4: str

    cardHolderName: str

    cardType: str

    expirationDate: str

    customer: TransactionCaptureAuthorizationResponseSaleCardCustomer

    guid: str

class TransactionCaptureAuthorizationResponseSaleCard(RequiredTransactionCaptureAuthorizationResponseSaleCard, OptionalTransactionCaptureAuthorizationResponseSaleCard):
    pass
