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

from connex_pay_python_sdk.model.addendum_create_virtual_card_response import AddendumCreateVirtualCardResponse as AddendumCreateVirtualCardResponseSchema
from connex_pay_python_sdk.model.addendum_create_virtual_card_request import AddendumCreateVirtualCardRequest as AddendumCreateVirtualCardRequestSchema

from connex_pay_python_sdk.type.addendum_create_virtual_card_response import AddendumCreateVirtualCardResponse
from connex_pay_python_sdk.type.addendum_create_virtual_card_request import AddendumCreateVirtualCardRequest

from ...api_client import Dictionary
from connex_pay_python_sdk.pydantic.addendum_create_virtual_card_request import AddendumCreateVirtualCardRequest as AddendumCreateVirtualCardRequestPydantic
from connex_pay_python_sdk.pydantic.addendum_create_virtual_card_response import AddendumCreateVirtualCardResponse as AddendumCreateVirtualCardResponsePydantic

# body param
SchemaForRequestBodyApplicationJson = AddendumCreateVirtualCardRequestSchema


request_body_addendum_create_virtual_card_request = api_client.RequestBody(
    content={
        'application/json': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationJson),
    },
)
SchemaFor201ResponseBodyApplicationJson = AddendumCreateVirtualCardResponseSchema


@dataclass
class ApiResponseFor201(api_client.ApiResponse):
    body: AddendumCreateVirtualCardResponse


@dataclass
class ApiResponseFor201Async(api_client.AsyncApiResponse):
    body: AddendumCreateVirtualCardResponse


_response_for_201 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor201,
    response_cls_async=ApiResponseFor201Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor201ResponseBodyApplicationJson),
    },
)
_all_accept_content_types = (
    'application/json',
)


class BaseApi(api_client.Api):

    def _create_virtual_card_mapped_args(
        self,
        item_guid: typing.Optional[str] = None,
        value: typing.Optional[str] = None,
        category: typing.Optional[str] = None,
        id_external: typing.Optional[str] = None,
        note: typing.Optional[str] = None,
        sequence: typing.Optional[str] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _body = {}
        if item_guid is not None:
            _body["ItemGuid"] = item_guid
        if value is not None:
            _body["Value"] = value
        if category is not None:
            _body["Category"] = category
        if id_external is not None:
            _body["IdExternal"] = id_external
        if note is not None:
            _body["Note"] = note
        if sequence is not None:
            _body["Sequence"] = sequence
        args.body = _body
        return args

    async def _acreate_virtual_card_oapg(
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
        Virtual Card Addendum
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
            path_template='/api/v1/Addendum/VirtualCard',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_addendum_create_virtual_card_request.serialize(body, content_type)
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


    def _create_virtual_card_oapg(
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
        Virtual Card Addendum
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
            path_template='/api/v1/Addendum/VirtualCard',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_addendum_create_virtual_card_request.serialize(body, content_type)
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


class CreateVirtualCardRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def acreate_virtual_card(
        self,
        item_guid: typing.Optional[str] = None,
        value: typing.Optional[str] = None,
        category: typing.Optional[str] = None,
        id_external: typing.Optional[str] = None,
        note: typing.Optional[str] = None,
        sequence: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor201Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._create_virtual_card_mapped_args(
            item_guid=item_guid,
            value=value,
            category=category,
            id_external=id_external,
            note=note,
            sequence=sequence,
        )
        return await self._acreate_virtual_card_oapg(
            body=args.body,
            **kwargs,
        )
    
    def create_virtual_card(
        self,
        item_guid: typing.Optional[str] = None,
        value: typing.Optional[str] = None,
        category: typing.Optional[str] = None,
        id_external: typing.Optional[str] = None,
        note: typing.Optional[str] = None,
        sequence: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor201,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._create_virtual_card_mapped_args(
            item_guid=item_guid,
            value=value,
            category=category,
            id_external=id_external,
            note=note,
            sequence=sequence,
        )
        return self._create_virtual_card_oapg(
            body=args.body,
        )

class CreateVirtualCard(BaseApi):

    async def acreate_virtual_card(
        self,
        item_guid: typing.Optional[str] = None,
        value: typing.Optional[str] = None,
        category: typing.Optional[str] = None,
        id_external: typing.Optional[str] = None,
        note: typing.Optional[str] = None,
        sequence: typing.Optional[str] = None,
        validate: bool = False,
        **kwargs,
    ) -> AddendumCreateVirtualCardResponsePydantic:
        raw_response = await self.raw.acreate_virtual_card(
            item_guid=item_guid,
            value=value,
            category=category,
            id_external=id_external,
            note=note,
            sequence=sequence,
            **kwargs,
        )
        if validate:
            return AddendumCreateVirtualCardResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(AddendumCreateVirtualCardResponsePydantic, raw_response.body)
    
    
    def create_virtual_card(
        self,
        item_guid: typing.Optional[str] = None,
        value: typing.Optional[str] = None,
        category: typing.Optional[str] = None,
        id_external: typing.Optional[str] = None,
        note: typing.Optional[str] = None,
        sequence: typing.Optional[str] = None,
        validate: bool = False,
    ) -> AddendumCreateVirtualCardResponsePydantic:
        raw_response = self.raw.create_virtual_card(
            item_guid=item_guid,
            value=value,
            category=category,
            id_external=id_external,
            note=note,
            sequence=sequence,
        )
        if validate:
            return AddendumCreateVirtualCardResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(AddendumCreateVirtualCardResponsePydantic, raw_response.body)


class ApiForpost(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def apost(
        self,
        item_guid: typing.Optional[str] = None,
        value: typing.Optional[str] = None,
        category: typing.Optional[str] = None,
        id_external: typing.Optional[str] = None,
        note: typing.Optional[str] = None,
        sequence: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor201Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._create_virtual_card_mapped_args(
            item_guid=item_guid,
            value=value,
            category=category,
            id_external=id_external,
            note=note,
            sequence=sequence,
        )
        return await self._acreate_virtual_card_oapg(
            body=args.body,
            **kwargs,
        )
    
    def post(
        self,
        item_guid: typing.Optional[str] = None,
        value: typing.Optional[str] = None,
        category: typing.Optional[str] = None,
        id_external: typing.Optional[str] = None,
        note: typing.Optional[str] = None,
        sequence: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor201,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._create_virtual_card_mapped_args(
            item_guid=item_guid,
            value=value,
            category=category,
            id_external=id_external,
            note=note,
            sequence=sequence,
        )
        return self._create_virtual_card_oapg(
            body=args.body,
        )

