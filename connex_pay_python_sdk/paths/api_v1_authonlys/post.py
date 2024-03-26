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

from connex_pay_python_sdk.model.authentication_acquire_client_authorization_request_bank_account import AuthenticationAcquireClientAuthorizationRequestBankAccount as AuthenticationAcquireClientAuthorizationRequestBankAccountSchema
from connex_pay_python_sdk.model.authentication_acquire_client_authorization_request_enhanced_data import AuthenticationAcquireClientAuthorizationRequestEnhancedData as AuthenticationAcquireClientAuthorizationRequestEnhancedDataSchema
from connex_pay_python_sdk.model.authentication_acquire_client_authorization_response import AuthenticationAcquireClientAuthorizationResponse as AuthenticationAcquireClientAuthorizationResponseSchema
from connex_pay_python_sdk.model.authentication_acquire_client_authorization_request_card import AuthenticationAcquireClientAuthorizationRequestCard as AuthenticationAcquireClientAuthorizationRequestCardSchema
from connex_pay_python_sdk.model.authentication_acquire_client_authorization_request_browser_data import AuthenticationAcquireClientAuthorizationRequestBrowserData as AuthenticationAcquireClientAuthorizationRequestBrowserDataSchema
from connex_pay_python_sdk.model.authentication_acquire_client_authorization_request_risk_data import AuthenticationAcquireClientAuthorizationRequestRiskData as AuthenticationAcquireClientAuthorizationRequestRiskDataSchema
from connex_pay_python_sdk.model.authentication_acquire_client_authorization_request import AuthenticationAcquireClientAuthorizationRequest as AuthenticationAcquireClientAuthorizationRequestSchema
from connex_pay_python_sdk.model.authentication_acquire_client_authorization202_response import AuthenticationAcquireClientAuthorization202Response as AuthenticationAcquireClientAuthorization202ResponseSchema
from connex_pay_python_sdk.model.authentication_acquire_client_authorization_request_customer import AuthenticationAcquireClientAuthorizationRequestCustomer as AuthenticationAcquireClientAuthorizationRequestCustomerSchema

from connex_pay_python_sdk.type.authentication_acquire_client_authorization202_response import AuthenticationAcquireClientAuthorization202Response
from connex_pay_python_sdk.type.authentication_acquire_client_authorization_request_bank_account import AuthenticationAcquireClientAuthorizationRequestBankAccount
from connex_pay_python_sdk.type.authentication_acquire_client_authorization_request import AuthenticationAcquireClientAuthorizationRequest
from connex_pay_python_sdk.type.authentication_acquire_client_authorization_request_card import AuthenticationAcquireClientAuthorizationRequestCard
from connex_pay_python_sdk.type.authentication_acquire_client_authorization_request_browser_data import AuthenticationAcquireClientAuthorizationRequestBrowserData
from connex_pay_python_sdk.type.authentication_acquire_client_authorization_response import AuthenticationAcquireClientAuthorizationResponse
from connex_pay_python_sdk.type.authentication_acquire_client_authorization_request_risk_data import AuthenticationAcquireClientAuthorizationRequestRiskData
from connex_pay_python_sdk.type.authentication_acquire_client_authorization_request_customer import AuthenticationAcquireClientAuthorizationRequestCustomer
from connex_pay_python_sdk.type.authentication_acquire_client_authorization_request_enhanced_data import AuthenticationAcquireClientAuthorizationRequestEnhancedData

from ...api_client import Dictionary
from connex_pay_python_sdk.pydantic.authentication_acquire_client_authorization_request_risk_data import AuthenticationAcquireClientAuthorizationRequestRiskData as AuthenticationAcquireClientAuthorizationRequestRiskDataPydantic
from connex_pay_python_sdk.pydantic.authentication_acquire_client_authorization_request_card import AuthenticationAcquireClientAuthorizationRequestCard as AuthenticationAcquireClientAuthorizationRequestCardPydantic
from connex_pay_python_sdk.pydantic.authentication_acquire_client_authorization_request_customer import AuthenticationAcquireClientAuthorizationRequestCustomer as AuthenticationAcquireClientAuthorizationRequestCustomerPydantic
from connex_pay_python_sdk.pydantic.authentication_acquire_client_authorization_request import AuthenticationAcquireClientAuthorizationRequest as AuthenticationAcquireClientAuthorizationRequestPydantic
from connex_pay_python_sdk.pydantic.authentication_acquire_client_authorization_request_bank_account import AuthenticationAcquireClientAuthorizationRequestBankAccount as AuthenticationAcquireClientAuthorizationRequestBankAccountPydantic
from connex_pay_python_sdk.pydantic.authentication_acquire_client_authorization_request_enhanced_data import AuthenticationAcquireClientAuthorizationRequestEnhancedData as AuthenticationAcquireClientAuthorizationRequestEnhancedDataPydantic
from connex_pay_python_sdk.pydantic.authentication_acquire_client_authorization_request_browser_data import AuthenticationAcquireClientAuthorizationRequestBrowserData as AuthenticationAcquireClientAuthorizationRequestBrowserDataPydantic
from connex_pay_python_sdk.pydantic.authentication_acquire_client_authorization202_response import AuthenticationAcquireClientAuthorization202Response as AuthenticationAcquireClientAuthorization202ResponsePydantic
from connex_pay_python_sdk.pydantic.authentication_acquire_client_authorization_response import AuthenticationAcquireClientAuthorizationResponse as AuthenticationAcquireClientAuthorizationResponsePydantic

