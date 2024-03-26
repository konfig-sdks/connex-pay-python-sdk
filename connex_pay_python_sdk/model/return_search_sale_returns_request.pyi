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


class ReturnSearchSaleReturnsRequest(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            MerchantGuid = schemas.StrSchema
            AmountFrom = schemas.Float32Schema
            AmountTo = schemas.Float32Schema
            CardHolderName = schemas.StrSchema
            Status = schemas.StrSchema
            TimeStampFrom = schemas.DateSchema
            TimeStampTo = schemas.DateSchema
            __annotations__ = {
                "MerchantGuid": MerchantGuid,
                "AmountFrom": AmountFrom,
                "AmountTo": AmountTo,
                "CardHolderName": CardHolderName,
                "Status": Status,
                "TimeStampFrom": TimeStampFrom,
                "TimeStampTo": TimeStampTo,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["MerchantGuid"]) -> MetaOapg.properties.MerchantGuid: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["AmountFrom"]) -> MetaOapg.properties.AmountFrom: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["AmountTo"]) -> MetaOapg.properties.AmountTo: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["CardHolderName"]) -> MetaOapg.properties.CardHolderName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Status"]) -> MetaOapg.properties.Status: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["TimeStampFrom"]) -> MetaOapg.properties.TimeStampFrom: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["TimeStampTo"]) -> MetaOapg.properties.TimeStampTo: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["MerchantGuid", "AmountFrom", "AmountTo", "CardHolderName", "Status", "TimeStampFrom", "TimeStampTo", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["MerchantGuid"]) -> typing.Union[MetaOapg.properties.MerchantGuid, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["AmountFrom"]) -> typing.Union[MetaOapg.properties.AmountFrom, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["AmountTo"]) -> typing.Union[MetaOapg.properties.AmountTo, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["CardHolderName"]) -> typing.Union[MetaOapg.properties.CardHolderName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Status"]) -> typing.Union[MetaOapg.properties.Status, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["TimeStampFrom"]) -> typing.Union[MetaOapg.properties.TimeStampFrom, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["TimeStampTo"]) -> typing.Union[MetaOapg.properties.TimeStampTo, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["MerchantGuid", "AmountFrom", "AmountTo", "CardHolderName", "Status", "TimeStampFrom", "TimeStampTo", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        MerchantGuid: typing.Union[MetaOapg.properties.MerchantGuid, str, schemas.Unset] = schemas.unset,
        AmountFrom: typing.Union[MetaOapg.properties.AmountFrom, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        AmountTo: typing.Union[MetaOapg.properties.AmountTo, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        CardHolderName: typing.Union[MetaOapg.properties.CardHolderName, str, schemas.Unset] = schemas.unset,
        Status: typing.Union[MetaOapg.properties.Status, str, schemas.Unset] = schemas.unset,
        TimeStampFrom: typing.Union[MetaOapg.properties.TimeStampFrom, str, date, schemas.Unset] = schemas.unset,
        TimeStampTo: typing.Union[MetaOapg.properties.TimeStampTo, str, date, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ReturnSearchSaleReturnsRequest':
        return super().__new__(
            cls,
            *args,
            MerchantGuid=MerchantGuid,
            AmountFrom=AmountFrom,
            AmountTo=AmountTo,
            CardHolderName=CardHolderName,
            Status=Status,
            TimeStampFrom=TimeStampFrom,
            TimeStampTo=TimeStampTo,
            _configuration=_configuration,
            **kwargs,
        )
