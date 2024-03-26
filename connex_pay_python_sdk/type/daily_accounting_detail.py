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


class RequiredDailyAccountingDetail(TypedDict):
    pass

class OptionalDailyAccountingDetail(TypedDict, total=False):
    # Description    The type of transaction being released in this detail record.    Possible Values:    ACH Debit Reject    Bank A ACH Credit Reject    Credit to Client (Withdrawal from Cash Account)    Daily Flex Funding    Debit from Client (Deposit to Cash Account)    Empty    Prior Day Cash Balance    Purchase - ACH Purchase    Purchase - ACH Return    Purchase - Push To Card Payout    Purchase - Virtual Card Chargeback    Purchase - Virtual Card Purchase    Purchase - Virtual Card Return    Reserve Balance    Sale - ACH Return    Sale - ACH Sale    Sale - ACH Void    Sale - Credit Card Adjustment    Sale - Credit Card Chargeback    Sale - Credit Card Return    Sale - Credit Card Sale    Sale - Credit Card Void    Unspecified
    description: typing.Optional[str]

    # Merchant Guid    Unique identifier assigned to the merchant by ConnexPay.
    merchantGuid: str

    # Client Name    Unique name assigned to the client by ConnexPay.
    clientName: typing.Optional[str]

    # Released Date    Date on which the Accounting File for this detail record was released to the client.
    releasedDate: date

    # Order Number    Identifier that may be provided by the client during the Create Sale or IssueLite process to identify the order.  Can be comprised of multiple sales and purchases.
    orderNumber: typing.Optional[str]

    # Name    The name line 1 and 2 of the virtual credit card.
    name: typing.Optional[str]

    # Card Last Four    The last four digits of the card number associated with the detail record.
    cardLastFour: typing.Optional[str]

    # Incoming Transaction Code (ITC)    A unique ConnexPay generated token that connects an incoming sale transaction to an outbound  purchase (virtual card or ACH) transaction. An ITC is generated and returned for each successful  authorization associated with a Sale request and is required for each purchase request.
    incomingTransactionCode: typing.Optional[str]

    # Customer ID    Identifier that may be provided by the client during the Create Sale or IssueLite process. Can be comprised   of multiple sales and purchases. Acts as a secondary identifier in conjunction with OrderNumber.
    customerId: typing.Optional[str]

    # Amount    Amount of the sale or purchase transaction.
    amount: typing.Union[int, float]

    # Merchant Name    Name of the supplier processing the virtual credit card transaction.
    merchantName: typing.Optional[str]

    # Ticket Number    Addendum data associated with the transaction that is returned if provided during the virtual credit card or ACH creation
    ticketNumber: typing.Optional[str]

    # Entity Guid    Entity Guid of the detail record to link them back to the original entity.
    entityGuid: typing.Optional[str]

    # Purchase Type    Description of the client's category group. Essentially, the industry where the virtual card will be utilized.    See the Issue Card method in the Purchases API documentation for more details.
    purchaseType: typing.Optional[str]

    # Entity Id    Entity Guid of the detail record to link them back to the original entity.
    entityId: typing.Optional[str]

    # Issued Amount    Amount of the virtual credit card issued to the client.
    issuedAmount: typing.Union[int, float]

    # Label Name    Comma-separated list of labels associated with the sale.
    labelName: typing.Optional[str]

    # Association ID    Used to associate a virtual card to one or more sales.
    associationId: typing.Optional[str]

    # Sale Guid    Guid value returned from the Create Sale method in the Sales API. Associated with   sale transaction detail records.
    saleGuid: typing.Optional[str]

    # Card Guid    Guid value return from the Issue Card method in the Purchases API. Associated with   purchase and return detail records.
    cardGuid: typing.Optional[str]

    # Date Time    For Sale detail records, the date of the sale transaction.    For Purchase and Return detail records, the date of the purchase or return settlement.    Note: This date may not be the same as ReleasedDate because release does not occur on weekends and bank holidays.
    dateTime: typing.Optional[datetime]

class DailyAccountingDetail(RequiredDailyAccountingDetail, OptionalDailyAccountingDetail):
    pass
