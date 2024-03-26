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

from connex_pay_python_sdk.type.transaction_capture_authorization_response_sale_card import TransactionCaptureAuthorizationResponseSaleCard
from connex_pay_python_sdk.type.transaction_capture_authorization_response_sale_connex_pay_transaction import TransactionCaptureAuthorizationResponseSaleConnexPayTransaction
from connex_pay_python_sdk.type.transaction_capture_authorization_response_sale_risk_response import TransactionCaptureAuthorizationResponseSaleRiskResponse

class RequiredTransactionCaptureAuthorizationResponseSale(TypedDict):
    pass

class OptionalTransactionCaptureAuthorizationResponseSale(TypedDict, total=False):
    guid: str

    status: str

    type: str

    batchStatus: str

    timeStamp: str

    deviceGuid: str

    amount: int

    activated: bool

    tenderType: str

    effectiveAmount: int

    riskResponse: TransactionCaptureAuthorizationResponseSaleRiskResponse

    orderNumber: str

    cardDataSource: str

    customerID: str

    batchGuid: str

    connexPayTransaction: TransactionCaptureAuthorizationResponseSaleConnexPayTransaction

    processorStatusCode: str

    processorResponseMessage: str

    wasProcessed: bool

    authCode: str

    refNumber: str

    customerReceipt: str

    statementDescription: str

    generatedBy: str

    card: TransactionCaptureAuthorizationResponseSaleCard

    addressVerificationCode: str

    addressVerificationResult: str

    cvvVerificationCode: str

    cvvVerificationResult: str

class TransactionCaptureAuthorizationResponseSale(RequiredTransactionCaptureAuthorizationResponseSale, OptionalTransactionCaptureAuthorizationResponseSale):
    pass
