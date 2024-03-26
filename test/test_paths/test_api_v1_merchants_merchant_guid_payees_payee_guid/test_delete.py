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
from connex_pay_python_sdk.paths.api_v1_merchants_merchant_guid_payees_payee_guid import delete
from connex_pay_python_sdk import configuration, schemas, api_client

from .. import ApiTestMixin


class TestApiV1MerchantsMerchantGuidPayeesPayeeGuid(ApiTestMixin, unittest.TestCase):
    """
    ApiV1MerchantsMerchantGuidPayeesPayeeGuid unit test stubs
        Delete merchant payee
    """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    response_status = 204
    response_body = ''


if __name__ == '__main__':
    unittest.main()
