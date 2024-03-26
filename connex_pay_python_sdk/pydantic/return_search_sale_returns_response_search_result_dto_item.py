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

from connex_pay_python_sdk.pydantic.return_search_sale_returns_response_search_result_dto_item_card import ReturnSearchSaleReturnsResponseSearchResultDtoItemCard

class ReturnSearchSaleReturnsResponseSearchResultDtoItem(BaseModel):
    status: typing.Optional[str] = Field(None, alias='status')

    amount: typing.Optional[int] = Field(None, alias='amount')

    card: typing.Optional[ReturnSearchSaleReturnsResponseSearchResultDtoItemCard] = Field(None, alias='card')

    time_stamp: typing.Optional[str] = Field(None, alias='timeStamp')

    processor_status_code: typing.Optional[str] = Field(None, alias='processorStatusCode')

    batch_status: typing.Optional[str] = Field(None, alias='batchStatus')

    guid: typing.Optional[str] = Field(None, alias='guid')

    related_void: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = Field(None, alias='relatedVoid')

    device_guid: typing.Optional[str] = Field(None, alias='deviceGuid')

    type: typing.Optional[str] = Field(None, alias='type')

    card_data_source: typing.Optional[str] = Field(None, alias='cardDataSource')

    allow_card_emv: typing.Optional[bool] = Field(None, alias='allowCardEmv')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
