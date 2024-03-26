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


class RequiredTokenRequestHppTokenRequestSale(TypedDict):
    # Device's Guid provided by ConnexPay
    DeviceGuid: str

    # Amount of the transaction that will be processed. Note: this value is submitted multiple times (in different formats) within the integration to support different purposes i.e. risk analysis, merchant processinging, etc.  The minimun amount is: $0.50.
    Amount: int

class OptionalTokenRequestHppTokenRequestSale(TypedDict, total=False):
    # Allowed values:  1. Credit (default if TenderType not provided) 2. Cash 3. ACH
    TenderType: str

    # Transaction sequence number within client environment. Note: value is not searchable or reportable in ConnexPay portal.  Alphanumeric.
    SequenceNumber: str

    # This is the most common number you'll see throughout the ConnexPay Portal.  Transaction ID within client environment associated with the order. The value is searchable and reportable in the ConnexPay portal. This value may be sent in multiple instances of the integration for multiple purposes. Customers in the travel space often send the Record Locator/PNR in this field.  The maximum length is 50 alpha-numeric characters and allows dashes ( - ).
    OrderNumber: str

    # Value determines whether or not a customer shall be emailed a receipt from the ConnexPay platform if the email address is provided in the API customer block. The default value is TRUE. Set to FALSE so that an email receipt is not sent to the customer. Set to TRUE or leave empty if you want e-mail to be sent. If TRUE, customer's email must be included in the \"Card.Customer.email\" parameter.
    SendReceipt: bool

    # Indicator that determines if client would like to evaluate the transactions as risk only rather than process as merchant of record and create a virtual card. The allowed values:  1. Set to TRUE will only run risk validations. If TenderType is set to Cash, setting TRUE will throw a validation error.  2. Set to FALSE will run risk validations and an authorization on the card. For this option a Processing Merchant account is required, contact ConnexPay support if any questions.  3. Set to NULL and your Merchant Level settings would apply.
    RiskProcessingOnly: bool

    # The statement description allows a client to customize the Merchant name that appears on the cardholder statement such that the cardholder recognizes the transaction on their statement. ConnexPay recommends sending a recognizable DBA along with the PNR i.e. ABC Travel ABC123. Note: functionality not applicable for American Express OptBlue program.  The maximun length is 25 alpha-numeric characters.
    StatementDescription: str

    # Transaction ID within client environment associated with the customer. This value acts as a secondary identifier in conjunction with OrderNumber. The value is searchable and reportable in the ConnexPay portal. This value may be sent in multiple times within the integration for multiple purposes.  The maximum length is 50 characters and is alpha-numeric.
    CustomerID: str

    # Set a future date on which to run this sale, at least one day from creation date and within one year. If this parameter is supplied a record for this sale is created, supplied consumer card information is internally tokenized, but fraud check and authorization do not occur until ConnexPay processes it on the supplied ActivationDate. Alternatively, a client can force activation via the Activate API (see below). If this date is not supplied a sale is authorized immediately.
    ActivationDate: str

    # When needing to issue a Virtual Card that ties to more than one Sale transaction, you can send in a GroupId (with the same GroupId) on the Sales that you need to group together. By including a common GroupId for two or more Sales transaction, a Virtual Card may then be created for the sum of the Sales within that GroupId.  A common use case for this is when multiple families are going on a cruise - each family may want to pay separately on their credit card. However, the Travel Agent may want to pay for the cruise with one virtual card.  The maximum length is 25 alpha-numeric characters.  This is for limited use - please contact your Customer Success Manager if you would like to enable this functionality.
    GroupId: str

class TokenRequestHppTokenRequestSale(RequiredTokenRequestHppTokenRequestSale, OptionalTokenRequestHppTokenRequestSale):
    pass
