# coding: utf-8

"""
    ConnexPay Reporting API

    REST API for retrieving reporting data. Currently Daily Accounting data only.

    The version of the OpenAPI document: v1
    Created by: https://docs.connexpay.com
"""

import unittest
from unittest.mock import patch

import urllib3

import connex_pay_python_sdk
from connex_pay_python_sdk.paths.api_v1_purchase_event_history_resend import post
from connex_pay_python_sdk import configuration, schemas, api_client

from .. import ApiTestMixin


class TestApiV1PurchaseEventHistoryResend(ApiTestMixin, unittest.TestCase):
    """
    ApiV1PurchaseEventHistoryResend unit test stubs
        Purchase Event History (Replay Webhooks)
    """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    response_status = 200




if __name__ == '__main__':
    unittest.main()
