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

from connex_pay_python_sdk.type.authentication_acquire_client_authorization_response_card import AuthenticationAcquireClientAuthorizationResponseCard
from connex_pay_python_sdk.type.authentication_acquire_client_authorization_response_enhanced_data import AuthenticationAcquireClientAuthorizationResponseEnhancedData
from connex_pay_python_sdk.type.authentication_acquire_client_authorization_response_risk_response import AuthenticationAcquireClientAuthorizationResponseRiskResponse

class RequiredAuthenticationAcquireClientAuthorizationResponse(TypedDict):
    pass

class OptionalAuthenticationAcquireClientAuthorizationResponse(TypedDict, total=False):
    guid: str

    status: str

    batchStatus: str

    timeStamp: str

    amount: int

    effectiveAmount: int

    orderNumber: str

    deviceGuid: str

    cardDataSource: str

    customerID: str

    batchGuid: str

    sendReceipt: bool

    allowCardEmv: bool

    processorStatusCode: str

    processorResponseMessage: str

    wasProcessed: bool

    authCode: str

    refNumber: str

    invoiceNumber: str

    customerReceipt: str

    statementDescription: str

    enhancedData: AuthenticationAcquireClientAuthorizationResponseEnhancedData

    card: AuthenticationAcquireClientAuthorizationResponseCard

    addressVerificationCode: str

    addressVerificationResult: str

    cvvVerificationCode: str

    cvvVerificationResult: str

    riskResponse: AuthenticationAcquireClientAuthorizationResponseRiskResponse

    type: str

class AuthenticationAcquireClientAuthorizationResponse(RequiredAuthenticationAcquireClientAuthorizationResponse, OptionalAuthenticationAcquireClientAuthorizationResponse):
    pass
