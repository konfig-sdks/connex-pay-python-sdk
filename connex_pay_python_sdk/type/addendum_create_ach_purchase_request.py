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


class RequiredAddendumCreateAchPurchaseRequest(TypedDict):
    pass

class OptionalAddendumCreateAchPurchaseRequest(TypedDict, total=False):
    # Guid for the ACH Purchase you are attaching information to with this addendum request. This Guid was returned to client when the ACH Purchase was initially created.
    ItemGuid: str

    # Character data to associate with the Virtual card.
    Value: str

    # Can be used by client to specify a desired category for an Addenda item. Consistent category parameters will aid in reporting consistently. See note below regarding the \"MultipleSales\" category and how to use the category specifically to associate an ACH Purchase to an existing sale(s).
    Category: str

    # Can be supplied by client to associate this addendum with an ID in client's data.
    IdExternal: str

    # Additional information to associate with this addendum, as desired.
    Note: str

    # If client creates multiple addenda for a single ACH Purchase this sequence can be specified if a client desires.
    Sequence: str

class AddendumCreateAchPurchaseRequest(RequiredAddendumCreateAchPurchaseRequest, OptionalAddendumCreateAchPurchaseRequest):
    pass
