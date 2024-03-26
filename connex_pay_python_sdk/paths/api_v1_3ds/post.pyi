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

from connex_pay_python_sdk.model.authentication_obtain3_d_secure_authentication_request_card import AuthenticationObtain3DSecureAuthenticationRequestCard as AuthenticationObtain3DSecureAuthenticationRequestCardSchema
from connex_pay_python_sdk.model.authentication_obtain3_d_secure_authentication_response import AuthenticationObtain3DSecureAuthenticationResponse as AuthenticationObtain3DSecureAuthenticationResponseSchema
from connex_pay_python_sdk.model.authentication_obtain3_d_secure_authentication_request import AuthenticationObtain3DSecureAuthenticationRequest as AuthenticationObtain3DSecureAuthenticationRequestSchema
from connex_pay_python_sdk.model.authentication_obtain3_d_secure_authentication_request_browser_data import AuthenticationObtain3DSecureAuthenticationRequestBrowserData as AuthenticationObtain3DSecureAuthenticationRequestBrowserDataSchema
from connex_pay_python_sdk.model.authentication_obtain3_d_secure_authentication202_response import AuthenticationObtain3DSecureAuthentication202Response as AuthenticationObtain3DSecureAuthentication202ResponseSchema

from connex_pay_python_sdk.type.authentication_obtain3_d_secure_authentication_request_card import AuthenticationObtain3DSecureAuthenticationRequestCard
from connex_pay_python_sdk.type.authentication_obtain3_d_secure_authentication_request_browser_data import AuthenticationObtain3DSecureAuthenticationRequestBrowserData
from connex_pay_python_sdk.type.authentication_obtain3_d_secure_authentication_request import AuthenticationObtain3DSecureAuthenticationRequest
from connex_pay_python_sdk.type.authentication_obtain3_d_secure_authentication202_response import AuthenticationObtain3DSecureAuthentication202Response
from connex_pay_python_sdk.type.authentication_obtain3_d_secure_authentication_response import AuthenticationObtain3DSecureAuthenticationResponse

from ...api_client import Dictionary
from connex_pay_python_sdk.pydantic.authentication_obtain3_d_secure_authentication_request import AuthenticationObtain3DSecureAuthenticationRequest as AuthenticationObtain3DSecureAuthenticationRequestPydantic
from connex_pay_python_sdk.pydantic.authentication_obtain3_d_secure_authentication_request_card import AuthenticationObtain3DSecureAuthenticationRequestCard as AuthenticationObtain3DSecureAuthenticationRequestCardPydantic
from connex_pay_python_sdk.pydantic.authentication_obtain3_d_secure_authentication_response import AuthenticationObtain3DSecureAuthenticationResponse as AuthenticationObtain3DSecureAuthenticationResponsePydantic
from connex_pay_python_sdk.pydantic.authentication_obtain3_d_secure_authentication202_response import AuthenticationObtain3DSecureAuthentication202Response as AuthenticationObtain3DSecureAuthentication202ResponsePydantic
from connex_pay_python_sdk.pydantic.authentication_obtain3_d_secure_authentication_request_browser_data import AuthenticationObtain3DSecureAuthenticationRequestBrowserData as AuthenticationObtain3DSecureAuthenticationRequestBrowserDataPydantic

# body param
SchemaForRequestBodyApplicationJson = AuthenticationObtain3DSecureAuthenticationRequestSchema


request_body_authentication_obtain3_d_secure_authentication_request = api_client.RequestBody(
    content={
        'application/json': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationJson),
    },
)
SchemaFor200ResponseBodyApplicationJson = AuthenticationObtain3DSecureAuthenticationResponseSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: AuthenticationObtain3DSecureAuthenticationResponse


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: AuthenticationObtain3DSecureAuthenticationResponse


_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
    response_cls_async=ApiResponseFor200Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationJson),
    },
)
SchemaFor202ResponseBodyApplicationJson = AuthenticationObtain3DSecureAuthentication202ResponseSchema


@dataclass
class ApiResponseFor202(api_client.ApiResponse):
    body: AuthenticationObtain3DSecureAuthentication202Response


@dataclass
class ApiResponseFor202Async(api_client.AsyncApiResponse):
    body: AuthenticationObtain3DSecureAuthentication202Response


_response_for_202 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor202,
    response_cls_async=ApiResponseFor202Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor202ResponseBodyApplicationJson),
    },
)
SchemaFor400ResponseBodyApplicationJson = schemas.StrSchema


@dataclass
class ApiResponseFor400(api_client.ApiResponse):
    body: str


