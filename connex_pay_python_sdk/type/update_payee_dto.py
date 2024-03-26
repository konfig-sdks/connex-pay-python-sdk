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


class RequiredUpdatePayeeDto(TypedDict):
    pass

class OptionalUpdatePayeeDto(TypedDict, total=False):
    # First name for the Payee to be updated.
    firstName: str

    # Last name for the Payee to be updated.
    lastName: str

    # Email address for the Payee to be updated.
    email: str

    # Postal address line 1 for the Payee to be updated. Alphanumerics and [,.-'] are allowed.
    address1: str

    # Postal address line 2 for the Payee to be updated. Alphanumerics and [,.-'] are allowed.
    address2: str

    # Postal address city for the Payee to be updated.
    city: str

    # Postal address state for the Payee to be updated.
    state: str

    # Postal code for the Payee to be updated.
    zipCode: str

    # Phone number for the Payee to be updated, up to 10-character string.
    phone: str

    # Status for the Payee to be updated.
    status: str

class UpdatePayeeDto(RequiredUpdatePayeeDto, OptionalUpdatePayeeDto):
    pass
