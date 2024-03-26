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


class RequiredProblemDetails(TypedDict):
    pass

class OptionalProblemDetails(TypedDict, total=False):
    title: typing.Optional[str]

    type: typing.Optional[str]

    status: typing.Optional[int]

    detail: typing.Optional[str]

    instance: typing.Optional[str]

class ProblemDetails(RequiredProblemDetails, OptionalProblemDetails):
    pass
