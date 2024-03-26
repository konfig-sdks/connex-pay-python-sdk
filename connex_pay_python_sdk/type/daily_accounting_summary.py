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


class RequiredDailyAccountingSummary(TypedDict):
    pass

class OptionalDailyAccountingSummary(TypedDict, total=False):
    # Merchant Guid    Unique identifier assigned to the merchant by ConnexPay.
    merchantGuid: str

    # Client Name    Unique name assigned to the client by ConnexPay.
    clientName: typing.Optional[str]

    # Released Date    Date on which the requested transactions were released to the client.
    releasedDate: date

    # Prior Day Cash Balance    The starting cash balance from the previous day.
    priorDayCashBalance: typing.Union[int, float]

    # Wire/ACH to Fund Cash Account Amount (Credit) or Withdraw from Cash Account Amount (Debit)    Funds transferred between the client's bank account and ConnexPay to fund transactions or to return funds to the client.
    wireAchToFundCashAmount: typing.Union[int, float]

    # Beginning Cash Balance    The funds the client begins the day with.
    beginningCashBalance: typing.Union[int, float]

    # Credit Card Sale Amount (Credit)    Total amount of incoming credit card sales added to the client's cash balance.
    creditSaleAmount: typing.Union[int, float]

    # ACH Sale Amount (Credit)    Total amount of incoming ACH sales added to the client's cash balance.
    achSaleAmount: typing.Union[int, float]

    # ACH Purchase Amount (Debit)    Total amount of ACH purchases decreasing the client's cash balance.
    purchaseAchAmount: typing.Union[int, float]

    # Virtual Card Purchase Amount (Debit)    Total amount of issued virtual credit card purchases subtracting from the client's cash balance.
    purchaseCardAmount: typing.Union[int, float]

    # Purchase Push to Card Amount    Total amount of funds paid out through PushToCard subtracting from the client's cash balance.
    purchasePushToCardAmount: typing.Union[int, float]

    # Credit Card Void Amount (Debit)    Total amount of credit card sales voided subtracting from the client's cash balance.
    creditVoidAmount: typing.Union[int, float]

    # Credit Card Return Amount (Debit)    Total amount of credit card sales returned subtracting from the client's cash balance.
    creditReturnAmount: typing.Union[int, float]

    # Credit Chargeback Amount    Total amount of Chargebacks received on the credit card sales subtracting from the client's cash balance.
    creditChargebackAmount: typing.Union[int, float]

    # Credit Adjustment Amount    Total amount of manual credit adjustments created for the client.
    creditAdjustmentAmount: typing.Union[int, float]

    # ACH Void Amount (Debit)    Total amount of ACH sales voided subtracting from the client's cash balance.
    achVoidAmount: typing.Union[int, float]

    # ACH Return (Debit)    Total amount of ACH sales returned subtracting from the client's cash balance.
    achReturnAmount: typing.Union[int, float]

    # Virtual Card Return Amount (Credit)    Total amount returned to issued virtual credit cards adding to the client's cash balance.
    purchaseCardReturnAmount: typing.Union[int, float]

    # Purchase Card Chargeback Amount    Total amount of Chargebacks received on issued virtual credit cards as part of the dispute process.
    purchaseCardChargebackAmount: typing.Union[int, float]

    # Purchase - ACH Return Amount (Credit)    Total amount returned to issued ACHs adding to the client's cash balance.
    purchaseAchReturnAmount: typing.Union[int, float]

    # Total Activity    The sum of all debits and credits processed on the client's behalf for the previous day.
    totalActivity: typing.Union[int, float]

    # New Cash Balance    Reflects the day's beginning cash balance plus or minus the client's total activity.
    newCashBalance: typing.Union[int, float]

    # Credit/Debit    The amount to be credited to or debited from the client's bank account. ConnexPay will collaborate with  the client to determine the percentage that will be returned to the client's bank account each day.
    netDebitCreditToClient: typing.Union[int, float]

    # Ending Cash Balance    The client's New Cash Balance plus or minus the Credit/Debit amount.
    endingCashBalance: typing.Union[int, float]

    # Minimum Cash Balance (MCB)    Minimum funding balance that should be maintained by the client with ConnexPay.
    minimumCashBalance: typing.Union[int, float]

    # ACH Debit Reject Amount (Credit)    Total amount of payments that did not clear the supplier's account. Payments can be rejected for a variety of reasons, including closed accounts, incorrect account numbers, etc.
    achDebitRejectAmount: typing.Union[int, float]

class DailyAccountingSummary(RequiredDailyAccountingSummary, OptionalDailyAccountingSummary):
    pass