@dataclass
class ApiResponseFor400Async(api_client.AsyncApiResponse):
    body: str


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

    def _obtain3d_secure_authentication_mapped_args(
        self,
        card: AuthenticationObtain3DSecureAuthenticationRequestCard,
        device_guid: str,
        browser_data: AuthenticationObtain3DSecureAuthenticationRequestBrowserData,
        amount: typing.Union[int, float],
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _body = {}
        if card is not None:
            _body["Card"] = card
        if device_guid is not None:
            _body["DeviceGuid"] = device_guid
        if browser_data is not None:
            _body["BrowserData"] = browser_data
        if amount is not None:
            _body["Amount"] = amount
        args.body = _body
        return args

    async def _aobtain3d_secure_authentication_oapg(
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
        ApiResponseFor202Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        """
        3DS Authentication
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
            path_template='/api/v1/3ds',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_authentication_obtain3_d_secure_authentication_request.serialize(body, content_type)
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


    def _obtain3d_secure_authentication_oapg(
        self,
        body: typing.Any = None,
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'application/json',
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseFor200,
        ApiResponseFor202,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        3DS Authentication
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
            path_template='/api/v1/3ds',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_authentication_obtain3_d_secure_authentication_request.serialize(body, content_type)
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


class Obtain3dSecureAuthenticationRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def aobtain3d_secure_authentication(
        self,
        card: AuthenticationObtain3DSecureAuthenticationRequestCard,
        device_guid: str,
        browser_data: AuthenticationObtain3DSecureAuthenticationRequestBrowserData,
        amount: typing.Union[int, float],
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        ApiResponseFor202Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._obtain3d_secure_authentication_mapped_args(
            card=card,
            device_guid=device_guid,
            browser_data=browser_data,
            amount=amount,
        )
        return await self._aobtain3d_secure_authentication_oapg(
            body=args.body,
            **kwargs,
        )
    
    def obtain3d_secure_authentication(
        self,
        card: AuthenticationObtain3DSecureAuthenticationRequestCard,
        device_guid: str,
        browser_data: AuthenticationObtain3DSecureAuthenticationRequestBrowserData,
        amount: typing.Union[int, float],
    ) -> typing.Union[
        ApiResponseFor200,
        ApiResponseFor202,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._obtain3d_secure_authentication_mapped_args(
            card=card,
            device_guid=device_guid,
            browser_data=browser_data,
            amount=amount,
        )
        return self._obtain3d_secure_authentication_oapg(
            body=args.body,
        )

class Obtain3dSecureAuthentication(BaseApi):

    async def aobtain3d_secure_authentication(
        self,
        card: AuthenticationObtain3DSecureAuthenticationRequestCard,
        device_guid: str,
        browser_data: AuthenticationObtain3DSecureAuthenticationRequestBrowserData,
        amount: typing.Union[int, float],
        validate: bool = False,
        **kwargs,
    ) -> AuthenticationObtain3DSecureAuthenticationResponsePydantic:
        raw_response = await self.raw.aobtain3d_secure_authentication(
            card=card,
            device_guid=device_guid,
            browser_data=browser_data,
            amount=amount,
            **kwargs,
        )
        if validate:
            return AuthenticationObtain3DSecureAuthenticationResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(AuthenticationObtain3DSecureAuthenticationResponsePydantic, raw_response.body)
    
    
    def obtain3d_secure_authentication(
        self,
        card: AuthenticationObtain3DSecureAuthenticationRequestCard,
        device_guid: str,
        browser_data: AuthenticationObtain3DSecureAuthenticationRequestBrowserData,
        amount: typing.Union[int, float],
        validate: bool = False,
    ) -> AuthenticationObtain3DSecureAuthenticationResponsePydantic:
        raw_response = self.raw.obtain3d_secure_authentication(
            card=card,
            device_guid=device_guid,
            browser_data=browser_data,
            amount=amount,
        )
        if validate:
            return AuthenticationObtain3DSecureAuthenticationResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(AuthenticationObtain3DSecureAuthenticationResponsePydantic, raw_response.body)


class ApiForpost(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def apost(
        self,
        card: AuthenticationObtain3DSecureAuthenticationRequestCard,
        device_guid: str,
        browser_data: AuthenticationObtain3DSecureAuthenticationRequestBrowserData,
        amount: typing.Union[int, float],
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        ApiResponseFor202Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._obtain3d_secure_authentication_mapped_args(
            card=card,
            device_guid=device_guid,
            browser_data=browser_data,
            amount=amount,
        )
        return await self._aobtain3d_secure_authentication_oapg(
            body=args.body,
            **kwargs,
        )
    
    def post(
        self,
        card: AuthenticationObtain3DSecureAuthenticationRequestCard,
        device_guid: str,
        browser_data: AuthenticationObtain3DSecureAuthenticationRequestBrowserData,
        amount: typing.Union[int, float],
    ) -> typing.Union[
        ApiResponseFor200,
        ApiResponseFor202,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._obtain3d_secure_authentication_mapped_args(
            card=card,
            device_guid=device_guid,
            browser_data=browser_data,
            amount=amount,
        )
        return self._obtain3d_secure_authentication_oapg(
            body=args.body,
        )

