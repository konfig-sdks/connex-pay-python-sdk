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


class RequiredValidationSearchVerifyOperationRequest(TypedDict):
    pass

class OptionalValidationSearchVerifyOperationRequest(TypedDict, total=False):
    # Merchant’s Guid.
    MerchantGuid: str

    # Card last four number.
    CardLastFour: str

    # Cardholder’s name. Providing information in this field allows a user of the ConnexPay portal to search for a transaction using the cardholder name.
    CardHolderName: str

    # Card Type.
    CardType: str

    # Verify’s TimeStamp From.
    TimeStampFrom: date

    # Verify’s TimeStamp To.
    TimeStampTo: date

    # Verify’s status.  Allowed values:  1. Transaction - Approved 2. Transaction - Declined 3. Transaction - Created - Local 4. Transaction - Created - Error: Processor not reached 5. Transaction - Processor Error 6. Transaction - Approved - Warning
    Status: str

class ValidationSearchVerifyOperationRequest(RequiredValidationSearchVerifyOperationRequest, OptionalValidationSearchVerifyOperationRequest):
    pass
