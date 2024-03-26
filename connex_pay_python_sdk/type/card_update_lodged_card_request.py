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


class RequiredCardUpdateLodgedCardRequest(TypedDict):
    pass

class OptionalCardUpdateLodgedCardRequest(TypedDict, total=False):
    # Security Control: Maximum number of times the card may be authorized. This is used in conjunction with the Limit Window; for example, if you specify a Usage Limit of 4 and a Limit Window of Monthly, the card can be authorized up to 4 times per month. The maximum allowed field value is 99, and if you do not provide a value the card will be considered unlimited. Authorization attempts exceeding the provided value will be declined.
    UsageLimit: int

    # Security Control: Maximum dollar amount the card can be authorized and settled, which must be less than or equal to $1,000,000.00. The value must incorporate any anticipated overages such as currency conversion or taxes that a supplier may associate with the transaction. If a supplier attempts to authorize a card for more than the amount limit it will be declined.
    AmountLimit: typing.Union[int, float]

    # This is the time period that both the UsageLimit and the AmountLimit applies. Options are: Day, Week, Month, Lifetime. For example AmountLimit is $500 and LimitWindow is \"Week\" then the card can be approved for $500 per week.
    LimitWindow: str

    # Security Control: The industry where the virtual card will be utilized. For example, if value set to airline and the card is used at hotel, it will be declined. Available purchase type values are: '01' (Airline), '02' (Hotels and Resorts), '03' (Car Rental), '04' (Cable, Satellite, Television, and Radio Services),  '05' (Cruise Lines), '11' (Medical Services and Health Practitioners), '21' (Advertising Services), '22' (Misc Advertising and Business Services), '23' (Ticketing), '31' (Insurance Sales, Underwriting, and Premiums), '91' (Restaurants and Food Services), and '93' (Tax Payments). Leave this blank if you plan to utilize MID level controls.
    PurchaseType: str

    # True activates a lodged card. False suspends a lodged card.
    Activated: bool

    # Utilize the Association ID field to tie a lodged card to a sale or sales. For example, if you have several sales and one lodged card payment to a supplier, you can add association ID to the sales and the lodged card for downstream reporting.
    AssociationId: str

    # The TerminateDate (YYYY-MM-DD format) is the date the Lodged Card will be terminated by ConnexPay. TerminateDate is different than ExpirationDate in that TerminateDate indicates the actual date the card will no longer be active.  The recommendation is to set the ExpirationDate one or two years in the future and set the TerminateDate just a day or two after the Lodged Card is expected to be processed. If a terminate date is not indicated, the card will be inactivated as of the expiration date. Note, Returns can still be processed on terminated Lodged Cards.
    TerminateDate: date

class CardUpdateLodgedCardRequest(RequiredCardUpdateLodgedCardRequest, OptionalCardUpdateLodgedCardRequest):
    pass
