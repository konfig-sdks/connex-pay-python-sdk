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

from connex_pay_python_sdk.model.card_resend_transmission_info_response import CardResendTransmissionInfoResponse as CardResendTransmissionInfoResponseSchema
from connex_pay_python_sdk.model.card_resend_transmission_info_request_transmission_methods import CardResendTransmissionInfoRequestTransmissionMethods as CardResendTransmissionInfoRequestTransmissionMethodsSchema
from connex_pay_python_sdk.model.card_resend_transmission_info_request import CardResendTransmissionInfoRequest as CardResendTransmissionInfoRequestSchema

from connex_pay_python_sdk.type.card_resend_transmission_info_request_transmission_methods import CardResendTransmissionInfoRequestTransmissionMethods
from connex_pay_python_sdk.type.card_resend_transmission_info_response import CardResendTransmissionInfoResponse
from connex_pay_python_sdk.type.card_resend_transmission_info_request import CardResendTransmissionInfoRequest

from ...api_client import Dictionary
from connex_pay_python_sdk.pydantic.card_resend_transmission_info_response import CardResendTransmissionInfoResponse as CardResendTransmissionInfoResponsePydantic
from connex_pay_python_sdk.pydantic.card_resend_transmission_info_request import CardResendTransmissionInfoRequest as CardResendTransmissionInfoRequestPydantic
from connex_pay_python_sdk.pydantic.card_resend_transmission_info_request_transmission_methods import CardResendTransmissionInfoRequestTransmissionMethods as CardResendTransmissionInfoRequestTransmissionMethodsPydantic

from . import path

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
SchemaForRequestBodyApplicationJson = CardResendTransmissionInfoRequestSchema


