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

from connex_pay_python_sdk.type.sale_create_transaction_request_risk_data_flight_passengers_item import SaleCreateTransactionRequestRiskDataFlightPassengersItem

SaleCreateTransactionRequestRiskDataFlightPassengers = typing.List[SaleCreateTransactionRequestRiskDataFlightPassengersItem]
