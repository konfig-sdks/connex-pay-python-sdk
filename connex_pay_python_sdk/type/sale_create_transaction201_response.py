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

from connex_pay_python_sdk.type.sale_create_transaction201_response_bank_account import SaleCreateTransaction201ResponseBankAccount
from connex_pay_python_sdk.type.sale_create_transaction201_response_connex_pay_transaction import SaleCreateTransaction201ResponseConnexPayTransaction

class RequiredSaleCreateTransaction201Response(TypedDict):
    pass

class OptionalSaleCreateTransaction201Response(TypedDict, total=False):
    guid: str

    status: str

    type: str

    batchStatus: str

    timeStamp: str

    deviceGuid: str

    amount: typing.Union[int, float]

    activated: bool

    tenderType: str

    effectiveAmount: typing.Union[int, float]

    purchaseActivationDate: str

    orderNumber: str

    cardDataSource: str

    customerID: str

    batchGuid: str

    connexPayTransaction: SaleCreateTransaction201ResponseConnexPayTransaction

    riskProcessingOnly: bool

    processorStatusCode: str

    processorResponseMessage: str

    wasProcessed: bool

    refNumber: str

    customerReceipt: str

    statementDescription: str

    generatedBy: str

    bankAccount: SaleCreateTransaction201ResponseBankAccount

    sequenceNumber: str

    addressVerificationResult: str

    cvvVerificationResult: str

    walletProvider: int

    includeRiskAnalysis: bool

    isFromIssueLite: bool

    remainingAmount: typing.Union[int, float]

class SaleCreateTransaction201Response(RequiredSaleCreateTransaction201Response, OptionalSaleCreateTransaction201Response):
    pass
