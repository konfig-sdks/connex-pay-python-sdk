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


class RequiredSaleCreateTransactionResponseCardCustomer(TypedDict):
    pass

class OptionalSaleCreateTransactionResponseCardCustomer(TypedDict, total=False):
    FirstName: str

    LastName: str

    Email: str

    Address1: str

    Address2: str

    State: str

    City: str

    Country: str

    Zip: str

    Phone: str

    SSN4: str

class SaleCreateTransactionResponseCardCustomer(RequiredSaleCreateTransactionResponseCardCustomer, OptionalSaleCreateTransactionResponseCardCustomer):
    pass
