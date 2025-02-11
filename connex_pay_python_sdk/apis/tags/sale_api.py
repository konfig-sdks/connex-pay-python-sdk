# coding: utf-8

"""
    ConnexPay Reporting API

    REST API for retrieving reporting data. Currently Daily Accounting data only.

    The version of the OpenAPI document: v1
    Created by: https://docs.connexpay.com
"""

from connex_pay_python_sdk.paths.api_v1_sales_activate_sale_guid.put import ActivateDelayed
from connex_pay_python_sdk.paths.api_v1_sales.post import CreateTransaction
from connex_pay_python_sdk.paths.api_chargeback_get_by_user.get import GetChargebacksByUser
from connex_pay_python_sdk.paths.api_v1_search_sales_exportable_page_number_page_size.post import SearchSales
from connex_pay_python_sdk.paths.api_v1_sales_update_future_sale.post import UpdateDelayedActivation
from connex_pay_python_sdk.apis.tags.sale_api_raw import SaleApiRaw


class SaleApi(
    ActivateDelayed,
    CreateTransaction,
    GetChargebacksByUser,
    SearchSales,
    UpdateDelayedActivation,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: SaleApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = SaleApiRaw(api_client)
