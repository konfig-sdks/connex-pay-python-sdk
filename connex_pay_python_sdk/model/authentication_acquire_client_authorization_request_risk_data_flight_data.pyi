# coding: utf-8

"""
    ConnexPay Reporting API

    REST API for retrieving reporting data. Currently Daily Accounting data only.

    The version of the OpenAPI document: v1
    Created by: https://docs.connexpay.com
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from connex_pay_python_sdk import schemas  # noqa: F401


class AuthenticationAcquireClientAuthorizationRequestRiskDataFlightData(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Flight Data
    """


    class MetaOapg:
        
        class properties:
            Airline = schemas.StrSchema
            DepartureAirport = schemas.StrSchema
            DepartureDate = schemas.StrSchema
            DestinationAirport = schemas.StrSchema
            HoursToDeparture = schemas.StrSchema
            JourneyType = schemas.StrSchema
            Route = schemas.StrSchema
            RouteByCountry = schemas.StrSchema
            __annotations__ = {
                "Airline": Airline,
                "DepartureAirport": DepartureAirport,
                "DepartureDate": DepartureDate,
                "DestinationAirport": DestinationAirport,
                "HoursToDeparture": HoursToDeparture,
                "JourneyType": JourneyType,
                "Route": Route,
                "RouteByCountry": RouteByCountry,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Airline"]) -> MetaOapg.properties.Airline: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["DepartureAirport"]) -> MetaOapg.properties.DepartureAirport: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["DepartureDate"]) -> MetaOapg.properties.DepartureDate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["DestinationAirport"]) -> MetaOapg.properties.DestinationAirport: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["HoursToDeparture"]) -> MetaOapg.properties.HoursToDeparture: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["JourneyType"]) -> MetaOapg.properties.JourneyType: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Route"]) -> MetaOapg.properties.Route: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["RouteByCountry"]) -> MetaOapg.properties.RouteByCountry: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["Airline", "DepartureAirport", "DepartureDate", "DestinationAirport", "HoursToDeparture", "JourneyType", "Route", "RouteByCountry", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Airline"]) -> typing.Union[MetaOapg.properties.Airline, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["DepartureAirport"]) -> typing.Union[MetaOapg.properties.DepartureAirport, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["DepartureDate"]) -> typing.Union[MetaOapg.properties.DepartureDate, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["DestinationAirport"]) -> typing.Union[MetaOapg.properties.DestinationAirport, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["HoursToDeparture"]) -> typing.Union[MetaOapg.properties.HoursToDeparture, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["JourneyType"]) -> typing.Union[MetaOapg.properties.JourneyType, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Route"]) -> typing.Union[MetaOapg.properties.Route, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["RouteByCountry"]) -> typing.Union[MetaOapg.properties.RouteByCountry, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["Airline", "DepartureAirport", "DepartureDate", "DestinationAirport", "HoursToDeparture", "JourneyType", "Route", "RouteByCountry", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        Airline: typing.Union[MetaOapg.properties.Airline, str, schemas.Unset] = schemas.unset,
        DepartureAirport: typing.Union[MetaOapg.properties.DepartureAirport, str, schemas.Unset] = schemas.unset,
        DepartureDate: typing.Union[MetaOapg.properties.DepartureDate, str, schemas.Unset] = schemas.unset,
        DestinationAirport: typing.Union[MetaOapg.properties.DestinationAirport, str, schemas.Unset] = schemas.unset,
        HoursToDeparture: typing.Union[MetaOapg.properties.HoursToDeparture, str, schemas.Unset] = schemas.unset,
        JourneyType: typing.Union[MetaOapg.properties.JourneyType, str, schemas.Unset] = schemas.unset,
        Route: typing.Union[MetaOapg.properties.Route, str, schemas.Unset] = schemas.unset,
        RouteByCountry: typing.Union[MetaOapg.properties.RouteByCountry, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'AuthenticationAcquireClientAuthorizationRequestRiskDataFlightData':
        return super().__new__(
            cls,
            *args,
            Airline=Airline,
            DepartureAirport=DepartureAirport,
            DepartureDate=DepartureDate,
            DestinationAirport=DestinationAirport,
            HoursToDeparture=HoursToDeparture,
            JourneyType=JourneyType,
            Route=Route,
            RouteByCountry=RouteByCountry,
            _configuration=_configuration,
            **kwargs,
        )
