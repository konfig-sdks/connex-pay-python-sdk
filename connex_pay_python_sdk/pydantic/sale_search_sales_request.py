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


class SaleSearchSalesRequest(BaseModel):
    # Merchant’s Guid.
    merchant_guid: typing.Optional[str] = Field(None, alias='MerchantGuid')

    # Amount of the transaction. Min. amt.: $0.50
    amount_from: typing.Optional[typing.Union[int, float]] = Field(None, alias='AmountFrom')

    # Amount of the transaction. Min. amt.: $0.50
    amount_to: typing.Optional[typing.Union[int, float]] = Field(None, alias='AmountTo')

    # Cardholder’s name.
    card_holder_name: typing.Optional[str] = Field(None, alias='CardHolderName')

    # Card last four number.
    card_last_four: typing.Optional[str] = Field(None, alias='CardLastFour')

    # Card type.
    card_type: typing.Optional[str] = Field(None, alias='CardType')

    # Sale’s InvoiceNumber.
    invoice_number: typing.Optional[int] = Field(None, alias='InvoiceNumber')

    # Sale’s order number. Length = 17.
    order_number: typing.Optional[str] = Field(None, alias='OrderNumber')

    # Sale’s order Date.
    order_date_from: typing.Optional[date] = Field(None, alias='OrderDateFrom')

    # Sale’s order Date.
    order_date_to: typing.Optional[date] = Field(None, alias='OrderDateTo')

    # Sale’s TimeStamp.
    time_stamp_from: typing.Optional[date] = Field(None, alias='TimeStampFrom')

    # Sale’s TimeStamp.
    time_stamp_to: typing.Optional[date] = Field(None, alias='TimeStampTo')

    # Sale’s status. Allowed values:  1. Transaction - Approved 2. Transaction - Declined 3. Transaction - Created - Local 4. Transaction - Created - Error: Processor not reached 5. Transaction - Processor Error 6. Transaction - Approved - Warning
    status: typing.Optional[str] = Field(None, alias='Status')

    # Merchant Customer Id.
    merchant_customer_id: typing.Optional[str] = Field(None, alias='MerchantCustomerId')

    # Delayed Activation Sales to be included or not
    activated: typing.Optional[bool] = Field(None, alias='Activated')

    # Activation Start Date. This field is applicable only when Activated flag is set to true.
    activation_date_from: typing.Optional[date] = Field(None, alias='ActivationDateFrom')

    # Activation End Date. This field is applicable only when Activated flag is set to true.
    activation_date_to: typing.Optional[date] = Field(None, alias='ActivationDateTo')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
