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


class DailyAccountingDetail(BaseModel):
    # Description    The type of transaction being released in this detail record.    Possible Values:    ACH Debit Reject    Bank A ACH Credit Reject    Credit to Client (Withdrawal from Cash Account)    Daily Flex Funding    Debit from Client (Deposit to Cash Account)    Empty    Prior Day Cash Balance    Purchase - ACH Purchase    Purchase - ACH Return    Purchase - Push To Card Payout    Purchase - Virtual Card Chargeback    Purchase - Virtual Card Purchase    Purchase - Virtual Card Return    Reserve Balance    Sale - ACH Return    Sale - ACH Sale    Sale - ACH Void    Sale - Credit Card Adjustment    Sale - Credit Card Chargeback    Sale - Credit Card Return    Sale - Credit Card Sale    Sale - Credit Card Void    Unspecified
    description: typing.Optional[typing.Optional[str]] = Field(None, alias='description')

    # Merchant Guid    Unique identifier assigned to the merchant by ConnexPay.
    merchant_guid: typing.Optional[str] = Field(None, alias='merchantGuid')

    # Client Name    Unique name assigned to the client by ConnexPay.
    client_name: typing.Optional[typing.Optional[str]] = Field(None, alias='clientName')

    # Released Date    Date on which the Accounting File for this detail record was released to the client.
    released_date: typing.Optional[date] = Field(None, alias='releasedDate')

    # Order Number    Identifier that may be provided by the client during the Create Sale or IssueLite process to identify the order.  Can be comprised of multiple sales and purchases.
    order_number: typing.Optional[typing.Optional[str]] = Field(None, alias='orderNumber')

    # Name    The name line 1 and 2 of the virtual credit card.
    name: typing.Optional[typing.Optional[str]] = Field(None, alias='name')

    # Card Last Four    The last four digits of the card number associated with the detail record.
    card_last_four: typing.Optional[typing.Optional[str]] = Field(None, alias='cardLastFour')

    # Incoming Transaction Code (ITC)    A unique ConnexPay generated token that connects an incoming sale transaction to an outbound  purchase (virtual card or ACH) transaction. An ITC is generated and returned for each successful  authorization associated with a Sale request and is required for each purchase request.
    incoming_transaction_code: typing.Optional[typing.Optional[str]] = Field(None, alias='incomingTransactionCode')

    # Customer ID    Identifier that may be provided by the client during the Create Sale or IssueLite process. Can be comprised   of multiple sales and purchases. Acts as a secondary identifier in conjunction with OrderNumber.
    customer_id: typing.Optional[typing.Optional[str]] = Field(None, alias='customerId')

    # Amount    Amount of the sale or purchase transaction.
    amount: typing.Optional[typing.Union[int, float]] = Field(None, alias='amount')

    # Merchant Name    Name of the supplier processing the virtual credit card transaction.
    merchant_name: typing.Optional[typing.Optional[str]] = Field(None, alias='merchantName')

    # Ticket Number    Addendum data associated with the transaction that is returned if provided during the virtual credit card or ACH creation
    ticket_number: typing.Optional[typing.Optional[str]] = Field(None, alias='ticketNumber')

    # Entity Guid    Entity Guid of the detail record to link them back to the original entity.
    entity_guid: typing.Optional[typing.Optional[str]] = Field(None, alias='entityGuid')

    # Purchase Type    Description of the client's category group. Essentially, the industry where the virtual card will be utilized.    See the Issue Card method in the Purchases API documentation for more details.
    purchase_type: typing.Optional[typing.Optional[str]] = Field(None, alias='purchaseType')

    # Entity Id    Entity Guid of the detail record to link them back to the original entity.
    entity_id: typing.Optional[typing.Optional[str]] = Field(None, alias='entityId')

    # Issued Amount    Amount of the virtual credit card issued to the client.
    issued_amount: typing.Optional[typing.Union[int, float]] = Field(None, alias='issuedAmount')

    # Label Name    Comma-separated list of labels associated with the sale.
    label_name: typing.Optional[typing.Optional[str]] = Field(None, alias='labelName')

    # Association ID    Used to associate a virtual card to one or more sales.
    association_id: typing.Optional[typing.Optional[str]] = Field(None, alias='associationId')

    # Sale Guid    Guid value returned from the Create Sale method in the Sales API. Associated with   sale transaction detail records.
    sale_guid: typing.Optional[typing.Optional[str]] = Field(None, alias='saleGuid')

    # Card Guid    Guid value return from the Issue Card method in the Purchases API. Associated with   purchase and return detail records.
    card_guid: typing.Optional[typing.Optional[str]] = Field(None, alias='cardGuid')

    # Date Time    For Sale detail records, the date of the sale transaction.    For Purchase and Return detail records, the date of the purchase or return settlement.    Note: This date may not be the same as ReleasedDate because release does not occur on weekends and bank holidays.
    date_time: typing.Optional[typing.Optional[datetime]] = Field(None, alias='dateTime')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
