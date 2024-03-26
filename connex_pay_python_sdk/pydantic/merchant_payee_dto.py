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


class MerchantPayeeDto(BaseModel):
    is_business: bool = Field(alias='isBusiness')

    payee_id: str = Field(alias='payeeId')

    preferred_payout_method: str = Field(alias='preferredPayoutMethod')

    id_merchant: typing.Optional[int] = Field(None, alias='idMerchant')

    first_name: typing.Optional[str] = Field(None, alias='firstName')

    last_name: typing.Optional[str] = Field(None, alias='lastName')

    dba_name: typing.Optional[str] = Field(None, alias='dbaName')

    tax_id: typing.Optional[str] = Field(None, alias='taxId')

    customer_id: typing.Optional[str] = Field(None, alias='customerId')

    email: typing.Optional[str] = Field(None, alias='email')

    address1: typing.Optional[str] = Field(None, alias='address1')

    address2: typing.Optional[str] = Field(None, alias='address2')

    city: typing.Optional[str] = Field(None, alias='city')

    state: typing.Optional[str] = Field(None, alias='state')

    zip: typing.Optional[str] = Field(None, alias='zip')

    country: typing.Optional[str] = Field(None, alias='country')

    preferred_card_brand: typing.Optional[str] = Field(None, alias='preferredCardBrand')

    preferred_card_class: typing.Optional[str] = Field(None, alias='preferredCardClass')

    purchase_type: typing.Optional[str] = Field(None, alias='purchaseType')

    guid: typing.Optional[str] = Field(None, alias='guid')

    timestamp: typing.Optional[datetime] = Field(None, alias='timestamp')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
