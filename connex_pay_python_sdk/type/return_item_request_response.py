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

from connex_pay_python_sdk.type.return_item_request_response_sale import ReturnItemRequestResponseSale

class RequiredReturnItemRequestResponse(TypedDict):
    pass

class OptionalReturnItemRequestResponse(TypedDict, total=False):
    guid: str

    batchStatus: str

    timeStamp: str

    deviceGuid: str

    saleGuid: str

    status: str

    amount: typing.Union[int, float]

    batchGuid: str

    processorStatusCode: str

    wasProcessed: bool

    authCode: str

    refNumber: str

    invoiceNumber: str

    customerReceipt: str

    sequenceNumber: str

    sale: ReturnItemRequestResponseSale

class ReturnItemRequestResponse(RequiredReturnItemRequestResponse, OptionalReturnItemRequestResponse):
    pass
