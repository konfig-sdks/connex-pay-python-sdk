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


class CardTerminateByDateResponse(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            cardGuid = schemas.StrSchema
            amountLimit = schemas.IntSchema
            usageLimit = schemas.IntSchema
            limitWindow = schemas.StrSchema
            expirationDate = schemas.StrSchema
            expiration = schemas.StrSchema
            terminateDate = schemas.StrSchema
            currencyCode = schemas.StrSchema
            firstSix = schemas.StrSchema
            lastFour = schemas.StrSchema
            nameLine1 = schemas.StrSchema
            nameLine2 = schemas.StrSchema
            status = schemas.StrSchema
            customerServicePhoneNumber = schemas.StrSchema
            sequenceNumber = schemas.StrSchema
            cardType = schemas.StrSchema
            gatewayMerchantGuid = schemas.StrSchema
            availableBalance = schemas.IntSchema
            isPhysical = schemas.BoolSchema
            isLodged = schemas.BoolSchema
            fingerprint = schemas.StrSchema
            __annotations__ = {
                "cardGuid": cardGuid,
                "amountLimit": amountLimit,
                "usageLimit": usageLimit,
                "limitWindow": limitWindow,
                "expirationDate": expirationDate,
                "expiration": expiration,
                "terminateDate": terminateDate,
                "currencyCode": currencyCode,
                "firstSix": firstSix,
                "lastFour": lastFour,
                "nameLine1": nameLine1,
                "nameLine2": nameLine2,
                "status": status,
                "customerServicePhoneNumber": customerServicePhoneNumber,
                "sequenceNumber": sequenceNumber,
                "cardType": cardType,
                "gatewayMerchantGuid": gatewayMerchantGuid,
                "availableBalance": availableBalance,
                "isPhysical": isPhysical,
                "isLodged": isLodged,
                "fingerprint": fingerprint,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["cardGuid"]) -> MetaOapg.properties.cardGuid: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["amountLimit"]) -> MetaOapg.properties.amountLimit: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["usageLimit"]) -> MetaOapg.properties.usageLimit: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["limitWindow"]) -> MetaOapg.properties.limitWindow: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["expirationDate"]) -> MetaOapg.properties.expirationDate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["expiration"]) -> MetaOapg.properties.expiration: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["terminateDate"]) -> MetaOapg.properties.terminateDate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["currencyCode"]) -> MetaOapg.properties.currencyCode: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["firstSix"]) -> MetaOapg.properties.firstSix: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["lastFour"]) -> MetaOapg.properties.lastFour: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["nameLine1"]) -> MetaOapg.properties.nameLine1: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["nameLine2"]) -> MetaOapg.properties.nameLine2: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["status"]) -> MetaOapg.properties.status: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["customerServicePhoneNumber"]) -> MetaOapg.properties.customerServicePhoneNumber: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["sequenceNumber"]) -> MetaOapg.properties.sequenceNumber: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["cardType"]) -> MetaOapg.properties.cardType: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["gatewayMerchantGuid"]) -> MetaOapg.properties.gatewayMerchantGuid: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["availableBalance"]) -> MetaOapg.properties.availableBalance: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["isPhysical"]) -> MetaOapg.properties.isPhysical: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["isLodged"]) -> MetaOapg.properties.isLodged: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["fingerprint"]) -> MetaOapg.properties.fingerprint: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["cardGuid", "amountLimit", "usageLimit", "limitWindow", "expirationDate", "expiration", "terminateDate", "currencyCode", "firstSix", "lastFour", "nameLine1", "nameLine2", "status", "customerServicePhoneNumber", "sequenceNumber", "cardType", "gatewayMerchantGuid", "availableBalance", "isPhysical", "isLodged", "fingerprint", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["cardGuid"]) -> typing.Union[MetaOapg.properties.cardGuid, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["amountLimit"]) -> typing.Union[MetaOapg.properties.amountLimit, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["usageLimit"]) -> typing.Union[MetaOapg.properties.usageLimit, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["limitWindow"]) -> typing.Union[MetaOapg.properties.limitWindow, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["expirationDate"]) -> typing.Union[MetaOapg.properties.expirationDate, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["expiration"]) -> typing.Union[MetaOapg.properties.expiration, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["terminateDate"]) -> typing.Union[MetaOapg.properties.terminateDate, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["currencyCode"]) -> typing.Union[MetaOapg.properties.currencyCode, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["firstSix"]) -> typing.Union[MetaOapg.properties.firstSix, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["lastFour"]) -> typing.Union[MetaOapg.properties.lastFour, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["nameLine1"]) -> typing.Union[MetaOapg.properties.nameLine1, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["nameLine2"]) -> typing.Union[MetaOapg.properties.nameLine2, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["status"]) -> typing.Union[MetaOapg.properties.status, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["customerServicePhoneNumber"]) -> typing.Union[MetaOapg.properties.customerServicePhoneNumber, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["sequenceNumber"]) -> typing.Union[MetaOapg.properties.sequenceNumber, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["cardType"]) -> typing.Union[MetaOapg.properties.cardType, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["gatewayMerchantGuid"]) -> typing.Union[MetaOapg.properties.gatewayMerchantGuid, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["availableBalance"]) -> typing.Union[MetaOapg.properties.availableBalance, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["isPhysical"]) -> typing.Union[MetaOapg.properties.isPhysical, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["isLodged"]) -> typing.Union[MetaOapg.properties.isLodged, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["fingerprint"]) -> typing.Union[MetaOapg.properties.fingerprint, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["cardGuid", "amountLimit", "usageLimit", "limitWindow", "expirationDate", "expiration", "terminateDate", "currencyCode", "firstSix", "lastFour", "nameLine1", "nameLine2", "status", "customerServicePhoneNumber", "sequenceNumber", "cardType", "gatewayMerchantGuid", "availableBalance", "isPhysical", "isLodged", "fingerprint", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        cardGuid: typing.Union[MetaOapg.properties.cardGuid, str, schemas.Unset] = schemas.unset,
        amountLimit: typing.Union[MetaOapg.properties.amountLimit, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        usageLimit: typing.Union[MetaOapg.properties.usageLimit, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        limitWindow: typing.Union[MetaOapg.properties.limitWindow, str, schemas.Unset] = schemas.unset,
        expirationDate: typing.Union[MetaOapg.properties.expirationDate, str, schemas.Unset] = schemas.unset,
        expiration: typing.Union[MetaOapg.properties.expiration, str, schemas.Unset] = schemas.unset,
        terminateDate: typing.Union[MetaOapg.properties.terminateDate, str, schemas.Unset] = schemas.unset,
        currencyCode: typing.Union[MetaOapg.properties.currencyCode, str, schemas.Unset] = schemas.unset,
        firstSix: typing.Union[MetaOapg.properties.firstSix, str, schemas.Unset] = schemas.unset,
        lastFour: typing.Union[MetaOapg.properties.lastFour, str, schemas.Unset] = schemas.unset,
        nameLine1: typing.Union[MetaOapg.properties.nameLine1, str, schemas.Unset] = schemas.unset,
        nameLine2: typing.Union[MetaOapg.properties.nameLine2, str, schemas.Unset] = schemas.unset,
        status: typing.Union[MetaOapg.properties.status, str, schemas.Unset] = schemas.unset,
        customerServicePhoneNumber: typing.Union[MetaOapg.properties.customerServicePhoneNumber, str, schemas.Unset] = schemas.unset,
        sequenceNumber: typing.Union[MetaOapg.properties.sequenceNumber, str, schemas.Unset] = schemas.unset,
        cardType: typing.Union[MetaOapg.properties.cardType, str, schemas.Unset] = schemas.unset,
        gatewayMerchantGuid: typing.Union[MetaOapg.properties.gatewayMerchantGuid, str, schemas.Unset] = schemas.unset,
        availableBalance: typing.Union[MetaOapg.properties.availableBalance, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        isPhysical: typing.Union[MetaOapg.properties.isPhysical, bool, schemas.Unset] = schemas.unset,
        isLodged: typing.Union[MetaOapg.properties.isLodged, bool, schemas.Unset] = schemas.unset,
        fingerprint: typing.Union[MetaOapg.properties.fingerprint, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'CardTerminateByDateResponse':
        return super().__new__(
            cls,
            *args,
            cardGuid=cardGuid,
            amountLimit=amountLimit,
            usageLimit=usageLimit,
            limitWindow=limitWindow,
            expirationDate=expirationDate,
            expiration=expiration,
            terminateDate=terminateDate,
            currencyCode=currencyCode,
            firstSix=firstSix,
            lastFour=lastFour,
            nameLine1=nameLine1,
            nameLine2=nameLine2,
            status=status,
            customerServicePhoneNumber=customerServicePhoneNumber,
            sequenceNumber=sequenceNumber,
            cardType=cardType,
            gatewayMerchantGuid=gatewayMerchantGuid,
            availableBalance=availableBalance,
            isPhysical=isPhysical,
            isLodged=isLodged,
            fingerprint=fingerprint,
            _configuration=_configuration,
            **kwargs,
        )
