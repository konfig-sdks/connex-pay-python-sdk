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


class TransactionCreateAchCreditPaymentResponse(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            description = schemas.StrSchema
            merchantId = schemas.StrSchema
            incomingTransactionCode = schemas.StrSchema
            paymentId = schemas.StrSchema
            isCredit = schemas.BoolSchema
            amount = schemas.IntSchema
            payeeName = schemas.StrSchema
            paymentStatus = schemas.StrSchema
            scheduleDate = schemas.StrSchema
            receiptDate = schemas.StrSchema
            processingDate = schemas.AnyTypeSchema
            __annotations__ = {
                "description": description,
                "merchantId": merchantId,
                "incomingTransactionCode": incomingTransactionCode,
                "paymentId": paymentId,
                "isCredit": isCredit,
                "amount": amount,
                "payeeName": payeeName,
                "paymentStatus": paymentStatus,
                "scheduleDate": scheduleDate,
                "receiptDate": receiptDate,
                "processingDate": processingDate,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["description"]) -> MetaOapg.properties.description: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["merchantId"]) -> MetaOapg.properties.merchantId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["incomingTransactionCode"]) -> MetaOapg.properties.incomingTransactionCode: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["paymentId"]) -> MetaOapg.properties.paymentId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["isCredit"]) -> MetaOapg.properties.isCredit: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["amount"]) -> MetaOapg.properties.amount: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["payeeName"]) -> MetaOapg.properties.payeeName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["paymentStatus"]) -> MetaOapg.properties.paymentStatus: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["scheduleDate"]) -> MetaOapg.properties.scheduleDate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["receiptDate"]) -> MetaOapg.properties.receiptDate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["processingDate"]) -> MetaOapg.properties.processingDate: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["description", "merchantId", "incomingTransactionCode", "paymentId", "isCredit", "amount", "payeeName", "paymentStatus", "scheduleDate", "receiptDate", "processingDate", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["description"]) -> typing.Union[MetaOapg.properties.description, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["merchantId"]) -> typing.Union[MetaOapg.properties.merchantId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["incomingTransactionCode"]) -> typing.Union[MetaOapg.properties.incomingTransactionCode, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["paymentId"]) -> typing.Union[MetaOapg.properties.paymentId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["isCredit"]) -> typing.Union[MetaOapg.properties.isCredit, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["amount"]) -> typing.Union[MetaOapg.properties.amount, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["payeeName"]) -> typing.Union[MetaOapg.properties.payeeName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["paymentStatus"]) -> typing.Union[MetaOapg.properties.paymentStatus, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["scheduleDate"]) -> typing.Union[MetaOapg.properties.scheduleDate, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["receiptDate"]) -> typing.Union[MetaOapg.properties.receiptDate, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["processingDate"]) -> typing.Union[MetaOapg.properties.processingDate, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["description", "merchantId", "incomingTransactionCode", "paymentId", "isCredit", "amount", "payeeName", "paymentStatus", "scheduleDate", "receiptDate", "processingDate", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        description: typing.Union[MetaOapg.properties.description, str, schemas.Unset] = schemas.unset,
        merchantId: typing.Union[MetaOapg.properties.merchantId, str, schemas.Unset] = schemas.unset,
        incomingTransactionCode: typing.Union[MetaOapg.properties.incomingTransactionCode, str, schemas.Unset] = schemas.unset,
        paymentId: typing.Union[MetaOapg.properties.paymentId, str, schemas.Unset] = schemas.unset,
        isCredit: typing.Union[MetaOapg.properties.isCredit, bool, schemas.Unset] = schemas.unset,
        amount: typing.Union[MetaOapg.properties.amount, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        payeeName: typing.Union[MetaOapg.properties.payeeName, str, schemas.Unset] = schemas.unset,
        paymentStatus: typing.Union[MetaOapg.properties.paymentStatus, str, schemas.Unset] = schemas.unset,
        scheduleDate: typing.Union[MetaOapg.properties.scheduleDate, str, schemas.Unset] = schemas.unset,
        receiptDate: typing.Union[MetaOapg.properties.receiptDate, str, schemas.Unset] = schemas.unset,
        processingDate: typing.Union[MetaOapg.properties.processingDate, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'TransactionCreateAchCreditPaymentResponse':
        return super().__new__(
            cls,
            *args,
            description=description,
            merchantId=merchantId,
            incomingTransactionCode=incomingTransactionCode,
            paymentId=paymentId,
            isCredit=isCredit,
            amount=amount,
            payeeName=payeeName,
            paymentStatus=paymentStatus,
            scheduleDate=scheduleDate,
            receiptDate=receiptDate,
            processingDate=processingDate,
            _configuration=_configuration,
            **kwargs,
        )
