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

from connex_pay_python_sdk.model.sale_create_transaction_request_risk_data import SaleCreateTransactionRequestRiskData as SaleCreateTransactionRequestRiskDataSchema
from connex_pay_python_sdk.model.sale_create_transaction201_response import SaleCreateTransaction201Response as SaleCreateTransaction201ResponseSchema
from connex_pay_python_sdk.model.sale_create_transaction_request_custom_parameters import SaleCreateTransactionRequestCustomParameters as SaleCreateTransactionRequestCustomParametersSchema
from connex_pay_python_sdk.model.sale_create_transaction_response import SaleCreateTransactionResponse as SaleCreateTransactionResponseSchema
from connex_pay_python_sdk.model.sale_create_transaction_request import SaleCreateTransactionRequest as SaleCreateTransactionRequestSchema
from connex_pay_python_sdk.model.sale_create_transaction_request_card import SaleCreateTransactionRequestCard as SaleCreateTransactionRequestCardSchema
from connex_pay_python_sdk.model.sale_create_transaction_request_connex_pay_transaction import SaleCreateTransactionRequestConnexPayTransaction as SaleCreateTransactionRequestConnexPayTransactionSchema
from connex_pay_python_sdk.model.sale_create_transaction202_response import SaleCreateTransaction202Response as SaleCreateTransaction202ResponseSchema
from connex_pay_python_sdk.model.sale_create_transaction_request_label_ids import SaleCreateTransactionRequestLabelIDs as SaleCreateTransactionRequestLabelIDsSchema
from connex_pay_python_sdk.model.sale_create_transaction_request_browser_data import SaleCreateTransactionRequestBrowserData as SaleCreateTransactionRequestBrowserDataSchema
from connex_pay_python_sdk.model.sale_create_transaction_request_bank_account import SaleCreateTransactionRequestBankAccount as SaleCreateTransactionRequestBankAccountSchema
from connex_pay_python_sdk.model.sale_create_transaction_request_customer import SaleCreateTransactionRequestCustomer as SaleCreateTransactionRequestCustomerSchema
from connex_pay_python_sdk.model.sale_create_transaction_request_enhanced_data import SaleCreateTransactionRequestEnhancedData as SaleCreateTransactionRequestEnhancedDataSchema

from connex_pay_python_sdk.type.sale_create_transaction_request import SaleCreateTransactionRequest
from connex_pay_python_sdk.type.sale_create_transaction_request_customer import SaleCreateTransactionRequestCustomer
from connex_pay_python_sdk.type.sale_create_transaction_request_connex_pay_transaction import SaleCreateTransactionRequestConnexPayTransaction
from connex_pay_python_sdk.type.sale_create_transaction_request_risk_data import SaleCreateTransactionRequestRiskData
from connex_pay_python_sdk.type.sale_create_transaction202_response import SaleCreateTransaction202Response
from connex_pay_python_sdk.type.sale_create_transaction_request_browser_data import SaleCreateTransactionRequestBrowserData
from connex_pay_python_sdk.type.sale_create_transaction201_response import SaleCreateTransaction201Response
from connex_pay_python_sdk.type.sale_create_transaction_request_card import SaleCreateTransactionRequestCard
from connex_pay_python_sdk.type.sale_create_transaction_request_enhanced_data import SaleCreateTransactionRequestEnhancedData
from connex_pay_python_sdk.type.sale_create_transaction_request_label_ids import SaleCreateTransactionRequestLabelIDs
from connex_pay_python_sdk.type.sale_create_transaction_response import SaleCreateTransactionResponse
from connex_pay_python_sdk.type.sale_create_transaction_request_custom_parameters import SaleCreateTransactionRequestCustomParameters
from connex_pay_python_sdk.type.sale_create_transaction_request_bank_account import SaleCreateTransactionRequestBankAccount

