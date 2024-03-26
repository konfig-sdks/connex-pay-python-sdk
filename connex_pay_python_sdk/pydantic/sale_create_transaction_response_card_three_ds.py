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


class SaleCreateTransactionResponseCardThreeDs(BaseModel):
    secure_code: typing.Optional[str] = Field(None, alias='SecureCode')

    cavv: typing.Optional[str] = Field(None, alias='Cavv')

    version: typing.Optional[str] = Field(None, alias='Version')

    directory_server_transaction_i_d: typing.Optional[str] = Field(None, alias='DirectoryServerTransactionID')

    acs_transaction_id: typing.Optional[str] = Field(None, alias='AcsTransactionId')

    e_c_i: typing.Optional[str] = Field(None, alias='ECI')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
