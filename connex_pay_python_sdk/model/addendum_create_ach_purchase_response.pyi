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


class AddendumCreateAchPurchaseResponse(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            guid = schemas.StrSchema
            itemGuid = schemas.StrSchema
            value = schemas.StrSchema
            category = schemas.StrSchema
            idExternal = schemas.StrSchema
            note = schemas.StrSchema
            sequence = schemas.StrSchema
            __annotations__ = {
                "guid": guid,
                "itemGuid": itemGuid,
                "value": value,
                "category": category,
                "idExternal": idExternal,
                "note": note,
                "sequence": sequence,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["guid"]) -> MetaOapg.properties.guid: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["itemGuid"]) -> MetaOapg.properties.itemGuid: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["value"]) -> MetaOapg.properties.value: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["category"]) -> MetaOapg.properties.category: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["idExternal"]) -> MetaOapg.properties.idExternal: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["note"]) -> MetaOapg.properties.note: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["sequence"]) -> MetaOapg.properties.sequence: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["guid", "itemGuid", "value", "category", "idExternal", "note", "sequence", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["guid"]) -> typing.Union[MetaOapg.properties.guid, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["itemGuid"]) -> typing.Union[MetaOapg.properties.itemGuid, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["value"]) -> typing.Union[MetaOapg.properties.value, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["category"]) -> typing.Union[MetaOapg.properties.category, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["idExternal"]) -> typing.Union[MetaOapg.properties.idExternal, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["note"]) -> typing.Union[MetaOapg.properties.note, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["sequence"]) -> typing.Union[MetaOapg.properties.sequence, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["guid", "itemGuid", "value", "category", "idExternal", "note", "sequence", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        guid: typing.Union[MetaOapg.properties.guid, str, schemas.Unset] = schemas.unset,
        itemGuid: typing.Union[MetaOapg.properties.itemGuid, str, schemas.Unset] = schemas.unset,
        value: typing.Union[MetaOapg.properties.value, str, schemas.Unset] = schemas.unset,
        category: typing.Union[MetaOapg.properties.category, str, schemas.Unset] = schemas.unset,
        idExternal: typing.Union[MetaOapg.properties.idExternal, str, schemas.Unset] = schemas.unset,
        note: typing.Union[MetaOapg.properties.note, str, schemas.Unset] = schemas.unset,
        sequence: typing.Union[MetaOapg.properties.sequence, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'AddendumCreateAchPurchaseResponse':
        return super().__new__(
            cls,
            *args,
            guid=guid,
            itemGuid=itemGuid,
            value=value,
            category=category,
            idExternal=idExternal,
            note=note,
            sequence=sequence,
            _configuration=_configuration,
            **kwargs,
        )
