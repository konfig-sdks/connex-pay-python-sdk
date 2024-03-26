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


class RequiredSaleCreateTransactionRequestRiskDataFlightData(TypedDict):
    pass

class OptionalSaleCreateTransactionRequestRiskDataFlightData(TypedDict, total=False):
    # Name of airline; likely carrier code
    Airline: str

    # Departure airport code
    DepartureAirport: str

    # Departure date of flight. Format: mm/dd/yyyy
    DepartureDate: str

    # Destination airport code
    DestinationAirport: str

    # Time in hours to flight departure
    HoursToDeparture: str

    # Type of journey i.e. Day/Night journey
    JourneyType: str

    # The route type i.e. Direct/Indirect
    Route: str

    # Complete flight route by country
    RouteByCountry: str

class SaleCreateTransactionRequestRiskDataFlightData(RequiredSaleCreateTransactionRequestRiskDataFlightData, OptionalSaleCreateTransactionRequestRiskDataFlightData):
    pass
