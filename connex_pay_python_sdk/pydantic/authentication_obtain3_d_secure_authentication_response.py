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

from connex_pay_python_sdk.pydantic.authentication_obtain3_d_secure_authentication_response_card import AuthenticationObtain3DSecureAuthenticationResponseCard

class AuthenticationObtain3DSecureAuthenticationResponse(BaseModel):
    guid: typing.Optional[str] = Field(None, alias='guid')

    status: typing.Optional[str] = Field(None, alias='status')

    time_stamp: typing.Optional[str] = Field(None, alias='timeStamp')

    device_guid: typing.Optional[str] = Field(None, alias='deviceGuid')

    amount: typing.Optional[int] = Field(None, alias='amount')

    three_d_s_status: typing.Optional[str] = Field(None, alias='threeDSStatus')

    secure_data: typing.Optional[str] = Field(None, alias='SecureData')

    cavv: typing.Optional[str] = Field(None, alias='Cavv')

    version: typing.Optional[str] = Field(None, alias='Version')

    directory_server_transaction_i_d: typing.Optional[str] = Field(None, alias='DirectoryServerTransactionID')

    acs_transaction_id: typing.Optional[str] = Field(None, alias='AcsTransactionId')

    e_c_i: typing.Optional[str] = Field(None, alias='ECI')

    card: typing.Optional[AuthenticationObtain3DSecureAuthenticationResponseCard] = Field(None, alias='card')

    exempt_three_d_s_request: typing.Optional[bool] = Field(None, alias='exemptThreeDSRequest')

    exempt_three_d_s_payment: typing.Optional[bool] = Field(None, alias='exemptThreeDSPayment')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
