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

from connex_pay_python_sdk.type.card_update_card_details_request_mid_blacklist import CardUpdateCardDetailsRequestMidBlacklist
from connex_pay_python_sdk.type.card_update_card_details_request_mid_whitelist import CardUpdateCardDetailsRequestMidWhitelist

class RequiredCardUpdateCardDetailsRequest(TypedDict):
    pass

class OptionalCardUpdateCardDetailsRequest(TypedDict, total=False):
    # Security Control: The industry where the virtual card will be utilized. For example, if value set to airline and the card is used at hotel, it will be declined. Available purchase type values are: '01' (Airline), '02' (Hotels and Resorts), '03' (Car Rental), '04' (Cable, Satellite, Television, and Radio Services),  '05' (Cruise Lines), '11' (Medical Services and Health Practitioners), '21' (Advertising Services), '22' (Misc Advertising and Business Services), '23' (Ticketing), '31' (Insurance Sales, Underwriting, and Premiums), '91' (Restaurants and Food Services), and '93' (Tax Payments). Leave this blank if you plan to utilize MID level controls.
    PurchaseType: str

    MIDWhitelist: CardUpdateCardDetailsRequestMidWhitelist

    MIDBlacklist: CardUpdateCardDetailsRequestMidBlacklist

    # Security Control: Maximum number of times the card may be authorized. The maximum allowed field value is 99, and if you do not provide a value the card will be considered unlimited. Authorization attempts exceeding the provided value will be declined. Even though a virtual card is often considered a “one-time-use” card, some suppliers may need to authorize a card multiple times (pre-authorizations, a purchase comprised of multiple tickets, etc.) and you may consider a value that is not overly restrictive to avoid unwanted declines.
    UsageLimit: int

    # Utilize the Association ID field to tie a virtual card to a sale or sales. For example, if you have several sales and one virtual card payment to a supplier, you can add association ID to the sales and the virtual card for downstream reporting.
    AssociationId: str

    # The TerminateDate (YYYY-MM-DD format) is the date the Virtual Credit Card will be terminated by ConnexPay. TerminateDate is different than ExpirationDate in that TerminateDate indicates the actual date the card will no longer be active.  The recommendation is to set the ExpirationDate one or two years in the future and set the TerminateDate just a day or two after the VCC is expected to be processed. If a terminate date is not indicated, the card will be inactivated as of the expiration date. Note, Returns can still be processed on terminated VCCs.
    TerminateDate: date

    # Security Control: Maximum dollar amount the card can be authorized and settled, which must be less than or equal to $1,000,000.00. The value must incorporate any anticipated overages such as currency conversion or taxes that a supplier may associate with the transaction. If a supplier attempts to authorize a card for more than the amount limit it will be declined.
    AmountLimit: typing.Union[int, float]

class CardUpdateCardDetailsRequest(RequiredCardUpdateCardDetailsRequest, OptionalCardUpdateCardDetailsRequest):
    pass
