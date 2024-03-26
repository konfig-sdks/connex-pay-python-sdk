# coding: utf-8

"""
    ConnexPay Reporting API

    REST API for retrieving reporting data. Currently Daily Accounting data only.

    The version of the OpenAPI document: v1
    Created by: https://docs.connexpay.com
"""

from datetime import datetime, date
import typing
from enum import Enum
from typing_extensions import TypedDict, Literal, TYPE_CHECKING

from connex_pay_python_sdk.type.card_issuance_create_virtual_card_request_custom_parameters_item import CardIssuanceCreateVirtualCardRequestCustomParametersItem

CardIssuanceCreateVirtualCardRequestCustomParameters = typing.List[CardIssuanceCreateVirtualCardRequestCustomParametersItem]
