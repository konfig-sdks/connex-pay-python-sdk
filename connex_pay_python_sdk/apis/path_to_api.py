import typing_extensions

from connex_pay_python_sdk.paths import PathValues
from connex_pay_python_sdk.apis.paths.api_v1_token import ApiV1Token
from connex_pay_python_sdk.apis.paths.api_v1_sales import ApiV1Sales
from connex_pay_python_sdk.apis.paths.api_v1_void import ApiV1Void
from connex_pay_python_sdk.apis.paths.api_v1_returns import ApiV1Returns
from connex_pay_python_sdk.apis.paths.api_v1_cancel import ApiV1Cancel
from connex_pay_python_sdk.apis.paths.api_v1_authonlys import ApiV1Authonlys
from connex_pay_python_sdk.apis.paths.api_v1_captures import ApiV1Captures
from connex_pay_python_sdk.apis.paths.api_v1_verify import ApiV1Verify
from connex_pay_python_sdk.apis.paths.api_v1_3ds import ApiV13ds
from connex_pay_python_sdk.apis.paths.api_v1_3ds_guid import ApiV13dsGUID
from connex_pay_python_sdk.apis.paths.api_v1_sales_update_future_sale import ApiV1SalesUpdateFutureSale
from connex_pay_python_sdk.apis.paths.api_v1_sales_activate_sale_guid import ApiV1SalesActivateSaleGuid
from connex_pay_python_sdk.apis.paths.api_v1_search_sales_exportable_page_number_page_size import ApiV1SearchSalesExportablePageNumberPageSize
from connex_pay_python_sdk.apis.paths.api_v1_search_voids_exportable_page_number_page_size import ApiV1SearchVoidsExportablePageNumberPageSize
from connex_pay_python_sdk.apis.paths.api_v1_search_returns_exportable_page_number_page_size import ApiV1SearchReturnsExportablePageNumberPageSize
from connex_pay_python_sdk.apis.paths.api_v1_search_verify_exportable_page_number_page_size import ApiV1SearchVerifyExportablePageNumberPageSize
from connex_pay_python_sdk.apis.paths.api_v1_hosted_payment_page_requests import ApiV1HostedPaymentPageRequests
from connex_pay_python_sdk.apis.paths.api_v1_merchant_self_service_funding import ApiV1MerchantSelfServiceFunding
from connex_pay_python_sdk.apis.paths.api_v1_merchant_flex_funding_funds_transfer import ApiV1MerchantFlexFundingFundsTransfer
from connex_pay_python_sdk.apis.paths.api_v1_issue_card import ApiV1IssueCard
from connex_pay_python_sdk.apis.paths.api_v1_issue_card_issue_lite import ApiV1IssueCardIssueLite
from connex_pay_python_sdk.apis.paths.api_v1_issue_card_lodged_card import ApiV1IssueCardLodgedCard
from connex_pay_python_sdk.apis.paths.api_v1_issue_card_card_guid import ApiV1IssueCardCardGuid
from connex_pay_python_sdk.apis.paths.api_v1_issue_card_lodged_card_card_guid import ApiV1IssueCardLodgedCardCardGuid
from connex_pay_python_sdk.apis.paths.api_v1_terminate_card_guid import ApiV1TerminateCardGuid
from connex_pay_python_sdk.apis.paths.api_v1_issue_card_cancel_card_guid import ApiV1IssueCardCancelCardGuid
from connex_pay_python_sdk.apis.paths.api_v1_issue_card_send_payment_info_card_guid import ApiV1IssueCardSendPaymentInfoCardGuid
from connex_pay_python_sdk.apis.paths.api_v1_cards_card_guid_show_full_pan import ApiV1CardsCardGuidShowFullPan
from connex_pay_python_sdk.apis.paths.api_v1_addendum_virtual_card import ApiV1AddendumVirtualCard
from connex_pay_python_sdk.apis.paths.v1_addendum_remove_guid import V1AddendumRemoveGuid
from connex_pay_python_sdk.apis.paths.api_v1_issue_card_update_delayed_card_card_guid import ApiV1IssueCardUpdateDelayedCardCardGuid
from connex_pay_python_sdk.apis.paths.api_v1_issue_card_activate_delayed_card_card_guid import ApiV1IssueCardActivateDelayedCardCardGuid
from connex_pay_python_sdk.apis.paths.api_v1_merchants_merchant_guid_payees import ApiV1MerchantsMerchantGuidPayees
from connex_pay_python_sdk.apis.paths.api_v1_merchants_merchant_guid_payees_search_page_pagesize import ApiV1MerchantsMerchantGuidPayeesSearchPagePagesize
from connex_pay_python_sdk.apis.paths.api_v1_merchants_merchant_guid_payees_payee_guid import ApiV1MerchantsMerchantGuidPayeesPayeeGuid
from connex_pay_python_sdk.apis.paths.api_v1_push_to_card_payees import ApiV1PushToCardPayees
from connex_pay_python_sdk.apis.paths.api_v1_push_to_card_payees_payee_guid_status import ApiV1PushToCardPayeesPayeeGuidStatus
from connex_pay_python_sdk.apis.paths.api_v1_push_to_card_payees_payee_guid import ApiV1PushToCardPayeesPayeeGuid
from connex_pay_python_sdk.apis.paths.api_v1_push_to_card_payouts import ApiV1PushToCardPayouts
from connex_pay_python_sdk.apis.paths.api_v1_push_to_card_payouts_payout_guid_cancel import ApiV1PushToCardPayoutsPayoutGuidCancel
from connex_pay_python_sdk.apis.paths.api_v1_push_to_card_payouts_payout_guid import ApiV1PushToCardPayoutsPayoutGuid
from connex_pay_python_sdk.apis.paths.api_v1_push_to_card_authenticate_payment_widget import ApiV1PushToCardAuthenticatePaymentWidget
from connex_pay_python_sdk.apis.paths.api_v1_push_to_card_payments_rid_guid_card_id import ApiV1PushToCardPaymentsRidGuidCardId
from connex_pay_python_sdk.apis.paths.api_v1_issue_ach import ApiV1IssueACH
from connex_pay_python_sdk.apis.paths.api_v1_issue_ach_issue_lite import ApiV1IssueACHIssueLite
from connex_pay_python_sdk.apis.paths.api_v1_addendum_ach import ApiV1AddendumACH
from connex_pay_python_sdk.apis.paths.api_v1_merchantsupplier_settings import ApiV1MerchantsupplierSettings
from connex_pay_python_sdk.apis.paths.api_v1_cards_transactions_card_guid import ApiV1CardsTransactionsCardGuid
from connex_pay_python_sdk.apis.paths.api_v1_search_available_funds_merchant_guid import ApiV1SearchAvailableFundsMerchantGuid
from connex_pay_python_sdk.apis.paths.api_v1_purchase_event_history_resend import ApiV1PurchaseEventHistoryResend
from connex_pay_python_sdk.apis.paths.api_chargeback_get_by_user import ApiChargebackGetByUser
from connex_pay_python_sdk.apis.paths.api_v1_authenticate import ApiV1Authenticate
from connex_pay_python_sdk.apis.paths.api_v1_accounting_daily_detail import ApiV1AccountingDailyDetail
from connex_pay_python_sdk.apis.paths.api_v1_accounting_daily_summary import ApiV1AccountingDailySummary
from connex_pay_python_sdk.apis.paths.api_v1_search_issued_cards import ApiV1SearchIssuedCards
from connex_pay_python_sdk.apis.paths.api_v1_search_settlements import ApiV1SearchSettlements

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.API_V1_TOKEN: ApiV1Token,
        PathValues.API_V1_SALES: ApiV1Sales,
        PathValues.API_V1_VOID: ApiV1Void,
        PathValues.API_V1_RETURNS: ApiV1Returns,
        PathValues.API_V1_CANCEL: ApiV1Cancel,
        PathValues.API_V1_AUTHONLYS: ApiV1Authonlys,
        PathValues.API_V1_CAPTURES: ApiV1Captures,
        PathValues.API_V1_VERIFY: ApiV1Verify,
        PathValues.API_V1_3DS: ApiV13ds,
        PathValues.API_V1_3DS_GUID: ApiV13dsGUID,
        PathValues.API_V1_SALES_UPDATE_FUTURE_SALE: ApiV1SalesUpdateFutureSale,
        PathValues.API_V1_SALES_ACTIVATE_SALE_GUID: ApiV1SalesActivateSaleGuid,
        PathValues.API_V1_SEARCH_SALES_EXPORTABLE_PAGE_NUMBER_PAGE_SIZE: ApiV1SearchSalesExportablePageNumberPageSize,
        PathValues.API_V1_SEARCH_VOIDS_EXPORTABLE_PAGE_NUMBER_PAGE_SIZE: ApiV1SearchVoidsExportablePageNumberPageSize,
        PathValues.API_V1_SEARCH_RETURNS_EXPORTABLE_PAGE_NUMBER_PAGE_SIZE: ApiV1SearchReturnsExportablePageNumberPageSize,
        PathValues.API_V1_SEARCH_VERIFY_EXPORTABLE_PAGE_NUMBER_PAGE_SIZE: ApiV1SearchVerifyExportablePageNumberPageSize,
        PathValues.API_V1_HOSTED_PAYMENT_PAGE_REQUESTS: ApiV1HostedPaymentPageRequests,
        PathValues.API_V1_MERCHANT_SELF_SERVICE_FUNDING: ApiV1MerchantSelfServiceFunding,
        PathValues.API_V1_MERCHANT_FLEX_FUNDING_FUNDS_TRANSFER: ApiV1MerchantFlexFundingFundsTransfer,
        PathValues.API_V1_ISSUE_CARD: ApiV1IssueCard,
        PathValues.API_V1_ISSUE_CARD_ISSUE_LITE: ApiV1IssueCardIssueLite,
        PathValues.API_V1_ISSUE_CARD_LODGED_CARD: ApiV1IssueCardLodgedCard,
        PathValues.API_V1_ISSUE_CARD_CARD_GUID: ApiV1IssueCardCardGuid,
        PathValues.API_V1_ISSUE_CARD_LODGED_CARD_CARD_GUID: ApiV1IssueCardLodgedCardCardGuid,
        PathValues.API_V1_TERMINATE_CARD_GUID: ApiV1TerminateCardGuid,
        PathValues.API_V1_ISSUE_CARD_CANCEL_CARD_GUID: ApiV1IssueCardCancelCardGuid,
        PathValues.API_V1_ISSUE_CARD_SEND_PAYMENT_INFO_CARD_GUID: ApiV1IssueCardSendPaymentInfoCardGuid,
        PathValues.API_V1_CARDS_CARD_GUID_SHOW_FULL_PAN: ApiV1CardsCardGuidShowFullPan,
        PathValues.API_V1_ADDENDUM_VIRTUAL_CARD: ApiV1AddendumVirtualCard,
        PathValues.V1_ADDENDUM_REMOVE_GUID: V1AddendumRemoveGuid,
        PathValues.API_V1_ISSUE_CARD_UPDATE_DELAYED_CARD_CARD_GUID: ApiV1IssueCardUpdateDelayedCardCardGuid,
        PathValues.API_V1_ISSUE_CARD_ACTIVATE_DELAYED_CARD_CARD_GUID: ApiV1IssueCardActivateDelayedCardCardGuid,
        PathValues.API_V1_MERCHANTS_MERCHANT_GUID_PAYEES: ApiV1MerchantsMerchantGuidPayees,
        PathValues.API_V1_MERCHANTS_MERCHANT_GUID_PAYEES_SEARCH_PAGE_PAGESIZE: ApiV1MerchantsMerchantGuidPayeesSearchPagePagesize,
        PathValues.API_V1_MERCHANTS_MERCHANT_GUID_PAYEES_PAYEE_GUID: ApiV1MerchantsMerchantGuidPayeesPayeeGuid,
        PathValues.API_V1_PUSH_TO_CARD_PAYEES: ApiV1PushToCardPayees,
        PathValues.API_V1_PUSH_TO_CARD_PAYEES_PAYEE_GUID_STATUS: ApiV1PushToCardPayeesPayeeGuidStatus,
        PathValues.API_V1_PUSH_TO_CARD_PAYEES_PAYEE_GUID: ApiV1PushToCardPayeesPayeeGuid,
        PathValues.API_V1_PUSH_TO_CARD_PAYOUTS: ApiV1PushToCardPayouts,
        PathValues.API_V1_PUSH_TO_CARD_PAYOUTS_PAYOUT_GUID_CANCEL: ApiV1PushToCardPayoutsPayoutGuidCancel,
        PathValues.API_V1_PUSH_TO_CARD_PAYOUTS_PAYOUT_GUID: ApiV1PushToCardPayoutsPayoutGuid,
        PathValues.API_V1_PUSH_TO_CARD_AUTHENTICATE_PAYMENT_WIDGET: ApiV1PushToCardAuthenticatePaymentWidget,
        PathValues.API_V1_PUSH_TO_CARD_PAYMENTS_RID_GUID_CARD_ID: ApiV1PushToCardPaymentsRidGuidCardId,
        PathValues.API_V1_ISSUE_ACH: ApiV1IssueACH,
        PathValues.API_V1_ISSUE_ACH_ISSUE_LITE: ApiV1IssueACHIssueLite,
        PathValues.API_V1_ADDENDUM_ACH: ApiV1AddendumACH,
        PathValues.API_V1_MERCHANTSUPPLIER_SETTINGS: ApiV1MerchantsupplierSettings,
        PathValues.API_V1_CARDS_TRANSACTIONS_CARD_GUID: ApiV1CardsTransactionsCardGuid,
        PathValues.API_V1_SEARCH_AVAILABLE_FUNDS_MERCHANT_GUID: ApiV1SearchAvailableFundsMerchantGuid,
        PathValues.API_V1_PURCHASE_EVENT_HISTORY_RESEND: ApiV1PurchaseEventHistoryResend,
        PathValues.API_CHARGEBACK_GET_BY_USER: ApiChargebackGetByUser,
        PathValues.API_V1_AUTHENTICATE: ApiV1Authenticate,
        PathValues.API_V1_ACCOUNTING_DAILY_DETAIL: ApiV1AccountingDailyDetail,
        PathValues.API_V1_ACCOUNTING_DAILY_SUMMARY: ApiV1AccountingDailySummary,
        PathValues.API_V1_SEARCH_ISSUED_CARDS: ApiV1SearchIssuedCards,
        PathValues.API_V1_SEARCH_SETTLEMENTS: ApiV1SearchSettlements,
    }
)

