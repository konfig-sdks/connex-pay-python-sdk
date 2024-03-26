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

from connex_pay_python_sdk.model.search_merchant_payee_dto import SearchMerchantPayeeDto as SearchMerchantPayeeDtoSchema
from connex_pay_python_sdk.model.merchant_payee_paginated_response import MerchantPayeePaginatedResponse as MerchantPayeePaginatedResponseSchema

from connex_pay_python_sdk.type.search_merchant_payee_dto import SearchMerchantPayeeDto
from connex_pay_python_sdk.type.merchant_payee_paginated_response import MerchantPayeePaginatedResponse

from ...api_client import Dictionary
from connex_pay_python_sdk.pydantic.merchant_payee_paginated_response import MerchantPayeePaginatedResponse as MerchantPayeePaginatedResponsePydantic
from connex_pay_python_sdk.pydantic.search_merchant_payee_dto import SearchMerchantPayeeDto as SearchMerchantPayeeDtoPydantic

# Path params
MerchantGuidSchema = schemas.UUIDSchema
PageSchema = schemas.Int32Schema
PagesizeSchema = schemas.Int32Schema
RequestRequiredPathParams = typing_extensions.TypedDict(
    'RequestRequiredPathParams',
    {
        'merchantGuid': typing.Union[MerchantGuidSchema, str, uuid.UUID, ],
        'page': typing.Union[PageSchema, decimal.Decimal, int, ],
        'pagesize': typing.Union[PagesizeSchema, decimal.Decimal, int, ],
    }
)
RequestOptionalPathParams = typing_extensions.TypedDict(
    'RequestOptionalPathParams',
    {
    },
    total=False
)


class RequestPathParams(RequestRequiredPathParams, RequestOptionalPathParams):
    pass


request_path_merchant_guid = api_client.PathParameter(
    name="merchantGuid",
    style=api_client.ParameterStyle.SIMPLE,
    schema=MerchantGuidSchema,
    required=True,
)
request_path_page = api_client.PathParameter(
    name="page",
    style=api_client.ParameterStyle.SIMPLE,
    schema=PageSchema,
    required=True,
)
request_path_pagesize = api_client.PathParameter(
    name="pagesize",
    style=api_client.ParameterStyle.SIMPLE,
    schema=PagesizeSchema,
    required=True,
)
# body param
SchemaForRequestBodyApplicationJson = SearchMerchantPayeeDtoSchema
SchemaForRequestBodyTextJson = SearchMerchantPayeeDtoSchema
SchemaForRequestBodyApplicationXml = SearchMerchantPayeeDtoSchema
SchemaForRequestBodyTextXml = SearchMerchantPayeeDtoSchema
SchemaForRequestBodyApplicationXWwwFormUrlencoded = SearchMerchantPayeeDtoSchema


request_body_search_merchant_payee_dto = api_client.RequestBody(
    content={
        'application/json': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationJson),
        'text/json': api_client.MediaType(
            schema=SchemaForRequestBodyTextJson),
        'application/xml': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationXml),
        'text/xml': api_client.MediaType(
            schema=SchemaForRequestBodyTextXml),
        'application/x-www-form-urlencoded': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationXWwwFormUrlencoded),
    },
    required=True,
)
SchemaFor200ResponseBodyApplicationJson = MerchantPayeePaginatedResponseSchema
SchemaFor200ResponseBodyTextJson = MerchantPayeePaginatedResponseSchema
SchemaFor200ResponseBodyApplicationXml = MerchantPayeePaginatedResponseSchema
SchemaFor200ResponseBodyTextXml = MerchantPayeePaginatedResponseSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: MerchantPayeePaginatedResponse


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: MerchantPayeePaginatedResponse


_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
    response_cls_async=ApiResponseFor200Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationJson),
        'text/json': api_client.MediaType(
            schema=SchemaFor200ResponseBodyTextJson),
        'application/xml': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationXml),
        'text/xml': api_client.MediaType(
            schema=SchemaFor200ResponseBodyTextXml),
    },
)


@dataclass
class ApiResponseFor400(api_client.ApiResponse):
    body: schemas.Unset = schemas.unset


@dataclass
class ApiResponseFor400Async(api_client.AsyncApiResponse):
    body: schemas.Unset = schemas.unset


_response_for_400 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor400,
    response_cls_async=ApiResponseFor400Async,
)


@dataclass
class ApiResponseFor403(api_client.ApiResponse):
    body: schemas.Unset = schemas.unset


@dataclass
class ApiResponseFor403Async(api_client.AsyncApiResponse):
    body: schemas.Unset = schemas.unset


_response_for_403 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor403,
    response_cls_async=ApiResponseFor403Async,
)
_all_accept_content_types = (
    'application/json',
    'text/json',
    'application/xml',
    'text/xml',
)


