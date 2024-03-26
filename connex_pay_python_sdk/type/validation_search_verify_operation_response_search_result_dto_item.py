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

from connex_pay_python_sdk.type.validation_search_verify_operation_response_search_result_dto_item_card import ValidationSearchVerifyOperationResponseSearchResultDtoItemCard

class RequiredValidationSearchVerifyOperationResponseSearchResultDtoItem(TypedDict):
    pass

class OptionalValidationSearchVerifyOperationResponseSearchResultDtoItem(TypedDict, total=False):
    status: str

    card: ValidationSearchVerifyOperationResponseSearchResultDtoItemCard

    timeStamp: str

    processorStatusCode: str

class ValidationSearchVerifyOperationResponseSearchResultDtoItem(RequiredValidationSearchVerifyOperationResponseSearchResultDtoItem, OptionalValidationSearchVerifyOperationResponseSearchResultDtoItem):
    pass
