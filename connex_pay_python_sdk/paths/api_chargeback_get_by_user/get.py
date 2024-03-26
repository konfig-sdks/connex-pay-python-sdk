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



from ...api_client import Dictionary

from . import path

# Path params
GetByUserstartDate20161201Schema = schemas.StrSchema
GetByUserstartDate20161201endDate20161201Schema = schemas.StrSchema
GetByResolvedDatestartDate20190920endDate20191021Schema = schemas.StrSchema
RequestRequiredPathParams = typing_extensions.TypedDict(
    'RequestRequiredPathParams',
    {
        '/GetByUser?startDate&#x3D;2016-12-01': typing.Union[GetByUserstartDate20161201Schema, str, ],
        '/GetByUser?startDate&#x3D;2016-12-01&amp;endDate&#x3D;2016-12-01': typing.Union[GetByUserstartDate20161201endDate20161201Schema, str, ],
        '/GetByResolvedDate?startDate&#x3D;2019-09-20&amp;endDate&#x3D;2019-10-21': typing.Union[GetByResolvedDatestartDate20190920endDate20191021Schema, str, ],
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


request_path_get_by_userstart_date2016_12_01 = api_client.PathParameter(
    name="/GetByUser?startDate&#x3D;2016-12-01",
    style=api_client.ParameterStyle.SIMPLE,
    schema=GetByUserstartDate20161201Schema,
    required=True,
)
request_path_get_by_userstart_date2016_12_01end_date2016_12_01 = api_client.PathParameter(
    name="/GetByUser?startDate&#x3D;2016-12-01&amp;endDate&#x3D;2016-12-01",
    style=api_client.ParameterStyle.SIMPLE,
    schema=GetByUserstartDate20161201endDate20161201Schema,
    required=True,
)
request_path_get_by_resolved_datestart_date2019_09_20end_date2019_10_21 = api_client.PathParameter(
    name="/GetByResolvedDate?startDate&#x3D;2019-09-20&amp;endDate&#x3D;2019-10-21",
    style=api_client.ParameterStyle.SIMPLE,
    schema=GetByResolvedDatestartDate20190920endDate20191021Schema,
    required=True,
)
_auth = [
    'sec0',
]
SchemaFor200ResponseBodyApplicationJson = schemas.StrSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: str


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: str


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

    def _get_chargebacks_by_user_mapped_args(
        self,
        get_by_userstart_date2016_12_01: str,
        get_by_userstart_date2016_12_01end_date2016_12_01: str,
        get_by_resolved_datestart_date2019_09_20end_date2019_10_21: str,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _path_params = {}
        if get_by_userstart_date2016_12_01 is not None:
            _path_params["/GetByUser?startDate=2016-12-01"] = get_by_userstart_date2016_12_01
        if get_by_userstart_date2016_12_01end_date2016_12_01 is not None:
            _path_params["/GetByUser?startDate=2016-12-01&endDate=2016-12-01"] = get_by_userstart_date2016_12_01end_date2016_12_01
        if get_by_resolved_datestart_date2019_09_20end_date2019_10_21 is not None:
            _path_params["/GetByResolvedDate?startDate=2019-09-20&endDate=2019-10-21"] = get_by_resolved_datestart_date2019_09_20end_date2019_10_21
        args.path = _path_params
        return args

    async def _aget_chargebacks_by_user_oapg(
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
        Sales Chargebacks
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_get_by_userstart_date2016_12_01,
            request_path_get_by_userstart_date2016_12_01end_date2016_12_01,
            request_path_get_by_resolved_datestart_date2019_09_20end_date2019_10_21,
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
        method = 'get'.upper()
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/api/chargeback/GetByUser',
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


    def _get_chargebacks_by_user_oapg(
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
        Sales Chargebacks
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_get_by_userstart_date2016_12_01,
            request_path_get_by_userstart_date2016_12_01end_date2016_12_01,
            request_path_get_by_resolved_datestart_date2019_09_20end_date2019_10_21,
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
        method = 'get'.upper()
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/api/chargeback/GetByUser',
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


class GetChargebacksByUserRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def aget_chargebacks_by_user(
        self,
        get_by_userstart_date2016_12_01: str,
        get_by_userstart_date2016_12_01end_date2016_12_01: str,
        get_by_resolved_datestart_date2019_09_20end_date2019_10_21: str,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._get_chargebacks_by_user_mapped_args(
            get_by_userstart_date2016_12_01=get_by_userstart_date2016_12_01,
            get_by_userstart_date2016_12_01end_date2016_12_01=get_by_userstart_date2016_12_01end_date2016_12_01,
            get_by_resolved_datestart_date2019_09_20end_date2019_10_21=get_by_resolved_datestart_date2019_09_20end_date2019_10_21,
        )
        return await self._aget_chargebacks_by_user_oapg(
            path_params=args.path,
            **kwargs,
        )
    
    def get_chargebacks_by_user(
        self,
        get_by_userstart_date2016_12_01: str,
        get_by_userstart_date2016_12_01end_date2016_12_01: str,
        get_by_resolved_datestart_date2019_09_20end_date2019_10_21: str,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._get_chargebacks_by_user_mapped_args(
            get_by_userstart_date2016_12_01=get_by_userstart_date2016_12_01,
            get_by_userstart_date2016_12_01end_date2016_12_01=get_by_userstart_date2016_12_01end_date2016_12_01,
            get_by_resolved_datestart_date2019_09_20end_date2019_10_21=get_by_resolved_datestart_date2019_09_20end_date2019_10_21,
        )
        return self._get_chargebacks_by_user_oapg(
            path_params=args.path,
        )

class GetChargebacksByUser(BaseApi):

    async def aget_chargebacks_by_user(
        self,
        get_by_userstart_date2016_12_01: str,
        get_by_userstart_date2016_12_01end_date2016_12_01: str,
        get_by_resolved_datestart_date2019_09_20end_date2019_10_21: str,
        validate: bool = False,
        **kwargs,
    ) -> str:
        raw_response = await self.raw.aget_chargebacks_by_user(
            get_by_userstart_date2016_12_01=get_by_userstart_date2016_12_01,
            get_by_userstart_date2016_12_01end_date2016_12_01=get_by_userstart_date2016_12_01end_date2016_12_01,
            get_by_resolved_datestart_date2019_09_20end_date2019_10_21=get_by_resolved_datestart_date2019_09_20end_date2019_10_21,
            **kwargs,
        )
        if validate:
            return RootModel[str](raw_response.body).root
        return raw_response.body
    
    
    def get_chargebacks_by_user(
        self,
        get_by_userstart_date2016_12_01: str,
        get_by_userstart_date2016_12_01end_date2016_12_01: str,
        get_by_resolved_datestart_date2019_09_20end_date2019_10_21: str,
        validate: bool = False,
    ) -> str:
        raw_response = self.raw.get_chargebacks_by_user(
            get_by_userstart_date2016_12_01=get_by_userstart_date2016_12_01,
            get_by_userstart_date2016_12_01end_date2016_12_01=get_by_userstart_date2016_12_01end_date2016_12_01,
            get_by_resolved_datestart_date2019_09_20end_date2019_10_21=get_by_resolved_datestart_date2019_09_20end_date2019_10_21,
        )
        if validate:
            return RootModel[str](raw_response.body).root
        return raw_response.body


class ApiForget(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def aget(
        self,
        get_by_userstart_date2016_12_01: str,
        get_by_userstart_date2016_12_01end_date2016_12_01: str,
        get_by_resolved_datestart_date2019_09_20end_date2019_10_21: str,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._get_chargebacks_by_user_mapped_args(
            get_by_userstart_date2016_12_01=get_by_userstart_date2016_12_01,
            get_by_userstart_date2016_12_01end_date2016_12_01=get_by_userstart_date2016_12_01end_date2016_12_01,
            get_by_resolved_datestart_date2019_09_20end_date2019_10_21=get_by_resolved_datestart_date2019_09_20end_date2019_10_21,
        )
        return await self._aget_chargebacks_by_user_oapg(
            path_params=args.path,
            **kwargs,
        )
    
    def get(
        self,
        get_by_userstart_date2016_12_01: str,
        get_by_userstart_date2016_12_01end_date2016_12_01: str,
        get_by_resolved_datestart_date2019_09_20end_date2019_10_21: str,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._get_chargebacks_by_user_mapped_args(
            get_by_userstart_date2016_12_01=get_by_userstart_date2016_12_01,
            get_by_userstart_date2016_12_01end_date2016_12_01=get_by_userstart_date2016_12_01end_date2016_12_01,
            get_by_resolved_datestart_date2019_09_20end_date2019_10_21=get_by_resolved_datestart_date2019_09_20end_date2019_10_21,
        )
        return self._get_chargebacks_by_user_oapg(
            path_params=args.path,
        )

