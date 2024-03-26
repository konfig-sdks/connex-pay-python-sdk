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

from connex_pay_python_sdk.model.ach_create_credit_payment_request import AchCreateCreditPaymentRequest as AchCreateCreditPaymentRequestSchema
from connex_pay_python_sdk.model.ach_create_credit_payment_request_account_holder import AchCreateCreditPaymentRequestAccountHolder as AchCreateCreditPaymentRequestAccountHolderSchema
from connex_pay_python_sdk.model.ach_create_credit_payment_response import AchCreateCreditPaymentResponse as AchCreateCreditPaymentResponseSchema

from connex_pay_python_sdk.type.ach_create_credit_payment_response import AchCreateCreditPaymentResponse
from connex_pay_python_sdk.type.ach_create_credit_payment_request_account_holder import AchCreateCreditPaymentRequestAccountHolder
from connex_pay_python_sdk.type.ach_create_credit_payment_request import AchCreateCreditPaymentRequest

from ...api_client import Dictionary
from connex_pay_python_sdk.pydantic.ach_create_credit_payment_request import AchCreateCreditPaymentRequest as AchCreateCreditPaymentRequestPydantic
from connex_pay_python_sdk.pydantic.ach_create_credit_payment_response import AchCreateCreditPaymentResponse as AchCreateCreditPaymentResponsePydantic
from connex_pay_python_sdk.pydantic.ach_create_credit_payment_request_account_holder import AchCreateCreditPaymentRequestAccountHolder as AchCreateCreditPaymentRequestAccountHolderPydantic

from . import path

# body param
SchemaForRequestBodyApplicationJson = AchCreateCreditPaymentRequestSchema


