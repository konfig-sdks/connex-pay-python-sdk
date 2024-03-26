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


class DtoPayments(BaseModel):
    payment_guid: typing.Optional[str] = Field(None, alias='paymentGuid')

    # Identifier needed by ConnexPay support teams to research Payment issues.
    payment_reference_token: typing.Optional[str] = Field(None, alias='paymentReferenceToken')

    # Payee identifier needed by ConnexPay support teams to research Payee issues.
    payee_reference_token: typing.Optional[str] = Field(None, alias='payeeReferenceToken')

    # For Payment Widget customers only. Identifier needed by ConnexPay support teams to research issues related to the Payment Widget.
    rid_reference_token: typing.Optional[str] = Field(None, alias='ridReferenceToken')

    # Payment-level description highlighting the reason for this Payment.
    memo: typing.Optional[str] = Field(None, alias='memo')

    # Amount of the Payment.
    value: typing.Optional[typing.Union[int, float]] = Field(None, alias='value')

    # Status of the Payment.
    status: typing.Optional[str] = Field(None, alias='status')

    # Additional data field that can be used to provide additional data to the Payee and for your reporting purposes.
    field2: typing.Optional[str] = Field(None, alias='field2')

    # Additional data field that can be used to provide additional data to the Payee and for your reporting purposes.
    field3: typing.Optional[str] = Field(None, alias='field3')

    # Additional data field that can be used to provide additional data to the Payee and for your reporting purposes.
    field4: typing.Optional[str] = Field(None, alias='field4')

    # Additional data field that can be used to provide additional data to the Payee and for your reporting purposes.
    field5: typing.Optional[str] = Field(None, alias='field5')

    termination_date: typing.Optional[str] = Field(None, alias='terminationDate')

    # The Payee's name.
    payee_name: typing.Optional[str] = Field(None, alias='payeeName')

    # Email address the Payment was sent to for the Payee.
    email: typing.Optional[str] = Field(None, alias='email')

    # Last four digits of the Payee's card number.
    last_four: typing.Optional[str] = Field(None, alias='lastFour')

    # Postal address line 1 of the Payee. Alphanumerics and [,.-'] are allowed.
    address1: typing.Optional[str] = Field(None, alias='address1')

    # Postal address line 2 of the Payee. Alphanumerics and [,.-'] are allowed.
    address2: typing.Optional[str] = Field(None, alias='address2')

    # Postal address city of the Payee.
    city: typing.Optional[str] = Field(None, alias='city')

    # Postal address state for the Payee.
    state: typing.Optional[str] = Field(None, alias='state')

    # Postal code for the Payee.
    zip_code: typing.Optional[str] = Field(None, alias='zipCode')

    # Postal address country for the Payee.
    country: typing.Optional[str] = Field(None, alias='country')

    created_by: typing.Optional[str] = Field(None, alias='createdBy')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
