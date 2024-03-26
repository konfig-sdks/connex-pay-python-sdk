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


class AchCreateCreditPaymentResponse(BaseModel):
    description: typing.Optional[str] = Field(None, alias='description')

    merchant_id: typing.Optional[str] = Field(None, alias='merchantId')

    incoming_transaction_code: typing.Optional[str] = Field(None, alias='incomingTransactionCode')

    payment_id: typing.Optional[str] = Field(None, alias='paymentId')

    is_credit: typing.Optional[bool] = Field(None, alias='isCredit')

    amount: typing.Optional[int] = Field(None, alias='amount')

    payee_name: typing.Optional[str] = Field(None, alias='payeeName')

    payment_status: typing.Optional[str] = Field(None, alias='paymentStatus')

    schedule_date: typing.Optional[str] = Field(None, alias='scheduleDate')

    receipt_date: typing.Optional[str] = Field(None, alias='receiptDate')

    processing_date: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = Field(None, alias='processingDate')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