path_to_api = PathToApi(
    {
        PathValues.API_V1_TOKEN: ApiV1Token,
        PathValues.API_V1_SALES: ApiV1Sales,
        PathValues.API_V1_VOID: ApiV1Void,
        PathValues.API_V1_RETURNS: ApiV1Returns,
        PathValues.API_V1_CANCEL: ApiV1Cancel,
        PathValues.API_V1_AUTHONLYS: ApiV1Authonlys,
        PathValues.API_V1_CAPTURES: ApiV1Captures,
        PathValues.API_V1_VERIFY: ApiV1Verify,
        PathValues.API_V1_3DS: ApiV13ds,
        PathValues.API_V1_3DS_GUID: ApiV13dsGUID,
        PathValues.API_V1_SALES_UPDATE_FUTURE_SALE: ApiV1SalesUpdateFutureSale,
        PathValues.API_V1_SALES_ACTIVATE_SALE_GUID: ApiV1SalesActivateSaleGuid,
        PathValues.API_V1_SEARCH_SALES_EXPORTABLE_PAGE_NUMBER_PAGE_SIZE: ApiV1SearchSalesExportablePageNumberPageSize,
        PathValues.API_V1_SEARCH_VOIDS_EXPORTABLE_PAGE_NUMBER_PAGE_SIZE: ApiV1SearchVoidsExportablePageNumberPageSize,
        PathValues.API_V1_SEARCH_RETURNS_EXPORTABLE_PAGE_NUMBER_PAGE_SIZE: ApiV1SearchReturnsExportablePageNumberPageSize,
        PathValues.API_V1_SEARCH_VERIFY_EXPORTABLE_PAGE_NUMBER_PAGE_SIZE: ApiV1SearchVerifyExportablePageNumberPageSize,
        PathValues.API_V1_HOSTED_PAYMENT_PAGE_REQUESTS: ApiV1HostedPaymentPageRequests,
        PathValues.API_V1_MERCHANT_SELF_SERVICE_FUNDING: ApiV1MerchantSelfServiceFunding,
        PathValues.API_V1_MERCHANT_FLEX_FUNDING_FUNDS_TRANSFER: ApiV1MerchantFlexFundingFundsTransfer,
        PathValues.API_V1_ISSUE_CARD: ApiV1IssueCard,
        PathValues.API_V1_ISSUE_CARD_ISSUE_LITE: ApiV1IssueCardIssueLite,
        PathValues.API_V1_ISSUE_CARD_LODGED_CARD: ApiV1IssueCardLodgedCard,
        PathValues.API_V1_ISSUE_CARD_CARD_GUID: ApiV1IssueCardCardGuid,
        PathValues.API_V1_ISSUE_CARD_LODGED_CARD_CARD_GUID: ApiV1IssueCardLodgedCardCardGuid,
        PathValues.API_V1_TERMINATE_CARD_GUID: ApiV1TerminateCardGuid,
        PathValues.API_V1_ISSUE_CARD_CANCEL_CARD_GUID: ApiV1IssueCardCancelCardGuid,
        PathValues.API_V1_ISSUE_CARD_SEND_PAYMENT_INFO_CARD_GUID: ApiV1IssueCardSendPaymentInfoCardGuid,
        PathValues.API_V1_CARDS_CARD_GUID_SHOW_FULL_PAN: ApiV1CardsCardGuidShowFullPan,
        PathValues.API_V1_ADDENDUM_VIRTUAL_CARD: ApiV1AddendumVirtualCard,
        PathValues.V1_ADDENDUM_REMOVE_GUID: V1AddendumRemoveGuid,
        PathValues.API_V1_ISSUE_CARD_UPDATE_DELAYED_CARD_CARD_GUID: ApiV1IssueCardUpdateDelayedCardCardGuid,
        PathValues.API_V1_ISSUE_CARD_ACTIVATE_DELAYED_CARD_CARD_GUID: ApiV1IssueCardActivateDelayedCardCardGuid,
        PathValues.API_V1_MERCHANTS_MERCHANT_GUID_PAYEES: ApiV1MerchantsMerchantGuidPayees,
        PathValues.API_V1_MERCHANTS_MERCHANT_GUID_PAYEES_SEARCH_PAGE_PAGESIZE: ApiV1MerchantsMerchantGuidPayeesSearchPagePagesize,
        PathValues.API_V1_MERCHANTS_MERCHANT_GUID_PAYEES_PAYEE_GUID: ApiV1MerchantsMerchantGuidPayeesPayeeGuid,
        PathValues.API_V1_PUSH_TO_CARD_PAYEES: ApiV1PushToCardPayees,
        PathValues.API_V1_PUSH_TO_CARD_PAYEES_PAYEE_GUID_STATUS: ApiV1PushToCardPayeesPayeeGuidStatus,
        PathValues.API_V1_PUSH_TO_CARD_PAYEES_PAYEE_GUID: ApiV1PushToCardPayeesPayeeGuid,
        PathValues.API_V1_PUSH_TO_CARD_PAYOUTS: ApiV1PushToCardPayouts,
        PathValues.API_V1_PUSH_TO_CARD_PAYOUTS_PAYOUT_GUID_CANCEL: ApiV1PushToCardPayoutsPayoutGuidCancel,
        PathValues.API_V1_PUSH_TO_CARD_PAYOUTS_PAYOUT_GUID: ApiV1PushToCardPayoutsPayoutGuid,
        PathValues.API_V1_PUSH_TO_CARD_AUTHENTICATE_PAYMENT_WIDGET: ApiV1PushToCardAuthenticatePaymentWidget,
        PathValues.API_V1_PUSH_TO_CARD_PAYMENTS_RID_GUID_CARD_ID: ApiV1PushToCardPaymentsRidGuidCardId,
        PathValues.API_V1_ISSUE_ACH: ApiV1IssueACH,
        PathValues.API_V1_ISSUE_ACH_ISSUE_LITE: ApiV1IssueACHIssueLite,
        PathValues.API_V1_ADDENDUM_ACH: ApiV1AddendumACH,
        PathValues.API_V1_MERCHANTSUPPLIER_SETTINGS: ApiV1MerchantsupplierSettings,
        PathValues.API_V1_CARDS_TRANSACTIONS_CARD_GUID: ApiV1CardsTransactionsCardGuid,
        PathValues.API_V1_SEARCH_AVAILABLE_FUNDS_MERCHANT_GUID: ApiV1SearchAvailableFundsMerchantGuid,
        PathValues.API_V1_PURCHASE_EVENT_HISTORY_RESEND: ApiV1PurchaseEventHistoryResend,
        PathValues.API_CHARGEBACK_GET_BY_USER: ApiChargebackGetByUser,
        PathValues.API_V1_AUTHENTICATE: ApiV1Authenticate,
        PathValues.API_V1_ACCOUNTING_DAILY_DETAIL: ApiV1AccountingDailyDetail,
        PathValues.API_V1_ACCOUNTING_DAILY_SUMMARY: ApiV1AccountingDailySummary,
        PathValues.API_V1_SEARCH_ISSUED_CARDS: ApiV1SearchIssuedCards,
        PathValues.API_V1_SEARCH_SETTLEMENTS: ApiV1SearchSettlements,
    }
)
