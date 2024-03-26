# coding: utf-8

"""
    ConnexPay Reporting API

    REST API for retrieving reporting data. Currently Daily Accounting data only.

    The version of the OpenAPI document: v1
    Created by: https://docs.connexpay.com
"""

from connex_pay_python_sdk.paths.api_v1_merchant_self_service_funding.post import MerchantCashBalance
from connex_pay_python_sdk.paths.api_v1_merchant_flex_funding_funds_transfer.post import TransferMerchantCashBalance
from connex_pay_python_sdk.apis.tags.funding_api_raw import FundingApiRaw


class FundingApi(
    MerchantCashBalance,
    TransferMerchantCashBalance,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: FundingApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = FundingApiRaw(api_client)
