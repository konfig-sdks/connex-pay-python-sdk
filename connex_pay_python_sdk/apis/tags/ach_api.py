# coding: utf-8

"""
    ConnexPay Reporting API

    REST API for retrieving reporting data. Currently Daily Accounting data only.

    The version of the OpenAPI document: v1
    Created by: https://docs.connexpay.com
"""

from connex_pay_python_sdk.paths.api_v1_issue_ach_issue_lite.post import CreateCreditPayment
from connex_pay_python_sdk.apis.tags.ach_api_raw import ACHApiRaw


class ACHApi(
    CreateCreditPayment,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: ACHApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = ACHApiRaw(api_client)
