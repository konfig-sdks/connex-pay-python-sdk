# coding: utf-8

"""
    ConnexPay Reporting API

    REST API for retrieving reporting data. Currently Daily Accounting data only.

    The version of the OpenAPI document: v1
    Created by: https://docs.connexpay.com
"""

from dataclasses import dataclass
import typing_extensions
import urllib3
from pydantic import RootModel
from connex_pay_python_sdk.request_before_hook import request_before_hook
import json
from urllib3._collections import HTTPHeaderDict

from connex_pay_python_sdk.api_response import AsyncGeneratorResponse
from connex_pay_python_sdk import api_client, exceptions
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

from connex_pay_python_sdk.model.funding_merchant_cash_balance422_response import FundingMerchantCashBalance422Response as FundingMerchantCashBalance422ResponseSchema
from connex_pay_python_sdk.model.funding_merchant_cash_balance_response import FundingMerchantCashBalanceResponse as FundingMerchantCashBalanceResponseSchema
from connex_pay_python_sdk.model.funding_merchant_cash_balance_request import FundingMerchantCashBalanceRequest as FundingMerchantCashBalanceRequestSchema
from connex_pay_python_sdk.model.funding_merchant_cash_balance500_response import FundingMerchantCashBalance500Response as FundingMerchantCashBalance500ResponseSchema

from connex_pay_python_sdk.type.funding_merchant_cash_balance_response import FundingMerchantCashBalanceResponse
from connex_pay_python_sdk.type.funding_merchant_cash_balance500_response import FundingMerchantCashBalance500Response
from connex_pay_python_sdk.type.funding_merchant_cash_balance422_response import FundingMerchantCashBalance422Response
from connex_pay_python_sdk.type.funding_merchant_cash_balance_request import FundingMerchantCashBalanceRequest

from ...api_client import Dictionary
from connex_pay_python_sdk.pydantic.funding_merchant_cash_balance_request import FundingMerchantCashBalanceRequest as FundingMerchantCashBalanceRequestPydantic
from connex_pay_python_sdk.pydantic.funding_merchant_cash_balance422_response import FundingMerchantCashBalance422Response as FundingMerchantCashBalance422ResponsePydantic
from connex_pay_python_sdk.pydantic.funding_merchant_cash_balance500_response import FundingMerchantCashBalance500Response as FundingMerchantCashBalance500ResponsePydantic
from connex_pay_python_sdk.pydantic.funding_merchant_cash_balance_response import FundingMerchantCashBalanceResponse as FundingMerchantCashBalanceResponsePydantic

from . import path

# body param
SchemaForRequestBodyApplicationJson = FundingMerchantCashBalanceRequestSchema


request_body_funding_merchant_cash_balance_request = api_client.RequestBody(
    content={
        'application/json': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationJson),
    },
)
_auth = [
    'sec0',
]
SchemaFor201ResponseBodyApplicationJson = FundingMerchantCashBalanceResponseSchema


@dataclass
class ApiResponseFor201(api_client.ApiResponse):
    body: FundingMerchantCashBalanceResponse


@dataclass
class ApiResponseFor201Async(api_client.AsyncApiResponse):
    body: FundingMerchantCashBalanceResponse


_response_for_201 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor201,
    response_cls_async=ApiResponseFor201Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor201ResponseBodyApplicationJson),
    },
)
SchemaFor422ResponseBodyApplicationJson = FundingMerchantCashBalance422ResponseSchema


@dataclass
class ApiResponseFor422(api_client.ApiResponse):
    body: FundingMerchantCashBalance422Response


@dataclass
class ApiResponseFor422Async(api_client.AsyncApiResponse):
    body: FundingMerchantCashBalance422Response


_response_for_422 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor422,
    response_cls_async=ApiResponseFor422Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor422ResponseBodyApplicationJson),
    },
)
SchemaFor500ResponseBodyApplicationJson = FundingMerchantCashBalance500ResponseSchema


