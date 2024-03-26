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

from connex_pay_python_sdk.pydantic.status_group3_ds_authentication_status_response_card import StatusGroup3DsAuthenticationStatusResponseCard

class StatusGroup3DsAuthenticationStatusResponse(BaseModel):
    version: typing.Optional[str] = Field(None, alias='version')

    guid: typing.Optional[str] = Field(None, alias='guid')

    status: typing.Optional[str] = Field(None, alias='status')

    time_stamp: typing.Optional[str] = Field(None, alias='timeStamp')

    device_guid: typing.Optional[str] = Field(None, alias='deviceGuid')

    amount: typing.Optional[typing.Union[int, float]] = Field(None, alias='amount')

    secure_data: typing.Optional[str] = Field(None, alias='secureData')

    eci: typing.Optional[str] = Field(None, alias='eci')

    cavv: typing.Optional[str] = Field(None, alias='cavv')

    directory_server_transaction_i_d: typing.Optional[str] = Field(None, alias='directoryServerTransactionID')

    acs_transaction_id: typing.Optional[str] = Field(None, alias='acsTransactionId')

    card: typing.Optional[StatusGroup3DsAuthenticationStatusResponseCard] = Field(None, alias='card')

    processor_response_code: typing.Optional[str] = Field(None, alias='processorResponseCode')

    processor_message: typing.Optional[str] = Field(None, alias='processorMessage')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
