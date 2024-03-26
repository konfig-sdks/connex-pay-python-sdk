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

from connex_pay_python_sdk.type.card_create_lodged_card_request_custom_parameters import CardCreateLodgedCardRequestCustomParameters
from connex_pay_python_sdk.type.card_create_lodged_card_request_label_ids import CardCreateLodgedCardRequestLabelIDs
from connex_pay_python_sdk.type.card_create_lodged_card_request_transmission import CardCreateLodgedCardRequestTransmission

class RequiredCardCreateLodgedCardRequest(TypedDict):
    # Merchant's guid. Application level value that indicates a virtual card is being requested for clients account. Value provided by ConnexPay.
    MerchantGuid: str

    # Cardholder's first name. This is the first name placed on the virtual card provided to the supplier. The value is also searchable in the ConnexPay portal.
    FirstName: str

    # Cardholder's last name. This is the last name placed on the virtual card provided to the supplier. The value is also searchable in the ConnexPay portal.
    LastName: str

    # Security Control: Maximum dollar amount the card can be authorized and settled, which must be less than or equal to $1,000,000.00. The value must incorporate any anticipated overages such as currency conversion or taxes that a supplier may associate with the transaction. If a supplier attempts to authorize a card for more than the amount limit it will be declined.
    AmountLimit: typing.Union[int, float]

    # This is the time period that both the UsageLimit and the AmountLimit applies. Options are: Day, Week, Month, Lifetime. For example AmountLimit is $500 and LimitWindow is \"Week\" then the card can be approved for $500 per week.
    LimitWindow: str

class OptionalCardCreateLodgedCardRequest(TypedDict, total=False):
    # Cardholder's phone number. Phone number up to 20 character string, numbers and plus sign (+) allowed only. Telephone number of the user (including area code), prepended by the + symbol and the 1- to 3-digit country calling code. Do not include hyphens, spaces, or parentheses.
    Phone: str

    # Cardholder's address line 1. The street number is used by the supplier when submitting the transaction to perform an AVS check. Alphanumerics and [,.-'] are allowed.
    Address1: str

    # Cardholder's address line 2. Alphanumerics and [,.-'] are allowed.
    Address2: str

    # Cardholder's city.
    City: str

    # Cardholder's short name state.  The ISO 3166-2 CA and US state or province code of a user. Length = 2. If a non U.S. or Canadian value is submitted the virtual card request will not be processed and an error response returned.
    State: str

    # Cardholder's zipcode. The zip code is used by the supplier when submitting the transaction to perform an AVS check.  The Zipcode must be between 1 and 10 characters long, only numbers and letters are allowed.
    ZipCode: str

    # Cardholder's country.  Only alpha-2 digit country code allowed and numbers are not allowed.  See ISO-3166 country list of Alpha-2 country codes (https://www.iso.org/obp/ui/) .
    Country: str

    # Security Control: Maximum number of times the card may be authorized. This is used in conjunction with the Limit Window: for example, if you specify a Usage Limit of 4 and a Limit Window of Monthly, the card can be authorized up to 4 times per month. The maximum allowed field value is 99, and if you do not provide a value the card will be considered unlimited. Authorization attempts exceeding the provided value will be declined.
    UsageLimit: int

    # The ExpirationDate (YYYY-MM-DD) is the date to be provided to the supplier as the actual expiration date for the virtual card. The recommendation is to set the ExpirationDate one or two years in the future and set the TerminateDate just a day or two after the VCC is expected to be processed to avoid acceptance issues.  The expiration date cannot be more than 36 months in the future. If an expiration date is not provided, the expiration will default to issue date plus three years. For cards issued outside of the US/Canada, the expiration date will default to issue date plus three years and can not be overwritten - even if this parameter is included in the request. Note, Returns can still be processed on expired or terminated VCCs.
    ExpirationDate: date

    # The TerminateDate (YYYY-MM-DD format) is the date the Virtual Credit Card will be terminated by ConnexPay. TerminateDate is different than ExpirationDate in that TerminateDate indicates the actual date the card will no longer be active.  The recommendation is to set the ExpirationDate one or two years in the future and set the TerminateDate just a day or two after the VCC is expected to be processed. If a terminate date is not indicated, the card will be inactivated as of the expiration date. Note, Returns can still be processed on terminated VCCs.
    TerminateDate: date

    # Security Control: The industry where the virtual card will be utilized. For example, if value set to airline and the card is used at hotel, it will be declined. Available purchase type values are: '01' (Airline), '02' (Hotels and Resorts), '03' (Car Rental), '04' (Cable, Satellite, Television, and Radio Services),  '05' (Cruise Lines), '11' (Medical Services and Health Practitioners), '21' (Advertising Services), '22' (Misc Advertising and Business Services), '23' (Ticketing), '31' (Insurance Sales, Underwriting, and Premiums), '91' (Restaurants and Food Services), and '93' (Tax Payments). Leave this blank if you plan to utilize MID level controls.
    PurchaseType: str

    # Transaction sequence number within client environment. Provide a unique SequenceNumber for each new request. If the same value is sent within 30 minutes it will be considered a duplicate request. Note: value is not searchable or reportable in ConnexPay portal.  Alphanumeric.
    SequenceNumber: str

    # This is the most common number you'll see throughout the ConnexPay Portal.  Transaction ID within client environment associated with the order. The value is searchable and reportable in the ConnexPay portal. This value may be sent in multiple instances of the integration for multiple purposes. Customers in the travel space often send the Record Locator/PNR in this field.  The maximum length is 50 alpha-numeric characters and allows dashes and spaces (\"-\", \" \").
    OrderNumber: str

    # The SupplierId is used to assist with Intelligent Routing functionality. In many cases, a Lodged Card is used at several different suppliers. In this case, there may be no reason to include SupplierId. However, if the Lodged Card will be used at a single supplier, we recommend sending in the SupplierId to assist with acceptance and rebate. The field accepts up to 100 alpha-numeric characters.
    SupplierId: str

    # We can issue the “Global VCC” if the Supplier accepting that VCC has an overseas merchant account. This is an optional field. Indicating true will result in issuing this Global VCC. Indicating false (or not including this property in your request) will result in receiving a VCC created for domestic use.
    NonDomesticSupplier: bool

    Transmission: CardCreateLodgedCardRequestTransmission

    # Optional field that may be set to true or false. When set to a value of true or if the field is not provided at all, card data is returned in the response. When set to a value of false, the Card Account Number and Security Code (CVV) will be excluded from the response.
    ReturnCardData: bool

    # Transaction ID within client environment associated with the customer. This value acts as a secondary identifier in conjunction with OrderNumber. The value is searchable and reportable in the ConnexPay portal. This value may be sent in multiple times within the integration for multiple purposes.  The maximum length is 50 characters and is alpha-numeric.
    CustomerID: str

    # Utilize the Association ID field to tie a virtual card to a sale or sales. For example, if you have several sales and one virtual card payment to a supplier, you can add association ID to the sales and the virtual card for downstream reporting.
    AssociationId: str

    LabelIDs: CardCreateLodgedCardRequestLabelIDs

    CustomParameters: CardCreateLodgedCardRequestCustomParameters

class CardCreateLodgedCardRequest(RequiredCardCreateLodgedCardRequest, OptionalCardCreateLodgedCardRequest):
    pass
