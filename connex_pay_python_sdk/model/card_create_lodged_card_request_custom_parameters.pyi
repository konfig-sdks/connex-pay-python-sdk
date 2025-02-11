# coding: utf-8

"""
    ConnexPay Reporting API

    REST API for retrieving reporting data. Currently Daily Accounting data only.

    The version of the OpenAPI document: v1
    Created by: https://docs.connexpay.com
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from connex_pay_python_sdk import schemas  # noqa: F401


class CardCreateLodgedCardRequestCustomParameters(
    schemas.ListSchema
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)

    You can add custom parameters to your issue card request in the event that you need to associate additional information with the virtual card. For example, if you want to add an invoice number you would include the custom parameters object with the name parameter = "invoice" and the value parameter as the invoice number. This requires customized reporting so you'll need to work with your implementations specialist to determine what's required.
    """


    class MetaOapg:
        
        @staticmethod
        def items() -> typing.Type['CardCreateLodgedCardRequestCustomParametersItem']:
            return CardCreateLodgedCardRequestCustomParametersItem

    def __new__(
        cls,
        arg: typing.Union[typing.Tuple['CardCreateLodgedCardRequestCustomParametersItem'], typing.List['CardCreateLodgedCardRequestCustomParametersItem']],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'CardCreateLodgedCardRequestCustomParameters':
        return super().__new__(
            cls,
            arg,
            _configuration=_configuration,
        )

    def __getitem__(self, i: int) -> 'CardCreateLodgedCardRequestCustomParametersItem':
        return super().__getitem__(i)

from connex_pay_python_sdk.model.card_create_lodged_card_request_custom_parameters_item import CardCreateLodgedCardRequestCustomParametersItem
