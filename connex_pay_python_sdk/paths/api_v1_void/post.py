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

from connex_pay_python_sdk.model.void_create_void_request import VoidCreateVoidRequest as VoidCreateVoidRequestSchema
from connex_pay_python_sdk.model.void_create_void_response import VoidCreateVoidResponse as VoidCreateVoidResponseSchema

from connex_pay_python_sdk.type.void_create_void_response import VoidCreateVoidResponse
from connex_pay_python_sdk.type.void_create_void_request import VoidCreateVoidRequest

from ...api_client import Dictionary
from connex_pay_python_sdk.pydantic.void_create_void_request import VoidCreateVoidRequest as VoidCreateVoidRequestPydantic
from connex_pay_python_sdk.pydantic.void_create_void_response import VoidCreateVoidResponse as VoidCreateVoidResponsePydantic

from . import path

# body param
SchemaForRequestBodyApplicationJson = VoidCreateVoidRequestSchema


request_body_void_create_void_request = api_client.RequestBody(
    content={
        'application/json': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationJson),
    },
)
_auth = [
    'sec0',
]
SchemaFor201ResponseBodyApplicationJson = VoidCreateVoidResponseSchema


@dataclass
class ApiResponseFor201(api_client.ApiResponse):
    body: VoidCreateVoidResponse


@dataclass
class ApiResponseFor201Async(api_client.AsyncApiResponse):
    body: VoidCreateVoidResponse


_response_for_201 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor201,
    response_cls_async=ApiResponseFor201Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor201ResponseBodyApplicationJson),
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
    '201': _response_for_201,
    '400': _response_for_400,
}
_all_accept_content_types = (
    'application/json',
)


