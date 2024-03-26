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


class RequiredAddendumCreateVirtualCardRequest(TypedDict):
    pass

class OptionalAddendumCreateVirtualCardRequest(TypedDict, total=False):
    # Guid for the Virtual Card you are attaching information to with this addendum request. This Guid was returned to client when the Virtual Card was initially created.
    ItemGuid: str

    # Character data to associate with the Virtual card.
    Value: str

    # Can be used by client to specify a desired category for an Addenda item.
    Category: str

    # Can be supplied by client to associate this addendum with an ID in client's data.
    IdExternal: str

    # Additional information to associate with this addendum, as desired.
    Note: str

    # If client creates multiple addenda for a single Virtual Card this sequence can be specified if a client desires.
    Sequence: str

class AddendumCreateVirtualCardRequest(RequiredAddendumCreateVirtualCardRequest, OptionalAddendumCreateVirtualCardRequest):
    pass
