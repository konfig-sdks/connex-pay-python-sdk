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

from connex_pay_python_sdk.pydantic.token_request_hpp_token_request_sale import TokenRequestHppTokenRequestSale
from connex_pay_python_sdk.pydantic.token_request_hpp_token_request_tender_type_options import TokenRequestHppTokenRequestTenderTypeOptions

class TokenRequestHppTokenRequest(BaseModel):
    # Merchant Name. ConnexPay displays this on the Hosted Payment Page. The max length is 100 characters.
    merchant_name: str = Field(alias='MerchantName')

    sale: TokenRequestHppTokenRequestSale = Field(alias='Sale')

    # Additional information ConnexPay can display in the Hosted Payment Page. The max length is 2048 characters.
    description: typing.Optional[str] = Field(None, alias='Description')

    # This is a ConnexPay CLIENT server route ConnexPay uses to (re)direct the consumer payment result back to our client upon payment success, failure or cancel. If this data is not set, then it will use the default one from ConnexPay.
    result_redirect_url: typing.Optional[str] = Field(None, alias='ResultRedirectUrl')

    # ConnexPay can display this instead of “MerchantName” in the payment dialog.
    logo_url: typing.Optional[str] = Field(None, alias='LogoUrl')

    tender_type_options: typing.Optional[TokenRequestHppTokenRequestTenderTypeOptions] = Field(None, alias='TenderTypeOptions')

    # Client can request a specific expiration date to identify when the HPP Link will expire. Timestamps will be converted to UTC for consistency within the ConnexPay environment.
    expiration: typing.Optional[datetime] = Field(None, alias='Expiration')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
