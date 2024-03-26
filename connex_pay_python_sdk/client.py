# coding: utf-8
"""
    ConnexPay Reporting API

    REST API for retrieving reporting data. Currently Daily Accounting data only.

    The version of the OpenAPI document: v1
    Created by: https://docs.connexpay.com
"""

import typing
import inspect
from datetime import date, datetime
from connex_pay_python_sdk.client_custom import ClientCustom
from connex_pay_python_sdk.configuration import Configuration
from connex_pay_python_sdk.api_client import ApiClient
from connex_pay_python_sdk.type_util import copy_signature
from connex_pay_python_sdk.apis.tags.ach_api import ACHApi
from connex_pay_python_sdk.apis.tags.accounting_api import AccountingApi
from connex_pay_python_sdk.apis.tags.addendum_api import AddendumApi
from connex_pay_python_sdk.apis.tags.authentication_api import AuthenticationApi
from connex_pay_python_sdk.apis.tags.cancellation_api import CancellationApi
from connex_pay_python_sdk.apis.tags.card_api import CardApi
from connex_pay_python_sdk.apis.tags.card_issuance_api import CardIssuanceApi
from connex_pay_python_sdk.apis.tags.card_issue_api import CardIssueApi
from connex_pay_python_sdk.apis.tags.funding_api import FundingApi
from connex_pay_python_sdk.apis.tags.funds_api import FundsApi
from connex_pay_python_sdk.apis.tags.merchant_payees_api import MerchantPayeesApi
from connex_pay_python_sdk.apis.tags.push_to_card_api import PushToCardApi
from connex_pay_python_sdk.apis.tags.replay_api import ReplayApi
from connex_pay_python_sdk.apis.tags.model_return_api import ModelReturnApi
from connex_pay_python_sdk.apis.tags.sale_api import SaleApi
from connex_pay_python_sdk.apis.tags.setting_api import SettingApi
from connex_pay_python_sdk.apis.tags.settlement_api import SettlementApi
from connex_pay_python_sdk.apis.tags.status_group_api import StatusGroupApi
from connex_pay_python_sdk.apis.tags.token_api import TokenApi
from connex_pay_python_sdk.apis.tags.transaction_api import TransactionApi
from connex_pay_python_sdk.apis.tags.validation_api import ValidationApi
from connex_pay_python_sdk.apis.tags.verification_api import VerificationApi
from connex_pay_python_sdk.apis.tags.void_api import VoidApi



class ConnexPay(ClientCustom):

    def __init__(self, configuration: typing.Union[Configuration, None] = None, **kwargs):
        super().__init__(configuration, **kwargs)
        if (len(kwargs) > 0):
            configuration = Configuration(**kwargs)
        if (configuration is None):
            raise Exception("configuration is required")
        api_client = ApiClient(configuration)
        self.ach: ACHApi = ACHApi(api_client)
        self.accounting: AccountingApi = AccountingApi(api_client)
        self.addendum: AddendumApi = AddendumApi(api_client)
        self.authentication: AuthenticationApi = AuthenticationApi(api_client)
        self.cancellation: CancellationApi = CancellationApi(api_client)
        self.card: CardApi = CardApi(api_client)
        self.card_issuance: CardIssuanceApi = CardIssuanceApi(api_client)
        self.card_issue: CardIssueApi = CardIssueApi(api_client)
        self.funding: FundingApi = FundingApi(api_client)
        self.funds: FundsApi = FundsApi(api_client)
        self.merchant_payees: MerchantPayeesApi = MerchantPayeesApi(api_client)
        self.push_to_card: PushToCardApi = PushToCardApi(api_client)
        self.replay: ReplayApi = ReplayApi(api_client)
        self.return: ModelReturnApi = ModelReturnApi(api_client)
        self.sale: SaleApi = SaleApi(api_client)
        self.setting: SettingApi = SettingApi(api_client)
        self.settlement: SettlementApi = SettlementApi(api_client)
        self.status_group: StatusGroupApi = StatusGroupApi(api_client)
        self.token: TokenApi = TokenApi(api_client)
        self.transaction: TransactionApi = TransactionApi(api_client)
        self.validation: ValidationApi = ValidationApi(api_client)
        self.verification: VerificationApi = VerificationApi(api_client)
        self.void: VoidApi = VoidApi(api_client)
