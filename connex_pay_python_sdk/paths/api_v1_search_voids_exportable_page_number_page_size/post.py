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

from connex_pay_python_sdk.model.void_search_voids_response import VoidSearchVoidsResponse as VoidSearchVoidsResponseSchema
from connex_pay_python_sdk.model.void_search_voids_request import VoidSearchVoidsRequest as VoidSearchVoidsRequestSchema

from connex_pay_python_sdk.type.void_search_voids_request import VoidSearchVoidsRequest
from connex_pay_python_sdk.type.void_search_voids_response import VoidSearchVoidsResponse

from ...api_client import Dictionary
from connex_pay_python_sdk.pydantic.void_search_voids_response import VoidSearchVoidsResponse as VoidSearchVoidsResponsePydantic
from connex_pay_python_sdk.pydantic.void_search_voids_request import VoidSearchVoidsRequest as VoidSearchVoidsRequestPydantic

from . import path

# Path params
ExportableSchema = schemas.StrSchema
PageNumberSchema = schemas.Int32Schema
PageSizeSchema = schemas.StrSchema
RequestRequiredPathParams = typing_extensions.TypedDict(
    'RequestRequiredPathParams',
    {
        'Exportable': typing.Union[ExportableSchema, str, ],
        'PageNumber': typing.Union[PageNumberSchema, decimal.Decimal, int, ],
        'PageSize': typing.Union[PageSizeSchema, str, ],
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


request_path_exportable = api_client.PathParameter(
    name="Exportable",
    style=api_client.ParameterStyle.SIMPLE,
    schema=ExportableSchema,
    required=True,
)
request_path_page_number = api_client.PathParameter(
    name="PageNumber",
    style=api_client.ParameterStyle.SIMPLE,
    schema=PageNumberSchema,
    required=True,
)
request_path_page_size = api_client.PathParameter(
    name="PageSize",
    style=api_client.ParameterStyle.SIMPLE,
    schema=PageSizeSchema,
    required=True,
)
# body param
SchemaForRequestBodyApplicationJson = VoidSearchVoidsRequestSchema


request_body_void_search_voids_request = api_client.RequestBody(
    content={
        'application/json': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationJson),
    },
)
_auth = [
    'sec0',
]
SchemaFor200ResponseBodyApplicationJson = VoidSearchVoidsResponseSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: VoidSearchVoidsResponse


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: VoidSearchVoidsResponse


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

    def _search_voids_mapped_args(
        self,
        exportable: str,
        page_number: int,
        page_size: str,
        merchant_guid: typing.Optional[str] = None,
        void_reason: typing.Optional[str] = None,
        status: typing.Optional[str] = None,
        time_stamp_from: typing.Optional[date] = None,
        time_stamp_to: typing.Optional[date] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _path_params = {}
        _body = {}
        if merchant_guid is not None:
            _body["MerchantGuid"] = merchant_guid
        if void_reason is not None:
            _body["VoidReason"] = void_reason
        if status is not None:
            _body["Status"] = status
        if time_stamp_from is not None:
            _body["TimeStampFrom"] = time_stamp_from
        if time_stamp_to is not None:
            _body["TimeStampTo"] = time_stamp_to
        args.body = _body
        if exportable is not None:
            _path_params["Exportable"] = exportable
        if page_number is not None:
            _path_params["PageNumber"] = page_number
        if page_size is not None:
            _path_params["PageSize"] = page_size
        args.path = _path_params
        return args

    async def _asearch_voids_oapg(
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
        Search voids
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_exportable,
            request_path_page_number,
            request_path_page_size,
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
    
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/api/v1/Search/Voids/{exportable}/{pageNumber}/{pageSize}',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_void_search_voids_request.serialize(body, content_type)
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


    def _search_voids_oapg(
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
        Search voids
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_exportable,
            request_path_page_number,
            request_path_page_size,
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
    
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/api/v1/Search/Voids/{exportable}/{pageNumber}/{pageSize}',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_void_search_voids_request.serialize(body, content_type)
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


class SearchVoidsRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def asearch_voids(
        self,
        exportable: str,
        page_number: int,
        page_size: str,
        merchant_guid: typing.Optional[str] = None,
        void_reason: typing.Optional[str] = None,
        status: typing.Optional[str] = None,
        time_stamp_from: typing.Optional[date] = None,
        time_stamp_to: typing.Optional[date] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._search_voids_mapped_args(
            exportable=exportable,
            page_number=page_number,
            page_size=page_size,
            merchant_guid=merchant_guid,
            void_reason=void_reason,
            status=status,
            time_stamp_from=time_stamp_from,
            time_stamp_to=time_stamp_to,
        )
        return await self._asearch_voids_oapg(
            body=args.body,
            path_params=args.path,
            **kwargs,
        )
    
    def search_voids(
        self,
        exportable: str,
        page_number: int,
        page_size: str,
        merchant_guid: typing.Optional[str] = None,
        void_reason: typing.Optional[str] = None,
        status: typing.Optional[str] = None,
        time_stamp_from: typing.Optional[date] = None,
        time_stamp_to: typing.Optional[date] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._search_voids_mapped_args(
            exportable=exportable,
            page_number=page_number,
            page_size=page_size,
            merchant_guid=merchant_guid,
            void_reason=void_reason,
            status=status,
            time_stamp_from=time_stamp_from,
            time_stamp_to=time_stamp_to,
        )
        return self._search_voids_oapg(
            body=args.body,
            path_params=args.path,
        )

class SearchVoids(BaseApi):

    async def asearch_voids(
        self,
        exportable: str,
        page_number: int,
        page_size: str,
        merchant_guid: typing.Optional[str] = None,
        void_reason: typing.Optional[str] = None,
        status: typing.Optional[str] = None,
        time_stamp_from: typing.Optional[date] = None,
        time_stamp_to: typing.Optional[date] = None,
        validate: bool = False,
        **kwargs,
    ) -> VoidSearchVoidsResponsePydantic:
        raw_response = await self.raw.asearch_voids(
            exportable=exportable,
            page_number=page_number,
            page_size=page_size,
            merchant_guid=merchant_guid,
            void_reason=void_reason,
            status=status,
            time_stamp_from=time_stamp_from,
            time_stamp_to=time_stamp_to,
            **kwargs,
        )
        if validate:
            return VoidSearchVoidsResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(VoidSearchVoidsResponsePydantic, raw_response.body)
    
    
    def search_voids(
        self,
        exportable: str,
        page_number: int,
        page_size: str,
        merchant_guid: typing.Optional[str] = None,
        void_reason: typing.Optional[str] = None,
        status: typing.Optional[str] = None,
        time_stamp_from: typing.Optional[date] = None,
        time_stamp_to: typing.Optional[date] = None,
        validate: bool = False,
    ) -> VoidSearchVoidsResponsePydantic:
        raw_response = self.raw.search_voids(
            exportable=exportable,
            page_number=page_number,
            page_size=page_size,
            merchant_guid=merchant_guid,
            void_reason=void_reason,
            status=status,
            time_stamp_from=time_stamp_from,
            time_stamp_to=time_stamp_to,
        )
        if validate:
            return VoidSearchVoidsResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(VoidSearchVoidsResponsePydantic, raw_response.body)


class ApiForpost(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def apost(
        self,
        exportable: str,
        page_number: int,
        page_size: str,
        merchant_guid: typing.Optional[str] = None,
        void_reason: typing.Optional[str] = None,
        status: typing.Optional[str] = None,
        time_stamp_from: typing.Optional[date] = None,
        time_stamp_to: typing.Optional[date] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._search_voids_mapped_args(
            exportable=exportable,
            page_number=page_number,
            page_size=page_size,
            merchant_guid=merchant_guid,
            void_reason=void_reason,
            status=status,
            time_stamp_from=time_stamp_from,
            time_stamp_to=time_stamp_to,
        )
        return await self._asearch_voids_oapg(
            body=args.body,
            path_params=args.path,
            **kwargs,
        )
    
    def post(
        self,
        exportable: str,
        page_number: int,
        page_size: str,
        merchant_guid: typing.Optional[str] = None,
        void_reason: typing.Optional[str] = None,
        status: typing.Optional[str] = None,
        time_stamp_from: typing.Optional[date] = None,
        time_stamp_to: typing.Optional[date] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._search_voids_mapped_args(
            exportable=exportable,
            page_number=page_number,
            page_size=page_size,
            merchant_guid=merchant_guid,
            void_reason=void_reason,
            status=status,
            time_stamp_from=time_stamp_from,
            time_stamp_to=time_stamp_to,
        )
        return self._search_voids_oapg(
            body=args.body,
            path_params=args.path,
        )