from ...api_client import Dictionary
from connex_pay_python_sdk.pydantic.sale_create_transaction_request import SaleCreateTransactionRequest as SaleCreateTransactionRequestPydantic
from connex_pay_python_sdk.pydantic.sale_create_transaction_request_custom_parameters import SaleCreateTransactionRequestCustomParameters as SaleCreateTransactionRequestCustomParametersPydantic
from connex_pay_python_sdk.pydantic.sale_create_transaction_request_label_ids import SaleCreateTransactionRequestLabelIDs as SaleCreateTransactionRequestLabelIDsPydantic
from connex_pay_python_sdk.pydantic.sale_create_transaction_request_bank_account import SaleCreateTransactionRequestBankAccount as SaleCreateTransactionRequestBankAccountPydantic
from connex_pay_python_sdk.pydantic.sale_create_transaction201_response import SaleCreateTransaction201Response as SaleCreateTransaction201ResponsePydantic
from connex_pay_python_sdk.pydantic.sale_create_transaction_response import SaleCreateTransactionResponse as SaleCreateTransactionResponsePydantic
from connex_pay_python_sdk.pydantic.sale_create_transaction_request_customer import SaleCreateTransactionRequestCustomer as SaleCreateTransactionRequestCustomerPydantic
from connex_pay_python_sdk.pydantic.sale_create_transaction_request_browser_data import SaleCreateTransactionRequestBrowserData as SaleCreateTransactionRequestBrowserDataPydantic
from connex_pay_python_sdk.pydantic.sale_create_transaction_request_card import SaleCreateTransactionRequestCard as SaleCreateTransactionRequestCardPydantic
from connex_pay_python_sdk.pydantic.sale_create_transaction_request_enhanced_data import SaleCreateTransactionRequestEnhancedData as SaleCreateTransactionRequestEnhancedDataPydantic
from connex_pay_python_sdk.pydantic.sale_create_transaction_request_connex_pay_transaction import SaleCreateTransactionRequestConnexPayTransaction as SaleCreateTransactionRequestConnexPayTransactionPydantic
from connex_pay_python_sdk.pydantic.sale_create_transaction_request_risk_data import SaleCreateTransactionRequestRiskData as SaleCreateTransactionRequestRiskDataPydantic
from connex_pay_python_sdk.pydantic.sale_create_transaction202_response import SaleCreateTransaction202Response as SaleCreateTransaction202ResponsePydantic

from . import path

# body param
SchemaForRequestBodyApplicationJson = SaleCreateTransactionRequestSchema


request_body_sale_create_transaction_request = api_client.RequestBody(
    content={
        'application/json': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationJson),
    },
)
_auth = [
    'sec0',
]
SchemaFor200ResponseBodyApplicationJson = SaleCreateTransactionResponseSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: SaleCreateTransactionResponse


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: SaleCreateTransactionResponse


_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
    response_cls_async=ApiResponseFor200Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationJson),
    },
)
SchemaFor201ResponseBodyApplicationJson = SaleCreateTransaction201ResponseSchema


@dataclass
class ApiResponseFor201(api_client.ApiResponse):
    body: SaleCreateTransaction201Response


@dataclass
class ApiResponseFor201Async(api_client.AsyncApiResponse):
    body: SaleCreateTransaction201Response


_response_for_201 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor201,
    response_cls_async=ApiResponseFor201Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor201ResponseBodyApplicationJson),
    },
)
SchemaFor202ResponseBodyApplicationJson = SaleCreateTransaction202ResponseSchema


@dataclass
class ApiResponseFor202(api_client.ApiResponse):
    body: SaleCreateTransaction202Response


@dataclass
class ApiResponseFor202Async(api_client.AsyncApiResponse):
    body: SaleCreateTransaction202Response


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
    '201': _response_for_201,
    '202': _response_for_202,
}
_all_accept_content_types = (
    'application/json',
)