request_body_ach_create_credit_payment_request = api_client.RequestBody(
    content={
        'application/json': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationJson),
    },
)
_auth = [
    'sec0',
]
SchemaFor200ResponseBodyApplicationJson = AchCreateCreditPaymentResponseSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: AchCreateCreditPaymentResponse


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: AchCreateCreditPaymentResponse


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

    def _create_credit_payment_mapped_args(
        self,
        merchant_guid: str,
        amount: typing.Union[int, float],
        payee_name: str,
        account_holder: AchCreateCreditPaymentRequestAccountHolder,
        statement_company_name: typing.Optional[str] = None,
        description: typing.Optional[str] = None,
        order_number: typing.Optional[str] = None,
        sequence_number: typing.Optional[str] = None,
        association_id: typing.Optional[str] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _body = {}
        if merchant_guid is not None:
            _body["MerchantGuid"] = merchant_guid
        if amount is not None:
            _body["Amount"] = amount
        if payee_name is not None:
            _body["PayeeName"] = payee_name
        if statement_company_name is not None:
            _body["StatementCompanyName"] = statement_company_name
        if description is not None:
            _body["Description"] = description
        if account_holder is not None:
            _body["AccountHolder"] = account_holder
        if order_number is not None:
            _body["OrderNumber"] = order_number
        if sequence_number is not None:
            _body["SequenceNumber"] = sequence_number
        if association_id is not None:
            _body["AssociationId"] = association_id
        args.body = _body
        return args

    async def _acreate_credit_payment_oapg(
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
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        """
        Issue ACH Lite
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
            path_template='/api/v1/IssueACH/IssueLite',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_ach_create_credit_payment_request.serialize(body, content_type)
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


    def _create_credit_payment_oapg(
        self,
        body: typing.Any = None,
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
        Issue ACH Lite
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
            path_template='/api/v1/IssueACH/IssueLite',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_ach_create_credit_payment_request.serialize(body, content_type)
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


class CreateCreditPaymentRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def acreate_credit_payment(
        self,
        merchant_guid: str,
        amount: typing.Union[int, float],
        payee_name: str,
        account_holder: AchCreateCreditPaymentRequestAccountHolder,
        statement_company_name: typing.Optional[str] = None,
        description: typing.Optional[str] = None,
        order_number: typing.Optional[str] = None,
        sequence_number: typing.Optional[str] = None,
        association_id: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._create_credit_payment_mapped_args(
            merchant_guid=merchant_guid,
            amount=amount,
            payee_name=payee_name,
            account_holder=account_holder,
            statement_company_name=statement_company_name,
            description=description,
            order_number=order_number,
            sequence_number=sequence_number,
            association_id=association_id,
        )
        return await self._acreate_credit_payment_oapg(
            body=args.body,
            **kwargs,
        )
    
    def create_credit_payment(
        self,
        merchant_guid: str,
        amount: typing.Union[int, float],
        payee_name: str,
        account_holder: AchCreateCreditPaymentRequestAccountHolder,
        statement_company_name: typing.Optional[str] = None,
        description: typing.Optional[str] = None,
        order_number: typing.Optional[str] = None,
        sequence_number: typing.Optional[str] = None,
        association_id: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._create_credit_payment_mapped_args(
            merchant_guid=merchant_guid,
            amount=amount,
            payee_name=payee_name,
            account_holder=account_holder,
            statement_company_name=statement_company_name,
            description=description,
            order_number=order_number,
            sequence_number=sequence_number,
            association_id=association_id,
        )
        return self._create_credit_payment_oapg(
            body=args.body,
        )

class CreateCreditPayment(BaseApi):

    async def acreate_credit_payment(
        self,
        merchant_guid: str,
        amount: typing.Union[int, float],
        payee_name: str,
        account_holder: AchCreateCreditPaymentRequestAccountHolder,
        statement_company_name: typing.Optional[str] = None,
        description: typing.Optional[str] = None,
        order_number: typing.Optional[str] = None,
        sequence_number: typing.Optional[str] = None,
        association_id: typing.Optional[str] = None,
        validate: bool = False,
        **kwargs,
    ) -> AchCreateCreditPaymentResponsePydantic:
        raw_response = await self.raw.acreate_credit_payment(
            merchant_guid=merchant_guid,
            amount=amount,
            payee_name=payee_name,
            account_holder=account_holder,
            statement_company_name=statement_company_name,
            description=description,
            order_number=order_number,
            sequence_number=sequence_number,
            association_id=association_id,
            **kwargs,
        )
        if validate:
            return AchCreateCreditPaymentResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(AchCreateCreditPaymentResponsePydantic, raw_response.body)
    
    
    def create_credit_payment(
        self,
        merchant_guid: str,
        amount: typing.Union[int, float],
        payee_name: str,
        account_holder: AchCreateCreditPaymentRequestAccountHolder,
        statement_company_name: typing.Optional[str] = None,
        description: typing.Optional[str] = None,
        order_number: typing.Optional[str] = None,
        sequence_number: typing.Optional[str] = None,
        association_id: typing.Optional[str] = None,
        validate: bool = False,
    ) -> AchCreateCreditPaymentResponsePydantic:
        raw_response = self.raw.create_credit_payment(
            merchant_guid=merchant_guid,
            amount=amount,
            payee_name=payee_name,
            account_holder=account_holder,
            statement_company_name=statement_company_name,
            description=description,
            order_number=order_number,
            sequence_number=sequence_number,
            association_id=association_id,
        )
        if validate:
            return AchCreateCreditPaymentResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(AchCreateCreditPaymentResponsePydantic, raw_response.body)


class ApiForpost(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def apost(
        self,
        merchant_guid: str,
        amount: typing.Union[int, float],
        payee_name: str,
        account_holder: AchCreateCreditPaymentRequestAccountHolder,
        statement_company_name: typing.Optional[str] = None,
        description: typing.Optional[str] = None,
        order_number: typing.Optional[str] = None,
        sequence_number: typing.Optional[str] = None,
        association_id: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._create_credit_payment_mapped_args(
            merchant_guid=merchant_guid,
            amount=amount,
            payee_name=payee_name,
            account_holder=account_holder,
            statement_company_name=statement_company_name,
            description=description,
            order_number=order_number,
            sequence_number=sequence_number,
            association_id=association_id,
        )
        return await self._acreate_credit_payment_oapg(
            body=args.body,
            **kwargs,
        )
    
    def post(
        self,
        merchant_guid: str,
        amount: typing.Union[int, float],
        payee_name: str,
        account_holder: AchCreateCreditPaymentRequestAccountHolder,
        statement_company_name: typing.Optional[str] = None,
        description: typing.Optional[str] = None,
        order_number: typing.Optional[str] = None,
        sequence_number: typing.Optional[str] = None,
        association_id: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._create_credit_payment_mapped_args(
            merchant_guid=merchant_guid,
            amount=amount,
            payee_name=payee_name,
            account_holder=account_holder,
            statement_company_name=statement_company_name,
            description=description,
            order_number=order_number,
            sequence_number=sequence_number,
            association_id=association_id,
        )
        return self._create_credit_payment_oapg(
            body=args.body,
        )

