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
from connex_pay_python_sdk.paths.api_v1_verify import post
from connex_pay_python_sdk import configuration, schemas, api_client

from .. import ApiTestMixin


class TestApiV1Verify(ApiTestMixin, unittest.TestCase):
    """
    ApiV1Verify unit test stubs
        Verify
    """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    response_status = 201




if __name__ == '__main__':
    unittest.main()
