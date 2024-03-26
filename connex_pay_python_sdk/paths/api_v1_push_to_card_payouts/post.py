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

from connex_pay_python_sdk.model.payments_dto import PaymentsDto as PaymentsDtoSchema
from connex_pay_python_sdk.model.payout_dto_label_ids import PayoutDtoLabelIds as PayoutDtoLabelIdsSchema
from connex_pay_python_sdk.model.payout_dto import PayoutDto as PayoutDtoSchema

from connex_pay_python_sdk.type.payout_dto_label_ids import PayoutDtoLabelIds
from connex_pay_python_sdk.type.payments_dto import PaymentsDto
from connex_pay_python_sdk.type.payout_dto import PayoutDto

from ...api_client import Dictionary
from connex_pay_python_sdk.pydantic.payout_dto_label_ids import PayoutDtoLabelIds as PayoutDtoLabelIdsPydantic
from connex_pay_python_sdk.pydantic.payments_dto import PaymentsDto as PaymentsDtoPydantic
from connex_pay_python_sdk.pydantic.payout_dto import PayoutDto as PayoutDtoPydantic

from . import path

# body param
SchemaForRequestBodyApplicationJson = PayoutDtoSchema
SchemaForRequestBodyTextJson = PayoutDtoSchema
SchemaForRequestBodyApplicationXml = PayoutDtoSchema
SchemaForRequestBodyTextXml = PayoutDtoSchema
SchemaForRequestBodyApplicationXWwwFormUrlencoded = PayoutDtoSchema


request_body_payout_dto = api_client.RequestBody(
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
_auth = [
    'sec0',
]
SchemaFor201ResponseBodyApplicationJson = PayoutDtoSchema
SchemaFor201ResponseBodyTextJson = PayoutDtoSchema
SchemaFor201ResponseBodyApplicationXml = PayoutDtoSchema
SchemaFor201ResponseBodyTextXml = PayoutDtoSchema


@dataclass
class ApiResponseFor201(api_client.ApiResponse):
    body: PayoutDto


@dataclass
class ApiResponseFor201Async(api_client.AsyncApiResponse):
    body: PayoutDto


_response_for_201 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor201,
    response_cls_async=ApiResponseFor201Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor201ResponseBodyApplicationJson),
        'text/json': api_client.MediaType(
            schema=SchemaFor201ResponseBodyTextJson),
        'application/xml': api_client.MediaType(
            schema=SchemaFor201ResponseBodyApplicationXml),
        'text/xml': api_client.MediaType(
            schema=SchemaFor201ResponseBodyTextXml),
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
_status_code_to_response = {
    '201': _response_for_201,
    '400': _response_for_400,
}
_all_accept_content_types = (
    'application/json',
    'text/json',
    'application/xml',
    'text/xml',
)


