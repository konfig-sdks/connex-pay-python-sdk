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


class AddendumCreateVirtualCardRequest(BaseModel):
    # Guid for the Virtual Card you are attaching information to with this addendum request. This Guid was returned to client when the Virtual Card was initially created.
    item_guid: typing.Optional[str] = Field(None, alias='ItemGuid')

    # Character data to associate with the Virtual card.
    value: typing.Optional[str] = Field(None, alias='Value')

    # Can be used by client to specify a desired category for an Addenda item.
    category: typing.Optional[str] = Field(None, alias='Category')

    # Can be supplied by client to associate this addendum with an ID in client's data.
    id_external: typing.Optional[str] = Field(None, alias='IdExternal')

    # Additional information to associate with this addendum, as desired.
    note: typing.Optional[str] = Field(None, alias='Note')

    # If client creates multiple addenda for a single Virtual Card this sequence can be specified if a client desires.
    sequence: typing.Optional[str] = Field(None, alias='Sequence')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
