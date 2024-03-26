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

from connex_pay_python_sdk.model.card_terminate_by_date_response import CardTerminateByDateResponse as CardTerminateByDateResponseSchema
from connex_pay_python_sdk.model.card_terminate_by_date400_response import CardTerminateByDate400Response as CardTerminateByDate400ResponseSchema

from connex_pay_python_sdk.type.card_terminate_by_date_response import CardTerminateByDateResponse
from connex_pay_python_sdk.type.card_terminate_by_date400_response import CardTerminateByDate400Response

from ...api_client import Dictionary
from connex_pay_python_sdk.pydantic.card_terminate_by_date400_response import CardTerminateByDate400Response as CardTerminateByDate400ResponsePydantic
from connex_pay_python_sdk.pydantic.card_terminate_by_date_response import CardTerminateByDateResponse as CardTerminateByDateResponsePydantic

# Path params
GuidSchema = schemas.StrSchema
RequestRequiredPathParams = typing_extensions.TypedDict(
    'RequestRequiredPathParams',
    {
        'guid': typing.Union[GuidSchema, str, ],
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


request_path_guid = api_client.PathParameter(
    name="guid",
    style=api_client.ParameterStyle.SIMPLE,
    schema=GuidSchema,
    required=True,
)
SchemaFor200ResponseBodyApplicationJson = CardTerminateByDateResponseSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: CardTerminateByDateResponse


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: CardTerminateByDateResponse


_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
    response_cls_async=ApiResponseFor200Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationJson),
    },
)
SchemaFor400ResponseBodyApplicationJson = CardTerminateByDate400ResponseSchema


@dataclass
class ApiResponseFor400(api_client.ApiResponse):
    body: CardTerminateByDate400Response


@dataclass
class ApiResponseFor400Async(api_client.AsyncApiResponse):
    body: CardTerminateByDate400Response


_response_for_400 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor400,
    response_cls_async=ApiResponseFor400Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor400ResponseBodyApplicationJson),
    },
)
_all_accept_content_types = (
    'application/json',
)


class BaseApi(api_client.Api):

    def _terminate_by_date_mapped_args(
        self,
        guid: str,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _path_params = {}
        if guid is not None:
            _path_params["guid"] = guid
        args.path = _path_params
        return args

    async def _aterminate_by_date_oapg(
        self,
            path_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        """
        Terminate Card
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_guid,
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
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/api/v1/TerminateCard/<guid>',
            auth_settings=_auth,
            headers=_headers,
        )
    
        response = await self.api_client.async_call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
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


    def _terminate_by_date_oapg(
        self,
            path_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        Terminate Card
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_guid,
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
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/api/v1/TerminateCard/<guid>',
            auth_settings=_auth,
            headers=_headers,
        )
    
        response = self.api_client.call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
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


class TerminateByDateRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def aterminate_by_date(
        self,
        guid: str,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._terminate_by_date_mapped_args(
            guid=guid,
        )
        return await self._aterminate_by_date_oapg(
            path_params=args.path,
            **kwargs,
        )
    
    def terminate_by_date(
        self,
        guid: str,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._terminate_by_date_mapped_args(
            guid=guid,
        )
        return self._terminate_by_date_oapg(
            path_params=args.path,
        )

class TerminateByDate(BaseApi):

    async def aterminate_by_date(
        self,
        guid: str,
        validate: bool = False,
        **kwargs,
    ) -> CardTerminateByDateResponsePydantic:
        raw_response = await self.raw.aterminate_by_date(
            guid=guid,
            **kwargs,
        )
        if validate:
            return CardTerminateByDateResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(CardTerminateByDateResponsePydantic, raw_response.body)
    
    
    def terminate_by_date(
        self,
        guid: str,
        validate: bool = False,
    ) -> CardTerminateByDateResponsePydantic:
        raw_response = self.raw.terminate_by_date(
            guid=guid,
        )
        if validate:
            return CardTerminateByDateResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(CardTerminateByDateResponsePydantic, raw_response.body)


class ApiForpost(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def apost(
        self,
        guid: str,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._terminate_by_date_mapped_args(
            guid=guid,
        )
        return await self._aterminate_by_date_oapg(
            path_params=args.path,
            **kwargs,
        )
    
    def post(
        self,
        guid: str,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._terminate_by_date_mapped_args(
            guid=guid,
        )
        return self._terminate_by_date_oapg(
            path_params=args.path,
        )

