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


class VoidCreateVoidResponse(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            guid = schemas.StrSchema
            amount = schemas.NumberSchema
            batchStatus = schemas.StrSchema
            timeStamp = schemas.StrSchema
            deviceGuid = schemas.StrSchema
            saleGuid = schemas.StrSchema
            status = schemas.StrSchema
            voidReason = schemas.StrSchema
            processorStatusCode = schemas.StrSchema
            wasProcessed = schemas.BoolSchema
            batchGuid = schemas.StrSchema
            authCode = schemas.StrSchema
            refNumber = schemas.StrSchema
            invoiceNumber = schemas.StrSchema
            customerReceipt = schemas.StrSchema
            sequenceNumber = schemas.StrSchema
        
            @staticmethod
            def sale() -> typing.Type['VoidCreateVoidResponseSale']:
                return VoidCreateVoidResponseSale
            __annotations__ = {
                "guid": guid,
                "amount": amount,
                "batchStatus": batchStatus,
                "timeStamp": timeStamp,
                "deviceGuid": deviceGuid,
                "saleGuid": saleGuid,
                "status": status,
                "voidReason": voidReason,
                "processorStatusCode": processorStatusCode,
                "wasProcessed": wasProcessed,
                "batchGuid": batchGuid,
                "authCode": authCode,
                "refNumber": refNumber,
                "invoiceNumber": invoiceNumber,
                "customerReceipt": customerReceipt,
                "sequenceNumber": sequenceNumber,
                "sale": sale,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["guid"]) -> MetaOapg.properties.guid: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["amount"]) -> MetaOapg.properties.amount: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["batchStatus"]) -> MetaOapg.properties.batchStatus: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["timeStamp"]) -> MetaOapg.properties.timeStamp: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["deviceGuid"]) -> MetaOapg.properties.deviceGuid: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["saleGuid"]) -> MetaOapg.properties.saleGuid: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["status"]) -> MetaOapg.properties.status: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["voidReason"]) -> MetaOapg.properties.voidReason: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["processorStatusCode"]) -> MetaOapg.properties.processorStatusCode: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["wasProcessed"]) -> MetaOapg.properties.wasProcessed: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["batchGuid"]) -> MetaOapg.properties.batchGuid: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["authCode"]) -> MetaOapg.properties.authCode: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["refNumber"]) -> MetaOapg.properties.refNumber: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["invoiceNumber"]) -> MetaOapg.properties.invoiceNumber: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["customerReceipt"]) -> MetaOapg.properties.customerReceipt: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["sequenceNumber"]) -> MetaOapg.properties.sequenceNumber: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["sale"]) -> 'VoidCreateVoidResponseSale': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["guid", "amount", "batchStatus", "timeStamp", "deviceGuid", "saleGuid", "status", "voidReason", "processorStatusCode", "wasProcessed", "batchGuid", "authCode", "refNumber", "invoiceNumber", "customerReceipt", "sequenceNumber", "sale", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["guid"]) -> typing.Union[MetaOapg.properties.guid, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["amount"]) -> typing.Union[MetaOapg.properties.amount, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["batchStatus"]) -> typing.Union[MetaOapg.properties.batchStatus, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["timeStamp"]) -> typing.Union[MetaOapg.properties.timeStamp, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["deviceGuid"]) -> typing.Union[MetaOapg.properties.deviceGuid, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["saleGuid"]) -> typing.Union[MetaOapg.properties.saleGuid, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["status"]) -> typing.Union[MetaOapg.properties.status, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["voidReason"]) -> typing.Union[MetaOapg.properties.voidReason, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["processorStatusCode"]) -> typing.Union[MetaOapg.properties.processorStatusCode, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["wasProcessed"]) -> typing.Union[MetaOapg.properties.wasProcessed, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["batchGuid"]) -> typing.Union[MetaOapg.properties.batchGuid, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["authCode"]) -> typing.Union[MetaOapg.properties.authCode, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["refNumber"]) -> typing.Union[MetaOapg.properties.refNumber, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["invoiceNumber"]) -> typing.Union[MetaOapg.properties.invoiceNumber, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["customerReceipt"]) -> typing.Union[MetaOapg.properties.customerReceipt, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["sequenceNumber"]) -> typing.Union[MetaOapg.properties.sequenceNumber, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["sale"]) -> typing.Union['VoidCreateVoidResponseSale', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["guid", "amount", "batchStatus", "timeStamp", "deviceGuid", "saleGuid", "status", "voidReason", "processorStatusCode", "wasProcessed", "batchGuid", "authCode", "refNumber", "invoiceNumber", "customerReceipt", "sequenceNumber", "sale", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        guid: typing.Union[MetaOapg.properties.guid, str, schemas.Unset] = schemas.unset,
        amount: typing.Union[MetaOapg.properties.amount, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        batchStatus: typing.Union[MetaOapg.properties.batchStatus, str, schemas.Unset] = schemas.unset,
        timeStamp: typing.Union[MetaOapg.properties.timeStamp, str, schemas.Unset] = schemas.unset,
        deviceGuid: typing.Union[MetaOapg.properties.deviceGuid, str, schemas.Unset] = schemas.unset,
        saleGuid: typing.Union[MetaOapg.properties.saleGuid, str, schemas.Unset] = schemas.unset,
        status: typing.Union[MetaOapg.properties.status, str, schemas.Unset] = schemas.unset,
        voidReason: typing.Union[MetaOapg.properties.voidReason, str, schemas.Unset] = schemas.unset,
        processorStatusCode: typing.Union[MetaOapg.properties.processorStatusCode, str, schemas.Unset] = schemas.unset,
        wasProcessed: typing.Union[MetaOapg.properties.wasProcessed, bool, schemas.Unset] = schemas.unset,
        batchGuid: typing.Union[MetaOapg.properties.batchGuid, str, schemas.Unset] = schemas.unset,
        authCode: typing.Union[MetaOapg.properties.authCode, str, schemas.Unset] = schemas.unset,
        refNumber: typing.Union[MetaOapg.properties.refNumber, str, schemas.Unset] = schemas.unset,
        invoiceNumber: typing.Union[MetaOapg.properties.invoiceNumber, str, schemas.Unset] = schemas.unset,
        customerReceipt: typing.Union[MetaOapg.properties.customerReceipt, str, schemas.Unset] = schemas.unset,
        sequenceNumber: typing.Union[MetaOapg.properties.sequenceNumber, str, schemas.Unset] = schemas.unset,
        sale: typing.Union['VoidCreateVoidResponseSale', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'VoidCreateVoidResponse':
        return super().__new__(
            cls,
            *args,
            guid=guid,
            amount=amount,
            batchStatus=batchStatus,
            timeStamp=timeStamp,
            deviceGuid=deviceGuid,
            saleGuid=saleGuid,
            status=status,
            voidReason=voidReason,
            processorStatusCode=processorStatusCode,
            wasProcessed=wasProcessed,
            batchGuid=batchGuid,
            authCode=authCode,
            refNumber=refNumber,
            invoiceNumber=invoiceNumber,
            customerReceipt=customerReceipt,
            sequenceNumber=sequenceNumber,
            sale=sale,
            _configuration=_configuration,
            **kwargs,
        )

from connex_pay_python_sdk.model.void_create_void_response_sale import VoidCreateVoidResponseSale
