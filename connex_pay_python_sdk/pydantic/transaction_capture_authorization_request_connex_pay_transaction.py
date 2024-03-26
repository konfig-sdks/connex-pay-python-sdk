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


class TransactionCaptureAuthorizationRequestConnexPayTransaction(BaseModel):
    # This is the number of outbound payments that will be made to suppliers. If paying a single supplier the value is 1, if paying two suppliers the value is 2, etc.
    expected_payments: int = Field(alias='ExpectedPayments')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
