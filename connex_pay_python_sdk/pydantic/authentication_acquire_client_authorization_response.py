# coding: utf-8

"""
    ConnexPay Reporting API

    REST API for retrieving reporting data. Currently Daily Accounting data only.

    The version of the OpenAPI document: v1
    Created by: https://docs.connexpay.com
"""

from datetime import datetime, date
import typing
from enum import Enum
from typing_extensions import TypedDict, Literal, TYPE_CHECKING
from pydantic import BaseModel, Field, RootModel, ConfigDict

from connex_pay_python_sdk.pydantic.authentication_acquire_client_authorization_response_card import AuthenticationAcquireClientAuthorizationResponseCard
from connex_pay_python_sdk.pydantic.authentication_acquire_client_authorization_response_enhanced_data import AuthenticationAcquireClientAuthorizationResponseEnhancedData
from connex_pay_python_sdk.pydantic.authentication_acquire_client_authorization_response_risk_response import AuthenticationAcquireClientAuthorizationResponseRiskResponse

class AuthenticationAcquireClientAuthorizationResponse(BaseModel):
    guid: typing.Optional[str] = Field(None, alias='guid')

    status: typing.Optional[str] = Field(None, alias='status')

    batch_status: typing.Optional[str] = Field(None, alias='batchStatus')

    time_stamp: typing.Optional[str] = Field(None, alias='timeStamp')

    amount: typing.Optional[int] = Field(None, alias='amount')

    effective_amount: typing.Optional[int] = Field(None, alias='effectiveAmount')

    order_number: typing.Optional[str] = Field(None, alias='orderNumber')

    device_guid: typing.Optional[str] = Field(None, alias='deviceGuid')

    card_data_source: typing.Optional[str] = Field(None, alias='cardDataSource')

    customer_i_d: typing.Optional[str] = Field(None, alias='customerID')

    batch_guid: typing.Optional[str] = Field(None, alias='batchGuid')

    send_receipt: typing.Optional[bool] = Field(None, alias='sendReceipt')

    allow_card_emv: typing.Optional[bool] = Field(None, alias='allowCardEmv')

    processor_status_code: typing.Optional[str] = Field(None, alias='processorStatusCode')

    processor_response_message: typing.Optional[str] = Field(None, alias='processorResponseMessage')

    was_processed: typing.Optional[bool] = Field(None, alias='wasProcessed')

    auth_code: typing.Optional[str] = Field(None, alias='authCode')

    ref_number: typing.Optional[str] = Field(None, alias='refNumber')

    invoice_number: typing.Optional[str] = Field(None, alias='invoiceNumber')

    customer_receipt: typing.Optional[str] = Field(None, alias='customerReceipt')

    statement_description: typing.Optional[str] = Field(None, alias='statementDescription')

    enhanced_data: typing.Optional[AuthenticationAcquireClientAuthorizationResponseEnhancedData] = Field(None, alias='enhancedData')

    card: typing.Optional[AuthenticationAcquireClientAuthorizationResponseCard] = Field(None, alias='card')

    address_verification_code: typing.Optional[str] = Field(None, alias='addressVerificationCode')

    address_verification_result: typing.Optional[str] = Field(None, alias='addressVerificationResult')

    cvv_verification_code: typing.Optional[str] = Field(None, alias='cvvVerificationCode')

    cvv_verification_result: typing.Optional[str] = Field(None, alias='cvvVerificationResult')

    risk_response: typing.Optional[AuthenticationAcquireClientAuthorizationResponseRiskResponse] = Field(None, alias='riskResponse')

    type: typing.Optional[str] = Field(None, alias='type')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
