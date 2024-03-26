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
from connex_pay_python_sdk.paths.v1_addendum_remove_guid import post
from connex_pay_python_sdk import configuration, schemas, api_client

from .. import ApiTestMixin


class TestV1AddendumRemoveGuid(ApiTestMixin, unittest.TestCase):
    """
    V1AddendumRemoveGuid unit test stubs
        Addendum Remove
    """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    response_status = 200




if __name__ == '__main__':
    unittest.main()
