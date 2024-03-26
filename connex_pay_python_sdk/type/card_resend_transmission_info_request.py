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

from connex_pay_python_sdk.type.card_resend_transmission_info_request_transmission_methods import CardResendTransmissionInfoRequestTransmissionMethods

class RequiredCardResendTransmissionInfoRequest(TypedDict):
    TransmissionMethods: CardResendTransmissionInfoRequestTransmissionMethods

class OptionalCardResendTransmissionInfoRequest(TypedDict, total=False):
    # Mandatory when transmission is Email. Otherwise don't include. This is the email address of the intended recipient. 255 char max.
    EmailRecipient: str

    # This is the phone number that should display on the virtual card and is the number that should be used if the link has expired. Up to 15 characters. Numbers and plus sign (+) allowed only.
    MerchantPhoneNumber: str

    # For email transmissions, this will be the email address that populates the ‘reply to’ section of the email message. Do not include this parameter on other transmission method types. 255 char max.
    EmailFrom: str

    # A descriptive name of the email or fax recipient. Does not apply to the Link transmission method type. 255 char max
    RecipientName: str

    # High-level subject line description of the transmission contents. Does not apply to the Link transmission method type. 255 char max.
    Subject: str

    # The message body of the email or fax. Does not apply to the Link transmission method type. 1024 char max.
    Message: str

    # The number of days after card issuance until the link to the VC expires. Range: 1-999 days.
    DaysToExpire: int

    # Mandatory for fax transmission. This can be the client name or fax number the fax is coming from that populates the ‘FaxFrom’ section of the fax. 255 char max.
    FaxFrom: str

    # Mandatory for fax transmissions.  The fax number of the intended recipient.
    FaxRecipient: str

class CardResendTransmissionInfoRequest(RequiredCardResendTransmissionInfoRequest, OptionalCardResendTransmissionInfoRequest):
    pass
