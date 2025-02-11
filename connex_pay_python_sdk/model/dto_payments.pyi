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


class DtoPayments(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            paymentGuid = schemas.UUIDSchema
            paymentReferenceToken = schemas.StrSchema
            payeeReferenceToken = schemas.StrSchema
            ridReferenceToken = schemas.StrSchema
            memo = schemas.StrSchema
            value = schemas.Float64Schema
            status = schemas.StrSchema
            field2 = schemas.StrSchema
            field3 = schemas.StrSchema
            field4 = schemas.StrSchema
            field5 = schemas.StrSchema
            terminationDate = schemas.StrSchema
            payeeName = schemas.StrSchema
            email = schemas.StrSchema
            lastFour = schemas.StrSchema
            address1 = schemas.StrSchema
            address2 = schemas.StrSchema
            city = schemas.StrSchema
            state = schemas.StrSchema
            zipCode = schemas.StrSchema
            country = schemas.StrSchema
            createdBy = schemas.StrSchema
            __annotations__ = {
                "paymentGuid": paymentGuid,
                "paymentReferenceToken": paymentReferenceToken,
                "payeeReferenceToken": payeeReferenceToken,
                "ridReferenceToken": ridReferenceToken,
                "memo": memo,
                "value": value,
                "status": status,
                "field2": field2,
                "field3": field3,
                "field4": field4,
                "field5": field5,
                "terminationDate": terminationDate,
                "payeeName": payeeName,
                "email": email,
                "lastFour": lastFour,
                "address1": address1,
                "address2": address2,
                "city": city,
                "state": state,
                "zipCode": zipCode,
                "country": country,
                "createdBy": createdBy,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["paymentGuid"]) -> MetaOapg.properties.paymentGuid: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["paymentReferenceToken"]) -> MetaOapg.properties.paymentReferenceToken: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["payeeReferenceToken"]) -> MetaOapg.properties.payeeReferenceToken: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ridReferenceToken"]) -> MetaOapg.properties.ridReferenceToken: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["memo"]) -> MetaOapg.properties.memo: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["value"]) -> MetaOapg.properties.value: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["status"]) -> MetaOapg.properties.status: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["field2"]) -> MetaOapg.properties.field2: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["field3"]) -> MetaOapg.properties.field3: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["field4"]) -> MetaOapg.properties.field4: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["field5"]) -> MetaOapg.properties.field5: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["terminationDate"]) -> MetaOapg.properties.terminationDate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["payeeName"]) -> MetaOapg.properties.payeeName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["email"]) -> MetaOapg.properties.email: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["lastFour"]) -> MetaOapg.properties.lastFour: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["address1"]) -> MetaOapg.properties.address1: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["address2"]) -> MetaOapg.properties.address2: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["city"]) -> MetaOapg.properties.city: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["state"]) -> MetaOapg.properties.state: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["zipCode"]) -> MetaOapg.properties.zipCode: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["country"]) -> MetaOapg.properties.country: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["createdBy"]) -> MetaOapg.properties.createdBy: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["paymentGuid", "paymentReferenceToken", "payeeReferenceToken", "ridReferenceToken", "memo", "value", "status", "field2", "field3", "field4", "field5", "terminationDate", "payeeName", "email", "lastFour", "address1", "address2", "city", "state", "zipCode", "country", "createdBy", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["paymentGuid"]) -> typing.Union[MetaOapg.properties.paymentGuid, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["paymentReferenceToken"]) -> typing.Union[MetaOapg.properties.paymentReferenceToken, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["payeeReferenceToken"]) -> typing.Union[MetaOapg.properties.payeeReferenceToken, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ridReferenceToken"]) -> typing.Union[MetaOapg.properties.ridReferenceToken, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["memo"]) -> typing.Union[MetaOapg.properties.memo, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["value"]) -> typing.Union[MetaOapg.properties.value, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["status"]) -> typing.Union[MetaOapg.properties.status, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["field2"]) -> typing.Union[MetaOapg.properties.field2, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["field3"]) -> typing.Union[MetaOapg.properties.field3, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["field4"]) -> typing.Union[MetaOapg.properties.field4, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["field5"]) -> typing.Union[MetaOapg.properties.field5, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["terminationDate"]) -> typing.Union[MetaOapg.properties.terminationDate, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["payeeName"]) -> typing.Union[MetaOapg.properties.payeeName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["email"]) -> typing.Union[MetaOapg.properties.email, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["lastFour"]) -> typing.Union[MetaOapg.properties.lastFour, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["address1"]) -> typing.Union[MetaOapg.properties.address1, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["address2"]) -> typing.Union[MetaOapg.properties.address2, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["city"]) -> typing.Union[MetaOapg.properties.city, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["state"]) -> typing.Union[MetaOapg.properties.state, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["zipCode"]) -> typing.Union[MetaOapg.properties.zipCode, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["country"]) -> typing.Union[MetaOapg.properties.country, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["createdBy"]) -> typing.Union[MetaOapg.properties.createdBy, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["paymentGuid", "paymentReferenceToken", "payeeReferenceToken", "ridReferenceToken", "memo", "value", "status", "field2", "field3", "field4", "field5", "terminationDate", "payeeName", "email", "lastFour", "address1", "address2", "city", "state", "zipCode", "country", "createdBy", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        paymentGuid: typing.Union[MetaOapg.properties.paymentGuid, str, uuid.UUID, schemas.Unset] = schemas.unset,
        paymentReferenceToken: typing.Union[MetaOapg.properties.paymentReferenceToken, str, schemas.Unset] = schemas.unset,
        payeeReferenceToken: typing.Union[MetaOapg.properties.payeeReferenceToken, str, schemas.Unset] = schemas.unset,
        ridReferenceToken: typing.Union[MetaOapg.properties.ridReferenceToken, str, schemas.Unset] = schemas.unset,
        memo: typing.Union[MetaOapg.properties.memo, str, schemas.Unset] = schemas.unset,
        value: typing.Union[MetaOapg.properties.value, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        status: typing.Union[MetaOapg.properties.status, str, schemas.Unset] = schemas.unset,
        field2: typing.Union[MetaOapg.properties.field2, str, schemas.Unset] = schemas.unset,
        field3: typing.Union[MetaOapg.properties.field3, str, schemas.Unset] = schemas.unset,
        field4: typing.Union[MetaOapg.properties.field4, str, schemas.Unset] = schemas.unset,
        field5: typing.Union[MetaOapg.properties.field5, str, schemas.Unset] = schemas.unset,
        terminationDate: typing.Union[MetaOapg.properties.terminationDate, str, schemas.Unset] = schemas.unset,
        payeeName: typing.Union[MetaOapg.properties.payeeName, str, schemas.Unset] = schemas.unset,
        email: typing.Union[MetaOapg.properties.email, str, schemas.Unset] = schemas.unset,
        lastFour: typing.Union[MetaOapg.properties.lastFour, str, schemas.Unset] = schemas.unset,
        address1: typing.Union[MetaOapg.properties.address1, str, schemas.Unset] = schemas.unset,
        address2: typing.Union[MetaOapg.properties.address2, str, schemas.Unset] = schemas.unset,
        city: typing.Union[MetaOapg.properties.city, str, schemas.Unset] = schemas.unset,
        state: typing.Union[MetaOapg.properties.state, str, schemas.Unset] = schemas.unset,
        zipCode: typing.Union[MetaOapg.properties.zipCode, str, schemas.Unset] = schemas.unset,
        country: typing.Union[MetaOapg.properties.country, str, schemas.Unset] = schemas.unset,
        createdBy: typing.Union[MetaOapg.properties.createdBy, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'DtoPayments':
        return super().__new__(
            cls,
            *args,
            paymentGuid=paymentGuid,
            paymentReferenceToken=paymentReferenceToken,
            payeeReferenceToken=payeeReferenceToken,
            ridReferenceToken=ridReferenceToken,
            memo=memo,
            value=value,
            status=status,
            field2=field2,
            field3=field3,
            field4=field4,
            field5=field5,
            terminationDate=terminationDate,
            payeeName=payeeName,
            email=email,
            lastFour=lastFour,
            address1=address1,
            address2=address2,
            city=city,
            state=state,
            zipCode=zipCode,
            country=country,
            createdBy=createdBy,
            _configuration=_configuration,
            **kwargs,
        )
