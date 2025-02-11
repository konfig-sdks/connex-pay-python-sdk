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


class AuthenticationResult(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            AccessToken = schemas.StrSchema
            ExpiresIn = schemas.Int32Schema
            TokenType = schemas.StrSchema
            RefreshToken = schemas.StrSchema
            IdToken = schemas.StrSchema
            __annotations__ = {
                "AccessToken": AccessToken,
                "ExpiresIn": ExpiresIn,
                "TokenType": TokenType,
                "RefreshToken": RefreshToken,
                "IdToken": IdToken,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["AccessToken"]) -> MetaOapg.properties.AccessToken: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ExpiresIn"]) -> MetaOapg.properties.ExpiresIn: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["TokenType"]) -> MetaOapg.properties.TokenType: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["RefreshToken"]) -> MetaOapg.properties.RefreshToken: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["IdToken"]) -> MetaOapg.properties.IdToken: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["AccessToken", "ExpiresIn", "TokenType", "RefreshToken", "IdToken", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["AccessToken"]) -> typing.Union[MetaOapg.properties.AccessToken, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ExpiresIn"]) -> typing.Union[MetaOapg.properties.ExpiresIn, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["TokenType"]) -> typing.Union[MetaOapg.properties.TokenType, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["RefreshToken"]) -> typing.Union[MetaOapg.properties.RefreshToken, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["IdToken"]) -> typing.Union[MetaOapg.properties.IdToken, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["AccessToken", "ExpiresIn", "TokenType", "RefreshToken", "IdToken", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        AccessToken: typing.Union[MetaOapg.properties.AccessToken, str, schemas.Unset] = schemas.unset,
        ExpiresIn: typing.Union[MetaOapg.properties.ExpiresIn, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        TokenType: typing.Union[MetaOapg.properties.TokenType, str, schemas.Unset] = schemas.unset,
        RefreshToken: typing.Union[MetaOapg.properties.RefreshToken, str, schemas.Unset] = schemas.unset,
        IdToken: typing.Union[MetaOapg.properties.IdToken, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'AuthenticationResult':
        return super().__new__(
            cls,
            *args,
            AccessToken=AccessToken,
            ExpiresIn=ExpiresIn,
            TokenType=TokenType,
            RefreshToken=RefreshToken,
            IdToken=IdToken,
            _configuration=_configuration,
            **kwargs,
        )
