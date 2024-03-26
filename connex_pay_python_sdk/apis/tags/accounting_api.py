# coding: utf-8

"""
    ConnexPay Reporting API

    REST API for retrieving reporting data. Currently Daily Accounting data only.

    The version of the OpenAPI document: v1
    Created by: https://docs.connexpay.com
"""

from connex_pay_python_sdk.paths.api_v1_accounting_daily_detail.get import GetDailyDetail
from connex_pay_python_sdk.paths.api_v1_accounting_daily_summary.get import GetDailySummary
from connex_pay_python_sdk.apis.tags.accounting_api_raw import AccountingApiRaw


class AccountingApi(
    GetDailyDetail,
    GetDailySummary,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: AccountingApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = AccountingApiRaw(api_client)
