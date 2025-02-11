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


class ReturnItemRequestResponseSaleCardCustomer(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            guid = schemas.StrSchema
            firstName = schemas.StrSchema
            lastName = schemas.StrSchema
            phone = schemas.StrSchema
            city = schemas.StrSchema
            country = schemas.StrSchema
            email = schemas.StrSchema
            zip = schemas.StrSchema
            address1 = schemas.StrSchema
            address2 = schemas.StrSchema
            state = schemas.StrSchema
            dateOfBirth = schemas.StrSchema
            driverLicenseNumber = schemas.StrSchema
            driverLicenseState = schemas.StrSchema
            ssN4 = schemas.StrSchema
            __annotations__ = {
                "guid": guid,
                "firstName": firstName,
                "lastName": lastName,
                "phone": phone,
                "city": city,
                "country": country,
                "email": email,
                "zip": zip,
                "address1": address1,
                "address2": address2,
                "state": state,
                "dateOfBirth": dateOfBirth,
                "driverLicenseNumber": driverLicenseNumber,
                "driverLicenseState": driverLicenseState,
                "ssN4": ssN4,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["guid"]) -> MetaOapg.properties.guid: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["firstName"]) -> MetaOapg.properties.firstName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["lastName"]) -> MetaOapg.properties.lastName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["phone"]) -> MetaOapg.properties.phone: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["city"]) -> MetaOapg.properties.city: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["country"]) -> MetaOapg.properties.country: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["email"]) -> MetaOapg.properties.email: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["zip"]) -> MetaOapg.properties.zip: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["address1"]) -> MetaOapg.properties.address1: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["address2"]) -> MetaOapg.properties.address2: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["state"]) -> MetaOapg.properties.state: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["dateOfBirth"]) -> MetaOapg.properties.dateOfBirth: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["driverLicenseNumber"]) -> MetaOapg.properties.driverLicenseNumber: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["driverLicenseState"]) -> MetaOapg.properties.driverLicenseState: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ssN4"]) -> MetaOapg.properties.ssN4: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["guid", "firstName", "lastName", "phone", "city", "country", "email", "zip", "address1", "address2", "state", "dateOfBirth", "driverLicenseNumber", "driverLicenseState", "ssN4", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["guid"]) -> typing.Union[MetaOapg.properties.guid, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["firstName"]) -> typing.Union[MetaOapg.properties.firstName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["lastName"]) -> typing.Union[MetaOapg.properties.lastName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["phone"]) -> typing.Union[MetaOapg.properties.phone, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["city"]) -> typing.Union[MetaOapg.properties.city, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["country"]) -> typing.Union[MetaOapg.properties.country, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["email"]) -> typing.Union[MetaOapg.properties.email, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["zip"]) -> typing.Union[MetaOapg.properties.zip, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["address1"]) -> typing.Union[MetaOapg.properties.address1, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["address2"]) -> typing.Union[MetaOapg.properties.address2, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["state"]) -> typing.Union[MetaOapg.properties.state, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["dateOfBirth"]) -> typing.Union[MetaOapg.properties.dateOfBirth, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["driverLicenseNumber"]) -> typing.Union[MetaOapg.properties.driverLicenseNumber, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["driverLicenseState"]) -> typing.Union[MetaOapg.properties.driverLicenseState, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ssN4"]) -> typing.Union[MetaOapg.properties.ssN4, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["guid", "firstName", "lastName", "phone", "city", "country", "email", "zip", "address1", "address2", "state", "dateOfBirth", "driverLicenseNumber", "driverLicenseState", "ssN4", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        guid: typing.Union[MetaOapg.properties.guid, str, schemas.Unset] = schemas.unset,
        firstName: typing.Union[MetaOapg.properties.firstName, str, schemas.Unset] = schemas.unset,
        lastName: typing.Union[MetaOapg.properties.lastName, str, schemas.Unset] = schemas.unset,
        phone: typing.Union[MetaOapg.properties.phone, str, schemas.Unset] = schemas.unset,
        city: typing.Union[MetaOapg.properties.city, str, schemas.Unset] = schemas.unset,
        country: typing.Union[MetaOapg.properties.country, str, schemas.Unset] = schemas.unset,
        email: typing.Union[MetaOapg.properties.email, str, schemas.Unset] = schemas.unset,
        zip: typing.Union[MetaOapg.properties.zip, str, schemas.Unset] = schemas.unset,
        address1: typing.Union[MetaOapg.properties.address1, str, schemas.Unset] = schemas.unset,
        address2: typing.Union[MetaOapg.properties.address2, str, schemas.Unset] = schemas.unset,
        state: typing.Union[MetaOapg.properties.state, str, schemas.Unset] = schemas.unset,
        dateOfBirth: typing.Union[MetaOapg.properties.dateOfBirth, str, schemas.Unset] = schemas.unset,
        driverLicenseNumber: typing.Union[MetaOapg.properties.driverLicenseNumber, str, schemas.Unset] = schemas.unset,
        driverLicenseState: typing.Union[MetaOapg.properties.driverLicenseState, str, schemas.Unset] = schemas.unset,
        ssN4: typing.Union[MetaOapg.properties.ssN4, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ReturnItemRequestResponseSaleCardCustomer':
        return super().__new__(
            cls,
            *args,
            guid=guid,
            firstName=firstName,
            lastName=lastName,
            phone=phone,
            city=city,
            country=country,
            email=email,
            zip=zip,
            address1=address1,
            address2=address2,
            state=state,
            dateOfBirth=dateOfBirth,
            driverLicenseNumber=driverLicenseNumber,
            driverLicenseState=driverLicenseState,
            ssN4=ssN4,
            _configuration=_configuration,
            **kwargs,
        )
