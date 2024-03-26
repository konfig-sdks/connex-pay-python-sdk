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


class ValidationSearchVerifyOperationResponse(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            pageCurrent = schemas.IntSchema
            pageCurrentResults = schemas.IntSchema
            pageTotal = schemas.IntSchema
            pageSize = schemas.IntSchema
            totalResults = schemas.IntSchema
            cardSummary = schemas.AnyTypeSchema
        
            @staticmethod
            def searchResultDTO() -> typing.Type['ValidationSearchVerifyOperationResponseSearchResultDto']:
                return ValidationSearchVerifyOperationResponseSearchResultDto
            __annotations__ = {
                "pageCurrent": pageCurrent,
                "pageCurrentResults": pageCurrentResults,
                "pageTotal": pageTotal,
                "pageSize": pageSize,
                "totalResults": totalResults,
                "cardSummary": cardSummary,
                "searchResultDTO": searchResultDTO,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["pageCurrent"]) -> MetaOapg.properties.pageCurrent: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["pageCurrentResults"]) -> MetaOapg.properties.pageCurrentResults: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["pageTotal"]) -> MetaOapg.properties.pageTotal: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["pageSize"]) -> MetaOapg.properties.pageSize: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["totalResults"]) -> MetaOapg.properties.totalResults: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["cardSummary"]) -> MetaOapg.properties.cardSummary: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["searchResultDTO"]) -> 'ValidationSearchVerifyOperationResponseSearchResultDto': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["pageCurrent", "pageCurrentResults", "pageTotal", "pageSize", "totalResults", "cardSummary", "searchResultDTO", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["pageCurrent"]) -> typing.Union[MetaOapg.properties.pageCurrent, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["pageCurrentResults"]) -> typing.Union[MetaOapg.properties.pageCurrentResults, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["pageTotal"]) -> typing.Union[MetaOapg.properties.pageTotal, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["pageSize"]) -> typing.Union[MetaOapg.properties.pageSize, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["totalResults"]) -> typing.Union[MetaOapg.properties.totalResults, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["cardSummary"]) -> typing.Union[MetaOapg.properties.cardSummary, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["searchResultDTO"]) -> typing.Union['ValidationSearchVerifyOperationResponseSearchResultDto', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["pageCurrent", "pageCurrentResults", "pageTotal", "pageSize", "totalResults", "cardSummary", "searchResultDTO", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        pageCurrent: typing.Union[MetaOapg.properties.pageCurrent, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        pageCurrentResults: typing.Union[MetaOapg.properties.pageCurrentResults, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        pageTotal: typing.Union[MetaOapg.properties.pageTotal, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        pageSize: typing.Union[MetaOapg.properties.pageSize, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        totalResults: typing.Union[MetaOapg.properties.totalResults, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        cardSummary: typing.Union[MetaOapg.properties.cardSummary, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, schemas.Unset] = schemas.unset,
        searchResultDTO: typing.Union['ValidationSearchVerifyOperationResponseSearchResultDto', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ValidationSearchVerifyOperationResponse':
        return super().__new__(
            cls,
            *args,
            pageCurrent=pageCurrent,
            pageCurrentResults=pageCurrentResults,
            pageTotal=pageTotal,
            pageSize=pageSize,
            totalResults=totalResults,
            cardSummary=cardSummary,
            searchResultDTO=searchResultDTO,
            _configuration=_configuration,
            **kwargs,
        )

from connex_pay_python_sdk.model.validation_search_verify_operation_response_search_result_dto import ValidationSearchVerifyOperationResponseSearchResultDto
