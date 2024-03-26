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

from connex_pay_python_sdk.model.token_request_hpp_token_request import TokenRequestHppTokenRequest as TokenRequestHppTokenRequestSchema
from connex_pay_python_sdk.model.token_request_hpp_token_request_tender_type_options import TokenRequestHppTokenRequestTenderTypeOptions as TokenRequestHppTokenRequestTenderTypeOptionsSchema
from connex_pay_python_sdk.model.token_request_hpp_token_response import TokenRequestHppTokenResponse as TokenRequestHppTokenResponseSchema
from connex_pay_python_sdk.model.token_request_hpp_token_request_sale import TokenRequestHppTokenRequestSale as TokenRequestHppTokenRequestSaleSchema

from connex_pay_python_sdk.type.token_request_hpp_token_response import TokenRequestHppTokenResponse
from connex_pay_python_sdk.type.token_request_hpp_token_request_sale import TokenRequestHppTokenRequestSale
from connex_pay_python_sdk.type.token_request_hpp_token_request import TokenRequestHppTokenRequest
from connex_pay_python_sdk.type.token_request_hpp_token_request_tender_type_options import TokenRequestHppTokenRequestTenderTypeOptions

from ...api_client import Dictionary
from connex_pay_python_sdk.pydantic.token_request_hpp_token_response import TokenRequestHppTokenResponse as TokenRequestHppTokenResponsePydantic
from connex_pay_python_sdk.pydantic.token_request_hpp_token_request_tender_type_options import TokenRequestHppTokenRequestTenderTypeOptions as TokenRequestHppTokenRequestTenderTypeOptionsPydantic
from connex_pay_python_sdk.pydantic.token_request_hpp_token_request_sale import TokenRequestHppTokenRequestSale as TokenRequestHppTokenRequestSalePydantic
from connex_pay_python_sdk.pydantic.token_request_hpp_token_request import TokenRequestHppTokenRequest as TokenRequestHppTokenRequestPydantic

from . import path

# body param
SchemaForRequestBodyApplicationJson = TokenRequestHppTokenRequestSchema


request_body_token_request_hpp_token_request = api_client.RequestBody(
    content={
        'application/json': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationJson),
    },
)
_auth = [
    'sec0',
]
SchemaFor200ResponseBodyApplicationJson = TokenRequestHppTokenResponseSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: TokenRequestHppTokenResponse


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: TokenRequestHppTokenResponse


_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
    response_cls_async=ApiResponseFor200Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationJson),
    },
)
SchemaFor400ResponseBodyApplicationJson = schemas.DictSchema


@dataclass
class ApiResponseFor400(api_client.ApiResponse):
    body: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]


@dataclass
class ApiResponseFor400Async(api_client.AsyncApiResponse):
    body: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]


_response_for_400 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor400,
    response_cls_async=ApiResponseFor400Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor400ResponseBodyApplicationJson),
    },
)
_status_code_to_response = {
    '200': _response_for_200,
    '400': _response_for_400,
}
_all_accept_content_types = (
    'application/json',
)


