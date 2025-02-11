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


class SettingTokenizeBankAccountInfoRequestAccountHolderAddress(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Account Holder Address
    """


    class MetaOapg:
        
        class properties:
            Address1 = schemas.StrSchema
            Address2 = schemas.StrSchema
            City = schemas.StrSchema
            State = schemas.StrSchema
            Country = schemas.StrSchema
            ZipCode = schemas.StrSchema
            __annotations__ = {
                "Address1": Address1,
                "Address2": Address2,
                "City": City,
                "State": State,
                "Country": Country,
                "ZipCode": ZipCode,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Address1"]) -> MetaOapg.properties.Address1: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Address2"]) -> MetaOapg.properties.Address2: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["City"]) -> MetaOapg.properties.City: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["State"]) -> MetaOapg.properties.State: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Country"]) -> MetaOapg.properties.Country: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ZipCode"]) -> MetaOapg.properties.ZipCode: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["Address1", "Address2", "City", "State", "Country", "ZipCode", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Address1"]) -> typing.Union[MetaOapg.properties.Address1, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Address2"]) -> typing.Union[MetaOapg.properties.Address2, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["City"]) -> typing.Union[MetaOapg.properties.City, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["State"]) -> typing.Union[MetaOapg.properties.State, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Country"]) -> typing.Union[MetaOapg.properties.Country, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ZipCode"]) -> typing.Union[MetaOapg.properties.ZipCode, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["Address1", "Address2", "City", "State", "Country", "ZipCode", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        Address1: typing.Union[MetaOapg.properties.Address1, str, schemas.Unset] = schemas.unset,
        Address2: typing.Union[MetaOapg.properties.Address2, str, schemas.Unset] = schemas.unset,
        City: typing.Union[MetaOapg.properties.City, str, schemas.Unset] = schemas.unset,
        State: typing.Union[MetaOapg.properties.State, str, schemas.Unset] = schemas.unset,
        Country: typing.Union[MetaOapg.properties.Country, str, schemas.Unset] = schemas.unset,
        ZipCode: typing.Union[MetaOapg.properties.ZipCode, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'SettingTokenizeBankAccountInfoRequestAccountHolderAddress':
        return super().__new__(
            cls,
            *args,
            Address1=Address1,
            Address2=Address2,
            City=City,
            State=State,
            Country=Country,
            ZipCode=ZipCode,
            _configuration=_configuration,
            **kwargs,
        )
