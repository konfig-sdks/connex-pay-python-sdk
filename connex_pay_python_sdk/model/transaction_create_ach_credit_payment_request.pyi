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


class TransactionCreateAchCreditPaymentRequest(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "MerchantGuid",
            "Amount",
            "PayeeName",
            "IncomingTransactionCode",
            "AccountHolder",
        }
        
        class properties:
            MerchantGuid = schemas.StrSchema
            Amount = schemas.Float32Schema
            PayeeName = schemas.StrSchema
            IncomingTransactionCode = schemas.StrSchema
        
            @staticmethod
            def AccountHolder() -> typing.Type['TransactionCreateAchCreditPaymentRequestAccountHolder']:
                return TransactionCreateAchCreditPaymentRequestAccountHolder
            StatementCompanyName = schemas.StrSchema
            Description = schemas.StrSchema
            __annotations__ = {
                "MerchantGuid": MerchantGuid,
                "Amount": Amount,
                "PayeeName": PayeeName,
                "IncomingTransactionCode": IncomingTransactionCode,
                "AccountHolder": AccountHolder,
                "StatementCompanyName": StatementCompanyName,
                "Description": Description,
            }
    
    MerchantGuid: MetaOapg.properties.MerchantGuid
    Amount: MetaOapg.properties.Amount
    PayeeName: MetaOapg.properties.PayeeName
    IncomingTransactionCode: MetaOapg.properties.IncomingTransactionCode
    AccountHolder: 'TransactionCreateAchCreditPaymentRequestAccountHolder'
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["MerchantGuid"]) -> MetaOapg.properties.MerchantGuid: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Amount"]) -> MetaOapg.properties.Amount: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["PayeeName"]) -> MetaOapg.properties.PayeeName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["IncomingTransactionCode"]) -> MetaOapg.properties.IncomingTransactionCode: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["AccountHolder"]) -> 'TransactionCreateAchCreditPaymentRequestAccountHolder': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["StatementCompanyName"]) -> MetaOapg.properties.StatementCompanyName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Description"]) -> MetaOapg.properties.Description: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["MerchantGuid", "Amount", "PayeeName", "IncomingTransactionCode", "AccountHolder", "StatementCompanyName", "Description", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["MerchantGuid"]) -> MetaOapg.properties.MerchantGuid: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Amount"]) -> MetaOapg.properties.Amount: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["PayeeName"]) -> MetaOapg.properties.PayeeName: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["IncomingTransactionCode"]) -> MetaOapg.properties.IncomingTransactionCode: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["AccountHolder"]) -> 'TransactionCreateAchCreditPaymentRequestAccountHolder': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["StatementCompanyName"]) -> typing.Union[MetaOapg.properties.StatementCompanyName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Description"]) -> typing.Union[MetaOapg.properties.Description, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["MerchantGuid", "Amount", "PayeeName", "IncomingTransactionCode", "AccountHolder", "StatementCompanyName", "Description", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        MerchantGuid: typing.Union[MetaOapg.properties.MerchantGuid, str, ],
        Amount: typing.Union[MetaOapg.properties.Amount, decimal.Decimal, int, float, ],
        PayeeName: typing.Union[MetaOapg.properties.PayeeName, str, ],
        IncomingTransactionCode: typing.Union[MetaOapg.properties.IncomingTransactionCode, str, ],
        AccountHolder: 'TransactionCreateAchCreditPaymentRequestAccountHolder',
        StatementCompanyName: typing.Union[MetaOapg.properties.StatementCompanyName, str, schemas.Unset] = schemas.unset,
        Description: typing.Union[MetaOapg.properties.Description, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'TransactionCreateAchCreditPaymentRequest':
        return super().__new__(
            cls,
            *args,
            MerchantGuid=MerchantGuid,
            Amount=Amount,
            PayeeName=PayeeName,
            IncomingTransactionCode=IncomingTransactionCode,
            AccountHolder=AccountHolder,
            StatementCompanyName=StatementCompanyName,
            Description=Description,
            _configuration=_configuration,
            **kwargs,
        )

from connex_pay_python_sdk.model.transaction_create_ach_credit_payment_request_account_holder import TransactionCreateAchCreditPaymentRequestAccountHolder