class BaseApi(api_client.Api):

    def _create_payout_mapped_args(
        self,
        merchant_guid: str,
        memo: str,
        payments: typing.List[PaymentsDto],
        payout_guid: typing.Optional[str] = None,
        payout_reference_token: typing.Optional[str] = None,
        status: typing.Optional[str] = None,
        order_number: typing.Optional[str] = None,
        customer_id: typing.Optional[str] = None,
        association_id: typing.Optional[str] = None,
        label_ids: typing.Optional[PayoutDtoLabelIds] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _body = {}
        if payout_guid is not None:
            _body["payoutGuid"] = payout_guid
        if merchant_guid is not None:
            _body["merchantGuid"] = merchant_guid
        if payout_reference_token is not None:
            _body["payoutReferenceToken"] = payout_reference_token
        if memo is not None:
            _body["memo"] = memo
        if status is not None:
            _body["status"] = status
        if payments is not None:
            _body["payments"] = payments
        if order_number is not None:
            _body["orderNumber"] = order_number
        if customer_id is not None:
            _body["customerId"] = customer_id
        if association_id is not None:
            _body["associationId"] = association_id
        if label_ids is not None:
            _body["labelIds"] = label_ids
        args.body = _body
        return args

    async def _acreate_payout_oapg(
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
        Create Payout
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
    
        if body is schemas.unset:
            raise exceptions.ApiValueError(
                'The required body parameter has an invalid value of: unset. Set a valid value instead')
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/api/v1/PushToCard/Payouts',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        serialized_data = request_body_payout_dto.serialize(body, content_type)
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


    def _create_payout_oapg(
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
        Create Payout
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
    
        if body is schemas.unset:
            raise exceptions.ApiValueError(
                'The required body parameter has an invalid value of: unset. Set a valid value instead')
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/api/v1/PushToCard/Payouts',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        serialized_data = request_body_payout_dto.serialize(body, content_type)
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


class CreatePayoutRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def acreate_payout(
        self,
        merchant_guid: str,
        memo: str,
        payments: typing.List[PaymentsDto],
        payout_guid: typing.Optional[str] = None,
        payout_reference_token: typing.Optional[str] = None,
        status: typing.Optional[str] = None,
        order_number: typing.Optional[str] = None,
        customer_id: typing.Optional[str] = None,
        association_id: typing.Optional[str] = None,
        label_ids: typing.Optional[PayoutDtoLabelIds] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor201Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._create_payout_mapped_args(
            merchant_guid=merchant_guid,
            memo=memo,
            payments=payments,
            payout_guid=payout_guid,
            payout_reference_token=payout_reference_token,
            status=status,
            order_number=order_number,
            customer_id=customer_id,
            association_id=association_id,
            label_ids=label_ids,
        )
        return await self._acreate_payout_oapg(
            body=args.body,
            **kwargs,
        )
    
    def create_payout(
        self,
        merchant_guid: str,
        memo: str,
        payments: typing.List[PaymentsDto],
        payout_guid: typing.Optional[str] = None,
        payout_reference_token: typing.Optional[str] = None,
        status: typing.Optional[str] = None,
        order_number: typing.Optional[str] = None,
        customer_id: typing.Optional[str] = None,
        association_id: typing.Optional[str] = None,
        label_ids: typing.Optional[PayoutDtoLabelIds] = None,
    ) -> typing.Union[
        ApiResponseFor201,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._create_payout_mapped_args(
            merchant_guid=merchant_guid,
            memo=memo,
            payments=payments,
            payout_guid=payout_guid,
            payout_reference_token=payout_reference_token,
            status=status,
            order_number=order_number,
            customer_id=customer_id,
            association_id=association_id,
            label_ids=label_ids,
        )
        return self._create_payout_oapg(
            body=args.body,
        )

class CreatePayout(BaseApi):

    async def acreate_payout(
        self,
        merchant_guid: str,
        memo: str,
        payments: typing.List[PaymentsDto],
        payout_guid: typing.Optional[str] = None,
        payout_reference_token: typing.Optional[str] = None,
        status: typing.Optional[str] = None,
        order_number: typing.Optional[str] = None,
        customer_id: typing.Optional[str] = None,
        association_id: typing.Optional[str] = None,
        label_ids: typing.Optional[PayoutDtoLabelIds] = None,
        validate: bool = False,
        **kwargs,
    ) -> PayoutDtoPydantic:
        raw_response = await self.raw.acreate_payout(
            merchant_guid=merchant_guid,
            memo=memo,
            payments=payments,
            payout_guid=payout_guid,
            payout_reference_token=payout_reference_token,
            status=status,
            order_number=order_number,
            customer_id=customer_id,
            association_id=association_id,
            label_ids=label_ids,
            **kwargs,
        )
        if validate:
            return PayoutDtoPydantic(**raw_response.body)
        return api_client.construct_model_instance(PayoutDtoPydantic, raw_response.body)
    
    
    def create_payout(
        self,
        merchant_guid: str,
        memo: str,
        payments: typing.List[PaymentsDto],
        payout_guid: typing.Optional[str] = None,
        payout_reference_token: typing.Optional[str] = None,
        status: typing.Optional[str] = None,
        order_number: typing.Optional[str] = None,
        customer_id: typing.Optional[str] = None,
        association_id: typing.Optional[str] = None,
        label_ids: typing.Optional[PayoutDtoLabelIds] = None,
        validate: bool = False,
    ) -> PayoutDtoPydantic:
        raw_response = self.raw.create_payout(
            merchant_guid=merchant_guid,
            memo=memo,
            payments=payments,
            payout_guid=payout_guid,
            payout_reference_token=payout_reference_token,
            status=status,
            order_number=order_number,
            customer_id=customer_id,
            association_id=association_id,
            label_ids=label_ids,
        )
        if validate:
            return PayoutDtoPydantic(**raw_response.body)
        return api_client.construct_model_instance(PayoutDtoPydantic, raw_response.body)


class ApiForpost(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def apost(
        self,
        merchant_guid: str,
        memo: str,
        payments: typing.List[PaymentsDto],
        payout_guid: typing.Optional[str] = None,
        payout_reference_token: typing.Optional[str] = None,
        status: typing.Optional[str] = None,
        order_number: typing.Optional[str] = None,
        customer_id: typing.Optional[str] = None,
        association_id: typing.Optional[str] = None,
        label_ids: typing.Optional[PayoutDtoLabelIds] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor201Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._create_payout_mapped_args(
            merchant_guid=merchant_guid,
            memo=memo,
            payments=payments,
            payout_guid=payout_guid,
            payout_reference_token=payout_reference_token,
            status=status,
            order_number=order_number,
            customer_id=customer_id,
            association_id=association_id,
            label_ids=label_ids,
        )
        return await self._acreate_payout_oapg(
            body=args.body,
            **kwargs,
        )
    
    def post(
        self,
        merchant_guid: str,
        memo: str,
        payments: typing.List[PaymentsDto],
        payout_guid: typing.Optional[str] = None,
        payout_reference_token: typing.Optional[str] = None,
        status: typing.Optional[str] = None,
        order_number: typing.Optional[str] = None,
        customer_id: typing.Optional[str] = None,
        association_id: typing.Optional[str] = None,
        label_ids: typing.Optional[PayoutDtoLabelIds] = None,
    ) -> typing.Union[
        ApiResponseFor201,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._create_payout_mapped_args(
            merchant_guid=merchant_guid,
            memo=memo,
            payments=payments,
            payout_guid=payout_guid,
            payout_reference_token=payout_reference_token,
            status=status,
            order_number=order_number,
            customer_id=customer_id,
            association_id=association_id,
            label_ids=label_ids,
        )
        return self._create_payout_oapg(
            body=args.body,
        )

