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


class RequiredAuthenticationAcquireClientAuthorizationRequestCardThreeDs(TypedDict):
    pass

class OptionalAuthenticationAcquireClientAuthorizationRequestCardThreeDs(TypedDict, total=False):
    SecureCode: str

    # Cardholder authentication verification value
    Cavv: str

    # Version of 3DS being used
    Version: str

    # Unique identifier provided by the card scheme as part of 3D Secure authentication.
    DirectoryServerTransactionID: str

    # Unique Identifier provided by the Access Control Server of the Card Issuer.
    AcsTransactionId: str

    # Displays the Electronic Commerce Indicator (ECI). The ECI indicates the security level of the payment information provided to the merchant. A value of 0, 1 or 2 is a Mastercard transaction. A value of 5, 6 or 7 is a Visa, American Express, Diners or Discover card.
    ECI: str

class AuthenticationAcquireClientAuthorizationRequestCardThreeDs(RequiredAuthenticationAcquireClientAuthorizationRequestCardThreeDs, OptionalAuthenticationAcquireClientAuthorizationRequestCardThreeDs):
    pass
