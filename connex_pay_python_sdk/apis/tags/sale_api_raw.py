# coding: utf-8

"""
    ConnexPay Reporting API

    REST API for retrieving reporting data. Currently Daily Accounting data only.

    The version of the OpenAPI document: v1
    Created by: https://docs.connexpay.com
"""

from connex_pay_python_sdk.paths.api_v1_sales_activate_sale_guid.put import ActivateDelayedRaw
from connex_pay_python_sdk.paths.api_v1_sales.post import CreateTransactionRaw
from connex_pay_python_sdk.paths.api_chargeback_get_by_user.get import GetChargebacksByUserRaw
from connex_pay_python_sdk.paths.api_v1_search_sales_exportable_page_number_page_size.post import SearchSalesRaw
from connex_pay_python_sdk.paths.api_v1_sales_update_future_sale.post import UpdateDelayedActivationRaw


class SaleApiRaw(
    ActivateDelayedRaw,
    CreateTransactionRaw,
    GetChargebacksByUserRaw,
    SearchSalesRaw,
    UpdateDelayedActivationRaw,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    pass
