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


class ReturnSearchSaleReturnsResponseSearchResultDtoItem(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            status = schemas.StrSchema
            amount = schemas.IntSchema
        
            @staticmethod
            def card() -> typing.Type['ReturnSearchSaleReturnsResponseSearchResultDtoItemCard']:
                return ReturnSearchSaleReturnsResponseSearchResultDtoItemCard
            timeStamp = schemas.StrSchema
            processorStatusCode = schemas.StrSchema
            batchStatus = schemas.StrSchema
            guid = schemas.StrSchema
            relatedVoid = schemas.AnyTypeSchema
            deviceGuid = schemas.StrSchema
            type = schemas.StrSchema
            cardDataSource = schemas.StrSchema
            allowCardEmv = schemas.BoolSchema
            __annotations__ = {
                "status": status,
                "amount": amount,
                "card": card,
                "timeStamp": timeStamp,
                "processorStatusCode": processorStatusCode,
                "batchStatus": batchStatus,
                "guid": guid,
                "relatedVoid": relatedVoid,
                "deviceGuid": deviceGuid,
                "type": type,
                "cardDataSource": cardDataSource,
                "allowCardEmv": allowCardEmv,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["status"]) -> MetaOapg.properties.status: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["amount"]) -> MetaOapg.properties.amount: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["card"]) -> 'ReturnSearchSaleReturnsResponseSearchResultDtoItemCard': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["timeStamp"]) -> MetaOapg.properties.timeStamp: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["processorStatusCode"]) -> MetaOapg.properties.processorStatusCode: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["batchStatus"]) -> MetaOapg.properties.batchStatus: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["guid"]) -> MetaOapg.properties.guid: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["relatedVoid"]) -> MetaOapg.properties.relatedVoid: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["deviceGuid"]) -> MetaOapg.properties.deviceGuid: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["cardDataSource"]) -> MetaOapg.properties.cardDataSource: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["allowCardEmv"]) -> MetaOapg.properties.allowCardEmv: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["status", "amount", "card", "timeStamp", "processorStatusCode", "batchStatus", "guid", "relatedVoid", "deviceGuid", "type", "cardDataSource", "allowCardEmv", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["status"]) -> typing.Union[MetaOapg.properties.status, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["amount"]) -> typing.Union[MetaOapg.properties.amount, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["card"]) -> typing.Union['ReturnSearchSaleReturnsResponseSearchResultDtoItemCard', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["timeStamp"]) -> typing.Union[MetaOapg.properties.timeStamp, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["processorStatusCode"]) -> typing.Union[MetaOapg.properties.processorStatusCode, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["batchStatus"]) -> typing.Union[MetaOapg.properties.batchStatus, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["guid"]) -> typing.Union[MetaOapg.properties.guid, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["relatedVoid"]) -> typing.Union[MetaOapg.properties.relatedVoid, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["deviceGuid"]) -> typing.Union[MetaOapg.properties.deviceGuid, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["type"]) -> typing.Union[MetaOapg.properties.type, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["cardDataSource"]) -> typing.Union[MetaOapg.properties.cardDataSource, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["allowCardEmv"]) -> typing.Union[MetaOapg.properties.allowCardEmv, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["status", "amount", "card", "timeStamp", "processorStatusCode", "batchStatus", "guid", "relatedVoid", "deviceGuid", "type", "cardDataSource", "allowCardEmv", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        status: typing.Union[MetaOapg.properties.status, str, schemas.Unset] = schemas.unset,
        amount: typing.Union[MetaOapg.properties.amount, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        card: typing.Union['ReturnSearchSaleReturnsResponseSearchResultDtoItemCard', schemas.Unset] = schemas.unset,
        timeStamp: typing.Union[MetaOapg.properties.timeStamp, str, schemas.Unset] = schemas.unset,
        processorStatusCode: typing.Union[MetaOapg.properties.processorStatusCode, str, schemas.Unset] = schemas.unset,
        batchStatus: typing.Union[MetaOapg.properties.batchStatus, str, schemas.Unset] = schemas.unset,
        guid: typing.Union[MetaOapg.properties.guid, str, schemas.Unset] = schemas.unset,
        relatedVoid: typing.Union[MetaOapg.properties.relatedVoid, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, schemas.Unset] = schemas.unset,
        deviceGuid: typing.Union[MetaOapg.properties.deviceGuid, str, schemas.Unset] = schemas.unset,
        type: typing.Union[MetaOapg.properties.type, str, schemas.Unset] = schemas.unset,
        cardDataSource: typing.Union[MetaOapg.properties.cardDataSource, str, schemas.Unset] = schemas.unset,
        allowCardEmv: typing.Union[MetaOapg.properties.allowCardEmv, bool, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ReturnSearchSaleReturnsResponseSearchResultDtoItem':
        return super().__new__(
            cls,
            *args,
            status=status,
            amount=amount,
            card=card,
            timeStamp=timeStamp,
            processorStatusCode=processorStatusCode,
            batchStatus=batchStatus,
            guid=guid,
            relatedVoid=relatedVoid,
            deviceGuid=deviceGuid,
            type=type,
            cardDataSource=cardDataSource,
            allowCardEmv=allowCardEmv,
            _configuration=_configuration,
            **kwargs,
        )

from connex_pay_python_sdk.model.return_search_sale_returns_response_search_result_dto_item_card import ReturnSearchSaleReturnsResponseSearchResultDtoItemCard
