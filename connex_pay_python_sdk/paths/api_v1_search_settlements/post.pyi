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

from connex_pay_python_sdk.model.settlement_search_virtual_card_settlements_request import SettlementSearchVirtualCardSettlementsRequest as SettlementSearchVirtualCardSettlementsRequestSchema

from connex_pay_python_sdk.type.settlement_search_virtual_card_settlements_request import SettlementSearchVirtualCardSettlementsRequest

from ...api_client import Dictionary
from connex_pay_python_sdk.pydantic.settlement_search_virtual_card_settlements_request import SettlementSearchVirtualCardSettlementsRequest as SettlementSearchVirtualCardSettlementsRequestPydantic

# Path params
PageNumberSchema = schemas.Int32Schema
PageSizeSchema = schemas.Int32Schema
RequestRequiredPathParams = typing_extensions.TypedDict(
    'RequestRequiredPathParams',
    {
        'PageNumber': typing.Union[PageNumberSchema, decimal.Decimal, int, ],
        'PageSize': typing.Union[PageSizeSchema, decimal.Decimal, int, ],
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
SchemaForRequestBodyApplicationJson = SettlementSearchVirtualCardSettlementsRequestSchema


request_body_settlement_search_virtual_card_settlements_request = api_client.RequestBody(
    content={
        'application/json': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationJson),
    },
)
SchemaFor200ResponseBodyApplicationJson = schemas.DictSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]


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

    def _search_virtual_card_settlements_mapped_args(
        self,
        merchant_guid: str,
        page_number: int,
        page_size: int,
        date_from: typing.Optional[date] = None,
        date_to: typing.Optional[date] = None,
        posted_date_from: typing.Optional[date] = None,
        posted_date_to: typing.Optional[date] = None,
        order_number: typing.Optional[str] = None,
        issued_amount_from: typing.Optional[int] = None,
        issued_amount_to: typing.Optional[int] = None,
        issued_card_last_four: typing.Optional[str] = None,
        posted_amount_from: typing.Optional[typing.Union[int, float]] = None,
        posted_amount_to: typing.Optional[typing.Union[int, float]] = None,
        expiration_date_from: typing.Optional[date] = None,
        expiration_date_to: typing.Optional[date] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _path_params = {}
        _body = {}
        if merchant_guid is not None:
            _body["MerchantGuid"] = merchant_guid
        if date_from is not None:
            _body["DateFrom"] = date_from
        if date_to is not None:
            _body["DateTo"] = date_to
        if posted_date_from is not None:
            _body["PostedDateFrom"] = posted_date_from
        if posted_date_to is not None:
            _body["PostedDateTo"] = posted_date_to
        if order_number is not None:
            _body["OrderNumber"] = order_number
        if issued_amount_from is not None:
            _body["IssuedAmountFrom"] = issued_amount_from
        if issued_amount_to is not None:
            _body["IssuedAmountTo"] = issued_amount_to
        if issued_card_last_four is not None:
            _body["IssuedCardLastFour"] = issued_card_last_four
        if posted_amount_from is not None:
            _body["PostedAmountFrom"] = posted_amount_from
        if posted_amount_to is not None:
            _body["PostedAmountTo"] = posted_amount_to
        if expiration_date_from is not None:
            _body["ExpirationDateFrom"] = expiration_date_from
        if expiration_date_to is not None:
            _body["ExpirationDateTo"] = expiration_date_to
        args.body = _body
        if page_number is not None:
            _path_params["PageNumber"] = page_number
        if page_size is not None:
            _path_params["PageSize"] = page_size
        args.path = _path_params
        return args

    async def _asearch_virtual_card_settlements_oapg(
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
        Search Settlements
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
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
            path_template='/api/v1/Search/Settlements',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_settlement_search_virtual_card_settlements_request.serialize(body, content_type)
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


    def _search_virtual_card_settlements_oapg(
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
        Search Settlements
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
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
            path_template='/api/v1/Search/Settlements',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_settlement_search_virtual_card_settlements_request.serialize(body, content_type)
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


class SearchVirtualCardSettlementsRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def asearch_virtual_card_settlements(
        self,
        merchant_guid: str,
        page_number: int,
        page_size: int,
        date_from: typing.Optional[date] = None,
        date_to: typing.Optional[date] = None,
        posted_date_from: typing.Optional[date] = None,
        posted_date_to: typing.Optional[date] = None,
        order_number: typing.Optional[str] = None,
        issued_amount_from: typing.Optional[int] = None,
        issued_amount_to: typing.Optional[int] = None,
        issued_card_last_four: typing.Optional[str] = None,
        posted_amount_from: typing.Optional[typing.Union[int, float]] = None,
        posted_amount_to: typing.Optional[typing.Union[int, float]] = None,
        expiration_date_from: typing.Optional[date] = None,
        expiration_date_to: typing.Optional[date] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._search_virtual_card_settlements_mapped_args(
            merchant_guid=merchant_guid,
            page_number=page_number,
            page_size=page_size,
            date_from=date_from,
            date_to=date_to,
            posted_date_from=posted_date_from,
            posted_date_to=posted_date_to,
            order_number=order_number,
            issued_amount_from=issued_amount_from,
            issued_amount_to=issued_amount_to,
            issued_card_last_four=issued_card_last_four,
            posted_amount_from=posted_amount_from,
            posted_amount_to=posted_amount_to,
            expiration_date_from=expiration_date_from,
            expiration_date_to=expiration_date_to,
        )
        return await self._asearch_virtual_card_settlements_oapg(
            body=args.body,
            path_params=args.path,
            **kwargs,
        )
    
    def search_virtual_card_settlements(
        self,
        merchant_guid: str,
        page_number: int,
        page_size: int,
        date_from: typing.Optional[date] = None,
        date_to: typing.Optional[date] = None,
        posted_date_from: typing.Optional[date] = None,
        posted_date_to: typing.Optional[date] = None,
        order_number: typing.Optional[str] = None,
        issued_amount_from: typing.Optional[int] = None,
        issued_amount_to: typing.Optional[int] = None,
        issued_card_last_four: typing.Optional[str] = None,
        posted_amount_from: typing.Optional[typing.Union[int, float]] = None,
        posted_amount_to: typing.Optional[typing.Union[int, float]] = None,
        expiration_date_from: typing.Optional[date] = None,
        expiration_date_to: typing.Optional[date] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._search_virtual_card_settlements_mapped_args(
            merchant_guid=merchant_guid,
            page_number=page_number,
            page_size=page_size,
            date_from=date_from,
            date_to=date_to,
            posted_date_from=posted_date_from,
            posted_date_to=posted_date_to,
            order_number=order_number,
            issued_amount_from=issued_amount_from,
            issued_amount_to=issued_amount_to,
            issued_card_last_four=issued_card_last_four,
            posted_amount_from=posted_amount_from,
            posted_amount_to=posted_amount_to,
            expiration_date_from=expiration_date_from,
            expiration_date_to=expiration_date_to,
        )
        return self._search_virtual_card_settlements_oapg(
            body=args.body,
            path_params=args.path,
        )

class SearchVirtualCardSettlements(BaseApi):

    async def asearch_virtual_card_settlements(
        self,
        merchant_guid: str,
        page_number: int,
        page_size: int,
        date_from: typing.Optional[date] = None,
        date_to: typing.Optional[date] = None,
        posted_date_from: typing.Optional[date] = None,
        posted_date_to: typing.Optional[date] = None,
        order_number: typing.Optional[str] = None,
        issued_amount_from: typing.Optional[int] = None,
        issued_amount_to: typing.Optional[int] = None,
        issued_card_last_four: typing.Optional[str] = None,
        posted_amount_from: typing.Optional[typing.Union[int, float]] = None,
        posted_amount_to: typing.Optional[typing.Union[int, float]] = None,
        expiration_date_from: typing.Optional[date] = None,
        expiration_date_to: typing.Optional[date] = None,
        validate: bool = False,
        **kwargs,
    ) -> Dictionary:
        raw_response = await self.raw.asearch_virtual_card_settlements(
            merchant_guid=merchant_guid,
            page_number=page_number,
            page_size=page_size,
            date_from=date_from,
            date_to=date_to,
            posted_date_from=posted_date_from,
            posted_date_to=posted_date_to,
            order_number=order_number,
            issued_amount_from=issued_amount_from,
            issued_amount_to=issued_amount_to,
            issued_card_last_four=issued_card_last_four,
            posted_amount_from=posted_amount_from,
            posted_amount_to=posted_amount_to,
            expiration_date_from=expiration_date_from,
            expiration_date_to=expiration_date_to,
            **kwargs,
        )
        if validate:
            return Dictionary(**raw_response.body)
        return api_client.construct_model_instance(Dictionary, raw_response.body)
    
    
    def search_virtual_card_settlements(
        self,
        merchant_guid: str,
        page_number: int,
        page_size: int,
        date_from: typing.Optional[date] = None,
        date_to: typing.Optional[date] = None,
        posted_date_from: typing.Optional[date] = None,
        posted_date_to: typing.Optional[date] = None,
        order_number: typing.Optional[str] = None,
        issued_amount_from: typing.Optional[int] = None,
        issued_amount_to: typing.Optional[int] = None,
        issued_card_last_four: typing.Optional[str] = None,
        posted_amount_from: typing.Optional[typing.Union[int, float]] = None,
        posted_amount_to: typing.Optional[typing.Union[int, float]] = None,
        expiration_date_from: typing.Optional[date] = None,
        expiration_date_to: typing.Optional[date] = None,
        validate: bool = False,
    ) -> Dictionary:
        raw_response = self.raw.search_virtual_card_settlements(
            merchant_guid=merchant_guid,
            page_number=page_number,
            page_size=page_size,
            date_from=date_from,
            date_to=date_to,
            posted_date_from=posted_date_from,
            posted_date_to=posted_date_to,
            order_number=order_number,
            issued_amount_from=issued_amount_from,
            issued_amount_to=issued_amount_to,
            issued_card_last_four=issued_card_last_four,
            posted_amount_from=posted_amount_from,
            posted_amount_to=posted_amount_to,
            expiration_date_from=expiration_date_from,
            expiration_date_to=expiration_date_to,
        )
        if validate:
            return Dictionary(**raw_response.body)
        return api_client.construct_model_instance(Dictionary, raw_response.body)


class ApiForpost(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def apost(
        self,
        merchant_guid: str,
        page_number: int,
        page_size: int,
        date_from: typing.Optional[date] = None,
        date_to: typing.Optional[date] = None,
        posted_date_from: typing.Optional[date] = None,
        posted_date_to: typing.Optional[date] = None,
        order_number: typing.Optional[str] = None,
        issued_amount_from: typing.Optional[int] = None,
        issued_amount_to: typing.Optional[int] = None,
        issued_card_last_four: typing.Optional[str] = None,
        posted_amount_from: typing.Optional[typing.Union[int, float]] = None,
        posted_amount_to: typing.Optional[typing.Union[int, float]] = None,
        expiration_date_from: typing.Optional[date] = None,
        expiration_date_to: typing.Optional[date] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._search_virtual_card_settlements_mapped_args(
            merchant_guid=merchant_guid,
            page_number=page_number,
            page_size=page_size,
            date_from=date_from,
            date_to=date_to,
            posted_date_from=posted_date_from,
            posted_date_to=posted_date_to,
            order_number=order_number,
            issued_amount_from=issued_amount_from,
            issued_amount_to=issued_amount_to,
            issued_card_last_four=issued_card_last_four,
            posted_amount_from=posted_amount_from,
            posted_amount_to=posted_amount_to,
            expiration_date_from=expiration_date_from,
            expiration_date_to=expiration_date_to,
        )
        return await self._asearch_virtual_card_settlements_oapg(
            body=args.body,
            path_params=args.path,
            **kwargs,
        )
    
    def post(
        self,
        merchant_guid: str,
        page_number: int,
        page_size: int,
        date_from: typing.Optional[date] = None,
        date_to: typing.Optional[date] = None,
        posted_date_from: typing.Optional[date] = None,
        posted_date_to: typing.Optional[date] = None,
        order_number: typing.Optional[str] = None,
        issued_amount_from: typing.Optional[int] = None,
        issued_amount_to: typing.Optional[int] = None,
        issued_card_last_four: typing.Optional[str] = None,
        posted_amount_from: typing.Optional[typing.Union[int, float]] = None,
        posted_amount_to: typing.Optional[typing.Union[int, float]] = None,
        expiration_date_from: typing.Optional[date] = None,
        expiration_date_to: typing.Optional[date] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._search_virtual_card_settlements_mapped_args(
            merchant_guid=merchant_guid,
            page_number=page_number,
            page_size=page_size,
            date_from=date_from,
            date_to=date_to,
            posted_date_from=posted_date_from,
            posted_date_to=posted_date_to,
            order_number=order_number,
            issued_amount_from=issued_amount_from,
            issued_amount_to=issued_amount_to,
            issued_card_last_four=issued_card_last_four,
            posted_amount_from=posted_amount_from,
            posted_amount_to=posted_amount_to,
            expiration_date_from=expiration_date_from,
            expiration_date_to=expiration_date_to,
        )
        return self._search_virtual_card_settlements_oapg(
            body=args.body,
            path_params=args.path,
        )