request_body_card_resend_transmission_info_request = api_client.RequestBody(
    content={
        'application/json': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationJson),
    },
)
_auth = [
    'sec0',
]
SchemaFor200ResponseBodyApplicationJson = CardResendTransmissionInfoResponseSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: CardResendTransmissionInfoResponse


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: CardResendTransmissionInfoResponse


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

    def _resend_transmission_info_mapped_args(
        self,
        transmission_methods: CardResendTransmissionInfoRequestTransmissionMethods,
        card_guid: str,
        email_recipient: typing.Optional[str] = None,
        merchant_phone_number: typing.Optional[str] = None,
        email_from: typing.Optional[str] = None,
        recipient_name: typing.Optional[str] = None,
        subject: typing.Optional[str] = None,
        message: typing.Optional[str] = None,
        days_to_expire: typing.Optional[int] = None,
        fax_from: typing.Optional[str] = None,
        fax_recipient: typing.Optional[str] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _path_params = {}
        _body = {}
        if transmission_methods is not None:
            _body["TransmissionMethods"] = transmission_methods
        if email_recipient is not None:
            _body["EmailRecipient"] = email_recipient
        if merchant_phone_number is not None:
            _body["MerchantPhoneNumber"] = merchant_phone_number
        if email_from is not None:
            _body["EmailFrom"] = email_from
        if recipient_name is not None:
            _body["RecipientName"] = recipient_name
        if subject is not None:
            _body["Subject"] = subject
        if message is not None:
            _body["Message"] = message
        if days_to_expire is not None:
            _body["DaysToExpire"] = days_to_expire
        if fax_from is not None:
            _body["FaxFrom"] = fax_from
        if fax_recipient is not None:
            _body["FaxRecipient"] = fax_recipient
        args.body = _body
        if card_guid is not None:
            _path_params["CardGuid"] = card_guid
        args.path = _path_params
        return args

    async def _aresend_transmission_info_oapg(
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
        Resend Transmission
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
            path_template='/api/v1/IssueCard/SendPaymentInfo/{cardGuid}',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_card_resend_transmission_info_request.serialize(body, content_type)
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


    def _resend_transmission_info_oapg(
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
        Resend Transmission
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
            path_template='/api/v1/IssueCard/SendPaymentInfo/{cardGuid}',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_card_resend_transmission_info_request.serialize(body, content_type)
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


class ResendTransmissionInfoRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def aresend_transmission_info(
        self,
        transmission_methods: CardResendTransmissionInfoRequestTransmissionMethods,
        card_guid: str,
        email_recipient: typing.Optional[str] = None,
        merchant_phone_number: typing.Optional[str] = None,
        email_from: typing.Optional[str] = None,
        recipient_name: typing.Optional[str] = None,
        subject: typing.Optional[str] = None,
        message: typing.Optional[str] = None,
        days_to_expire: typing.Optional[int] = None,
        fax_from: typing.Optional[str] = None,
        fax_recipient: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._resend_transmission_info_mapped_args(
            transmission_methods=transmission_methods,
            card_guid=card_guid,
            email_recipient=email_recipient,
            merchant_phone_number=merchant_phone_number,
            email_from=email_from,
            recipient_name=recipient_name,
            subject=subject,
            message=message,
            days_to_expire=days_to_expire,
            fax_from=fax_from,
            fax_recipient=fax_recipient,
        )
        return await self._aresend_transmission_info_oapg(
            body=args.body,
            path_params=args.path,
            **kwargs,
        )
    
    def resend_transmission_info(
        self,
        transmission_methods: CardResendTransmissionInfoRequestTransmissionMethods,
        card_guid: str,
        email_recipient: typing.Optional[str] = None,
        merchant_phone_number: typing.Optional[str] = None,
        email_from: typing.Optional[str] = None,
        recipient_name: typing.Optional[str] = None,
        subject: typing.Optional[str] = None,
        message: typing.Optional[str] = None,
        days_to_expire: typing.Optional[int] = None,
        fax_from: typing.Optional[str] = None,
        fax_recipient: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._resend_transmission_info_mapped_args(
            transmission_methods=transmission_methods,
            card_guid=card_guid,
            email_recipient=email_recipient,
            merchant_phone_number=merchant_phone_number,
            email_from=email_from,
            recipient_name=recipient_name,
            subject=subject,
            message=message,
            days_to_expire=days_to_expire,
            fax_from=fax_from,
            fax_recipient=fax_recipient,
        )
        return self._resend_transmission_info_oapg(
            body=args.body,
            path_params=args.path,
        )

class ResendTransmissionInfo(BaseApi):

    async def aresend_transmission_info(
        self,
        transmission_methods: CardResendTransmissionInfoRequestTransmissionMethods,
        card_guid: str,
        email_recipient: typing.Optional[str] = None,
        merchant_phone_number: typing.Optional[str] = None,
        email_from: typing.Optional[str] = None,
        recipient_name: typing.Optional[str] = None,
        subject: typing.Optional[str] = None,
        message: typing.Optional[str] = None,
        days_to_expire: typing.Optional[int] = None,
        fax_from: typing.Optional[str] = None,
        fax_recipient: typing.Optional[str] = None,
        validate: bool = False,
        **kwargs,
    ) -> CardResendTransmissionInfoResponsePydantic:
        raw_response = await self.raw.aresend_transmission_info(
            transmission_methods=transmission_methods,
            card_guid=card_guid,
            email_recipient=email_recipient,
            merchant_phone_number=merchant_phone_number,
            email_from=email_from,
            recipient_name=recipient_name,
            subject=subject,
            message=message,
            days_to_expire=days_to_expire,
            fax_from=fax_from,
            fax_recipient=fax_recipient,
            **kwargs,
        )
        if validate:
            return CardResendTransmissionInfoResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(CardResendTransmissionInfoResponsePydantic, raw_response.body)
    
    
    def resend_transmission_info(
        self,
        transmission_methods: CardResendTransmissionInfoRequestTransmissionMethods,
        card_guid: str,
        email_recipient: typing.Optional[str] = None,
        merchant_phone_number: typing.Optional[str] = None,
        email_from: typing.Optional[str] = None,
        recipient_name: typing.Optional[str] = None,
        subject: typing.Optional[str] = None,
        message: typing.Optional[str] = None,
        days_to_expire: typing.Optional[int] = None,
        fax_from: typing.Optional[str] = None,
        fax_recipient: typing.Optional[str] = None,
        validate: bool = False,
    ) -> CardResendTransmissionInfoResponsePydantic:
        raw_response = self.raw.resend_transmission_info(
            transmission_methods=transmission_methods,
            card_guid=card_guid,
            email_recipient=email_recipient,
            merchant_phone_number=merchant_phone_number,
            email_from=email_from,
            recipient_name=recipient_name,
            subject=subject,
            message=message,
            days_to_expire=days_to_expire,
            fax_from=fax_from,
            fax_recipient=fax_recipient,
        )
        if validate:
            return CardResendTransmissionInfoResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(CardResendTransmissionInfoResponsePydantic, raw_response.body)


class ApiForput(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def aput(
        self,
        transmission_methods: CardResendTransmissionInfoRequestTransmissionMethods,
        card_guid: str,
        email_recipient: typing.Optional[str] = None,
        merchant_phone_number: typing.Optional[str] = None,
        email_from: typing.Optional[str] = None,
        recipient_name: typing.Optional[str] = None,
        subject: typing.Optional[str] = None,
        message: typing.Optional[str] = None,
        days_to_expire: typing.Optional[int] = None,
        fax_from: typing.Optional[str] = None,
        fax_recipient: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._resend_transmission_info_mapped_args(
            transmission_methods=transmission_methods,
            card_guid=card_guid,
            email_recipient=email_recipient,
            merchant_phone_number=merchant_phone_number,
            email_from=email_from,
            recipient_name=recipient_name,
            subject=subject,
            message=message,
            days_to_expire=days_to_expire,
            fax_from=fax_from,
            fax_recipient=fax_recipient,
        )
        return await self._aresend_transmission_info_oapg(
            body=args.body,
            path_params=args.path,
            **kwargs,
        )
    
    def put(
        self,
        transmission_methods: CardResendTransmissionInfoRequestTransmissionMethods,
        card_guid: str,
        email_recipient: typing.Optional[str] = None,
        merchant_phone_number: typing.Optional[str] = None,
        email_from: typing.Optional[str] = None,
        recipient_name: typing.Optional[str] = None,
        subject: typing.Optional[str] = None,
        message: typing.Optional[str] = None,
        days_to_expire: typing.Optional[int] = None,
        fax_from: typing.Optional[str] = None,
        fax_recipient: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._resend_transmission_info_mapped_args(
            transmission_methods=transmission_methods,
            card_guid=card_guid,
            email_recipient=email_recipient,
            merchant_phone_number=merchant_phone_number,
            email_from=email_from,
            recipient_name=recipient_name,
            subject=subject,
            message=message,
            days_to_expire=days_to_expire,
            fax_from=fax_from,
            fax_recipient=fax_recipient,
        )
        return self._resend_transmission_info_oapg(
            body=args.body,
            path_params=args.path,
        )

