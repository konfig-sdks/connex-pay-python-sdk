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


class RequiredVoidCreateVoidResponseSaleCardCustomer(TypedDict):
    pass

class OptionalVoidCreateVoidResponseSaleCardCustomer(TypedDict, total=False):
    guid: str

    firstName: str

    lastName: str

    phone: str

    city: str

    country: str

    email: str

    zip: str

    address1: str

    address2: str

    state: str

    dateOfBirth: str

    driverLicenseNumber: str

    driverLicenseState: str

    ssN4: str

class VoidCreateVoidResponseSaleCardCustomer(RequiredVoidCreateVoidResponseSaleCardCustomer, OptionalVoidCreateVoidResponseSaleCardCustomer):
    pass