class BaseApi(api_client.Api):

    def _create_transaction_mapped_args(
        self,
        device_guid: str,
        amount: typing.Union[int, float],
        connex_pay_transaction: SaleCreateTransactionRequestConnexPayTransaction,
        risk_data: SaleCreateTransactionRequestRiskData,
        tender_type: typing.Optional[str] = None,
        sequence_number: typing.Optional[str] = None,
        order_number: typing.Optional[str] = None,
        send_receipt: typing.Optional[bool] = None,
        risk_processing_only: typing.Optional[bool] = None,
        statement_description: typing.Optional[str] = None,
        customer_id: typing.Optional[str] = None,
        activation_date: typing.Optional[date] = None,
        request_ip: typing.Optional[str] = None,
        card: typing.Optional[SaleCreateTransactionRequestCard] = None,
        bank_account: typing.Optional[SaleCreateTransactionRequestBankAccount] = None,
        customer: typing.Optional[SaleCreateTransactionRequestCustomer] = None,
        enhanced_data: typing.Optional[SaleCreateTransactionRequestEnhancedData] = None,
        association_id: typing.Optional[str] = None,
        custom_parameters: typing.Optional[SaleCreateTransactionRequestCustomParameters] = None,
        label_ids: typing.Optional[SaleCreateTransactionRequestLabelIDs] = None,
        browser_data: typing.Optional[SaleCreateTransactionRequestBrowserData] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _body = {}
        if device_guid is not None:
            _body["DeviceGuid"] = device_guid
        if amount is not None:
            _body["Amount"] = amount
        if tender_type is not None:
            _body["TenderType"] = tender_type
        if sequence_number is not None:
            _body["SequenceNumber"] = sequence_number
        if order_number is not None:
            _body["OrderNumber"] = order_number
        if send_receipt is not None:
            _body["SendReceipt"] = send_receipt
        if risk_processing_only is not None:
            _body["RiskProcessingOnly"] = risk_processing_only
        if statement_description is not None:
            _body["StatementDescription"] = statement_description
        if customer_id is not None:
            _body["CustomerID"] = customer_id
        if activation_date is not None:
            _body["ActivationDate"] = activation_date
        if request_ip is not None:
            _body["RequestIp"] = request_ip
        if connex_pay_transaction is not None:
            _body["ConnexPayTransaction"] = connex_pay_transaction
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
            _body["AssociationId"] = association_id
        if custom_parameters is not None:
            _body["CustomParameters"] = custom_parameters
        if label_ids is not None:
            _body["LabelIDs"] = label_ids
        if browser_data is not None:
            _body["BrowserData"] = browser_data
        args.body = _body
        return args

    async def _acreate_transaction_oapg(
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
        ApiResponseFor201Async,
        ApiResponseFor202Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        """
        Create Sale
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
            path_template='/api/v1/sales',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_sale_create_transaction_request.serialize(body, content_type)
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


    def _create_transaction_oapg(
        self,
        body: typing.Any = None,
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'application/json',
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseFor200,
        ApiResponseFor201,
        ApiResponseFor202,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        Create Sale
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
            path_template='/api/v1/sales',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_sale_create_transaction_request.serialize(body, content_type)
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


class CreateTransactionRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def acreate_transaction(
        self,
        device_guid: str,
        amount: typing.Union[int, float],
        connex_pay_transaction: SaleCreateTransactionRequestConnexPayTransaction,
        risk_data: SaleCreateTransactionRequestRiskData,
        tender_type: typing.Optional[str] = None,
        sequence_number: typing.Optional[str] = None,
        order_number: typing.Optional[str] = None,
        send_receipt: typing.Optional[bool] = None,
        risk_processing_only: typing.Optional[bool] = None,
        statement_description: typing.Optional[str] = None,
        customer_id: typing.Optional[str] = None,
        activation_date: typing.Optional[date] = None,
        request_ip: typing.Optional[str] = None,
        card: typing.Optional[SaleCreateTransactionRequestCard] = None,
        bank_account: typing.Optional[SaleCreateTransactionRequestBankAccount] = None,
        customer: typing.Optional[SaleCreateTransactionRequestCustomer] = None,
        enhanced_data: typing.Optional[SaleCreateTransactionRequestEnhancedData] = None,
        association_id: typing.Optional[str] = None,
        custom_parameters: typing.Optional[SaleCreateTransactionRequestCustomParameters] = None,
        label_ids: typing.Optional[SaleCreateTransactionRequestLabelIDs] = None,
        browser_data: typing.Optional[SaleCreateTransactionRequestBrowserData] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        ApiResponseFor201Async,
        ApiResponseFor202Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._create_transaction_mapped_args(
            device_guid=device_guid,
            amount=amount,
            connex_pay_transaction=connex_pay_transaction,
            risk_data=risk_data,
            tender_type=tender_type,
            sequence_number=sequence_number,
            order_number=order_number,
            send_receipt=send_receipt,
            risk_processing_only=risk_processing_only,
            statement_description=statement_description,
            customer_id=customer_id,
            activation_date=activation_date,
            request_ip=request_ip,
            card=card,
            bank_account=bank_account,
            customer=customer,
            enhanced_data=enhanced_data,
            association_id=association_id,
            custom_parameters=custom_parameters,
            label_ids=label_ids,
            browser_data=browser_data,
        )
        return await self._acreate_transaction_oapg(
            body=args.body,
            **kwargs,
        )
    
    def create_transaction(
        self,
        device_guid: str,
        amount: typing.Union[int, float],
        connex_pay_transaction: SaleCreateTransactionRequestConnexPayTransaction,
        risk_data: SaleCreateTransactionRequestRiskData,
        tender_type: typing.Optional[str] = None,
        sequence_number: typing.Optional[str] = None,
        order_number: typing.Optional[str] = None,
        send_receipt: typing.Optional[bool] = None,
        risk_processing_only: typing.Optional[bool] = None,
        statement_description: typing.Optional[str] = None,
        customer_id: typing.Optional[str] = None,
        activation_date: typing.Optional[date] = None,
        request_ip: typing.Optional[str] = None,
        card: typing.Optional[SaleCreateTransactionRequestCard] = None,
        bank_account: typing.Optional[SaleCreateTransactionRequestBankAccount] = None,
        customer: typing.Optional[SaleCreateTransactionRequestCustomer] = None,
        enhanced_data: typing.Optional[SaleCreateTransactionRequestEnhancedData] = None,
        association_id: typing.Optional[str] = None,
        custom_parameters: typing.Optional[SaleCreateTransactionRequestCustomParameters] = None,
        label_ids: typing.Optional[SaleCreateTransactionRequestLabelIDs] = None,
        browser_data: typing.Optional[SaleCreateTransactionRequestBrowserData] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        ApiResponseFor201,
        ApiResponseFor202,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._create_transaction_mapped_args(
            device_guid=device_guid,
            amount=amount,
            connex_pay_transaction=connex_pay_transaction,
            risk_data=risk_data,
            tender_type=tender_type,
            sequence_number=sequence_number,
            order_number=order_number,
            send_receipt=send_receipt,
            risk_processing_only=risk_processing_only,
            statement_description=statement_description,
            customer_id=customer_id,
            activation_date=activation_date,
            request_ip=request_ip,
            card=card,
            bank_account=bank_account,
            customer=customer,
            enhanced_data=enhanced_data,
            association_id=association_id,
            custom_parameters=custom_parameters,
            label_ids=label_ids,
            browser_data=browser_data,
        )
        return self._create_transaction_oapg(
            body=args.body,
        )

class CreateTransaction(BaseApi):

    async def acreate_transaction(
        self,
        device_guid: str,
        amount: typing.Union[int, float],
        connex_pay_transaction: SaleCreateTransactionRequestConnexPayTransaction,
        risk_data: SaleCreateTransactionRequestRiskData,
        tender_type: typing.Optional[str] = None,
        sequence_number: typing.Optional[str] = None,
        order_number: typing.Optional[str] = None,
        send_receipt: typing.Optional[bool] = None,
        risk_processing_only: typing.Optional[bool] = None,
        statement_description: typing.Optional[str] = None,
        customer_id: typing.Optional[str] = None,
        activation_date: typing.Optional[date] = None,
        request_ip: typing.Optional[str] = None,
        card: typing.Optional[SaleCreateTransactionRequestCard] = None,
        bank_account: typing.Optional[SaleCreateTransactionRequestBankAccount] = None,
        customer: typing.Optional[SaleCreateTransactionRequestCustomer] = None,
        enhanced_data: typing.Optional[SaleCreateTransactionRequestEnhancedData] = None,
        association_id: typing.Optional[str] = None,
        custom_parameters: typing.Optional[SaleCreateTransactionRequestCustomParameters] = None,
        label_ids: typing.Optional[SaleCreateTransactionRequestLabelIDs] = None,
        browser_data: typing.Optional[SaleCreateTransactionRequestBrowserData] = None,
        validate: bool = False,
        **kwargs,
    ) -> SaleCreateTransactionResponsePydantic:
        raw_response = await self.raw.acreate_transaction(
            device_guid=device_guid,
            amount=amount,
            connex_pay_transaction=connex_pay_transaction,
            risk_data=risk_data,
            tender_type=tender_type,
            sequence_number=sequence_number,
            order_number=order_number,
            send_receipt=send_receipt,
            risk_processing_only=risk_processing_only,
            statement_description=statement_description,
            customer_id=customer_id,
            activation_date=activation_date,
            request_ip=request_ip,
            card=card,
            bank_account=bank_account,
            customer=customer,
            enhanced_data=enhanced_data,
            association_id=association_id,
            custom_parameters=custom_parameters,
            label_ids=label_ids,
            browser_data=browser_data,
            **kwargs,
        )
        if validate:
            return SaleCreateTransactionResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(SaleCreateTransactionResponsePydantic, raw_response.body)
    
    
    def create_transaction(
        self,
        device_guid: str,
        amount: typing.Union[int, float],
        connex_pay_transaction: SaleCreateTransactionRequestConnexPayTransaction,
        risk_data: SaleCreateTransactionRequestRiskData,
        tender_type: typing.Optional[str] = None,
        sequence_number: typing.Optional[str] = None,
        order_number: typing.Optional[str] = None,
        send_receipt: typing.Optional[bool] = None,
        risk_processing_only: typing.Optional[bool] = None,
        statement_description: typing.Optional[str] = None,
        customer_id: typing.Optional[str] = None,
        activation_date: typing.Optional[date] = None,
        request_ip: typing.Optional[str] = None,
        card: typing.Optional[SaleCreateTransactionRequestCard] = None,
        bank_account: typing.Optional[SaleCreateTransactionRequestBankAccount] = None,
        customer: typing.Optional[SaleCreateTransactionRequestCustomer] = None,
        enhanced_data: typing.Optional[SaleCreateTransactionRequestEnhancedData] = None,
        association_id: typing.Optional[str] = None,
        custom_parameters: typing.Optional[SaleCreateTransactionRequestCustomParameters] = None,
        label_ids: typing.Optional[SaleCreateTransactionRequestLabelIDs] = None,
        browser_data: typing.Optional[SaleCreateTransactionRequestBrowserData] = None,
        validate: bool = False,
    ) -> SaleCreateTransactionResponsePydantic:
        raw_response = self.raw.create_transaction(
            device_guid=device_guid,
            amount=amount,
            connex_pay_transaction=connex_pay_transaction,
            risk_data=risk_data,
            tender_type=tender_type,
            sequence_number=sequence_number,
            order_number=order_number,
            send_receipt=send_receipt,
            risk_processing_only=risk_processing_only,
            statement_description=statement_description,
            customer_id=customer_id,
            activation_date=activation_date,
            request_ip=request_ip,
            card=card,
            bank_account=bank_account,
            customer=customer,
            enhanced_data=enhanced_data,
            association_id=association_id,
            custom_parameters=custom_parameters,
            label_ids=label_ids,
            browser_data=browser_data,
        )
        if validate:
            return SaleCreateTransactionResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(SaleCreateTransactionResponsePydantic, raw_response.body)


class ApiForpost(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def apost(
        self,
        device_guid: str,
        amount: typing.Union[int, float],
        connex_pay_transaction: SaleCreateTransactionRequestConnexPayTransaction,
        risk_data: SaleCreateTransactionRequestRiskData,
        tender_type: typing.Optional[str] = None,
        sequence_number: typing.Optional[str] = None,
        order_number: typing.Optional[str] = None,
        send_receipt: typing.Optional[bool] = None,
        risk_processing_only: typing.Optional[bool] = None,
        statement_description: typing.Optional[str] = None,
        customer_id: typing.Optional[str] = None,
        activation_date: typing.Optional[date] = None,
        request_ip: typing.Optional[str] = None,
        card: typing.Optional[SaleCreateTransactionRequestCard] = None,
        bank_account: typing.Optional[SaleCreateTransactionRequestBankAccount] = None,
        customer: typing.Optional[SaleCreateTransactionRequestCustomer] = None,
        enhanced_data: typing.Optional[SaleCreateTransactionRequestEnhancedData] = None,
        association_id: typing.Optional[str] = None,
        custom_parameters: typing.Optional[SaleCreateTransactionRequestCustomParameters] = None,
        label_ids: typing.Optional[SaleCreateTransactionRequestLabelIDs] = None,
        browser_data: typing.Optional[SaleCreateTransactionRequestBrowserData] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        ApiResponseFor201Async,
        ApiResponseFor202Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._create_transaction_mapped_args(
            device_guid=device_guid,
            amount=amount,
            connex_pay_transaction=connex_pay_transaction,
            risk_data=risk_data,
            tender_type=tender_type,
            sequence_number=sequence_number,
            order_number=order_number,
            send_receipt=send_receipt,
            risk_processing_only=risk_processing_only,
            statement_description=statement_description,
            customer_id=customer_id,
            activation_date=activation_date,
            request_ip=request_ip,
            card=card,
            bank_account=bank_account,
            customer=customer,
            enhanced_data=enhanced_data,
            association_id=association_id,
            custom_parameters=custom_parameters,
            label_ids=label_ids,
            browser_data=browser_data,
        )
        return await self._acreate_transaction_oapg(
            body=args.body,
            **kwargs,
        )
    
    def post(
        self,
        device_guid: str,
        amount: typing.Union[int, float],
        connex_pay_transaction: SaleCreateTransactionRequestConnexPayTransaction,
        risk_data: SaleCreateTransactionRequestRiskData,
        tender_type: typing.Optional[str] = None,
        sequence_number: typing.Optional[str] = None,
        order_number: typing.Optional[str] = None,
        send_receipt: typing.Optional[bool] = None,
        risk_processing_only: typing.Optional[bool] = None,
        statement_description: typing.Optional[str] = None,
        customer_id: typing.Optional[str] = None,
        activation_date: typing.Optional[date] = None,
        request_ip: typing.Optional[str] = None,
        card: typing.Optional[SaleCreateTransactionRequestCard] = None,
        bank_account: typing.Optional[SaleCreateTransactionRequestBankAccount] = None,
        customer: typing.Optional[SaleCreateTransactionRequestCustomer] = None,
        enhanced_data: typing.Optional[SaleCreateTransactionRequestEnhancedData] = None,
        association_id: typing.Optional[str] = None,
        custom_parameters: typing.Optional[SaleCreateTransactionRequestCustomParameters] = None,
        label_ids: typing.Optional[SaleCreateTransactionRequestLabelIDs] = None,
        browser_data: typing.Optional[SaleCreateTransactionRequestBrowserData] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        ApiResponseFor201,
        ApiResponseFor202,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._create_transaction_mapped_args(
            device_guid=device_guid,
            amount=amount,
            connex_pay_transaction=connex_pay_transaction,
            risk_data=risk_data,
            tender_type=tender_type,
            sequence_number=sequence_number,
            order_number=order_number,
            send_receipt=send_receipt,
            risk_processing_only=risk_processing_only,
            statement_description=statement_description,
            customer_id=customer_id,
            activation_date=activation_date,
            request_ip=request_ip,
            card=card,
            bank_account=bank_account,
            customer=customer,
            enhanced_data=enhanced_data,
            association_id=association_id,
            custom_parameters=custom_parameters,
            label_ids=label_ids,
            browser_data=browser_data,
        )
        return self._create_transaction_oapg(
            body=args.body,
        )

