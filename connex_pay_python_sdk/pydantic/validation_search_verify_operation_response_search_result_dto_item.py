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

from connex_pay_python_sdk.pydantic.validation_search_verify_operation_response_search_result_dto_item_card import ValidationSearchVerifyOperationResponseSearchResultDtoItemCard

class ValidationSearchVerifyOperationResponseSearchResultDtoItem(BaseModel):
    status: typing.Optional[str] = Field(None, alias='status')

    card: typing.Optional[ValidationSearchVerifyOperationResponseSearchResultDtoItemCard] = Field(None, alias='card')

    time_stamp: typing.Optional[str] = Field(None, alias='timeStamp')

    processor_status_code: typing.Optional[str] = Field(None, alias='processorStatusCode')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
