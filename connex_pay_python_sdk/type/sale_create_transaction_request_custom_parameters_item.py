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


class RequiredSaleCreateTransactionRequestCustomParametersItem(TypedDict):
    pass

class OptionalSaleCreateTransactionRequestCustomParametersItem(TypedDict, total=False):
    # Custom Parameter's Name, up to a maximum of 100 alphanumeric characters allowed.
    Name: str

    # Custom Parameter's Value, up to a maximum of 100 alphanumeric characters allowed.
    Value: str

class SaleCreateTransactionRequestCustomParametersItem(RequiredSaleCreateTransactionRequestCustomParametersItem, OptionalSaleCreateTransactionRequestCustomParametersItem):
    pass
