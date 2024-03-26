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


class PaymentsDto(BaseModel):
    # Unique identifier assigned to the Payee.
    payee_guid: str = Field(alias='payeeGuid')

    # Amount of the Payment.
    value: typing.Union[int, float] = Field(alias='value')

    # The Payee identifier used by ConnexPay support teams to research issues related to the Payee.
    payee_reference_token: typing.Optional[str] = Field(None, alias='payeeReferenceToken')

    # For Payment Widget customers only. This is the identifier that used by ConnexPay support teams to research issues related to the Payment Widget.
    rid_reference_token: typing.Optional[str] = Field(None, alias='ridReferenceToken')

    # Unique identifier assigned to the Payment.
    payment_guid: typing.Optional[str] = Field(None, alias='paymentGuid')

    # Unique identifier assigned when using the Payment Widget.
    rid_guid: typing.Optional[str] = Field(None, alias='ridGuid')

    # Payment-level description highlighting the reason for this Payment.
    memo: typing.Optional[str] = Field(None, alias='memo')

    # Additional data field that can be used to provide additional data to the Payee and for your reporting purposes.
    field2: typing.Optional[str] = Field(None, alias='field2')

    # Additional data field that can be used to provide additional data to the Payee and for your reporting purposes.
    field3: typing.Optional[str] = Field(None, alias='field3')

    # Additional data field that can be used to provide additional data to the Payee and for your reporting purposes.
    field4: typing.Optional[str] = Field(None, alias='field4')

    # Additional data field that can be used to provide additional data to the Payee and for your reporting purposes.
    field5: typing.Optional[str] = Field(None, alias='field5')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
