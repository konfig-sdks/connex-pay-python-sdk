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


class RequiredTransactionCaptureAuthorizationResponseSaleCardCustomer(TypedDict):
    pass

class OptionalTransactionCaptureAuthorizationResponseSaleCardCustomer(TypedDict, total=False):
    guid: str

    firstName: str

    lastName: str

    dateOfBirth: str

    address1: str

    address2: str

    zip: str

    city: str

    state: str

    country: str

    phone: str

    email: str

    ssN4: str

    driverLicenseNumber: str

    driverLicenseState: str

class TransactionCaptureAuthorizationResponseSaleCardCustomer(RequiredTransactionCaptureAuthorizationResponseSaleCardCustomer, OptionalTransactionCaptureAuthorizationResponseSaleCardCustomer):
    pass
