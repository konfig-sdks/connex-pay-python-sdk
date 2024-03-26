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

from connex_pay_python_sdk.pydantic.card_resend_transmission_info_request_transmission_methods import CardResendTransmissionInfoRequestTransmissionMethods

class CardResendTransmissionInfoRequest(BaseModel):
    transmission_methods: CardResendTransmissionInfoRequestTransmissionMethods = Field(alias='TransmissionMethods')

    # Mandatory when transmission is Email. Otherwise don't include. This is the email address of the intended recipient. 255 char max.
    email_recipient: typing.Optional[str] = Field(None, alias='EmailRecipient')

    # This is the phone number that should display on the virtual card and is the number that should be used if the link has expired. Up to 15 characters. Numbers and plus sign (+) allowed only.
    merchant_phone_number: typing.Optional[str] = Field(None, alias='MerchantPhoneNumber')

    # For email transmissions, this will be the email address that populates the ‘reply to’ section of the email message. Do not include this parameter on other transmission method types. 255 char max.
    email_from: typing.Optional[str] = Field(None, alias='EmailFrom')

    # A descriptive name of the email or fax recipient. Does not apply to the Link transmission method type. 255 char max
    recipient_name: typing.Optional[str] = Field(None, alias='RecipientName')

    # High-level subject line description of the transmission contents. Does not apply to the Link transmission method type. 255 char max.
    subject: typing.Optional[str] = Field(None, alias='Subject')

    # The message body of the email or fax. Does not apply to the Link transmission method type. 1024 char max.
    message: typing.Optional[str] = Field(None, alias='Message')

    # The number of days after card issuance until the link to the VC expires. Range: 1-999 days.
    days_to_expire: typing.Optional[int] = Field(None, alias='DaysToExpire')

    # Mandatory for fax transmission. This can be the client name or fax number the fax is coming from that populates the ‘FaxFrom’ section of the fax. 255 char max.
    fax_from: typing.Optional[str] = Field(None, alias='FaxFrom')

    # Mandatory for fax transmissions.  The fax number of the intended recipient.
    fax_recipient: typing.Optional[str] = Field(None, alias='FaxRecipient')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
