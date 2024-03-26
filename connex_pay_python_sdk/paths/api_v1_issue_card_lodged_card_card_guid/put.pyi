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

from connex_pay_python_sdk.model.card_update_lodged_card_request import CardUpdateLodgedCardRequest as CardUpdateLodgedCardRequestSchema
from connex_pay_python_sdk.model.card_update_lodged_card_response import CardUpdateLodgedCardResponse as CardUpdateLodgedCardResponseSchema

from connex_pay_python_sdk.type.card_update_lodged_card_response import CardUpdateLodgedCardResponse
from connex_pay_python_sdk.type.card_update_lodged_card_request import CardUpdateLodgedCardRequest

from ...api_client import Dictionary
from connex_pay_python_sdk.pydantic.card_update_lodged_card_request import CardUpdateLodgedCardRequest as CardUpdateLodgedCardRequestPydantic
from connex_pay_python_sdk.pydantic.card_update_lodged_card_response import CardUpdateLodgedCardResponse as CardUpdateLodgedCardResponsePydantic

# Path params
CardGuidSchema = schemas.StrSchema
RequestRequiredPathParams = typing_extensions.TypedDict(
    'RequestRequiredPathParams',
    {
        'CardGuid': typing.Union[CardGuidSchema, str, ],
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


request_path_card_guid = api_client.PathParameter(
    name="CardGuid",
    style=api_client.ParameterStyle.SIMPLE,
    schema=CardGuidSchema,
    required=True,
)
# body param
SchemaForRequestBodyApplicationJson = CardUpdateLodgedCardRequestSchema


request_body_card_update_lodged_card_request = api_client.RequestBody(
    content={
        'application/json': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationJson),
    },
)
SchemaFor200ResponseBodyApplicationJson = CardUpdateLodgedCardResponseSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: CardUpdateLodgedCardResponse


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: CardUpdateLodgedCardResponse


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
_all_accept_content_types = (
    'application/json',
)


class BaseApi(api_client.Api):

    def _update_lodged_card_mapped_args(
        self,
        card_guid: str,
        usage_limit: typing.Optional[int] = None,
        amount_limit: typing.Optional[typing.Union[int, float]] = None,
        limit_window: typing.Optional[str] = None,
        purchase_type: typing.Optional[str] = None,
        activated: typing.Optional[bool] = None,
        association_id: typing.Optional[str] = None,
        terminate_date: typing.Optional[date] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _path_params = {}
        _body = {}
        if usage_limit is not None:
            _body["UsageLimit"] = usage_limit
        if amount_limit is not None:
            _body["AmountLimit"] = amount_limit
        if limit_window is not None:
            _body["LimitWindow"] = limit_window
        if purchase_type is not None:
            _body["PurchaseType"] = purchase_type
        if activated is not None:
            _body["Activated"] = activated
        if association_id is not None:
            _body["AssociationId"] = association_id
        if terminate_date is not None:
            _body["TerminateDate"] = terminate_date
        args.body = _body
        if card_guid is not None:
            _path_params["CardGuid"] = card_guid
        args.path = _path_params
        return args

    async def _aupdate_lodged_card_oapg(
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
        Update Lodged Card
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_card_guid,
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
        method = 'put'.upper()
        _headers.add('Content-Type', content_type)
    
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/api/v1/IssueCard/LodgedCard/{CardGuid}',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_card_update_lodged_card_request.serialize(body, content_type)
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


    def _update_lodged_card_oapg(
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
        Update Lodged Card
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_card_guid,
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
        method = 'put'.upper()
        _headers.add('Content-Type', content_type)
    
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/api/v1/IssueCard/LodgedCard/{CardGuid}',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_card_update_lodged_card_request.serialize(body, content_type)
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


class UpdateLodgedCardRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def aupdate_lodged_card(
        self,
        card_guid: str,
        usage_limit: typing.Optional[int] = None,
        amount_limit: typing.Optional[typing.Union[int, float]] = None,
        limit_window: typing.Optional[str] = None,
        purchase_type: typing.Optional[str] = None,
        activated: typing.Optional[bool] = None,
        association_id: typing.Optional[str] = None,
        terminate_date: typing.Optional[date] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._update_lodged_card_mapped_args(
            card_guid=card_guid,
            usage_limit=usage_limit,
            amount_limit=amount_limit,
            limit_window=limit_window,
            purchase_type=purchase_type,
            activated=activated,
            association_id=association_id,
            terminate_date=terminate_date,
        )
        return await self._aupdate_lodged_card_oapg(
            body=args.body,
            path_params=args.path,
            **kwargs,
        )
    
    def update_lodged_card(
        self,
        card_guid: str,
        usage_limit: typing.Optional[int] = None,
        amount_limit: typing.Optional[typing.Union[int, float]] = None,
        limit_window: typing.Optional[str] = None,
        purchase_type: typing.Optional[str] = None,
        activated: typing.Optional[bool] = None,
        association_id: typing.Optional[str] = None,
        terminate_date: typing.Optional[date] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._update_lodged_card_mapped_args(
            card_guid=card_guid,
            usage_limit=usage_limit,
            amount_limit=amount_limit,
            limit_window=limit_window,
            purchase_type=purchase_type,
            activated=activated,
            association_id=association_id,
            terminate_date=terminate_date,
        )
        return self._update_lodged_card_oapg(
            body=args.body,
            path_params=args.path,
        )

class UpdateLodgedCard(BaseApi):

    async def aupdate_lodged_card(
        self,
        card_guid: str,
        usage_limit: typing.Optional[int] = None,
        amount_limit: typing.Optional[typing.Union[int, float]] = None,
        limit_window: typing.Optional[str] = None,
        purchase_type: typing.Optional[str] = None,
        activated: typing.Optional[bool] = None,
        association_id: typing.Optional[str] = None,
        terminate_date: typing.Optional[date] = None,
        validate: bool = False,
        **kwargs,
    ) -> CardUpdateLodgedCardResponsePydantic:
        raw_response = await self.raw.aupdate_lodged_card(
            card_guid=card_guid,
            usage_limit=usage_limit,
            amount_limit=amount_limit,
            limit_window=limit_window,
            purchase_type=purchase_type,
            activated=activated,
            association_id=association_id,
            terminate_date=terminate_date,
            **kwargs,
        )
        if validate:
            return CardUpdateLodgedCardResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(CardUpdateLodgedCardResponsePydantic, raw_response.body)
    
    
    def update_lodged_card(
        self,
        card_guid: str,
        usage_limit: typing.Optional[int] = None,
        amount_limit: typing.Optional[typing.Union[int, float]] = None,
        limit_window: typing.Optional[str] = None,
        purchase_type: typing.Optional[str] = None,
        activated: typing.Optional[bool] = None,
        association_id: typing.Optional[str] = None,
        terminate_date: typing.Optional[date] = None,
        validate: bool = False,
    ) -> CardUpdateLodgedCardResponsePydantic:
        raw_response = self.raw.update_lodged_card(
            card_guid=card_guid,
            usage_limit=usage_limit,
            amount_limit=amount_limit,
            limit_window=limit_window,
            purchase_type=purchase_type,
            activated=activated,
            association_id=association_id,
            terminate_date=terminate_date,
        )
        if validate:
            return CardUpdateLodgedCardResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(CardUpdateLodgedCardResponsePydantic, raw_response.body)


class ApiForput(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def aput(
        self,
        card_guid: str,
        usage_limit: typing.Optional[int] = None,
        amount_limit: typing.Optional[typing.Union[int, float]] = None,
        limit_window: typing.Optional[str] = None,
        purchase_type: typing.Optional[str] = None,
        activated: typing.Optional[bool] = None,
        association_id: typing.Optional[str] = None,
        terminate_date: typing.Optional[date] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._update_lodged_card_mapped_args(
            card_guid=card_guid,
            usage_limit=usage_limit,
            amount_limit=amount_limit,
            limit_window=limit_window,
            purchase_type=purchase_type,
            activated=activated,
            association_id=association_id,
            terminate_date=terminate_date,
        )
        return await self._aupdate_lodged_card_oapg(
            body=args.body,
            path_params=args.path,
            **kwargs,
        )
    
    def put(
        self,
        card_guid: str,
        usage_limit: typing.Optional[int] = None,
        amount_limit: typing.Optional[typing.Union[int, float]] = None,
        limit_window: typing.Optional[str] = None,
        purchase_type: typing.Optional[str] = None,
        activated: typing.Optional[bool] = None,
        association_id: typing.Optional[str] = None,
        terminate_date: typing.Optional[date] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._update_lodged_card_mapped_args(
            card_guid=card_guid,
            usage_limit=usage_limit,
            amount_limit=amount_limit,
            limit_window=limit_window,
            purchase_type=purchase_type,
            activated=activated,
            association_id=association_id,
            terminate_date=terminate_date,
        )
        return self._update_lodged_card_oapg(
            body=args.body,
            path_params=args.path,
        )

