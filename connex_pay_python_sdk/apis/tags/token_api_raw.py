# coding: utf-8

"""
    ConnexPay Reporting API

    REST API for retrieving reporting data. Currently Daily Accounting data only.

    The version of the OpenAPI document: v1
    Created by: https://docs.connexpay.com
"""

from connex_pay_python_sdk.paths.api_v1_authenticate.post import GenerateReportingTokenRaw
from connex_pay_python_sdk.paths.api_v1_token.post import IssueAuthenticationTokenRaw
from connex_pay_python_sdk.paths.api_v1_hosted_payment_page_requests.post import RequestHppTokenRaw


class TokenApiRaw(
    GenerateReportingTokenRaw,
    IssueAuthenticationTokenRaw,
    RequestHppTokenRaw,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    pass
