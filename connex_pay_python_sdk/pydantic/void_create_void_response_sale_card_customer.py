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


class VoidCreateVoidResponseSaleCardCustomer(BaseModel):
    guid: typing.Optional[str] = Field(None, alias='guid')

    first_name: typing.Optional[str] = Field(None, alias='firstName')

    last_name: typing.Optional[str] = Field(None, alias='lastName')

    phone: typing.Optional[str] = Field(None, alias='phone')

    city: typing.Optional[str] = Field(None, alias='city')

    country: typing.Optional[str] = Field(None, alias='country')

    email: typing.Optional[str] = Field(None, alias='email')

    zip: typing.Optional[str] = Field(None, alias='zip')

    address1: typing.Optional[str] = Field(None, alias='address1')

    address2: typing.Optional[str] = Field(None, alias='address2')

    state: typing.Optional[str] = Field(None, alias='state')

    date_of_birth: typing.Optional[str] = Field(None, alias='dateOfBirth')

    driver_license_number: typing.Optional[str] = Field(None, alias='driverLicenseNumber')

    driver_license_state: typing.Optional[str] = Field(None, alias='driverLicenseState')

    ss_n4: typing.Optional[str] = Field(None, alias='ssN4')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
