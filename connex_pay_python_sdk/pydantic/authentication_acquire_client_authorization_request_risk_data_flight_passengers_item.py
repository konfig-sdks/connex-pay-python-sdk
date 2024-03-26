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


class AuthenticationAcquireClientAuthorizationRequestRiskDataFlightPassengersItem(BaseModel):
    # Country of origin of passenger
    country: typing.Optional[str] = Field(None, alias='Country')

    # DOB of first passenger
    date_of_birth: typing.Optional[date] = Field(None, alias='DateOfBirth')

    # Passport, drivers license or id# associated with passenger
    id: typing.Optional[str] = Field(None, alias='Id')

    # Passenger information. Each passenger should be sent in it's own object.
    name: typing.Optional[str] = Field(None, alias='Name')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
