# coding: utf-8

"""
    ConnexPay Reporting API

    REST API for retrieving reporting data. Currently Daily Accounting data only.

    The version of the OpenAPI document: v1
    Created by: https://docs.connexpay.com
"""

import unittest

import os
from pprint import pprint
from connex_pay_python_sdk import ConnexPay

class TestSimple(unittest.TestCase):
    def setUp(self):
        pass

    def test_client(self):
        connexpay = ConnexPay(
        
            username = 'YOUR_USERNAME',
            password = 'YOUR_PASSWORD'
        )
        self.assertIsNotNone(connexpay)

    def tearDown(self):
        pass


if __name__ == "__main__":
    unittest.main()
