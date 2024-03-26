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


class DailyAccountingSummary(BaseModel):
    # Merchant Guid    Unique identifier assigned to the merchant by ConnexPay.
    merchant_guid: typing.Optional[str] = Field(None, alias='merchantGuid')

    # Client Name    Unique name assigned to the client by ConnexPay.
    client_name: typing.Optional[typing.Optional[str]] = Field(None, alias='clientName')

    # Released Date    Date on which the requested transactions were released to the client.
    released_date: typing.Optional[date] = Field(None, alias='releasedDate')

    # Prior Day Cash Balance    The starting cash balance from the previous day.
    prior_day_cash_balance: typing.Optional[typing.Union[int, float]] = Field(None, alias='priorDayCashBalance')

    # Wire/ACH to Fund Cash Account Amount (Credit) or Withdraw from Cash Account Amount (Debit)    Funds transferred between the client's bank account and ConnexPay to fund transactions or to return funds to the client.
    wire_ach_to_fund_cash_amount: typing.Optional[typing.Union[int, float]] = Field(None, alias='wireAchToFundCashAmount')

    # Beginning Cash Balance    The funds the client begins the day with.
    beginning_cash_balance: typing.Optional[typing.Union[int, float]] = Field(None, alias='beginningCashBalance')

    # Credit Card Sale Amount (Credit)    Total amount of incoming credit card sales added to the client's cash balance.
    credit_sale_amount: typing.Optional[typing.Union[int, float]] = Field(None, alias='creditSaleAmount')

    # ACH Sale Amount (Credit)    Total amount of incoming ACH sales added to the client's cash balance.
    ach_sale_amount: typing.Optional[typing.Union[int, float]] = Field(None, alias='achSaleAmount')

    # ACH Purchase Amount (Debit)    Total amount of ACH purchases decreasing the client's cash balance.
    purchase_ach_amount: typing.Optional[typing.Union[int, float]] = Field(None, alias='purchaseAchAmount')

    # Virtual Card Purchase Amount (Debit)    Total amount of issued virtual credit card purchases subtracting from the client's cash balance.
    purchase_card_amount: typing.Optional[typing.Union[int, float]] = Field(None, alias='purchaseCardAmount')

    # Purchase Push to Card Amount    Total amount of funds paid out through PushToCard subtracting from the client's cash balance.
    purchase_push_to_card_amount: typing.Optional[typing.Union[int, float]] = Field(None, alias='purchasePushToCardAmount')

    # Credit Card Void Amount (Debit)    Total amount of credit card sales voided subtracting from the client's cash balance.
    credit_void_amount: typing.Optional[typing.Union[int, float]] = Field(None, alias='creditVoidAmount')

    # Credit Card Return Amount (Debit)    Total amount of credit card sales returned subtracting from the client's cash balance.
    credit_return_amount: typing.Optional[typing.Union[int, float]] = Field(None, alias='creditReturnAmount')

    # Credit Chargeback Amount    Total amount of Chargebacks received on the credit card sales subtracting from the client's cash balance.
    credit_chargeback_amount: typing.Optional[typing.Union[int, float]] = Field(None, alias='creditChargebackAmount')

    # Credit Adjustment Amount    Total amount of manual credit adjustments created for the client.
    credit_adjustment_amount: typing.Optional[typing.Union[int, float]] = Field(None, alias='creditAdjustmentAmount')

    # ACH Void Amount (Debit)    Total amount of ACH sales voided subtracting from the client's cash balance.
    ach_void_amount: typing.Optional[typing.Union[int, float]] = Field(None, alias='achVoidAmount')

    # ACH Return (Debit)    Total amount of ACH sales returned subtracting from the client's cash balance.
    ach_return_amount: typing.Optional[typing.Union[int, float]] = Field(None, alias='achReturnAmount')

    # Virtual Card Return Amount (Credit)    Total amount returned to issued virtual credit cards adding to the client's cash balance.
    purchase_card_return_amount: typing.Optional[typing.Union[int, float]] = Field(None, alias='purchaseCardReturnAmount')

    # Purchase Card Chargeback Amount    Total amount of Chargebacks received on issued virtual credit cards as part of the dispute process.
    purchase_card_chargeback_amount: typing.Optional[typing.Union[int, float]] = Field(None, alias='purchaseCardChargebackAmount')

    # Purchase - ACH Return Amount (Credit)    Total amount returned to issued ACHs adding to the client's cash balance.
    purchase_ach_return_amount: typing.Optional[typing.Union[int, float]] = Field(None, alias='purchaseAchReturnAmount')

    # Total Activity    The sum of all debits and credits processed on the client's behalf for the previous day.
    total_activity: typing.Optional[typing.Union[int, float]] = Field(None, alias='totalActivity')

    # New Cash Balance    Reflects the day's beginning cash balance plus or minus the client's total activity.
    new_cash_balance: typing.Optional[typing.Union[int, float]] = Field(None, alias='newCashBalance')

    # Credit/Debit    The amount to be credited to or debited from the client's bank account. ConnexPay will collaborate with  the client to determine the percentage that will be returned to the client's bank account each day.
    net_debit_credit_to_client: typing.Optional[typing.Union[int, float]] = Field(None, alias='netDebitCreditToClient')

    # Ending Cash Balance    The client's New Cash Balance plus or minus the Credit/Debit amount.
    ending_cash_balance: typing.Optional[typing.Union[int, float]] = Field(None, alias='endingCashBalance')

    # Minimum Cash Balance (MCB)    Minimum funding balance that should be maintained by the client with ConnexPay.
    minimum_cash_balance: typing.Optional[typing.Union[int, float]] = Field(None, alias='minimumCashBalance')

    # ACH Debit Reject Amount (Credit)    Total amount of payments that did not clear the supplier's account. Payments can be rejected for a variety of reasons, including closed accounts, incorrect account numbers, etc.
    ach_debit_reject_amount: typing.Optional[typing.Union[int, float]] = Field(None, alias='achDebitRejectAmount')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
