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


class RequiredSettlementSearchVirtualCardSettlementsRequest(TypedDict):
    # Merchant's Guid.
    MerchantGuid: str

class OptionalSettlementSearchVirtualCardSettlementsRequest(TypedDict, total=False):
    # Card's Issued Date.
    DateFrom: date

    # Card's Issued Date.
    DateTo: date

    # Card settlement post date.
    PostedDateFrom: date

    # Card settlement post date.
    PostedDateTo: date

    # Order Number. Max. Length = 50.
    OrderNumber: str

    # Issued Amount of the Card.
    IssuedAmountFrom: int

    # Issued Amount of the Card.
    IssuedAmountTo: int

    # Card last four number.
    IssuedCardLastFour: str

    # Posted Amount of the Card.
    PostedAmountFrom: typing.Union[int, float]

    # Posted Amount of the Card.
    PostedAmountTo: typing.Union[int, float]

    # Card's expiration date.
    ExpirationDateFrom: date

    # Card's expiration date.
    ExpirationDateTo: date

class SettlementSearchVirtualCardSettlementsRequest(RequiredSettlementSearchVirtualCardSettlementsRequest, OptionalSettlementSearchVirtualCardSettlementsRequest):
    pass
