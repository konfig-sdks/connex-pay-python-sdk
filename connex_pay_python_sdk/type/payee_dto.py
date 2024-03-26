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


class RequiredPayeeDto(TypedDict):
    # Merchant guid for the Payee to be created.
    merchantGuid: str

    # First name for the Payee to be created.
    firstName: str

    # Last name for the Payee to be created.
    lastName: str

    # Email address for the Payee.
    email: str

    # Phone number for the Payee, up to 10-character string.
    phone: str

class OptionalPayeeDto(TypedDict, total=False):
    # Guid for the created Payee that is returned by ConnexPay upon creation of a Payee. Ignored if provided in a Payee creation request.
    payeeGuid: str

    # Postal address line 1 for the Payee. Alphanumerics and [,.-'] are allowed.
    address1: str

    # Postal address line 2 for the Payee. Alphanumerics and [,.-'] are allowed.
    address2: str

    # Postal address city for the Payee.
    city: str

    # Postal address state for the Payee.
    state: str

    # Postal code for the Payee.
    zipCode: str

    # Status for the Payee.
    status: str

    # Unique identifier that refers to the card saved for a Payee when using the Payment Widget. It will be null when a Payee is created but will have a value once stored for the Payee using the Payment Widget.
    cardId: str

class PayeeDto(RequiredPayeeDto, OptionalPayeeDto):
    pass
