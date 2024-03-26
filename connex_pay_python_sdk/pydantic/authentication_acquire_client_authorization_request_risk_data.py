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

from connex_pay_python_sdk.pydantic.authentication_acquire_client_authorization_request_risk_data_flight_data import AuthenticationAcquireClientAuthorizationRequestRiskDataFlightData
from connex_pay_python_sdk.pydantic.authentication_acquire_client_authorization_request_risk_data_flight_passengers import AuthenticationAcquireClientAuthorizationRequestRiskDataFlightPassengers

class AuthenticationAcquireClientAuthorizationRequestRiskData(BaseModel):
    # If you are using Kount's Device Data Collector, this would be the SessionId from that particular session. Do not include this property if not using Kount's Device Data Collector.
    session_id: typing.Optional[str] = Field(None, alias='SessionId')

    # This is the name of the individual making the purchase i.e. cardholder who may or may not also be the customer. This value is submitted in multiple integration points for different purposes. This value/object is specific to fraud mitigation. Note: for airline ticket purchases this value may or may not be the same as the passenger. Max Length = 64
    name: typing.Optional[str] = Field(None, alias='Name')

    # Cardholder gender. \"M\" or \"F\".
    gender: typing.Optional[str] = Field(None, alias='Gender')

    # Cardholder date of birth
    date_of_birth: typing.Optional[str] = Field(None, alias='DateOfBirth')

    # Phone number associated with cardholder making purchase. Cardholder billing phone number. More specifically, can be used for rule creation or additional identity validation using the White Pages Pro add on option.  Phone number up to 15 characters. Numbers and plus sign (+) allowed only.
    billing_phone_number: typing.Optional[str] = Field(None, alias='BillingPhoneNumber')

    # Cardholder billing address 1. This value is used in risk analysis and decisioning. More specifically, can be used for rule creation or additional identity validation using the White Pages Pro add on option.
    billing_address1: typing.Optional[str] = Field(None, alias='BillingAddress1')

    # Cardholder billing address 2. This value is used in risk analysis and decisioning. More specifically, can be used for rule creation or additional identity validation using the White Pages Pro add on option.
    billing_address2: typing.Optional[str] = Field(None, alias='BillingAddress2')

    # Cardholder billing city. This value is used in risk analysis and decisioning. More specifically, can be used for rule creation or additional identity validation using the White Pages Pro add on option.
    billing_city: typing.Optional[str] = Field(None, alias='BillingCity')

    # Cardholder billing state. This value is used in risk analysis and decisioning. More specifically, can be used for rule creation or additional identity validation using the White Pages Pro add on option.
    billing_state: typing.Optional[str] = Field(None, alias='BillingState')

    # Cardholder billing postal code. This value is used in risk analysis and decisioning. More specifically, can be used for rule creation or additional identity validation using the White Pages Pro add on option. Max Length = 15. Alphanumerics and \"-\" allowed.
    billing_postal_code: typing.Optional[str] = Field(None, alias='BillingPostalCode')

    # Cardholder billing country code. This value is used in risk analysis and decisioning. More specifically, can be used for rule creation or additional identity validation using the White Pages Pro add on option.  Length = 2.
    billing_country_code: typing.Optional[str] = Field(None, alias='BillingCountryCode')

    # Cardholder's valid email address. This value is used in risk analysis and decisioning. More specifically, can be used for rule creation or additional identity validation using the White Pages Pro add on option.
    email: typing.Optional[str] = Field(None, alias='Email')

    # Generalized description of the item added passed as plain text. This could be flight, tour, hotel, etc. (This is part of shopping cart information in Kount Console). Each transaction submitted for risk analysis and decisioning must be submitted with one shopping cart item.
    product_type: typing.Optional[str] = Field(None, alias='ProductType')

    # Attribute for a specific description of the item being purchased i.e. airline ticket. This information is general shopping cart information that describes the type of item being purchased. ConnexPay suggests clients submitted a high level description such as Flight, Hotel, Car Rental, etc... and leverage custom parameters to submit more detailed information that can be used for rule creation and transaction decisioning.
    product_description: typing.Optional[str] = Field(None, alias='ProductDescription')

    # Typically the SKU for an item passed as plain text. This information is general shopping cart information to provide secondary detail to the ProductDesc above. ConnexPay suggests clients submit a high level description such as One Way, Round Trip, Seven Nights, etc...and several customer parameters to submit more detailed information that can be used for rule creation and transaction decisioning.  Field is required by Kount therefore some value must be submitted. Alphanumeric.
    product_item: typing.Optional[str] = Field(None, alias='ProductItem')

    # Quantity of the item being purchased in the shopping cart. This is just a general quantity field.
    product_quantity: typing.Optional[int] = Field(None, alias='ProductQuantity')

    # Price per unit item, displayed in lowest currency factor - expressed in cents. Example: 42400 (which is $424.00).
    product_price: typing.Optional[int] = Field(None, alias='ProductPrice')

    # Transaction ID within client environment associated with the order. The value is searchable and reportable in the Kount portal. This value may be sent in multiple instances of the integration for multiple purposes. Customers in the travel space often send the Record Locator/PNR in this field.  The maximum length is 32 alpha-numeric characters and allows dashes ( - ).
    order_number: typing.Optional[str] = Field(None, alias='OrderNumber')

    # Transaction ID within client environment associated with the customer. This value acts as a secondary identifier in conjunction with OrderNumber. The value is searchable and reportable in the Kount portal. This value may be sent in multiple times within the integration for multiple purposes.  The maximum length is 32 characters.
    seller_id: typing.Optional[str] = Field(None, alias='SellerId')

    flight_data: typing.Optional[AuthenticationAcquireClientAuthorizationRequestRiskDataFlightData] = Field(None, alias='FlightData')

    flight_passengers: typing.Optional[AuthenticationAcquireClientAuthorizationRequestRiskDataFlightPassengers] = Field(None, alias='FlightPassengers')

    # Custom Parameters. Array.
    custom_parameters: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = Field(None, alias='CustomParameters')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
