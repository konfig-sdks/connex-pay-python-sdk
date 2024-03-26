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


class RequiredAuthenticationAcquireClientAuthorizationResponseEnhancedData(TypedDict):
    pass

class OptionalAuthenticationAcquireClientAuthorizationResponseEnhancedData(TypedDict, total=False):
    saleTax: int

    purchaseOrder: str

    additionalTaxDetailTaxCategory: str

    additionalTaxDetailTaxType: str

    additionalTaxDetailTaxAmount: int

    additionalTaxDetailTaxRate: typing.Union[int, float]

    shippingCharges: int

    dutyCharges: typing.Union[int, float]

    shipToZip: str

    shipFromZip: str

    destinationCountryCode: str

    customerVATNumber: str

    summaryCommodityCode: str

    vatInvoice: str

    orderDate: str

    supplierReferenceNumber: str

    customerRefID: str

    chargeDescriptor: str

    productName: str

    productCode: str

    price: int

    additionalAmount: typing.Union[int, float]

    additionalAmountType: str

class AuthenticationAcquireClientAuthorizationResponseEnhancedData(RequiredAuthenticationAcquireClientAuthorizationResponseEnhancedData, OptionalAuthenticationAcquireClientAuthorizationResponseEnhancedData):
    pass
