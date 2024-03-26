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

from connex_pay_python_sdk.type.card_create_lodged_card_request_transmission_transmission_methods import CardCreateLodgedCardRequestTransmissionTransmissionMethods

class RequiredCardCreateLodgedCardRequestTransmission(TypedDict):
    pass

class OptionalCardCreateLodgedCardRequestTransmission(TypedDict, total=False):
    TransmissionMethods: CardCreateLodgedCardRequestTransmissionTransmissionMethods

    # Mandatory for email transmission. The email address of the intended recipient. 255 char max.
    EmailRecipient: str

    # This is the phone number that should display on the virtual card and is the number that should be used if the link has expired. Up to 15 characters. Numbers and plus sign (+) allowed only.
    MerchantPhoneNumber: str

    # Mandatory for email transmission. This will be the email address that populates the ‘reply to’ section of the email message. 255 char max.
    EmailFrom: str

    # Mandatory for email or fax transmission. A descriptive name of the email or fax recipient. 255 char max
    RecipientName: str

    # Mandatory for email or fax transmission. High-level subject line description of the transmission contents. 255 char max.
    Subject: str

    # Mandatory for email or fax transmission. The message body of the email or fax. 1024 char max.
    Message: str

    # Mandatory for email transmission. The number of days after card issuance until link to VC expires. Range: 1-999 days.
    DaysToExpire: str

    # Mandatory for fax transmission. This can be the client name or fax number the fax is coming from that populates the ‘FaxFrom’ section of the fax. 255 char max.
    FaxFrom: str

    # Mandatory for fax transmissions.  The fax number of the intended recipient.
    FaxRecipient: str

class CardCreateLodgedCardRequestTransmission(RequiredCardCreateLodgedCardRequestTransmission, OptionalCardCreateLodgedCardRequestTransmission):
    pass
