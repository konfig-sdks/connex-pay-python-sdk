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

from connex_pay_python_sdk.type.sale_create_transaction_response_card_customer import SaleCreateTransactionResponseCardCustomer
from connex_pay_python_sdk.type.sale_create_transaction_response_card_three_ds import SaleCreateTransactionResponseCardThreeDs

class RequiredSaleCreateTransactionResponseCard(TypedDict):
    pass

class OptionalSaleCreateTransactionResponseCard(TypedDict, total=False):
    ThreeDS: SaleCreateTransactionResponseCardThreeDs

    CardNumber: str

    CardHolderName: str

    Cvv2: str

    ExpirationDate: str

    Customer: SaleCreateTransactionResponseCardCustomer

class SaleCreateTransactionResponseCard(RequiredSaleCreateTransactionResponseCard, OptionalSaleCreateTransactionResponseCard):
    pass
