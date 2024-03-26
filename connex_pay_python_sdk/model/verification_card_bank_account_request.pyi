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


class VerificationCardBankAccountRequest(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "DeviceGuid",
        }
        
        class properties:
            DeviceGuid = schemas.StrSchema
        
            @staticmethod
            def Card() -> typing.Type['VerificationCardBankAccountRequestCard']:
                return VerificationCardBankAccountRequestCard
        
            @staticmethod
            def BankAccount() -> typing.Type['VerificationCardBankAccountRequestBankAccount']:
                return VerificationCardBankAccountRequestBankAccount
            __annotations__ = {
                "DeviceGuid": DeviceGuid,
                "Card": Card,
                "BankAccount": BankAccount,
            }
    
    DeviceGuid: MetaOapg.properties.DeviceGuid
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["DeviceGuid"]) -> MetaOapg.properties.DeviceGuid: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Card"]) -> 'VerificationCardBankAccountRequestCard': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["BankAccount"]) -> 'VerificationCardBankAccountRequestBankAccount': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["DeviceGuid", "Card", "BankAccount", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["DeviceGuid"]) -> MetaOapg.properties.DeviceGuid: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Card"]) -> typing.Union['VerificationCardBankAccountRequestCard', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["BankAccount"]) -> typing.Union['VerificationCardBankAccountRequestBankAccount', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["DeviceGuid", "Card", "BankAccount", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        DeviceGuid: typing.Union[MetaOapg.properties.DeviceGuid, str, ],
        Card: typing.Union['VerificationCardBankAccountRequestCard', schemas.Unset] = schemas.unset,
        BankAccount: typing.Union['VerificationCardBankAccountRequestBankAccount', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'VerificationCardBankAccountRequest':
        return super().__new__(
            cls,
            *args,
            DeviceGuid=DeviceGuid,
            Card=Card,
            BankAccount=BankAccount,
            _configuration=_configuration,
            **kwargs,
        )

from connex_pay_python_sdk.model.verification_card_bank_account_request_bank_account import VerificationCardBankAccountRequestBankAccount
from connex_pay_python_sdk.model.verification_card_bank_account_request_card import VerificationCardBankAccountRequestCard
