# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from connex_pay_python_sdk.apis.tag_to_api import tag_to_api

import enum


class TagValues(str, enum.Enum):
    CARD = "Card"
    PUSH_TO_CARD = "PushToCard"
    MERCHANT_PAYEES = "MerchantPayees"
    SALE = "Sale"
    TOKEN = "Token"
    TRANSACTION = "Transaction"
    ADDENDUM = "Addendum"
    ACCOUNTING = "Accounting"
    AUTHENTICATION = "Authentication"
    VOID = "Void"
    RETURN = "Return"
    FUNDING = "Funding"
    CANCELLATION = "Cancellation"
    VERIFICATION = "Verification"
    CARD_ISSUANCE = "CardIssuance"
    STATUS_GROUP = "StatusGroup"
    ACH = "ACH"
    CARD_ISSUE = "CardIssue"
    SETTLEMENT = "Settlement"
    SETTING = "Setting"
    REPLAY = "Replay"
    FUNDS = "Funds"
    VALIDATION = "Validation"
