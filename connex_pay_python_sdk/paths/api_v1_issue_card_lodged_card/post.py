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

from connex_pay_python_sdk.model.card_create_lodged_card_request_label_ids import CardCreateLodgedCardRequestLabelIDs as CardCreateLodgedCardRequestLabelIDsSchema
from connex_pay_python_sdk.model.card_create_lodged_card_request_custom_parameters import CardCreateLodgedCardRequestCustomParameters as CardCreateLodgedCardRequestCustomParametersSchema
from connex_pay_python_sdk.model.card_create_lodged_card_request import CardCreateLodgedCardRequest as CardCreateLodgedCardRequestSchema
from connex_pay_python_sdk.model.card_create_lodged_card_response import CardCreateLodgedCardResponse as CardCreateLodgedCardResponseSchema
from connex_pay_python_sdk.model.card_create_lodged_card_request_transmission import CardCreateLodgedCardRequestTransmission as CardCreateLodgedCardRequestTransmissionSchema

from connex_pay_python_sdk.type.card_create_lodged_card_request_custom_parameters import CardCreateLodgedCardRequestCustomParameters
from connex_pay_python_sdk.type.card_create_lodged_card_request_label_ids import CardCreateLodgedCardRequestLabelIDs
from connex_pay_python_sdk.type.card_create_lodged_card_request_transmission import CardCreateLodgedCardRequestTransmission
from connex_pay_python_sdk.type.card_create_lodged_card_response import CardCreateLodgedCardResponse
from connex_pay_python_sdk.type.card_create_lodged_card_request import CardCreateLodgedCardRequest

from ...api_client import Dictionary
from connex_pay_python_sdk.pydantic.card_create_lodged_card_request import CardCreateLodgedCardRequest as CardCreateLodgedCardRequestPydantic
from connex_pay_python_sdk.pydantic.card_create_lodged_card_request_label_ids import CardCreateLodgedCardRequestLabelIDs as CardCreateLodgedCardRequestLabelIDsPydantic
from connex_pay_python_sdk.pydantic.card_create_lodged_card_response import CardCreateLodgedCardResponse as CardCreateLodgedCardResponsePydantic
from connex_pay_python_sdk.pydantic.card_create_lodged_card_request_transmission import CardCreateLodgedCardRequestTransmission as CardCreateLodgedCardRequestTransmissionPydantic
from connex_pay_python_sdk.pydantic.card_create_lodged_card_request_custom_parameters import CardCreateLodgedCardRequestCustomParameters as CardCreateLodgedCardRequestCustomParametersPydantic

from . import path

# body param
SchemaForRequestBodyApplicationJson = CardCreateLodgedCardRequestSchema


