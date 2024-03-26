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

from connex_pay_python_sdk.pydantic.sale_search_sales_response_search_result_dto_item_card import SaleSearchSalesResponseSearchResultDtoItemCard

class SaleSearchSalesResponseSearchResultDtoItem(BaseModel):
    status: typing.Optional[str] = Field(None, alias='status')

    amount: typing.Optional[int] = Field(None, alias='amount')

    card: typing.Optional[SaleSearchSalesResponseSearchResultDtoItemCard] = Field(None, alias='card')

    order_number: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = Field(None, alias='orderNumber')

    order_date: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = Field(None, alias='orderDate')

    time_stamp: typing.Optional[str] = Field(None, alias='timeStamp')

    customer_i_d: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = Field(None, alias='customerID')

    processor_response_message: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = Field(None, alias='processorResponseMessage')

    effective_amount: typing.Optional[int] = Field(None, alias='effectiveAmount')

    batch_status: typing.Optional[str] = Field(None, alias='batchStatus')

    related_void: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = Field(None, alias='relatedVoid')

    related_returns: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = Field(None, alias='relatedReturns')

    guid: typing.Optional[str] = Field(None, alias='guid')

    device_guid: typing.Optional[str] = Field(None, alias='deviceGuid')

    capture_guid: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = Field(None, alias='captureGuid')

    custom_data: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = Field(None, alias='customData')

    generated_by_capture: typing.Optional[bool] = Field(None, alias='generatedByCapture')

    partially_approved_amount: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = Field(None, alias='partiallyApprovedAmount')

    type: typing.Optional[str] = Field(None, alias='type')

    surcharge: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = Field(None, alias='surcharge')

    surcharge_type: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = Field(None, alias='surchargeType')

    service_fee: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = Field(None, alias='serviceFee')

    tip_amount: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = Field(None, alias='tipAmount')

    card_data_source: typing.Optional[str] = Field(None, alias='cardDataSource')

    allow_card_emv: typing.Optional[bool] = Field(None, alias='allowCardEmv')

    incoming_transaction_code: typing.Optional[str] = Field(None, alias='incomingTransactionCode')

    activation_date: typing.Optional[str] = Field(None, alias='activationDate')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