@dataclass
class ApiResponseFor500(api_client.ApiResponse):
    body: FundingMerchantCashBalance500Response


@dataclass
class ApiResponseFor500Async(api_client.AsyncApiResponse):
    body: FundingMerchantCashBalance500Response


_response_for_500 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor500,
    response_cls_async=ApiResponseFor500Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor500ResponseBodyApplicationJson),
    },
)
_status_code_to_response = {
    '201': _response_for_201,
    '422': _response_for_422,
    '500': _response_for_500,
}
_all_accept_content_types = (
    'application/json',
)


class BaseApi(api_client.Api):

    def _merchant_cash_balance_mapped_args(
        self,
        merchant_guid: str,
        amount: typing.Union[int, float],
        is_fund_cash_balance: bool,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _body = {}
        if merchant_guid is not None:
            _body["merchantGUID"] = merchant_guid
        if amount is not None:
            _body["amount"] = amount
        if is_fund_cash_balance is not None:
            _body["isFundCashBalance"] = is_fund_cash_balance
        args.body = _body
        return args

    async def _amerchant_cash_balance_oapg(
        self,
        body: typing.Any = None,
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'application/json',
        stream: bool = False,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor201Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        """
        Client Self-Service Funding
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        used_path = path.value
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'post'.upper()
        _headers.add('Content-Type', content_type)
    
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/api/v1/MerchantSelfServiceFunding',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_funding_merchant_cash_balance_request.serialize(body, content_type)
            if 'fields' in serialized_data:
                _fields = serialized_data['fields']
            elif 'body' in serialized_data:
                _body = serialized_data['body']
    
        response = await self.api_client.async_call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            fields=_fields,
            serialized_body=_body,
            body=body,
            auth_settings=_auth,
            timeout=timeout,
            **kwargs
        )
    
        if stream:
            if not 200 <= response.http_response.status <= 299:
                body = (await response.http_response.content.read()).decode("utf-8")
                raise exceptions.ApiStreamingException(
                    status=response.http_response.status,
                    reason=response.http_response.reason,
                    body=body,
                )
    
            async def stream_iterator():
                """
                iterates over response.http_response.content and closes connection once iteration has finished
                """
                async for line in response.http_response.content:
                    if line == b'\r\n':
                        continue
                    yield line
                response.http_response.close()
                await response.session.close()
            return AsyncGeneratorResponse(
                content=stream_iterator(),
                headers=response.http_response.headers,
                status=response.http_response.status,
                response=response.http_response
            )
    
        response_for_status = _status_code_to_response.get(str(response.http_response.status))
        if response_for_status:
            api_response = await response_for_status.deserialize_async(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
        else:
            # If response data is JSON then deserialize for SDK consumer convenience
            is_json = api_client.JSONDetector._content_type_is_json(response.http_response.headers.get('Content-Type', ''))
            api_response = api_client.ApiResponseWithoutDeserializationAsync(
                body=await response.http_response.json() if is_json else await response.http_response.text(),
                response=response.http_response,
                round_trip_time=response.round_trip_time,
                status=response.http_response.status,
                headers=response.http_response.headers,
            )
    
        if not 200 <= api_response.status <= 299:
            raise exceptions.ApiException(api_response=api_response)
    
        # cleanup session / response
        response.http_response.close()
        await response.session.close()
    
        return api_response


    def _merchant_cash_balance_oapg(
        self,
        body: typing.Any = None,
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'application/json',
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseFor201,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        Client Self-Service Funding
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        used_path = path.value
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'post'.upper()
        _headers.add('Content-Type', content_type)
    
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/api/v1/MerchantSelfServiceFunding',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_funding_merchant_cash_balance_request.serialize(body, content_type)
            if 'fields' in serialized_data:
                _fields = serialized_data['fields']
            elif 'body' in serialized_data:
                _body = serialized_data['body']
    
        response = self.api_client.call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            fields=_fields,
            serialized_body=_body,
            body=body,
            auth_settings=_auth,
            timeout=timeout,
        )
    
        response_for_status = _status_code_to_response.get(str(response.http_response.status))
        if response_for_status:
            api_response = response_for_status.deserialize(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
        else:
            # If response data is JSON then deserialize for SDK consumer convenience
            is_json = api_client.JSONDetector._content_type_is_json(response.http_response.headers.get('Content-Type', ''))
            api_response = api_client.ApiResponseWithoutDeserialization(
                body=json.loads(response.http_response.data) if is_json else response.http_response.data,
                response=response.http_response,
                round_trip_time=response.round_trip_time,
                status=response.http_response.status,
                headers=response.http_response.headers,
            )
    
        if not 200 <= api_response.status <= 299:
            raise exceptions.ApiException(api_response=api_response)
    
        return api_response


class MerchantCashBalanceRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def amerchant_cash_balance(
        self,
        merchant_guid: str,
        amount: typing.Union[int, float],
        is_fund_cash_balance: bool,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor201Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._merchant_cash_balance_mapped_args(
            merchant_guid=merchant_guid,
            amount=amount,
            is_fund_cash_balance=is_fund_cash_balance,
        )
        return await self._amerchant_cash_balance_oapg(
            body=args.body,
            **kwargs,
        )
    
    def merchant_cash_balance(
        self,
        merchant_guid: str,
        amount: typing.Union[int, float],
        is_fund_cash_balance: bool,
    ) -> typing.Union[
        ApiResponseFor201,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._merchant_cash_balance_mapped_args(
            merchant_guid=merchant_guid,
            amount=amount,
            is_fund_cash_balance=is_fund_cash_balance,
        )
        return self._merchant_cash_balance_oapg(
            body=args.body,
        )

class MerchantCashBalance(BaseApi):

    async def amerchant_cash_balance(
        self,
        merchant_guid: str,
        amount: typing.Union[int, float],
        is_fund_cash_balance: bool,
        validate: bool = False,
        **kwargs,
    ) -> FundingMerchantCashBalanceResponsePydantic:
        raw_response = await self.raw.amerchant_cash_balance(
            merchant_guid=merchant_guid,
            amount=amount,
            is_fund_cash_balance=is_fund_cash_balance,
            **kwargs,
        )
        if validate:
            return FundingMerchantCashBalanceResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(FundingMerchantCashBalanceResponsePydantic, raw_response.body)
    
    
    def merchant_cash_balance(
        self,
        merchant_guid: str,
        amount: typing.Union[int, float],
        is_fund_cash_balance: bool,
        validate: bool = False,
    ) -> FundingMerchantCashBalanceResponsePydantic:
        raw_response = self.raw.merchant_cash_balance(
            merchant_guid=merchant_guid,
            amount=amount,
            is_fund_cash_balance=is_fund_cash_balance,
        )
        if validate:
            return FundingMerchantCashBalanceResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(FundingMerchantCashBalanceResponsePydantic, raw_response.body)


class ApiForpost(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def apost(
        self,
        merchant_guid: str,
        amount: typing.Union[int, float],
        is_fund_cash_balance: bool,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor201Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._merchant_cash_balance_mapped_args(
            merchant_guid=merchant_guid,
            amount=amount,
            is_fund_cash_balance=is_fund_cash_balance,
        )
        return await self._amerchant_cash_balance_oapg(
            body=args.body,
            **kwargs,
        )
    
    def post(
        self,
        merchant_guid: str,
        amount: typing.Union[int, float],
        is_fund_cash_balance: bool,
    ) -> typing.Union[
        ApiResponseFor201,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._merchant_cash_balance_mapped_args(
            merchant_guid=merchant_guid,
            amount=amount,
            is_fund_cash_balance=is_fund_cash_balance,
        )
        return self._merchant_cash_balance_oapg(
            body=args.body,
        )