class BaseApi(api_client.Api):

    def _get_payees_mapped_args(
        self,
        merchant_guid: str,
        page: int,
        pagesize: int,
        search_term: typing.Optional[str] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _path_params = {}
        _body = {}
        if search_term is not None:
            _body["searchTerm"] = search_term
        args.body = _body
        if merchant_guid is not None:
            _path_params["merchantGuid"] = merchant_guid
        if page is not None:
            _path_params["page"] = page
        if pagesize is not None:
            _path_params["pagesize"] = pagesize
        args.path = _path_params
        return args

    async def _aget_payees_oapg(
        self,
        body: typing.Any = None,
            path_params: typing.Optional[dict] = {},
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
        Get merchant payees
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_merchant_guid,
            request_path_page,
            request_path_pagesize,
        ):
            parameter_data = path_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _path_params.update(serialized_data)
    
        for k, v in _path_params.items():
            used_path = used_path.replace('{%s}' % k, v)
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'post'.upper()
        _headers.add('Content-Type', content_type)
    
        if body is schemas.unset:
            raise exceptions.ApiValueError(
                'The required body parameter has an invalid value of: unset. Set a valid value instead')
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/api/v1/Merchants/{merchantGuid}/Payees/Search/{page}/{pagesize}',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        serialized_data = request_body_search_merchant_payee_dto.serialize(body, content_type)
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


    def _get_payees_oapg(
        self,
        body: typing.Any = None,
            path_params: typing.Optional[dict] = {},
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
        Get merchant payees
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_merchant_guid,
            request_path_page,
            request_path_pagesize,
        ):
            parameter_data = path_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _path_params.update(serialized_data)
    
        for k, v in _path_params.items():
            used_path = used_path.replace('{%s}' % k, v)
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'post'.upper()
        _headers.add('Content-Type', content_type)
    
        if body is schemas.unset:
            raise exceptions.ApiValueError(
                'The required body parameter has an invalid value of: unset. Set a valid value instead')
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/api/v1/Merchants/{merchantGuid}/Payees/Search/{page}/{pagesize}',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        serialized_data = request_body_search_merchant_payee_dto.serialize(body, content_type)
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


class GetPayeesRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def aget_payees(
        self,
        merchant_guid: str,
        page: int,
        pagesize: int,
        search_term: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._get_payees_mapped_args(
            merchant_guid=merchant_guid,
            page=page,
            pagesize=pagesize,
            search_term=search_term,
        )
        return await self._aget_payees_oapg(
            body=args.body,
            path_params=args.path,
            **kwargs,
        )
    
    def get_payees(
        self,
        merchant_guid: str,
        page: int,
        pagesize: int,
        search_term: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._get_payees_mapped_args(
            merchant_guid=merchant_guid,
            page=page,
            pagesize=pagesize,
            search_term=search_term,
        )
        return self._get_payees_oapg(
            body=args.body,
            path_params=args.path,
        )

class GetPayees(BaseApi):

    async def aget_payees(
        self,
        merchant_guid: str,
        page: int,
        pagesize: int,
        search_term: typing.Optional[str] = None,
        validate: bool = False,
        **kwargs,
    ) -> MerchantPayeePaginatedResponsePydantic:
        raw_response = await self.raw.aget_payees(
            merchant_guid=merchant_guid,
            page=page,
            pagesize=pagesize,
            search_term=search_term,
            **kwargs,
        )
        if validate:
            return MerchantPayeePaginatedResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(MerchantPayeePaginatedResponsePydantic, raw_response.body)
    
    
    def get_payees(
        self,
        merchant_guid: str,
        page: int,
        pagesize: int,
        search_term: typing.Optional[str] = None,
        validate: bool = False,
    ) -> MerchantPayeePaginatedResponsePydantic:
        raw_response = self.raw.get_payees(
            merchant_guid=merchant_guid,
            page=page,
            pagesize=pagesize,
            search_term=search_term,
        )
        if validate:
            return MerchantPayeePaginatedResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(MerchantPayeePaginatedResponsePydantic, raw_response.body)


class ApiForpost(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def apost(
        self,
        merchant_guid: str,
        page: int,
        pagesize: int,
        search_term: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._get_payees_mapped_args(
            merchant_guid=merchant_guid,
            page=page,
            pagesize=pagesize,
            search_term=search_term,
        )
        return await self._aget_payees_oapg(
            body=args.body,
            path_params=args.path,
            **kwargs,
        )
    
    def post(
        self,
        merchant_guid: str,
        page: int,
        pagesize: int,
        search_term: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._get_payees_mapped_args(
            merchant_guid=merchant_guid,
            page=page,
            pagesize=pagesize,
            search_term=search_term,
        )
        return self._get_payees_oapg(
            body=args.body,
            path_params=args.path,
        )

