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


class FundingMerchantCashBalanceRequest(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "amount",
            "isFundCashBalance",
            "merchantGUID",
        }
        
        class properties:
            merchantGUID = schemas.StrSchema
            amount = schemas.Float32Schema
            isFundCashBalance = schemas.BoolSchema
            __annotations__ = {
                "merchantGUID": merchantGUID,
                "amount": amount,
                "isFundCashBalance": isFundCashBalance,
            }
    
    amount: MetaOapg.properties.amount
    isFundCashBalance: MetaOapg.properties.isFundCashBalance
    merchantGUID: MetaOapg.properties.merchantGUID
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["merchantGUID"]) -> MetaOapg.properties.merchantGUID: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["amount"]) -> MetaOapg.properties.amount: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["isFundCashBalance"]) -> MetaOapg.properties.isFundCashBalance: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["merchantGUID", "amount", "isFundCashBalance", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["merchantGUID"]) -> MetaOapg.properties.merchantGUID: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["amount"]) -> MetaOapg.properties.amount: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["isFundCashBalance"]) -> MetaOapg.properties.isFundCashBalance: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["merchantGUID", "amount", "isFundCashBalance", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        amount: typing.Union[MetaOapg.properties.amount, decimal.Decimal, int, float, ],
        isFundCashBalance: typing.Union[MetaOapg.properties.isFundCashBalance, bool, ],
        merchantGUID: typing.Union[MetaOapg.properties.merchantGUID, str, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'FundingMerchantCashBalanceRequest':
        return super().__new__(
            cls,
            *args,
            amount=amount,
            isFundCashBalance=isFundCashBalance,
            merchantGUID=merchantGUID,
            _configuration=_configuration,
            **kwargs,
        )
