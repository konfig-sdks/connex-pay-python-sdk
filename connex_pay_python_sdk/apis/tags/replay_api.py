# coding: utf-8

"""
    ConnexPay Reporting API

    REST API for retrieving reporting data. Currently Daily Accounting data only.

    The version of the OpenAPI document: v1
    Created by: https://docs.connexpay.com
"""

from connex_pay_python_sdk.paths.api_v1_purchase_event_history_resend.post import PurchaseEventHistoryResend
from connex_pay_python_sdk.apis.tags.replay_api_raw import ReplayApiRaw


class ReplayApi(
    PurchaseEventHistoryResend,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: ReplayApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = ReplayApiRaw(api_client)