from . import path

# body param
SchemaForRequestBodyApplicationJson = AuthenticationAcquireClientAuthorizationRequestSchema


request_body_authentication_acquire_client_authorization_request = api_client.RequestBody(
    content={
        'application/json': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationJson),
    },
)
_auth = [
    'sec0',
]
SchemaFor200ResponseBodyApplicationJson = AuthenticationAcquireClientAuthorizationResponseSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: AuthenticationAcquireClientAuthorizationResponse


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: AuthenticationAcquireClientAuthorizationResponse


_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
    response_cls_async=ApiResponseFor200Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationJson),
    },
)
SchemaFor202ResponseBodyApplicationJson = AuthenticationAcquireClientAuthorization202ResponseSchema


@dataclass
class ApiResponseFor202(api_client.ApiResponse):
    body: AuthenticationAcquireClientAuthorization202Response


@dataclass
class ApiResponseFor202Async(api_client.AsyncApiResponse):
    body: AuthenticationAcquireClientAuthorization202Response


_response_for_202 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor202,
    response_cls_async=ApiResponseFor202Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor202ResponseBodyApplicationJson),
    },
)
_status_code_to_response = {
    '200': _response_for_200,
    '202': _response_for_202,
}
_all_accept_content_types = (
    'application/json',
)


class BaseApi(api_client.Api):

    def _acquire_client_authorization_mapped_args(
        self,
        device_guid: str,
        amount: typing.Union[int, float],
        risk_data: AuthenticationAcquireClientAuthorizationRequestRiskData,
        sequence_number: typing.Optional[str] = None,
        order_number: typing.Optional[str] = None,
        send_receipt: typing.Optional[bool] = None,
        statement_description: typing.Optional[str] = None,
        customer_id: typing.Optional[str] = None,
        card: typing.Optional[AuthenticationAcquireClientAuthorizationRequestCard] = None,
        bank_account: typing.Optional[AuthenticationAcquireClientAuthorizationRequestBankAccount] = None,
        customer: typing.Optional[AuthenticationAcquireClientAuthorizationRequestCustomer] = None,
        enhanced_data: typing.Optional[AuthenticationAcquireClientAuthorizationRequestEnhancedData] = None,
        association_id: typing.Optional[str] = None,
        browser_data: typing.Optional[AuthenticationAcquireClientAuthorizationRequestBrowserData] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _body = {}
        if device_guid is not None:
            _body["DeviceGuid"] = device_guid
        if amount is not None:
            _body["Amount"] = amount
        if sequence_number is not None:
            _body["SequenceNumber"] = sequence_number
        if order_number is not None:
            _body["OrderNumber"] = order_number
        if send_receipt is not None:
            _body["SendReceipt"] = send_receipt
        if statement_description is not None:
            _body["StatementDescription"] = statement_description
        if customer_id is not None:
            _body["CustomerID"] = customer_id
        if risk_data is not None:
            _body["RiskData"] = risk_data
        if card is not None:
            _body["Card"] = card
        if bank_account is not None:
            _body["BankAccount"] = bank_account
        if customer is not None:
            _body["Customer"] = customer
        if enhanced_data is not None:
            _body["EnhancedData"] = enhanced_data
        if association_id is not None:
            _body["AssociationID"] = association_id
        if browser_data is not None:
            _body["BrowserData"] = browser_data
        args.body = _body
        return args

    async def _aacquire_client_authorization_oapg(
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
        Auth Only
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
            path_template='/api/v1/authonlys',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_authentication_acquire_client_authorization_request.serialize(body, content_type)
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


    def _acquire_client_authorization_oapg(
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
        Auth Only
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
            path_template='/api/v1/authonlys',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_authentication_acquire_client_authorization_request.serialize(body, content_type)
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


class AcquireClientAuthorizationRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def aacquire_client_authorization(
        self,
        device_guid: str,
        amount: typing.Union[int, float],
        risk_data: AuthenticationAcquireClientAuthorizationRequestRiskData,
        sequence_number: typing.Optional[str] = None,
        order_number: typing.Optional[str] = None,
        send_receipt: typing.Optional[bool] = None,
        statement_description: typing.Optional[str] = None,
        customer_id: typing.Optional[str] = None,
        card: typing.Optional[AuthenticationAcquireClientAuthorizationRequestCard] = None,
        bank_account: typing.Optional[AuthenticationAcquireClientAuthorizationRequestBankAccount] = None,
        customer: typing.Optional[AuthenticationAcquireClientAuthorizationRequestCustomer] = None,
        enhanced_data: typing.Optional[AuthenticationAcquireClientAuthorizationRequestEnhancedData] = None,
        association_id: typing.Optional[str] = None,
        browser_data: typing.Optional[AuthenticationAcquireClientAuthorizationRequestBrowserData] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        ApiResponseFor202Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._acquire_client_authorization_mapped_args(
            device_guid=device_guid,
            amount=amount,
            risk_data=risk_data,
            sequence_number=sequence_number,
            order_number=order_number,
            send_receipt=send_receipt,
            statement_description=statement_description,
            customer_id=customer_id,
            card=card,
            bank_account=bank_account,
            customer=customer,
            enhanced_data=enhanced_data,
            association_id=association_id,
            browser_data=browser_data,
        )
        return await self._aacquire_client_authorization_oapg(
            body=args.body,
            **kwargs,
        )
    
    def acquire_client_authorization(
        self,
        device_guid: str,
        amount: typing.Union[int, float],
        risk_data: AuthenticationAcquireClientAuthorizationRequestRiskData,
        sequence_number: typing.Optional[str] = None,
        order_number: typing.Optional[str] = None,
        send_receipt: typing.Optional[bool] = None,
        statement_description: typing.Optional[str] = None,
        customer_id: typing.Optional[str] = None,
        card: typing.Optional[AuthenticationAcquireClientAuthorizationRequestCard] = None,
        bank_account: typing.Optional[AuthenticationAcquireClientAuthorizationRequestBankAccount] = None,
        customer: typing.Optional[AuthenticationAcquireClientAuthorizationRequestCustomer] = None,
        enhanced_data: typing.Optional[AuthenticationAcquireClientAuthorizationRequestEnhancedData] = None,
        association_id: typing.Optional[str] = None,
        browser_data: typing.Optional[AuthenticationAcquireClientAuthorizationRequestBrowserData] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        ApiResponseFor202,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._acquire_client_authorization_mapped_args(
            device_guid=device_guid,
            amount=amount,
            risk_data=risk_data,
            sequence_number=sequence_number,
            order_number=order_number,
            send_receipt=send_receipt,
            statement_description=statement_description,
            customer_id=customer_id,
            card=card,
            bank_account=bank_account,
            customer=customer,
            enhanced_data=enhanced_data,
            association_id=association_id,
            browser_data=browser_data,
        )
        return self._acquire_client_authorization_oapg(
            body=args.body,
        )

class AcquireClientAuthorization(BaseApi):

    async def aacquire_client_authorization(
        self,
        device_guid: str,
        amount: typing.Union[int, float],
        risk_data: AuthenticationAcquireClientAuthorizationRequestRiskData,
        sequence_number: typing.Optional[str] = None,
        order_number: typing.Optional[str] = None,
        send_receipt: typing.Optional[bool] = None,
        statement_description: typing.Optional[str] = None,
        customer_id: typing.Optional[str] = None,
        card: typing.Optional[AuthenticationAcquireClientAuthorizationRequestCard] = None,
        bank_account: typing.Optional[AuthenticationAcquireClientAuthorizationRequestBankAccount] = None,
        customer: typing.Optional[AuthenticationAcquireClientAuthorizationRequestCustomer] = None,
        enhanced_data: typing.Optional[AuthenticationAcquireClientAuthorizationRequestEnhancedData] = None,
        association_id: typing.Optional[str] = None,
        browser_data: typing.Optional[AuthenticationAcquireClientAuthorizationRequestBrowserData] = None,
        validate: bool = False,
        **kwargs,
    ) -> AuthenticationAcquireClientAuthorizationResponsePydantic:
        raw_response = await self.raw.aacquire_client_authorization(
            device_guid=device_guid,
            amount=amount,
            risk_data=risk_data,
            sequence_number=sequence_number,
            order_number=order_number,
            send_receipt=send_receipt,
            statement_description=statement_description,
            customer_id=customer_id,
            card=card,
            bank_account=bank_account,
            customer=customer,
            enhanced_data=enhanced_data,
            association_id=association_id,
            browser_data=browser_data,
            **kwargs,
        )
        if validate:
            return AuthenticationAcquireClientAuthorizationResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(AuthenticationAcquireClientAuthorizationResponsePydantic, raw_response.body)
    
    
    def acquire_client_authorization(
        self,
        device_guid: str,
        amount: typing.Union[int, float],
        risk_data: AuthenticationAcquireClientAuthorizationRequestRiskData,
        sequence_number: typing.Optional[str] = None,
        order_number: typing.Optional[str] = None,
        send_receipt: typing.Optional[bool] = None,
        statement_description: typing.Optional[str] = None,
        customer_id: typing.Optional[str] = None,
        card: typing.Optional[AuthenticationAcquireClientAuthorizationRequestCard] = None,
        bank_account: typing.Optional[AuthenticationAcquireClientAuthorizationRequestBankAccount] = None,
        customer: typing.Optional[AuthenticationAcquireClientAuthorizationRequestCustomer] = None,
        enhanced_data: typing.Optional[AuthenticationAcquireClientAuthorizationRequestEnhancedData] = None,
        association_id: typing.Optional[str] = None,
        browser_data: typing.Optional[AuthenticationAcquireClientAuthorizationRequestBrowserData] = None,
        validate: bool = False,
    ) -> AuthenticationAcquireClientAuthorizationResponsePydantic:
        raw_response = self.raw.acquire_client_authorization(
            device_guid=device_guid,
            amount=amount,
            risk_data=risk_data,
            sequence_number=sequence_number,
            order_number=order_number,
            send_receipt=send_receipt,
            statement_description=statement_description,
            customer_id=customer_id,
            card=card,
            bank_account=bank_account,
            customer=customer,
            enhanced_data=enhanced_data,
            association_id=association_id,
            browser_data=browser_data,
        )
        if validate:
            return AuthenticationAcquireClientAuthorizationResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(AuthenticationAcquireClientAuthorizationResponsePydantic, raw_response.body)


class ApiForpost(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def apost(
        self,
        device_guid: str,
        amount: typing.Union[int, float],
        risk_data: AuthenticationAcquireClientAuthorizationRequestRiskData,
        sequence_number: typing.Optional[str] = None,
        order_number: typing.Optional[str] = None,
        send_receipt: typing.Optional[bool] = None,
        statement_description: typing.Optional[str] = None,
        customer_id: typing.Optional[str] = None,
        card: typing.Optional[AuthenticationAcquireClientAuthorizationRequestCard] = None,
        bank_account: typing.Optional[AuthenticationAcquireClientAuthorizationRequestBankAccount] = None,
        customer: typing.Optional[AuthenticationAcquireClientAuthorizationRequestCustomer] = None,
        enhanced_data: typing.Optional[AuthenticationAcquireClientAuthorizationRequestEnhancedData] = None,
        association_id: typing.Optional[str] = None,
        browser_data: typing.Optional[AuthenticationAcquireClientAuthorizationRequestBrowserData] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        ApiResponseFor202Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._acquire_client_authorization_mapped_args(
            device_guid=device_guid,
            amount=amount,
            risk_data=risk_data,
            sequence_number=sequence_number,
            order_number=order_number,
            send_receipt=send_receipt,
            statement_description=statement_description,
            customer_id=customer_id,
            card=card,
            bank_account=bank_account,
            customer=customer,
            enhanced_data=enhanced_data,
            association_id=association_id,
            browser_data=browser_data,
        )
        return await self._aacquire_client_authorization_oapg(
            body=args.body,
            **kwargs,
        )
    
    def post(
        self,
        device_guid: str,
        amount: typing.Union[int, float],
        risk_data: AuthenticationAcquireClientAuthorizationRequestRiskData,
        sequence_number: typing.Optional[str] = None,
        order_number: typing.Optional[str] = None,
        send_receipt: typing.Optional[bool] = None,
        statement_description: typing.Optional[str] = None,
        customer_id: typing.Optional[str] = None,
        card: typing.Optional[AuthenticationAcquireClientAuthorizationRequestCard] = None,
        bank_account: typing.Optional[AuthenticationAcquireClientAuthorizationRequestBankAccount] = None,
        customer: typing.Optional[AuthenticationAcquireClientAuthorizationRequestCustomer] = None,
        enhanced_data: typing.Optional[AuthenticationAcquireClientAuthorizationRequestEnhancedData] = None,
        association_id: typing.Optional[str] = None,
        browser_data: typing.Optional[AuthenticationAcquireClientAuthorizationRequestBrowserData] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        ApiResponseFor202,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._acquire_client_authorization_mapped_args(
            device_guid=device_guid,
            amount=amount,
            risk_data=risk_data,
            sequence_number=sequence_number,
            order_number=order_number,
            send_receipt=send_receipt,
            statement_description=statement_description,
            customer_id=customer_id,
            card=card,
            bank_account=bank_account,
            customer=customer,
            enhanced_data=enhanced_data,
            association_id=association_id,
            browser_data=browser_data,
        )
        return self._acquire_client_authorization_oapg(
            body=args.body,
        )

