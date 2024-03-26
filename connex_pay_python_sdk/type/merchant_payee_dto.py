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


class RequiredMerchantPayeeDto(TypedDict):
    isBusiness: bool

    payeeId: str

    preferredPayoutMethod: str

class OptionalMerchantPayeeDto(TypedDict, total=False):
    idMerchant: int

    firstName: str

    lastName: str

    dbaName: str

    taxId: str

    customerId: str

    email: str

    address1: str

    address2: str

    city: str

    state: str

    zip: str

    country: str

    preferredCardBrand: str

    preferredCardClass: str

    purchaseType: str

    guid: str

    timestamp: datetime

class MerchantPayeeDto(RequiredMerchantPayeeDto, OptionalMerchantPayeeDto):
    pass
