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
from pydantic import BaseModel, Field, RootModel, ConfigDict


class AuthenticationAcquireClientAuthorizationRequestRiskDataFlightData(BaseModel):
    # Name of airline; likely carrier code
    airline: typing.Optional[str] = Field(None, alias='Airline')

    # Departure airport code
    departure_airport: typing.Optional[str] = Field(None, alias='DepartureAirport')

    # Departure date of flight. Format: mm/dd/yyyy
    departure_date: typing.Optional[str] = Field(None, alias='DepartureDate')

    # Destination airport code
    destination_airport: typing.Optional[str] = Field(None, alias='DestinationAirport')

    # Time in hours to flight departure
    hours_to_departure: typing.Optional[str] = Field(None, alias='HoursToDeparture')

    # Type of journey i.e. Day/Night journey
    journey_type: typing.Optional[str] = Field(None, alias='JourneyType')

    # The route type i.e. Direct/Indirect
    route: typing.Optional[str] = Field(None, alias='Route')

    # Complete flight route by country
    route_by_country: typing.Optional[str] = Field(None, alias='RouteByCountry')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
