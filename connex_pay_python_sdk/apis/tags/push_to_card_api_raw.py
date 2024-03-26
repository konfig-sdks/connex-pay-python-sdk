# coding: utf-8

"""
    ConnexPay Reporting API

    REST API for retrieving reporting data. Currently Daily Accounting data only.

    The version of the OpenAPI document: v1
    Created by: https://docs.connexpay.com
"""

from connex_pay_python_sdk.paths.api_v1_push_to_card_payouts_payout_guid_cancel.post import CancelPaymentsRaw
from connex_pay_python_sdk.paths.api_v1_push_to_card_payees.post import CreatePayeeRaw
from connex_pay_python_sdk.paths.api_v1_push_to_card_payouts.post import CreatePayoutRaw
from connex_pay_python_sdk.paths.api_v1_push_to_card_authenticate_payment_widget.get import GetAuthenticationTokenAsyncRaw
from connex_pay_python_sdk.paths.api_v1_push_to_card_payees.get import GetPayeeRaw
from connex_pay_python_sdk.paths.api_v1_push_to_card_payouts_payout_guid.get import GetPayoutDetailsRaw
from connex_pay_python_sdk.paths.api_v1_push_to_card_payees_payee_guid_status.put import ManagePayeeRaw
from connex_pay_python_sdk.paths.api_v1_push_to_card_payments_rid_guid_card_id.patch import PushFundsToCardAsyncRaw
from connex_pay_python_sdk.paths.api_v1_push_to_card_payees_payee_guid.patch import UpdatePayeeRaw


class PushToCardApiRaw(
    CancelPaymentsRaw,
    CreatePayeeRaw,
    CreatePayoutRaw,
    GetAuthenticationTokenAsyncRaw,
    GetPayeeRaw,
    GetPayoutDetailsRaw,
    ManagePayeeRaw,
    PushFundsToCardAsyncRaw,
    UpdatePayeeRaw,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    pass
