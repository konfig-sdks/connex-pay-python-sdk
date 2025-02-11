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


class MerchantPayeeDto(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "preferredPayoutMethod",
            "isBusiness",
            "payeeId",
        }
        
        class properties:
            isBusiness = schemas.BoolSchema
            
            
            class payeeId(
                schemas.StrSchema
            ):
                pass
            preferredPayoutMethod = schemas.StrSchema
            idMerchant = schemas.Int32Schema
            
            
            class firstName(
                schemas.StrSchema
            ):
                pass
            
            
            class lastName(
                schemas.StrSchema
            ):
                pass
            
            
            class dbaName(
                schemas.StrSchema
            ):
                pass
            
            
            class taxId(
                schemas.StrSchema
            ):
                pass
            
            
            class customerId(
                schemas.StrSchema
            ):
                pass
            
            
            class email(
                schemas.StrSchema
            ):
                pass
            
            
            class address1(
                schemas.StrSchema
            ):
                pass
            address2 = schemas.StrSchema
            
            
            class city(
                schemas.StrSchema
            ):
                pass
            
            
            class state(
                schemas.StrSchema
            ):
                pass
            
            
            class zip(
                schemas.StrSchema
            ):
                pass
            
            
            class country(
                schemas.StrSchema
            ):
                pass
            preferredCardBrand = schemas.StrSchema
            preferredCardClass = schemas.StrSchema
            purchaseType = schemas.StrSchema
            guid = schemas.UUIDSchema
            timestamp = schemas.DateTimeSchema
            __annotations__ = {
                "isBusiness": isBusiness,
                "payeeId": payeeId,
                "preferredPayoutMethod": preferredPayoutMethod,
                "idMerchant": idMerchant,
                "firstName": firstName,
                "lastName": lastName,
                "dbaName": dbaName,
                "taxId": taxId,
                "customerId": customerId,
                "email": email,
                "address1": address1,
                "address2": address2,
                "city": city,
                "state": state,
                "zip": zip,
                "country": country,
                "preferredCardBrand": preferredCardBrand,
                "preferredCardClass": preferredCardClass,
                "purchaseType": purchaseType,
                "guid": guid,
                "timestamp": timestamp,
            }
    
    preferredPayoutMethod: MetaOapg.properties.preferredPayoutMethod
    isBusiness: MetaOapg.properties.isBusiness
    payeeId: MetaOapg.properties.payeeId
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["isBusiness"]) -> MetaOapg.properties.isBusiness: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["payeeId"]) -> MetaOapg.properties.payeeId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["preferredPayoutMethod"]) -> MetaOapg.properties.preferredPayoutMethod: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["idMerchant"]) -> MetaOapg.properties.idMerchant: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["firstName"]) -> MetaOapg.properties.firstName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["lastName"]) -> MetaOapg.properties.lastName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["dbaName"]) -> MetaOapg.properties.dbaName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["taxId"]) -> MetaOapg.properties.taxId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["customerId"]) -> MetaOapg.properties.customerId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["email"]) -> MetaOapg.properties.email: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["address1"]) -> MetaOapg.properties.address1: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["address2"]) -> MetaOapg.properties.address2: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["city"]) -> MetaOapg.properties.city: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["state"]) -> MetaOapg.properties.state: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["zip"]) -> MetaOapg.properties.zip: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["country"]) -> MetaOapg.properties.country: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["preferredCardBrand"]) -> MetaOapg.properties.preferredCardBrand: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["preferredCardClass"]) -> MetaOapg.properties.preferredCardClass: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["purchaseType"]) -> MetaOapg.properties.purchaseType: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["guid"]) -> MetaOapg.properties.guid: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["timestamp"]) -> MetaOapg.properties.timestamp: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["isBusiness", "payeeId", "preferredPayoutMethod", "idMerchant", "firstName", "lastName", "dbaName", "taxId", "customerId", "email", "address1", "address2", "city", "state", "zip", "country", "preferredCardBrand", "preferredCardClass", "purchaseType", "guid", "timestamp", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["isBusiness"]) -> MetaOapg.properties.isBusiness: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["payeeId"]) -> MetaOapg.properties.payeeId: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["preferredPayoutMethod"]) -> MetaOapg.properties.preferredPayoutMethod: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["idMerchant"]) -> typing.Union[MetaOapg.properties.idMerchant, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["firstName"]) -> typing.Union[MetaOapg.properties.firstName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["lastName"]) -> typing.Union[MetaOapg.properties.lastName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["dbaName"]) -> typing.Union[MetaOapg.properties.dbaName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["taxId"]) -> typing.Union[MetaOapg.properties.taxId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["customerId"]) -> typing.Union[MetaOapg.properties.customerId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["email"]) -> typing.Union[MetaOapg.properties.email, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["address1"]) -> typing.Union[MetaOapg.properties.address1, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["address2"]) -> typing.Union[MetaOapg.properties.address2, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["city"]) -> typing.Union[MetaOapg.properties.city, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["state"]) -> typing.Union[MetaOapg.properties.state, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["zip"]) -> typing.Union[MetaOapg.properties.zip, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["country"]) -> typing.Union[MetaOapg.properties.country, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["preferredCardBrand"]) -> typing.Union[MetaOapg.properties.preferredCardBrand, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["preferredCardClass"]) -> typing.Union[MetaOapg.properties.preferredCardClass, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["purchaseType"]) -> typing.Union[MetaOapg.properties.purchaseType, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["guid"]) -> typing.Union[MetaOapg.properties.guid, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["timestamp"]) -> typing.Union[MetaOapg.properties.timestamp, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["isBusiness", "payeeId", "preferredPayoutMethod", "idMerchant", "firstName", "lastName", "dbaName", "taxId", "customerId", "email", "address1", "address2", "city", "state", "zip", "country", "preferredCardBrand", "preferredCardClass", "purchaseType", "guid", "timestamp", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        preferredPayoutMethod: typing.Union[MetaOapg.properties.preferredPayoutMethod, str, ],
        isBusiness: typing.Union[MetaOapg.properties.isBusiness, bool, ],
        payeeId: typing.Union[MetaOapg.properties.payeeId, str, ],
        idMerchant: typing.Union[MetaOapg.properties.idMerchant, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        firstName: typing.Union[MetaOapg.properties.firstName, str, schemas.Unset] = schemas.unset,
        lastName: typing.Union[MetaOapg.properties.lastName, str, schemas.Unset] = schemas.unset,
        dbaName: typing.Union[MetaOapg.properties.dbaName, str, schemas.Unset] = schemas.unset,
        taxId: typing.Union[MetaOapg.properties.taxId, str, schemas.Unset] = schemas.unset,
        customerId: typing.Union[MetaOapg.properties.customerId, str, schemas.Unset] = schemas.unset,
        email: typing.Union[MetaOapg.properties.email, str, schemas.Unset] = schemas.unset,
        address1: typing.Union[MetaOapg.properties.address1, str, schemas.Unset] = schemas.unset,
        address2: typing.Union[MetaOapg.properties.address2, str, schemas.Unset] = schemas.unset,
        city: typing.Union[MetaOapg.properties.city, str, schemas.Unset] = schemas.unset,
        state: typing.Union[MetaOapg.properties.state, str, schemas.Unset] = schemas.unset,
        zip: typing.Union[MetaOapg.properties.zip, str, schemas.Unset] = schemas.unset,
        country: typing.Union[MetaOapg.properties.country, str, schemas.Unset] = schemas.unset,
        preferredCardBrand: typing.Union[MetaOapg.properties.preferredCardBrand, str, schemas.Unset] = schemas.unset,
        preferredCardClass: typing.Union[MetaOapg.properties.preferredCardClass, str, schemas.Unset] = schemas.unset,
        purchaseType: typing.Union[MetaOapg.properties.purchaseType, str, schemas.Unset] = schemas.unset,
        guid: typing.Union[MetaOapg.properties.guid, str, uuid.UUID, schemas.Unset] = schemas.unset,
        timestamp: typing.Union[MetaOapg.properties.timestamp, str, datetime, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'MerchantPayeeDto':
        return super().__new__(
            cls,
            *args,
            preferredPayoutMethod=preferredPayoutMethod,
            isBusiness=isBusiness,
            payeeId=payeeId,
            idMerchant=idMerchant,
            firstName=firstName,
            lastName=lastName,
            dbaName=dbaName,
            taxId=taxId,
            customerId=customerId,
            email=email,
            address1=address1,
            address2=address2,
            city=city,
            state=state,
            zip=zip,
            country=country,
            preferredCardBrand=preferredCardBrand,
            preferredCardClass=preferredCardClass,
            purchaseType=purchaseType,
            guid=guid,
            timestamp=timestamp,
            _configuration=_configuration,
            **kwargs,
        )
