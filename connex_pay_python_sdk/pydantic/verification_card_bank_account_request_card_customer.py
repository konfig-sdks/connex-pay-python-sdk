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


class VerificationCardBankAccountRequestCardCustomer(BaseModel):
    # Mandatory for ACH Sales.  Min Length = 2 Max Length = 30
    first_name: typing.Optional[str] = Field(None, alias='FirstName')

    # Mandatory for ACH Sales. Min Length = 2 Max Length = 30
    last_name: typing.Optional[str] = Field(None, alias='LastName')

    # Customer's phone number. Phone number up to 15 characters. Numbers and plus sign (+) allowed only.
    phone: typing.Optional[str] = Field(None, alias='Phone')

    # Customer's City
    city: typing.Optional[str] = Field(None, alias='City')

    # Customer's short name state.  The ISO 3166-2 CA and US state or province code of a customer. Length = 2.
    state: typing.Optional[str] = Field(None, alias='State')

    # Customer's country. The ISO country code of a customer’s country.  Length = 2
    country: typing.Optional[str] = Field(None, alias='Country')

    # Customer's valid email address which is available in various reports. It is critical that SendReceipt is set to FALSE so that ConnexPay does not send a receipt to the cardholder when the transaction is processed
    email: typing.Optional[str] = Field(None, alias='Email')

    # Customer billing address 1. It is strongly recommended to send this value in a card-not-present environment such that enhanced Address Validation (AVS) can be performed on transaction and the lowest possible interchange is received on transaction. Note: only the street number value portion of address is used for enhanced AVS check
    address1: typing.Optional[str] = Field(None, alias='Address1')

    # Customer billing address 2. It is strongly recommended to send this value in a card-not-present environment such that Address Validation (AVS) can be performed on transaction and the lowest possible interchange is received on transaction
    address2: typing.Optional[str] = Field(None, alias='Address2')

    # Customer billing postal code. It is strongly recommended to send this value in a card-not-present environment such that basic Address Validation (AVS) can be performed on transaction and the lowest possible interchange is received on transaction.  Only the a standard U.S. 5 digit zip code is eligible for basic AVS check. Min Length = 2 Max Length = 15. Alphanumerics and \"-\" allowed.
    zip: typing.Optional[str] = Field(None, alias='Zip')

    # Customer's date of birth. Allowed format: YYYY-MM-DD. For example: 2002-05-30
    date_of_birth: typing.Optional[date] = Field(None, alias='DateOfBirth')

    # Customer's driver license number.  Only letters, numbers and a hyphen is allowed
    drivers_license_number: typing.Optional[int] = Field(None, alias='DriversLicenseNumber')

    # Mandatory when DriverLicenseNumber is provided. Customer's driver license short name state. The ISO 3166-2 CA and US state or province code of a customer.  Length = 2
    drivers_license_state: typing.Optional[str] = Field(None, alias='DriversLicenseState')

    # Last 4 of Customer's Social Security Number
    s_s_n4: typing.Optional[int] = Field(None, alias='SSN4')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
