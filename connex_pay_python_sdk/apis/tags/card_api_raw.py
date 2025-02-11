# coding: utf-8

"""
    ConnexPay Reporting API

    REST API for retrieving reporting data. Currently Daily Accounting data only.

    The version of the OpenAPI document: v1
    Created by: https://docs.connexpay.com
"""

from connex_pay_python_sdk.paths.api_v1_issue_card_activate_delayed_card_card_guid.put import ActivateDelayedRaw
from connex_pay_python_sdk.paths.api_v1_issue_card_cancel_card_guid.put import CancelVirtualCardRaw
from connex_pay_python_sdk.paths.api_v1_issue_card_lodged_card.post import CreateLodgedCardRaw
from connex_pay_python_sdk.paths.api_v1_cards_card_guid_show_full_pan.get import GetDetailRaw
from connex_pay_python_sdk.paths.api_v1_issue_card_send_payment_info_card_guid.put import ResendTransmissionInfoRaw
from connex_pay_python_sdk.paths.api_v1_search_issued_cards.post import SearchIssuedVirtualCardsRaw
from connex_pay_python_sdk.paths.api_v1_terminate_card_guid.post import TerminateByDateRaw
from connex_pay_python_sdk.paths.api_v1_issue_card_card_guid.put import UpdateCardDetailsRaw
from connex_pay_python_sdk.paths.api_v1_issue_card_update_delayed_card_card_guid.put import UpdateDelayedActivationRaw
from connex_pay_python_sdk.paths.api_v1_issue_card_lodged_card_card_guid.put import UpdateLodgedCardRaw


class CardApiRaw(
    ActivateDelayedRaw,
    CancelVirtualCardRaw,
    CreateLodgedCardRaw,
    GetDetailRaw,
    ResendTransmissionInfoRaw,
    SearchIssuedVirtualCardsRaw,
    TerminateByDateRaw,
    UpdateCardDetailsRaw,
    UpdateDelayedActivationRaw,
    UpdateLodgedCardRaw,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    pass
