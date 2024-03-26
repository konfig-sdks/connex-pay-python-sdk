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


class UpdatePayeeDto(BaseModel):
    # First name for the Payee to be updated.
    first_name: typing.Optional[str] = Field(None, alias='firstName')

    # Last name for the Payee to be updated.
    last_name: typing.Optional[str] = Field(None, alias='lastName')

    # Email address for the Payee to be updated.
    email: typing.Optional[str] = Field(None, alias='email')

    # Postal address line 1 for the Payee to be updated. Alphanumerics and [,.-'] are allowed.
    address1: typing.Optional[str] = Field(None, alias='address1')

    # Postal address line 2 for the Payee to be updated. Alphanumerics and [,.-'] are allowed.
    address2: typing.Optional[str] = Field(None, alias='address2')

    # Postal address city for the Payee to be updated.
    city: typing.Optional[str] = Field(None, alias='city')

    # Postal address state for the Payee to be updated.
    state: typing.Optional[str] = Field(None, alias='state')

    # Postal code for the Payee to be updated.
    zip_code: typing.Optional[str] = Field(None, alias='zipCode')

    # Phone number for the Payee to be updated, up to 10-character string.
    phone: typing.Optional[str] = Field(None, alias='phone')

    # Status for the Payee to be updated.
    status: typing.Optional[str] = Field(None, alias='status')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
