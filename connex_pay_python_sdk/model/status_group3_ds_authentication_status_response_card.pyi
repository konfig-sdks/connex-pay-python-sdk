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


class StatusGroup3DsAuthenticationStatusResponseCard(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            first6 = schemas.StrSchema
            first4 = schemas.StrSchema
            last4 = schemas.StrSchema
            cardType = schemas.StrSchema
            expirationDate = schemas.StrSchema
            guid = schemas.StrSchema
            __annotations__ = {
                "first6": first6,
                "first4": first4,
                "last4": last4,
                "cardType": cardType,
                "expirationDate": expirationDate,
                "guid": guid,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["first6"]) -> MetaOapg.properties.first6: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["first4"]) -> MetaOapg.properties.first4: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["last4"]) -> MetaOapg.properties.last4: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["cardType"]) -> MetaOapg.properties.cardType: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["expirationDate"]) -> MetaOapg.properties.expirationDate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["guid"]) -> MetaOapg.properties.guid: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["first6", "first4", "last4", "cardType", "expirationDate", "guid", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["first6"]) -> typing.Union[MetaOapg.properties.first6, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["first4"]) -> typing.Union[MetaOapg.properties.first4, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["last4"]) -> typing.Union[MetaOapg.properties.last4, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["cardType"]) -> typing.Union[MetaOapg.properties.cardType, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["expirationDate"]) -> typing.Union[MetaOapg.properties.expirationDate, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["guid"]) -> typing.Union[MetaOapg.properties.guid, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["first6", "first4", "last4", "cardType", "expirationDate", "guid", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        first6: typing.Union[MetaOapg.properties.first6, str, schemas.Unset] = schemas.unset,
        first4: typing.Union[MetaOapg.properties.first4, str, schemas.Unset] = schemas.unset,
        last4: typing.Union[MetaOapg.properties.last4, str, schemas.Unset] = schemas.unset,
        cardType: typing.Union[MetaOapg.properties.cardType, str, schemas.Unset] = schemas.unset,
        expirationDate: typing.Union[MetaOapg.properties.expirationDate, str, schemas.Unset] = schemas.unset,
        guid: typing.Union[MetaOapg.properties.guid, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'StatusGroup3DsAuthenticationStatusResponseCard':
        return super().__new__(
            cls,
            *args,
            first6=first6,
            first4=first4,
            last4=last4,
            cardType=cardType,
            expirationDate=expirationDate,
            guid=guid,
            _configuration=_configuration,
            **kwargs,
        )