request_body_card_create_lodged_card_request = api_client.RequestBody(
    content={
        'application/json': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationJson),
    },
)
_auth = [
    'sec0',
]
SchemaFor200ResponseBodyApplicationJson = CardCreateLodgedCardResponseSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: CardCreateLodgedCardResponse


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: CardCreateLodgedCardResponse


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

    def _create_lodged_card_mapped_args(
        self,
        merchant_guid: str,
        first_name: str,
        last_name: str,
        amount_limit: typing.Union[int, float],
        limit_window: str,
        phone: typing.Optional[str] = None,
        address1: typing.Optional[str] = None,
        address2: typing.Optional[str] = None,
        city: typing.Optional[str] = None,
        state: typing.Optional[str] = None,
        zip_code: typing.Optional[str] = None,
        country: typing.Optional[str] = None,
        usage_limit: typing.Optional[int] = None,
        expiration_date: typing.Optional[date] = None,
        terminate_date: typing.Optional[date] = None,
        purchase_type: typing.Optional[str] = None,
        sequence_number: typing.Optional[str] = None,
        order_number: typing.Optional[str] = None,
        supplier_id: typing.Optional[str] = None,
        non_domestic_supplier: typing.Optional[bool] = None,
        transmission: typing.Optional[CardCreateLodgedCardRequestTransmission] = None,
        return_card_data: typing.Optional[bool] = None,
        customer_id: typing.Optional[str] = None,
        association_id: typing.Optional[str] = None,
        label_ids: typing.Optional[CardCreateLodgedCardRequestLabelIDs] = None,
        custom_parameters: typing.Optional[CardCreateLodgedCardRequestCustomParameters] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _body = {}
        if merchant_guid is not None:
            _body["MerchantGuid"] = merchant_guid
        if first_name is not None:
            _body["FirstName"] = first_name
        if last_name is not None:
            _body["LastName"] = last_name
        if phone is not None:
            _body["Phone"] = phone
        if address1 is not None:
            _body["Address1"] = address1
        if address2 is not None:
            _body["Address2"] = address2
        if city is not None:
            _body["City"] = city
        if state is not None:
            _body["State"] = state
        if zip_code is not None:
            _body["ZipCode"] = zip_code
        if country is not None:
            _body["Country"] = country
        if usage_limit is not None:
            _body["UsageLimit"] = usage_limit
        if amount_limit is not None:
            _body["AmountLimit"] = amount_limit
        if limit_window is not None:
            _body["LimitWindow"] = limit_window
        if expiration_date is not None:
            _body["ExpirationDate"] = expiration_date
        if terminate_date is not None:
            _body["TerminateDate"] = terminate_date
        if purchase_type is not None:
            _body["PurchaseType"] = purchase_type
        if sequence_number is not None:
            _body["SequenceNumber"] = sequence_number
        if order_number is not None:
            _body["OrderNumber"] = order_number
        if supplier_id is not None:
            _body["SupplierId"] = supplier_id
        if non_domestic_supplier is not None:
            _body["NonDomesticSupplier"] = non_domestic_supplier
        if transmission is not None:
            _body["Transmission"] = transmission
        if return_card_data is not None:
            _body["ReturnCardData"] = return_card_data
        if customer_id is not None:
            _body["CustomerID"] = customer_id
        if association_id is not None:
            _body["AssociationId"] = association_id
        if label_ids is not None:
            _body["LabelIDs"] = label_ids
        if custom_parameters is not None:
            _body["CustomParameters"] = custom_parameters
        args.body = _body
        return args

    async def _acreate_lodged_card_oapg(
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
        Issue Lodged Card
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
            path_template='/api/v1/IssueCard/LodgedCard',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_card_create_lodged_card_request.serialize(body, content_type)
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


    def _create_lodged_card_oapg(
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
        Issue Lodged Card
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
            path_template='/api/v1/IssueCard/LodgedCard',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_card_create_lodged_card_request.serialize(body, content_type)
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


class CreateLodgedCardRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def acreate_lodged_card(
        self,
        merchant_guid: str,
        first_name: str,
        last_name: str,
        amount_limit: typing.Union[int, float],
        limit_window: str,
        phone: typing.Optional[str] = None,
        address1: typing.Optional[str] = None,
        address2: typing.Optional[str] = None,
        city: typing.Optional[str] = None,
        state: typing.Optional[str] = None,
        zip_code: typing.Optional[str] = None,
        country: typing.Optional[str] = None,
        usage_limit: typing.Optional[int] = None,
        expiration_date: typing.Optional[date] = None,
        terminate_date: typing.Optional[date] = None,
        purchase_type: typing.Optional[str] = None,
        sequence_number: typing.Optional[str] = None,
        order_number: typing.Optional[str] = None,
        supplier_id: typing.Optional[str] = None,
        non_domestic_supplier: typing.Optional[bool] = None,
        transmission: typing.Optional[CardCreateLodgedCardRequestTransmission] = None,
        return_card_data: typing.Optional[bool] = None,
        customer_id: typing.Optional[str] = None,
        association_id: typing.Optional[str] = None,
        label_ids: typing.Optional[CardCreateLodgedCardRequestLabelIDs] = None,
        custom_parameters: typing.Optional[CardCreateLodgedCardRequestCustomParameters] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._create_lodged_card_mapped_args(
            merchant_guid=merchant_guid,
            first_name=first_name,
            last_name=last_name,
            amount_limit=amount_limit,
            limit_window=limit_window,
            phone=phone,
            address1=address1,
            address2=address2,
            city=city,
            state=state,
            zip_code=zip_code,
            country=country,
            usage_limit=usage_limit,
            expiration_date=expiration_date,
            terminate_date=terminate_date,
            purchase_type=purchase_type,
            sequence_number=sequence_number,
            order_number=order_number,
            supplier_id=supplier_id,
            non_domestic_supplier=non_domestic_supplier,
            transmission=transmission,
            return_card_data=return_card_data,
            customer_id=customer_id,
            association_id=association_id,
            label_ids=label_ids,
            custom_parameters=custom_parameters,
        )
        return await self._acreate_lodged_card_oapg(
            body=args.body,
            **kwargs,
        )
    
    def create_lodged_card(
        self,
        merchant_guid: str,
        first_name: str,
        last_name: str,
        amount_limit: typing.Union[int, float],
        limit_window: str,
        phone: typing.Optional[str] = None,
        address1: typing.Optional[str] = None,
        address2: typing.Optional[str] = None,
        city: typing.Optional[str] = None,
        state: typing.Optional[str] = None,
        zip_code: typing.Optional[str] = None,
        country: typing.Optional[str] = None,
        usage_limit: typing.Optional[int] = None,
        expiration_date: typing.Optional[date] = None,
        terminate_date: typing.Optional[date] = None,
        purchase_type: typing.Optional[str] = None,
        sequence_number: typing.Optional[str] = None,
        order_number: typing.Optional[str] = None,
        supplier_id: typing.Optional[str] = None,
        non_domestic_supplier: typing.Optional[bool] = None,
        transmission: typing.Optional[CardCreateLodgedCardRequestTransmission] = None,
        return_card_data: typing.Optional[bool] = None,
        customer_id: typing.Optional[str] = None,
        association_id: typing.Optional[str] = None,
        label_ids: typing.Optional[CardCreateLodgedCardRequestLabelIDs] = None,
        custom_parameters: typing.Optional[CardCreateLodgedCardRequestCustomParameters] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._create_lodged_card_mapped_args(
            merchant_guid=merchant_guid,
            first_name=first_name,
            last_name=last_name,
            amount_limit=amount_limit,
            limit_window=limit_window,
            phone=phone,
            address1=address1,
            address2=address2,
            city=city,
            state=state,
            zip_code=zip_code,
            country=country,
            usage_limit=usage_limit,
            expiration_date=expiration_date,
            terminate_date=terminate_date,
            purchase_type=purchase_type,
            sequence_number=sequence_number,
            order_number=order_number,
            supplier_id=supplier_id,
            non_domestic_supplier=non_domestic_supplier,
            transmission=transmission,
            return_card_data=return_card_data,
            customer_id=customer_id,
            association_id=association_id,
            label_ids=label_ids,
            custom_parameters=custom_parameters,
        )
        return self._create_lodged_card_oapg(
            body=args.body,
        )

class CreateLodgedCard(BaseApi):

    async def acreate_lodged_card(
        self,
        merchant_guid: str,
        first_name: str,
        last_name: str,
        amount_limit: typing.Union[int, float],
        limit_window: str,
        phone: typing.Optional[str] = None,
        address1: typing.Optional[str] = None,
        address2: typing.Optional[str] = None,
        city: typing.Optional[str] = None,
        state: typing.Optional[str] = None,
        zip_code: typing.Optional[str] = None,
        country: typing.Optional[str] = None,
        usage_limit: typing.Optional[int] = None,
        expiration_date: typing.Optional[date] = None,
        terminate_date: typing.Optional[date] = None,
        purchase_type: typing.Optional[str] = None,
        sequence_number: typing.Optional[str] = None,
        order_number: typing.Optional[str] = None,
        supplier_id: typing.Optional[str] = None,
        non_domestic_supplier: typing.Optional[bool] = None,
        transmission: typing.Optional[CardCreateLodgedCardRequestTransmission] = None,
        return_card_data: typing.Optional[bool] = None,
        customer_id: typing.Optional[str] = None,
        association_id: typing.Optional[str] = None,
        label_ids: typing.Optional[CardCreateLodgedCardRequestLabelIDs] = None,
        custom_parameters: typing.Optional[CardCreateLodgedCardRequestCustomParameters] = None,
        validate: bool = False,
        **kwargs,
    ) -> CardCreateLodgedCardResponsePydantic:
        raw_response = await self.raw.acreate_lodged_card(
            merchant_guid=merchant_guid,
            first_name=first_name,
            last_name=last_name,
            amount_limit=amount_limit,
            limit_window=limit_window,
            phone=phone,
            address1=address1,
            address2=address2,
            city=city,
            state=state,
            zip_code=zip_code,
            country=country,
            usage_limit=usage_limit,
            expiration_date=expiration_date,
            terminate_date=terminate_date,
            purchase_type=purchase_type,
            sequence_number=sequence_number,
            order_number=order_number,
            supplier_id=supplier_id,
            non_domestic_supplier=non_domestic_supplier,
            transmission=transmission,
            return_card_data=return_card_data,
            customer_id=customer_id,
            association_id=association_id,
            label_ids=label_ids,
            custom_parameters=custom_parameters,
            **kwargs,
        )
        if validate:
            return RootModel[CardCreateLodgedCardResponsePydantic](raw_response.body).root
        return api_client.construct_model_instance(CardCreateLodgedCardResponsePydantic, raw_response.body)
    
    
    def create_lodged_card(
        self,
        merchant_guid: str,
        first_name: str,
        last_name: str,
        amount_limit: typing.Union[int, float],
        limit_window: str,
        phone: typing.Optional[str] = None,
        address1: typing.Optional[str] = None,
        address2: typing.Optional[str] = None,
        city: typing.Optional[str] = None,
        state: typing.Optional[str] = None,
        zip_code: typing.Optional[str] = None,
        country: typing.Optional[str] = None,
        usage_limit: typing.Optional[int] = None,
        expiration_date: typing.Optional[date] = None,
        terminate_date: typing.Optional[date] = None,
        purchase_type: typing.Optional[str] = None,
        sequence_number: typing.Optional[str] = None,
        order_number: typing.Optional[str] = None,
        supplier_id: typing.Optional[str] = None,
        non_domestic_supplier: typing.Optional[bool] = None,
        transmission: typing.Optional[CardCreateLodgedCardRequestTransmission] = None,
        return_card_data: typing.Optional[bool] = None,
        customer_id: typing.Optional[str] = None,
        association_id: typing.Optional[str] = None,
        label_ids: typing.Optional[CardCreateLodgedCardRequestLabelIDs] = None,
        custom_parameters: typing.Optional[CardCreateLodgedCardRequestCustomParameters] = None,
        validate: bool = False,
    ) -> CardCreateLodgedCardResponsePydantic:
        raw_response = self.raw.create_lodged_card(
            merchant_guid=merchant_guid,
            first_name=first_name,
            last_name=last_name,
            amount_limit=amount_limit,
            limit_window=limit_window,
            phone=phone,
            address1=address1,
            address2=address2,
            city=city,
            state=state,
            zip_code=zip_code,
            country=country,
            usage_limit=usage_limit,
            expiration_date=expiration_date,
            terminate_date=terminate_date,
            purchase_type=purchase_type,
            sequence_number=sequence_number,
            order_number=order_number,
            supplier_id=supplier_id,
            non_domestic_supplier=non_domestic_supplier,
            transmission=transmission,
            return_card_data=return_card_data,
            customer_id=customer_id,
            association_id=association_id,
            label_ids=label_ids,
            custom_parameters=custom_parameters,
        )
        if validate:
            return RootModel[CardCreateLodgedCardResponsePydantic](raw_response.body).root
        return api_client.construct_model_instance(CardCreateLodgedCardResponsePydantic, raw_response.body)


class ApiForpost(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def apost(
        self,
        merchant_guid: str,
        first_name: str,
        last_name: str,
        amount_limit: typing.Union[int, float],
        limit_window: str,
        phone: typing.Optional[str] = None,
        address1: typing.Optional[str] = None,
        address2: typing.Optional[str] = None,
        city: typing.Optional[str] = None,
        state: typing.Optional[str] = None,
        zip_code: typing.Optional[str] = None,
        country: typing.Optional[str] = None,
        usage_limit: typing.Optional[int] = None,
        expiration_date: typing.Optional[date] = None,
        terminate_date: typing.Optional[date] = None,
        purchase_type: typing.Optional[str] = None,
        sequence_number: typing.Optional[str] = None,
        order_number: typing.Optional[str] = None,
        supplier_id: typing.Optional[str] = None,
        non_domestic_supplier: typing.Optional[bool] = None,
        transmission: typing.Optional[CardCreateLodgedCardRequestTransmission] = None,
        return_card_data: typing.Optional[bool] = None,
        customer_id: typing.Optional[str] = None,
        association_id: typing.Optional[str] = None,
        label_ids: typing.Optional[CardCreateLodgedCardRequestLabelIDs] = None,
        custom_parameters: typing.Optional[CardCreateLodgedCardRequestCustomParameters] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._create_lodged_card_mapped_args(
            merchant_guid=merchant_guid,
            first_name=first_name,
            last_name=last_name,
            amount_limit=amount_limit,
            limit_window=limit_window,
            phone=phone,
            address1=address1,
            address2=address2,
            city=city,
            state=state,
            zip_code=zip_code,
            country=country,
            usage_limit=usage_limit,
            expiration_date=expiration_date,
            terminate_date=terminate_date,
            purchase_type=purchase_type,
            sequence_number=sequence_number,
            order_number=order_number,
            supplier_id=supplier_id,
            non_domestic_supplier=non_domestic_supplier,
            transmission=transmission,
            return_card_data=return_card_data,
            customer_id=customer_id,
            association_id=association_id,
            label_ids=label_ids,
            custom_parameters=custom_parameters,
        )
        return await self._acreate_lodged_card_oapg(
            body=args.body,
            **kwargs,
        )
    
    def post(
        self,
        merchant_guid: str,
        first_name: str,
        last_name: str,
        amount_limit: typing.Union[int, float],
        limit_window: str,
        phone: typing.Optional[str] = None,
        address1: typing.Optional[str] = None,
        address2: typing.Optional[str] = None,
        city: typing.Optional[str] = None,
        state: typing.Optional[str] = None,
        zip_code: typing.Optional[str] = None,
        country: typing.Optional[str] = None,
        usage_limit: typing.Optional[int] = None,
        expiration_date: typing.Optional[date] = None,
        terminate_date: typing.Optional[date] = None,
        purchase_type: typing.Optional[str] = None,
        sequence_number: typing.Optional[str] = None,
        order_number: typing.Optional[str] = None,
        supplier_id: typing.Optional[str] = None,
        non_domestic_supplier: typing.Optional[bool] = None,
        transmission: typing.Optional[CardCreateLodgedCardRequestTransmission] = None,
        return_card_data: typing.Optional[bool] = None,
        customer_id: typing.Optional[str] = None,
        association_id: typing.Optional[str] = None,
        label_ids: typing.Optional[CardCreateLodgedCardRequestLabelIDs] = None,
        custom_parameters: typing.Optional[CardCreateLodgedCardRequestCustomParameters] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._create_lodged_card_mapped_args(
            merchant_guid=merchant_guid,
            first_name=first_name,
            last_name=last_name,
            amount_limit=amount_limit,
            limit_window=limit_window,
            phone=phone,
            address1=address1,
            address2=address2,
            city=city,
            state=state,
            zip_code=zip_code,
            country=country,
            usage_limit=usage_limit,
            expiration_date=expiration_date,
            terminate_date=terminate_date,
            purchase_type=purchase_type,
            sequence_number=sequence_number,
            order_number=order_number,
            supplier_id=supplier_id,
            non_domestic_supplier=non_domestic_supplier,
            transmission=transmission,
            return_card_data=return_card_data,
            customer_id=customer_id,
            association_id=association_id,
            label_ids=label_ids,
            custom_parameters=custom_parameters,
        )
        return self._create_lodged_card_oapg(
            body=args.body,
        )

