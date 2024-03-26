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


class RequiredSaleSearchSalesRequest(TypedDict):
    pass

class OptionalSaleSearchSalesRequest(TypedDict, total=False):
    # Merchant’s Guid.
    MerchantGuid: str

    # Amount of the transaction. Min. amt.: $0.50
    AmountFrom: typing.Union[int, float]

    # Amount of the transaction. Min. amt.: $0.50
    AmountTo: typing.Union[int, float]

    # Cardholder’s name.
    CardHolderName: str

    # Card last four number.
    CardLastFour: str

    # Card type.
    CardType: str

    # Sale’s InvoiceNumber.
    InvoiceNumber: int

    # Sale’s order number. Length = 17.
    OrderNumber: str

    # Sale’s order Date.
    OrderDateFrom: date

    # Sale’s order Date.
    OrderDateTo: date

    # Sale’s TimeStamp.
    TimeStampFrom: date

    # Sale’s TimeStamp.
    TimeStampTo: date

    # Sale’s status. Allowed values:  1. Transaction - Approved 2. Transaction - Declined 3. Transaction - Created - Local 4. Transaction - Created - Error: Processor not reached 5. Transaction - Processor Error 6. Transaction - Approved - Warning
    Status: str

    # Merchant Customer Id.
    MerchantCustomerId: str

    # Delayed Activation Sales to be included or not
    Activated: bool

    # Activation Start Date. This field is applicable only when Activated flag is set to true.
    ActivationDateFrom: date

    # Activation End Date. This field is applicable only when Activated flag is set to true.
    ActivationDateTo: date

class SaleSearchSalesRequest(RequiredSaleSearchSalesRequest, OptionalSaleSearchSalesRequest):
    pass
