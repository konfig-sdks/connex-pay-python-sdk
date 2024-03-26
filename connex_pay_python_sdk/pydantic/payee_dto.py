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


class PayeeDto(BaseModel):
    # Merchant guid for the Payee to be created.
    merchant_guid: str = Field(alias='merchantGuid')

    # First name for the Payee to be created.
    first_name: str = Field(alias='firstName')

    # Last name for the Payee to be created.
    last_name: str = Field(alias='lastName')

    # Email address for the Payee.
    email: str = Field(alias='email')

    # Phone number for the Payee, up to 10-character string.
    phone: str = Field(alias='phone')

    # Guid for the created Payee that is returned by ConnexPay upon creation of a Payee. Ignored if provided in a Payee creation request.
    payee_guid: typing.Optional[str] = Field(None, alias='payeeGuid')

    # Postal address line 1 for the Payee. Alphanumerics and [,.-'] are allowed.
    address1: typing.Optional[str] = Field(None, alias='address1')

    # Postal address line 2 for the Payee. Alphanumerics and [,.-'] are allowed.
    address2: typing.Optional[str] = Field(None, alias='address2')

    # Postal address city for the Payee.
    city: typing.Optional[str] = Field(None, alias='city')

    # Postal address state for the Payee.
    state: typing.Optional[str] = Field(None, alias='state')

    # Postal code for the Payee.
    zip_code: typing.Optional[str] = Field(None, alias='zipCode')

    # Status for the Payee.
    status: typing.Optional[str] = Field(None, alias='status')

    # Unique identifier that refers to the card saved for a Payee when using the Payment Widget. It will be null when a Payee is created but will have a value once stored for the Payee using the Payment Widget.
    card_id: typing.Optional[str] = Field(None, alias='cardId')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
