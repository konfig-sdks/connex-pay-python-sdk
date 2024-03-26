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

from connex_pay_python_sdk.model.problem_details import ProblemDetails as ProblemDetailsSchema
from connex_pay_python_sdk.model.daily_accounting_summary import DailyAccountingSummary as DailyAccountingSummarySchema

from connex_pay_python_sdk.type.daily_accounting_summary import DailyAccountingSummary
from connex_pay_python_sdk.type.problem_details import ProblemDetails

from ...api_client import Dictionary
from connex_pay_python_sdk.pydantic.daily_accounting_summary import DailyAccountingSummary as DailyAccountingSummaryPydantic
from connex_pay_python_sdk.pydantic.problem_details import ProblemDetails as ProblemDetailsPydantic

from . import path

# Query params
MerchantGuidSchema = schemas.UUIDSchema
ReleasedDateSchema = schemas.DateSchema
RequestRequiredQueryParams = typing_extensions.TypedDict(
    'RequestRequiredQueryParams',
    {
        'merchantGuid': typing.Union[MerchantGuidSchema, str, uuid.UUID, ],
        'releasedDate': typing.Union[ReleasedDateSchema, str, date, ],
    }
)
RequestOptionalQueryParams = typing_extensions.TypedDict(
    'RequestOptionalQueryParams',
    {
    },
    total=False
)


class RequestQueryParams(RequestRequiredQueryParams, RequestOptionalQueryParams):
    pass


request_query_merchant_guid = api_client.QueryParameter(
    name="merchantGuid",
    style=api_client.ParameterStyle.FORM,
    schema=MerchantGuidSchema,
    required=True,
    explode=True,
)
request_query_released_date = api_client.QueryParameter(
    name="releasedDate",
    style=api_client.ParameterStyle.FORM,
    schema=ReleasedDateSchema,
    required=True,
    explode=True,
)
_auth = [
    'sec0',
]
SchemaFor200ResponseBodyApplicationJson = DailyAccountingSummarySchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: DailyAccountingSummary


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: DailyAccountingSummary


_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
    response_cls_async=ApiResponseFor200Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationJson),
    },
)
SchemaFor400ResponseBodyApplicationJson = ProblemDetailsSchema


@dataclass
class ApiResponseFor400(api_client.ApiResponse):
    body: ProblemDetails


@dataclass
class ApiResponseFor400Async(api_client.AsyncApiResponse):
    body: ProblemDetails


_response_for_400 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor400,
    response_cls_async=ApiResponseFor400Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor400ResponseBodyApplicationJson),
    },
)
SchemaFor401ResponseBodyApplicationJson = ProblemDetailsSchema


@dataclass
class ApiResponseFor401(api_client.ApiResponse):
    body: ProblemDetails


@dataclass
class ApiResponseFor401Async(api_client.AsyncApiResponse):
    body: ProblemDetails


_response_for_401 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor401,
    response_cls_async=ApiResponseFor401Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor401ResponseBodyApplicationJson),
    },
)
SchemaFor404ResponseBodyApplicationJson = ProblemDetailsSchema


@dataclass
class ApiResponseFor404(api_client.ApiResponse):
    body: ProblemDetails


@dataclass
class ApiResponseFor404Async(api_client.AsyncApiResponse):
    body: ProblemDetails


_response_for_404 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor404,
    response_cls_async=ApiResponseFor404Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor404ResponseBodyApplicationJson),
    },
)
_status_code_to_response = {
    '200': _response_for_200,
    '400': _response_for_400,
    '401': _response_for_401,
    '404': _response_for_404,
}
_all_accept_content_types = (
    'application/json',
)


class BaseApi(api_client.Api):

    def _get_daily_summary_mapped_args(
        self,
        merchant_guid: str,
        released_date: date,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _query_params = {}
        if merchant_guid is not None:
            _query_params["merchantGuid"] = merchant_guid
        if released_date is not None:
            _query_params["releasedDate"] = released_date
        args.query = _query_params
        return args

    async def _aget_daily_summary_oapg(
        self,
            query_params: typing.Optional[dict] = {},
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
        Get Daily Accounting Summary
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        used_path = path.value
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_merchant_guid,
            request_query_released_date,
        ):
            parameter_data = query_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            if prefix_separator_iterator is None:
                prefix_separator_iterator = parameter.get_prefix_separator_iterator()
            serialized_data = parameter.serialize(parameter_data, prefix_separator_iterator)
            for serialized_value in serialized_data.values():
                used_path += serialized_value
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'get'.upper()
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/api/v1/Accounting/DailySummary',
            auth_settings=_auth,
            headers=_headers,
        )
    
        response = await self.api_client.async_call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            auth_settings=_auth,
            prefix_separator_iterator=prefix_separator_iterator,
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


    def _get_daily_summary_oapg(
        self,
            query_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        Get Daily Accounting Summary
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        used_path = path.value
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_merchant_guid,
            request_query_released_date,
        ):
            parameter_data = query_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            if prefix_separator_iterator is None:
                prefix_separator_iterator = parameter.get_prefix_separator_iterator()
            serialized_data = parameter.serialize(parameter_data, prefix_separator_iterator)
            for serialized_value in serialized_data.values():
                used_path += serialized_value
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'get'.upper()
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/api/v1/Accounting/DailySummary',
            auth_settings=_auth,
            headers=_headers,
        )
    
        response = self.api_client.call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            auth_settings=_auth,
            prefix_separator_iterator=prefix_separator_iterator,
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


class GetDailySummaryRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def aget_daily_summary(
        self,
        merchant_guid: str,
        released_date: date,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._get_daily_summary_mapped_args(
            merchant_guid=merchant_guid,
            released_date=released_date,
        )
        return await self._aget_daily_summary_oapg(
            query_params=args.query,
            **kwargs,
        )
    
    def get_daily_summary(
        self,
        merchant_guid: str,
        released_date: date,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._get_daily_summary_mapped_args(
            merchant_guid=merchant_guid,
            released_date=released_date,
        )
        return self._get_daily_summary_oapg(
            query_params=args.query,
        )

class GetDailySummary(BaseApi):

    async def aget_daily_summary(
        self,
        merchant_guid: str,
        released_date: date,
        validate: bool = False,
        **kwargs,
    ) -> DailyAccountingSummaryPydantic:
        raw_response = await self.raw.aget_daily_summary(
            merchant_guid=merchant_guid,
            released_date=released_date,
            **kwargs,
        )
        if validate:
            return DailyAccountingSummaryPydantic(**raw_response.body)
        return api_client.construct_model_instance(DailyAccountingSummaryPydantic, raw_response.body)
    
    
    def get_daily_summary(
        self,
        merchant_guid: str,
        released_date: date,
        validate: bool = False,
    ) -> DailyAccountingSummaryPydantic:
        raw_response = self.raw.get_daily_summary(
            merchant_guid=merchant_guid,
            released_date=released_date,
        )
        if validate:
            return DailyAccountingSummaryPydantic(**raw_response.body)
        return api_client.construct_model_instance(DailyAccountingSummaryPydantic, raw_response.body)


class ApiForget(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def aget(
        self,
        merchant_guid: str,
        released_date: date,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._get_daily_summary_mapped_args(
            merchant_guid=merchant_guid,
            released_date=released_date,
        )
        return await self._aget_daily_summary_oapg(
            query_params=args.query,
            **kwargs,
        )
    
    def get(
        self,
        merchant_guid: str,
        released_date: date,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._get_daily_summary_mapped_args(
            merchant_guid=merchant_guid,
            released_date=released_date,
        )
        return self._get_daily_summary_oapg(
            query_params=args.query,
        )

