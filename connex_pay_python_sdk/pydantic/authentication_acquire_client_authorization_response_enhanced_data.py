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


class AuthenticationAcquireClientAuthorizationResponseEnhancedData(BaseModel):
    sale_tax: typing.Optional[int] = Field(None, alias='saleTax')

    purchase_order: typing.Optional[str] = Field(None, alias='purchaseOrder')

    additional_tax_detail_tax_category: typing.Optional[str] = Field(None, alias='additionalTaxDetailTaxCategory')

    additional_tax_detail_tax_type: typing.Optional[str] = Field(None, alias='additionalTaxDetailTaxType')

    additional_tax_detail_tax_amount: typing.Optional[int] = Field(None, alias='additionalTaxDetailTaxAmount')

    additional_tax_detail_tax_rate: typing.Optional[typing.Union[int, float]] = Field(None, alias='additionalTaxDetailTaxRate')

    shipping_charges: typing.Optional[int] = Field(None, alias='shippingCharges')

    duty_charges: typing.Optional[typing.Union[int, float]] = Field(None, alias='dutyCharges')

    ship_to_zip: typing.Optional[str] = Field(None, alias='shipToZip')

    ship_from_zip: typing.Optional[str] = Field(None, alias='shipFromZip')

    destination_country_code: typing.Optional[str] = Field(None, alias='destinationCountryCode')

    customer_v_a_t_number: typing.Optional[str] = Field(None, alias='customerVATNumber')

    summary_commodity_code: typing.Optional[str] = Field(None, alias='summaryCommodityCode')

    vat_invoice: typing.Optional[str] = Field(None, alias='vatInvoice')

    order_date: typing.Optional[str] = Field(None, alias='orderDate')

    supplier_reference_number: typing.Optional[str] = Field(None, alias='supplierReferenceNumber')

    customer_ref_i_d: typing.Optional[str] = Field(None, alias='customerRefID')

    charge_descriptor: typing.Optional[str] = Field(None, alias='chargeDescriptor')

    product_name: typing.Optional[str] = Field(None, alias='productName')

    product_code: typing.Optional[str] = Field(None, alias='productCode')

    price: typing.Optional[int] = Field(None, alias='price')

    additional_amount: typing.Optional[typing.Union[int, float]] = Field(None, alias='additionalAmount')

    additional_amount_type: typing.Optional[str] = Field(None, alias='additionalAmountType')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
