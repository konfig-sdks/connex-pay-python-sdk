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


class RequiredSaleCreateTransactionRequestRiskDataFlightPassengersItem(TypedDict):
    pass

class OptionalSaleCreateTransactionRequestRiskDataFlightPassengersItem(TypedDict, total=False):
    # Country of origin of passenger
    Country: str

    # DOB of first passenger
    DateOfBirth: date

    # Passport, drivers license or id# associated with passenger
    Id: str

    # Passenger information. Each passenger should be sent in it's own object.
    Name: str

class SaleCreateTransactionRequestRiskDataFlightPassengersItem(RequiredSaleCreateTransactionRequestRiskDataFlightPassengersItem, OptionalSaleCreateTransactionRequestRiskDataFlightPassengersItem):
    pass