class BaseApi(api_client.Api):

    def _create_void_mapped_args(
        self,
        device_guid: str,
        sale_guid: typing.Optional[str] = None,
        return_guid: typing.Optional[str] = None,
        sale_reference_number: typing.Optional[int] = None,
        auth_only_guid: typing.Optional[str] = None,
        void_reason: typing.Optional[str] = None,
        amount: typing.Optional[typing.Union[int, float]] = None,
        sequence_number: typing.Optional[str] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _body = {}
        if device_guid is not None:
            _body["DeviceGuid"] = device_guid
        if sale_guid is not None:
            _body["SaleGuid"] = sale_guid
        if return_guid is not None:
            _body["ReturnGuid"] = return_guid
        if sale_reference_number is not None:
            _body["SaleReferenceNumber"] = sale_reference_number
        if auth_only_guid is not None:
            _body["AuthOnlyGuid"] = auth_only_guid
        if void_reason is not None:
            _body["VoidReason"] = void_reason
        if amount is not None:
            _body["Amount"] = amount
        if sequence_number is not None:
            _body["SequenceNumber"] = sequence_number
        args.body = _body
        return args

    async def _acreate_void_oapg(
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
        Void
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
            path_template='/api/v1/void',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_void_create_void_request.serialize(body, content_type)
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


    def _create_void_oapg(
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
        Void
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
            path_template='/api/v1/void',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_void_create_void_request.serialize(body, content_type)
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


class CreateVoidRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def acreate_void(
        self,
        device_guid: str,
        sale_guid: typing.Optional[str] = None,
        return_guid: typing.Optional[str] = None,
        sale_reference_number: typing.Optional[int] = None,
        auth_only_guid: typing.Optional[str] = None,
        void_reason: typing.Optional[str] = None,
        amount: typing.Optional[typing.Union[int, float]] = None,
        sequence_number: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor201Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._create_void_mapped_args(
            device_guid=device_guid,
            sale_guid=sale_guid,
            return_guid=return_guid,
            sale_reference_number=sale_reference_number,
            auth_only_guid=auth_only_guid,
            void_reason=void_reason,
            amount=amount,
            sequence_number=sequence_number,
        )
        return await self._acreate_void_oapg(
            body=args.body,
            **kwargs,
        )
    
    def create_void(
        self,
        device_guid: str,
        sale_guid: typing.Optional[str] = None,
        return_guid: typing.Optional[str] = None,
        sale_reference_number: typing.Optional[int] = None,
        auth_only_guid: typing.Optional[str] = None,
        void_reason: typing.Optional[str] = None,
        amount: typing.Optional[typing.Union[int, float]] = None,
        sequence_number: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor201,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._create_void_mapped_args(
            device_guid=device_guid,
            sale_guid=sale_guid,
            return_guid=return_guid,
            sale_reference_number=sale_reference_number,
            auth_only_guid=auth_only_guid,
            void_reason=void_reason,
            amount=amount,
            sequence_number=sequence_number,
        )
        return self._create_void_oapg(
            body=args.body,
        )

class CreateVoid(BaseApi):

    async def acreate_void(
        self,
        device_guid: str,
        sale_guid: typing.Optional[str] = None,
        return_guid: typing.Optional[str] = None,
        sale_reference_number: typing.Optional[int] = None,
        auth_only_guid: typing.Optional[str] = None,
        void_reason: typing.Optional[str] = None,
        amount: typing.Optional[typing.Union[int, float]] = None,
        sequence_number: typing.Optional[str] = None,
        validate: bool = False,
        **kwargs,
    ) -> VoidCreateVoidResponsePydantic:
        raw_response = await self.raw.acreate_void(
            device_guid=device_guid,
            sale_guid=sale_guid,
            return_guid=return_guid,
            sale_reference_number=sale_reference_number,
            auth_only_guid=auth_only_guid,
            void_reason=void_reason,
            amount=amount,
            sequence_number=sequence_number,
            **kwargs,
        )
        if validate:
            return VoidCreateVoidResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(VoidCreateVoidResponsePydantic, raw_response.body)
    
    
    def create_void(
        self,
        device_guid: str,
        sale_guid: typing.Optional[str] = None,
        return_guid: typing.Optional[str] = None,
        sale_reference_number: typing.Optional[int] = None,
        auth_only_guid: typing.Optional[str] = None,
        void_reason: typing.Optional[str] = None,
        amount: typing.Optional[typing.Union[int, float]] = None,
        sequence_number: typing.Optional[str] = None,
        validate: bool = False,
    ) -> VoidCreateVoidResponsePydantic:
        raw_response = self.raw.create_void(
            device_guid=device_guid,
            sale_guid=sale_guid,
            return_guid=return_guid,
            sale_reference_number=sale_reference_number,
            auth_only_guid=auth_only_guid,
            void_reason=void_reason,
            amount=amount,
            sequence_number=sequence_number,
        )
        if validate:
            return VoidCreateVoidResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(VoidCreateVoidResponsePydantic, raw_response.body)


class ApiForpost(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def apost(
        self,
        device_guid: str,
        sale_guid: typing.Optional[str] = None,
        return_guid: typing.Optional[str] = None,
        sale_reference_number: typing.Optional[int] = None,
        auth_only_guid: typing.Optional[str] = None,
        void_reason: typing.Optional[str] = None,
        amount: typing.Optional[typing.Union[int, float]] = None,
        sequence_number: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor201Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._create_void_mapped_args(
            device_guid=device_guid,
            sale_guid=sale_guid,
            return_guid=return_guid,
            sale_reference_number=sale_reference_number,
            auth_only_guid=auth_only_guid,
            void_reason=void_reason,
            amount=amount,
            sequence_number=sequence_number,
        )
        return await self._acreate_void_oapg(
            body=args.body,
            **kwargs,
        )
    
    def post(
        self,
        device_guid: str,
        sale_guid: typing.Optional[str] = None,
        return_guid: typing.Optional[str] = None,
        sale_reference_number: typing.Optional[int] = None,
        auth_only_guid: typing.Optional[str] = None,
        void_reason: typing.Optional[str] = None,
        amount: typing.Optional[typing.Union[int, float]] = None,
        sequence_number: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor201,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._create_void_mapped_args(
            device_guid=device_guid,
            sale_guid=sale_guid,
            return_guid=return_guid,
            sale_reference_number=sale_reference_number,
            auth_only_guid=auth_only_guid,
            void_reason=void_reason,
            amount=amount,
            sequence_number=sequence_number,
        )
        return self._create_void_oapg(
            body=args.body,
        )

