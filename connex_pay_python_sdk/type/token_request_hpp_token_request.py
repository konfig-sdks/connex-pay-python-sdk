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

from connex_pay_python_sdk.type.token_request_hpp_token_request_sale import TokenRequestHppTokenRequestSale
from connex_pay_python_sdk.type.token_request_hpp_token_request_tender_type_options import TokenRequestHppTokenRequestTenderTypeOptions

class RequiredTokenRequestHppTokenRequest(TypedDict):
    # Merchant Name. ConnexPay displays this on the Hosted Payment Page. The max length is 100 characters.
    MerchantName: str

    Sale: TokenRequestHppTokenRequestSale

class OptionalTokenRequestHppTokenRequest(TypedDict, total=False):
    # Additional information ConnexPay can display in the Hosted Payment Page. The max length is 2048 characters.
    Description: str

    # This is a ConnexPay CLIENT server route ConnexPay uses to (re)direct the consumer payment result back to our client upon payment success, failure or cancel. If this data is not set, then it will use the default one from ConnexPay.
    ResultRedirectUrl: str

    # ConnexPay can display this instead of “MerchantName” in the payment dialog.
    LogoUrl: str

    TenderTypeOptions: TokenRequestHppTokenRequestTenderTypeOptions

    # Client can request a specific expiration date to identify when the HPP Link will expire. Timestamps will be converted to UTC for consistency within the ConnexPay environment.
    Expiration: datetime

class TokenRequestHppTokenRequest(RequiredTokenRequestHppTokenRequest, OptionalTokenRequestHppTokenRequest):
    pass
