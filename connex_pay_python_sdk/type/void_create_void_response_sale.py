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

from connex_pay_python_sdk.type.void_create_void_response_sale_card import VoidCreateVoidResponseSaleCard

class RequiredVoidCreateVoidResponseSale(TypedDict):
    pass

class OptionalVoidCreateVoidResponseSale(TypedDict, total=False):
    guid: str

    status: str

    batchStatus: str

    timeStamp: str

    deviceGuid: str

    amount: typing.Union[int, float]

    effectiveAmount: int

    orderNumber: str

    orderDate: str

    batchGuid: str

    processorStatusCode: str

    processorResponseMessage: str

    wasProcessed: bool

    authCode: str

    refNumber: str

    invoiceNumber: str

    customerReceipt: str

    customData: str

    card: VoidCreateVoidResponseSaleCard

class VoidCreateVoidResponseSale(RequiredVoidCreateVoidResponseSale, OptionalVoidCreateVoidResponseSale):
    pass
