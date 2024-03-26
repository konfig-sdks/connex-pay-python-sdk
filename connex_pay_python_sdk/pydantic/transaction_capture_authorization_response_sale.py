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

from connex_pay_python_sdk.pydantic.transaction_capture_authorization_response_sale_card import TransactionCaptureAuthorizationResponseSaleCard
from connex_pay_python_sdk.pydantic.transaction_capture_authorization_response_sale_connex_pay_transaction import TransactionCaptureAuthorizationResponseSaleConnexPayTransaction
from connex_pay_python_sdk.pydantic.transaction_capture_authorization_response_sale_risk_response import TransactionCaptureAuthorizationResponseSaleRiskResponse

class TransactionCaptureAuthorizationResponseSale(BaseModel):
    guid: typing.Optional[str] = Field(None, alias='guid')

    status: typing.Optional[str] = Field(None, alias='status')

    type: typing.Optional[str] = Field(None, alias='type')

    batch_status: typing.Optional[str] = Field(None, alias='batchStatus')

    time_stamp: typing.Optional[str] = Field(None, alias='timeStamp')

    device_guid: typing.Optional[str] = Field(None, alias='deviceGuid')

    amount: typing.Optional[int] = Field(None, alias='amount')

    activated: typing.Optional[bool] = Field(None, alias='activated')

    tender_type: typing.Optional[str] = Field(None, alias='tenderType')

    effective_amount: typing.Optional[int] = Field(None, alias='effectiveAmount')

    risk_response: typing.Optional[TransactionCaptureAuthorizationResponseSaleRiskResponse] = Field(None, alias='riskResponse')

    order_number: typing.Optional[str] = Field(None, alias='orderNumber')

    card_data_source: typing.Optional[str] = Field(None, alias='cardDataSource')

    customer_i_d: typing.Optional[str] = Field(None, alias='customerID')

    batch_guid: typing.Optional[str] = Field(None, alias='batchGuid')

    connex_pay_transaction: typing.Optional[TransactionCaptureAuthorizationResponseSaleConnexPayTransaction] = Field(None, alias='connexPayTransaction')

    processor_status_code: typing.Optional[str] = Field(None, alias='processorStatusCode')

    processor_response_message: typing.Optional[str] = Field(None, alias='processorResponseMessage')

    was_processed: typing.Optional[bool] = Field(None, alias='wasProcessed')

    auth_code: typing.Optional[str] = Field(None, alias='authCode')

    ref_number: typing.Optional[str] = Field(None, alias='refNumber')

    customer_receipt: typing.Optional[str] = Field(None, alias='customerReceipt')

    statement_description: typing.Optional[str] = Field(None, alias='statementDescription')

    generated_by: typing.Optional[str] = Field(None, alias='generatedBy')

    card: typing.Optional[TransactionCaptureAuthorizationResponseSaleCard] = Field(None, alias='card')

    address_verification_code: typing.Optional[str] = Field(None, alias='addressVerificationCode')

    address_verification_result: typing.Optional[str] = Field(None, alias='addressVerificationResult')

    cvv_verification_code: typing.Optional[str] = Field(None, alias='cvvVerificationCode')

    cvv_verification_result: typing.Optional[str] = Field(None, alias='cvvVerificationResult')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
