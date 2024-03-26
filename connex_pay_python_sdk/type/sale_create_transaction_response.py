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

from connex_pay_python_sdk.type.sale_create_transaction_response_card import SaleCreateTransactionResponseCard
from connex_pay_python_sdk.type.sale_create_transaction_response_connex_pay_transaction import SaleCreateTransactionResponseConnexPayTransaction
from connex_pay_python_sdk.type.sale_create_transaction_response_label_ids import SaleCreateTransactionResponseLabelIds
from connex_pay_python_sdk.type.sale_create_transaction_response_risk_response import SaleCreateTransactionResponseRiskResponse

class RequiredSaleCreateTransactionResponse(TypedDict):
    pass

class OptionalSaleCreateTransactionResponse(TypedDict, total=False):
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

    riskResponse: SaleCreateTransactionResponseRiskResponse

    orderNumber: str

    cardDataSource: str

    customerID: str

    batchGuid: str

    connexPayTransaction: SaleCreateTransactionResponseConnexPayTransaction

    associationId: str

    processorStatusCode: str

    processorResponseMessage: str

    wasProcessed: bool

    authCode: str

    refNumber: str

    customerReceipt: str

    statementDescription: str

    generatedBy: str

    Card: SaleCreateTransactionResponseCard

    addressVerificationResult: str

    cvvVerificationCode: str

    cvvVerificationResult: str

    cavvResponseCode: str

    walletProvider: int

    isFromIssueLite: bool

    labelIds: SaleCreateTransactionResponseLabelIds

    remainingAmount: int

class SaleCreateTransactionResponse(RequiredSaleCreateTransactionResponse, OptionalSaleCreateTransactionResponse):
    pass
