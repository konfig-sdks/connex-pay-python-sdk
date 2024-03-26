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


class VerificationCardBankAccountRequestCardThreeDs(BaseModel):
    secure_code: typing.Optional[str] = Field(None, alias='SecureCode')

    # Cardholder authentication verification value
    cavv: typing.Optional[str] = Field(None, alias='Cavv')

    # Version of 3DS being used
    version: typing.Optional[str] = Field(None, alias='Version')

    # Unique identifier provided by the card scheme as part of 3D Secure authentication.
    directory_server_transaction_i_d: typing.Optional[str] = Field(None, alias='DirectoryServerTransactionID')

    # Unique Identifier provided by the Access Control Server of the Card Issuer.
    acs_transaction_id: typing.Optional[str] = Field(None, alias='AcsTransactionId')

    # Displays the Electronic Commerce Indicator (ECI). The ECI indicates the security level of the payment information provided to the merchant. A value of 0, 1 or 2 is a Mastercard transaction. A value of 5, 6 or 7 is a Visa, American Express, Diners or Discover card.
    e_c_i: typing.Optional[str] = Field(None, alias='ECI')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
