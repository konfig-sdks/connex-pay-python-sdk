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

from connex_pay_python_sdk.pydantic.validation_search_verify_operation_response_search_result_dto import ValidationSearchVerifyOperationResponseSearchResultDto

class ValidationSearchVerifyOperationResponse(BaseModel):
    page_current: typing.Optional[int] = Field(None, alias='pageCurrent')

    page_current_results: typing.Optional[int] = Field(None, alias='pageCurrentResults')

    page_total: typing.Optional[int] = Field(None, alias='pageTotal')

    page_size: typing.Optional[int] = Field(None, alias='pageSize')

    total_results: typing.Optional[int] = Field(None, alias='totalResults')

    card_summary: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = Field(None, alias='cardSummary')

    search_result_d_t_o: typing.Optional[ValidationSearchVerifyOperationResponseSearchResultDto] = Field(None, alias='searchResultDTO')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
