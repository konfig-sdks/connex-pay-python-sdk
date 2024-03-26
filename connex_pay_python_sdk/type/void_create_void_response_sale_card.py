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

from connex_pay_python_sdk.type.void_create_void_response_sale_card_customer import VoidCreateVoidResponseSaleCardCustomer

class RequiredVoidCreateVoidResponseSaleCard(TypedDict):
    pass

class OptionalVoidCreateVoidResponseSaleCard(TypedDict, total=False):
    first4: str

    last4: str

    cardNumber: str

    cardHolderName: str

    expirationDate: str

    customer: VoidCreateVoidResponseSaleCardCustomer

class VoidCreateVoidResponseSaleCard(RequiredVoidCreateVoidResponseSaleCard, OptionalVoidCreateVoidResponseSaleCard):
    pass
