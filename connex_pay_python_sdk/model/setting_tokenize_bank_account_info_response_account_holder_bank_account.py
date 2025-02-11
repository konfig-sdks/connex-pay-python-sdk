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


class SettingTokenizeBankAccountInfoResponseAccountHolderBankAccount(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            bankAccountGuid = schemas.StrSchema
            accountType = schemas.StrSchema
            accountHolderName = schemas.StrSchema
            last4Digits = schemas.StrSchema
            __annotations__ = {
                "bankAccountGuid": bankAccountGuid,
                "accountType": accountType,
                "accountHolderName": accountHolderName,
                "last4Digits": last4Digits,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["bankAccountGuid"]) -> MetaOapg.properties.bankAccountGuid: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["accountType"]) -> MetaOapg.properties.accountType: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["accountHolderName"]) -> MetaOapg.properties.accountHolderName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["last4Digits"]) -> MetaOapg.properties.last4Digits: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["bankAccountGuid", "accountType", "accountHolderName", "last4Digits", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["bankAccountGuid"]) -> typing.Union[MetaOapg.properties.bankAccountGuid, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["accountType"]) -> typing.Union[MetaOapg.properties.accountType, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["accountHolderName"]) -> typing.Union[MetaOapg.properties.accountHolderName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["last4Digits"]) -> typing.Union[MetaOapg.properties.last4Digits, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["bankAccountGuid", "accountType", "accountHolderName", "last4Digits", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        bankAccountGuid: typing.Union[MetaOapg.properties.bankAccountGuid, str, schemas.Unset] = schemas.unset,
        accountType: typing.Union[MetaOapg.properties.accountType, str, schemas.Unset] = schemas.unset,
        accountHolderName: typing.Union[MetaOapg.properties.accountHolderName, str, schemas.Unset] = schemas.unset,
        last4Digits: typing.Union[MetaOapg.properties.last4Digits, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'SettingTokenizeBankAccountInfoResponseAccountHolderBankAccount':
        return super().__new__(
            cls,
            *args,
            bankAccountGuid=bankAccountGuid,
            accountType=accountType,
            accountHolderName=accountHolderName,
            last4Digits=last4Digits,
            _configuration=_configuration,
            **kwargs,
        )
