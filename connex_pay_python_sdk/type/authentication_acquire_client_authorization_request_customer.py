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


class RequiredAuthenticationAcquireClientAuthorizationRequestCustomer(TypedDict):
    pass

class OptionalAuthenticationAcquireClientAuthorizationRequestCustomer(TypedDict, total=False):
    # Mandatory for ACH Sales.  Min Length = 2 Max Length = 30
    FirstName: str

    # Mandatory for ACH Sales. Min Length = 2 Max Length = 30
    LastName: str

    # Customer's phone number. Phone number up to 15 characters. Numbers and plus sign (+) allowed only.
    Phone: str

    # Customer's City
    City: str

    # Customer's short name state.  The ISO 3166-2 CA and US state or province code of a customer. Length = 2.
    State: str

    # Customer's country. The ISO country code of a customer’s country.  Length = 2
    Country: str

    # Customer's valid email address which is available in various reports. It is critical that SendReceipt is set to FALSE so that ConnexPay does not send a receipt to the cardholder when the transaction is processed
    Email: str

    # Customer billing address 1. It is strongly recommended to send this value in a card-not-present environment such that enhanced Address Validation (AVS) can be performed on transaction and the lowest possible interchange is received on transaction. Note: only the street number value portion of address is used for enhanced AVS check
    Address1: str

    # Customer billing address 2. It is strongly recommended to send this value in a card-not-present environment such that Address Validation (AVS) can be performed on transaction and the lowest possible interchange is received on transaction
    Address2: str

    # Customer billing postal code. It is strongly recommended to send this value in a card-not-present environment such that basic Address Validation (AVS) can be performed on transaction and the lowest possible interchange is received on transaction.  Only the a standard U.S. 5 digit zip code is eligible for basic AVS check. Min Length = 2 Max Length = 15. Alphanumerics and \"-\" allowed.
    Zip: str

    # Customer's date of birth. Allowed format: YYYY-MM-DD. For example: 2002-05-30
    DateOfBirth: date

    # Customer's driver license number.  Only letters, numbers and a hyphen is allowed
    DriversLicenseNumber: int

    # Mandatory when DriverLicenseNumber is provided. Customer's driver license short name state. The ISO 3166-2 CA and US state or province code of a customer.  Length = 2
    DriversLicenseState: str

    # Last 4 of Customer's Social Security Number
    SSN4: int

class AuthenticationAcquireClientAuthorizationRequestCustomer(RequiredAuthenticationAcquireClientAuthorizationRequestCustomer, OptionalAuthenticationAcquireClientAuthorizationRequestCustomer):
    pass
