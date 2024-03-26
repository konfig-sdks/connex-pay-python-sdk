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

from connex_pay_python_sdk.pydantic.return_item_request_response_sale import ReturnItemRequestResponseSale

class ReturnItemRequestResponse(BaseModel):
    guid: typing.Optional[str] = Field(None, alias='guid')

    batch_status: typing.Optional[str] = Field(None, alias='batchStatus')

    time_stamp: typing.Optional[str] = Field(None, alias='timeStamp')

    device_guid: typing.Optional[str] = Field(None, alias='deviceGuid')

    sale_guid: typing.Optional[str] = Field(None, alias='saleGuid')

    status: typing.Optional[str] = Field(None, alias='status')

    amount: typing.Optional[typing.Union[int, float]] = Field(None, alias='amount')

    batch_guid: typing.Optional[str] = Field(None, alias='batchGuid')

    processor_status_code: typing.Optional[str] = Field(None, alias='processorStatusCode')

    was_processed: typing.Optional[bool] = Field(None, alias='wasProcessed')

    auth_code: typing.Optional[str] = Field(None, alias='authCode')

    ref_number: typing.Optional[str] = Field(None, alias='refNumber')

    invoice_number: typing.Optional[str] = Field(None, alias='invoiceNumber')

    customer_receipt: typing.Optional[str] = Field(None, alias='customerReceipt')

    sequence_number: typing.Optional[str] = Field(None, alias='sequenceNumber')

    sale: typing.Optional[ReturnItemRequestResponseSale] = Field(None, alias='sale')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
