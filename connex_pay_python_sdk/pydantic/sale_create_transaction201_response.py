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

from connex_pay_python_sdk.pydantic.sale_create_transaction201_response_bank_account import SaleCreateTransaction201ResponseBankAccount
from connex_pay_python_sdk.pydantic.sale_create_transaction201_response_connex_pay_transaction import SaleCreateTransaction201ResponseConnexPayTransaction

class SaleCreateTransaction201Response(BaseModel):
    guid: typing.Optional[str] = Field(None, alias='guid')

    status: typing.Optional[str] = Field(None, alias='status')

    type: typing.Optional[str] = Field(None, alias='type')

    batch_status: typing.Optional[str] = Field(None, alias='batchStatus')

    time_stamp: typing.Optional[str] = Field(None, alias='timeStamp')

    device_guid: typing.Optional[str] = Field(None, alias='deviceGuid')

    amount: typing.Optional[typing.Union[int, float]] = Field(None, alias='amount')

    activated: typing.Optional[bool] = Field(None, alias='activated')

    tender_type: typing.Optional[str] = Field(None, alias='tenderType')

    effective_amount: typing.Optional[typing.Union[int, float]] = Field(None, alias='effectiveAmount')

    purchase_activation_date: typing.Optional[str] = Field(None, alias='purchaseActivationDate')

    order_number: typing.Optional[str] = Field(None, alias='orderNumber')

    card_data_source: typing.Optional[str] = Field(None, alias='cardDataSource')

    customer_i_d: typing.Optional[str] = Field(None, alias='customerID')

    batch_guid: typing.Optional[str] = Field(None, alias='batchGuid')

    connex_pay_transaction: typing.Optional[SaleCreateTransaction201ResponseConnexPayTransaction] = Field(None, alias='connexPayTransaction')

    risk_processing_only: typing.Optional[bool] = Field(None, alias='riskProcessingOnly')

    processor_status_code: typing.Optional[str] = Field(None, alias='processorStatusCode')

    processor_response_message: typing.Optional[str] = Field(None, alias='processorResponseMessage')

    was_processed: typing.Optional[bool] = Field(None, alias='wasProcessed')

    ref_number: typing.Optional[str] = Field(None, alias='refNumber')

    customer_receipt: typing.Optional[str] = Field(None, alias='customerReceipt')

    statement_description: typing.Optional[str] = Field(None, alias='statementDescription')

    generated_by: typing.Optional[str] = Field(None, alias='generatedBy')

    bank_account: typing.Optional[SaleCreateTransaction201ResponseBankAccount] = Field(None, alias='bankAccount')

    sequence_number: typing.Optional[str] = Field(None, alias='sequenceNumber')

    address_verification_result: typing.Optional[str] = Field(None, alias='addressVerificationResult')

    cvv_verification_result: typing.Optional[str] = Field(None, alias='cvvVerificationResult')

    wallet_provider: typing.Optional[int] = Field(None, alias='walletProvider')

    include_risk_analysis: typing.Optional[bool] = Field(None, alias='includeRiskAnalysis')

    is_from_issue_lite: typing.Optional[bool] = Field(None, alias='isFromIssueLite')

    remaining_amount: typing.Optional[typing.Union[int, float]] = Field(None, alias='remainingAmount')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
