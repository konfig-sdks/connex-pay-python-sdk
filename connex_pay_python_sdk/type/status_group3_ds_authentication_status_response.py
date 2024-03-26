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

from connex_pay_python_sdk.type.status_group3_ds_authentication_status_response_card import StatusGroup3DsAuthenticationStatusResponseCard

class RequiredStatusGroup3DsAuthenticationStatusResponse(TypedDict):
    pass

class OptionalStatusGroup3DsAuthenticationStatusResponse(TypedDict, total=False):
    version: str

    guid: str

    status: str

    timeStamp: str

    deviceGuid: str

    amount: typing.Union[int, float]

    secureData: str

    eci: str

    cavv: str

    directoryServerTransactionID: str

    acsTransactionId: str

    card: StatusGroup3DsAuthenticationStatusResponseCard

    processorResponseCode: str

    processorMessage: str

class StatusGroup3DsAuthenticationStatusResponse(RequiredStatusGroup3DsAuthenticationStatusResponse, OptionalStatusGroup3DsAuthenticationStatusResponse):
    pass
