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

from connex_pay_python_sdk.type.verification_card_bank_account_request_card_customer import VerificationCardBankAccountRequestCardCustomer
from connex_pay_python_sdk.type.verification_card_bank_account_request_card_three_ds import VerificationCardBankAccountRequestCardThreeDs

class RequiredVerificationCardBankAccountRequestCard(TypedDict):
    pass

class OptionalVerificationCardBankAccountRequestCard(TypedDict, total=False):
    # Mandatory if Guid field is not provided. Card number.  Must be 16 characters. (example: 4532538795426624) or token (example: FfL7exC7Xe2y6624)
    CardNumber: str

    # Cardholder's name. Providing information in this field allows a user of the ConnexPay portal to search for a transaction using the cardholder name
    CardHolderName: str

    # The three or four digit CVV code at the back side of the credit and debit card. This value is required for all card-not-present processing environments
    Cvv2: str

    # Optional with Token. Card's expiry date in the YYMM format
    ExpirationDate: date

    # Guid is the unique identifier for a card info generated by Connexpay upon previous Sale creation. Create Sale API will accept either card info or Guid, but not both
    Guid: str

    # Flagging a transaction as \"IsRecurring\": true allows a recurring sale to be submitted without a valid CVV code, which is only intended for scenarios where you might be storing card data to perform repeated payments on the same card, such as a monthly subscriptions. Typically IsRecurring can be defaulted to False.
    IsRecurring: bool

    Customer: VerificationCardBankAccountRequestCardCustomer

    ThreeDS: VerificationCardBankAccountRequestCardThreeDs

class VerificationCardBankAccountRequestCard(RequiredVerificationCardBankAccountRequestCard, OptionalVerificationCardBankAccountRequestCard):
    pass