class BaseApi(api_client.Api):

    def _request_hpp_token_mapped_args(
        self,
        merchant_name: str,
        sale: TokenRequestHppTokenRequestSale,
        description: typing.Optional[str] = None,
        result_redirect_url: typing.Optional[str] = None,
        logo_url: typing.Optional[str] = None,
        tender_type_options: typing.Optional[TokenRequestHppTokenRequestTenderTypeOptions] = None,
        expiration: typing.Optional[datetime] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _body = {}
        if merchant_name is not None:
            _body["MerchantName"] = merchant_name
        if description is not None:
            _body["Description"] = description
        if result_redirect_url is not None:
            _body["ResultRedirectUrl"] = result_redirect_url
        if logo_url is not None:
            _body["LogoUrl"] = logo_url
        if tender_type_options is not None:
            _body["TenderTypeOptions"] = tender_type_options
        if expiration is not None:
            _body["Expiration"] = expiration
        if sale is not None:
            _body["Sale"] = sale
        args.body = _body
        return args

    async def _arequest_hpp_token_oapg(
        self,
        body: typing.Any = None,
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'application/json',
        stream: bool = False,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        """
        HPP Token Request
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
            path_template='/api/v1/HostedPaymentPageRequests',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_token_request_hpp_token_request.serialize(body, content_type)
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


    def _request_hpp_token_oapg(
        self,
        body: typing.Any = None,
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'application/json',
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        HPP Token Request
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
            path_template='/api/v1/HostedPaymentPageRequests',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_token_request_hpp_token_request.serialize(body, content_type)
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


class RequestHppTokenRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def arequest_hpp_token(
        self,
        merchant_name: str,
        sale: TokenRequestHppTokenRequestSale,
        description: typing.Optional[str] = None,
        result_redirect_url: typing.Optional[str] = None,
        logo_url: typing.Optional[str] = None,
        tender_type_options: typing.Optional[TokenRequestHppTokenRequestTenderTypeOptions] = None,
        expiration: typing.Optional[datetime] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._request_hpp_token_mapped_args(
            merchant_name=merchant_name,
            sale=sale,
            description=description,
            result_redirect_url=result_redirect_url,
            logo_url=logo_url,
            tender_type_options=tender_type_options,
            expiration=expiration,
        )
        return await self._arequest_hpp_token_oapg(
            body=args.body,
            **kwargs,
        )
    
    def request_hpp_token(
        self,
        merchant_name: str,
        sale: TokenRequestHppTokenRequestSale,
        description: typing.Optional[str] = None,
        result_redirect_url: typing.Optional[str] = None,
        logo_url: typing.Optional[str] = None,
        tender_type_options: typing.Optional[TokenRequestHppTokenRequestTenderTypeOptions] = None,
        expiration: typing.Optional[datetime] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._request_hpp_token_mapped_args(
            merchant_name=merchant_name,
            sale=sale,
            description=description,
            result_redirect_url=result_redirect_url,
            logo_url=logo_url,
            tender_type_options=tender_type_options,
            expiration=expiration,
        )
        return self._request_hpp_token_oapg(
            body=args.body,
        )

class RequestHppToken(BaseApi):

    async def arequest_hpp_token(
        self,
        merchant_name: str,
        sale: TokenRequestHppTokenRequestSale,
        description: typing.Optional[str] = None,
        result_redirect_url: typing.Optional[str] = None,
        logo_url: typing.Optional[str] = None,
        tender_type_options: typing.Optional[TokenRequestHppTokenRequestTenderTypeOptions] = None,
        expiration: typing.Optional[datetime] = None,
        validate: bool = False,
        **kwargs,
    ) -> TokenRequestHppTokenResponsePydantic:
        raw_response = await self.raw.arequest_hpp_token(
            merchant_name=merchant_name,
            sale=sale,
            description=description,
            result_redirect_url=result_redirect_url,
            logo_url=logo_url,
            tender_type_options=tender_type_options,
            expiration=expiration,
            **kwargs,
        )
        if validate:
            return TokenRequestHppTokenResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(TokenRequestHppTokenResponsePydantic, raw_response.body)
    
    
    def request_hpp_token(
        self,
        merchant_name: str,
        sale: TokenRequestHppTokenRequestSale,
        description: typing.Optional[str] = None,
        result_redirect_url: typing.Optional[str] = None,
        logo_url: typing.Optional[str] = None,
        tender_type_options: typing.Optional[TokenRequestHppTokenRequestTenderTypeOptions] = None,
        expiration: typing.Optional[datetime] = None,
        validate: bool = False,
    ) -> TokenRequestHppTokenResponsePydantic:
        raw_response = self.raw.request_hpp_token(
            merchant_name=merchant_name,
            sale=sale,
            description=description,
            result_redirect_url=result_redirect_url,
            logo_url=logo_url,
            tender_type_options=tender_type_options,
            expiration=expiration,
        )
        if validate:
            return TokenRequestHppTokenResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(TokenRequestHppTokenResponsePydantic, raw_response.body)


class ApiForpost(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def apost(
        self,
        merchant_name: str,
        sale: TokenRequestHppTokenRequestSale,
        description: typing.Optional[str] = None,
        result_redirect_url: typing.Optional[str] = None,
        logo_url: typing.Optional[str] = None,
        tender_type_options: typing.Optional[TokenRequestHppTokenRequestTenderTypeOptions] = None,
        expiration: typing.Optional[datetime] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._request_hpp_token_mapped_args(
            merchant_name=merchant_name,
            sale=sale,
            description=description,
            result_redirect_url=result_redirect_url,
            logo_url=logo_url,
            tender_type_options=tender_type_options,
            expiration=expiration,
        )
        return await self._arequest_hpp_token_oapg(
            body=args.body,
            **kwargs,
        )
    
    def post(
        self,
        merchant_name: str,
        sale: TokenRequestHppTokenRequestSale,
        description: typing.Optional[str] = None,
        result_redirect_url: typing.Optional[str] = None,
        logo_url: typing.Optional[str] = None,
        tender_type_options: typing.Optional[TokenRequestHppTokenRequestTenderTypeOptions] = None,
        expiration: typing.Optional[datetime] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._request_hpp_token_mapped_args(
            merchant_name=merchant_name,
            sale=sale,
            description=description,
            result_redirect_url=result_redirect_url,
            logo_url=logo_url,
            tender_type_options=tender_type_options,
            expiration=expiration,
        )
        return self._request_hpp_token_oapg(
            body=args.body,
        )

