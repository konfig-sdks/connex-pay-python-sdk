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


class RequiredAchCreateCreditPaymentRequestAccountHolderAddress(TypedDict):
    pass

class OptionalAchCreateCreditPaymentRequestAccountHolderAddress(TypedDict, total=False):
    # Address 1 up to 50 characters
    Address1: str

    # Address 2 up to 50 characters
    Address2: str

    # City up to 50 characters
    City: str

    # US State up to 2 characters
    State: str

    # Country. 'US' only as of now
    Country: str

    # ZipCode up to 10 characters
    ZipCode: str

class AchCreateCreditPaymentRequestAccountHolderAddress(RequiredAchCreateCreditPaymentRequestAccountHolderAddress, OptionalAchCreateCreditPaymentRequestAccountHolderAddress):
    pass
