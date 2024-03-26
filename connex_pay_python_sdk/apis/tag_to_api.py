import typing_extensions

from connex_pay_python_sdk.apis.tags import TagValues
from connex_pay_python_sdk.apis.tags.card_api import CardApi
from connex_pay_python_sdk.apis.tags.push_to_card_api import PushToCardApi
from connex_pay_python_sdk.apis.tags.merchant_payees_api import MerchantPayeesApi
from connex_pay_python_sdk.apis.tags.sale_api import SaleApi
from connex_pay_python_sdk.apis.tags.token_api import TokenApi
from connex_pay_python_sdk.apis.tags.transaction_api import TransactionApi
from connex_pay_python_sdk.apis.tags.addendum_api import AddendumApi
from connex_pay_python_sdk.apis.tags.accounting_api import AccountingApi
from connex_pay_python_sdk.apis.tags.authentication_api import AuthenticationApi
from connex_pay_python_sdk.apis.tags.void_api import VoidApi
from connex_pay_python_sdk.apis.tags.model_return_api import ModelReturnApi
from connex_pay_python_sdk.apis.tags.funding_api import FundingApi
from connex_pay_python_sdk.apis.tags.cancellation_api import CancellationApi
from connex_pay_python_sdk.apis.tags.verification_api import VerificationApi
from connex_pay_python_sdk.apis.tags.card_issuance_api import CardIssuanceApi
from connex_pay_python_sdk.apis.tags.status_group_api import StatusGroupApi
from connex_pay_python_sdk.apis.tags.ach_api import ACHApi
from connex_pay_python_sdk.apis.tags.card_issue_api import CardIssueApi
from connex_pay_python_sdk.apis.tags.settlement_api import SettlementApi
from connex_pay_python_sdk.apis.tags.setting_api import SettingApi
from connex_pay_python_sdk.apis.tags.replay_api import ReplayApi
from connex_pay_python_sdk.apis.tags.funds_api import FundsApi
from connex_pay_python_sdk.apis.tags.validation_api import ValidationApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.CARD: CardApi,
        TagValues.PUSH_TO_CARD: PushToCardApi,
        TagValues.MERCHANT_PAYEES: MerchantPayeesApi,
        TagValues.SALE: SaleApi,
        TagValues.TOKEN: TokenApi,
        TagValues.TRANSACTION: TransactionApi,
        TagValues.ADDENDUM: AddendumApi,
        TagValues.ACCOUNTING: AccountingApi,
        TagValues.AUTHENTICATION: AuthenticationApi,
        TagValues.VOID: VoidApi,
        TagValues.RETURN: ModelReturnApi,
        TagValues.FUNDING: FundingApi,
        TagValues.CANCELLATION: CancellationApi,
        TagValues.VERIFICATION: VerificationApi,
        TagValues.CARD_ISSUANCE: CardIssuanceApi,
        TagValues.STATUS_GROUP: StatusGroupApi,
        TagValues.ACH: ACHApi,
        TagValues.CARD_ISSUE: CardIssueApi,
        TagValues.SETTLEMENT: SettlementApi,
        TagValues.SETTING: SettingApi,
        TagValues.REPLAY: ReplayApi,
        TagValues.FUNDS: FundsApi,
        TagValues.VALIDATION: ValidationApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.CARD: CardApi,
        TagValues.PUSH_TO_CARD: PushToCardApi,
        TagValues.MERCHANT_PAYEES: MerchantPayeesApi,
        TagValues.SALE: SaleApi,
        TagValues.TOKEN: TokenApi,
        TagValues.TRANSACTION: TransactionApi,
        TagValues.ADDENDUM: AddendumApi,
        TagValues.ACCOUNTING: AccountingApi,
        TagValues.AUTHENTICATION: AuthenticationApi,
        TagValues.VOID: VoidApi,
        TagValues.RETURN: ModelReturnApi,
        TagValues.FUNDING: FundingApi,
        TagValues.CANCELLATION: CancellationApi,
        TagValues.VERIFICATION: VerificationApi,
        TagValues.CARD_ISSUANCE: CardIssuanceApi,
        TagValues.STATUS_GROUP: StatusGroupApi,
        TagValues.ACH: ACHApi,
        TagValues.CARD_ISSUE: CardIssueApi,
        TagValues.SETTLEMENT: SettlementApi,
        TagValues.SETTING: SettingApi,
        TagValues.REPLAY: ReplayApi,
        TagValues.FUNDS: FundsApi,
        TagValues.VALIDATION: ValidationApi,
    }
)
