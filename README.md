<div align="center">

[![Visit Connexpay](./header.png)](https://connexpay.com&#x2F;)

# Connexpay<a id="connexpay"></a>

REST API for retrieving reporting data. Currently Daily Accounting data only.


</div>

## Table of Contents<a id="table-of-contents"></a>

<!-- toc -->

- [Requirements](#requirements)
- [Installation](#installation)
- [Getting Started](#getting-started)
- [Async](#async)
- [Raw HTTP Response](#raw-http-response)
- [Reference](#reference)
  * [`connexpay.ach.create_credit_payment`](#connexpayachcreate_credit_payment)
  * [`connexpay.accounting.get_daily_detail`](#connexpayaccountingget_daily_detail)
  * [`connexpay.accounting.get_daily_summary`](#connexpayaccountingget_daily_summary)
  * [`connexpay.addendum.create_ach_purchase`](#connexpayaddendumcreate_ach_purchase)
  * [`connexpay.addendum.create_virtual_card`](#connexpayaddendumcreate_virtual_card)
  * [`connexpay.addendum.delete_item`](#connexpayaddendumdelete_item)
  * [`connexpay.authentication.acquire_client_authorization`](#connexpayauthenticationacquire_client_authorization)
  * [`connexpay.authentication.obtain3d_secure_authentication`](#connexpayauthenticationobtain3d_secure_authentication)
  * [`connexpay.cancellation.entire_trip_cancellation`](#connexpaycancellationentire_trip_cancellation)
  * [`connexpay.card.activate_delayed`](#connexpaycardactivate_delayed)
  * [`connexpay.card.cancel_virtual_card`](#connexpaycardcancel_virtual_card)
  * [`connexpay.card.create_lodged_card`](#connexpaycardcreate_lodged_card)
  * [`connexpay.card.get_detail`](#connexpaycardget_detail)
  * [`connexpay.card.resend_transmission_info`](#connexpaycardresend_transmission_info)
  * [`connexpay.card.search_issued_virtual_cards`](#connexpaycardsearch_issued_virtual_cards)
  * [`connexpay.card.terminate_by_date`](#connexpaycardterminate_by_date)
  * [`connexpay.card.update_card_details`](#connexpaycardupdate_card_details)
  * [`connexpay.card.update_delayed_activation`](#connexpaycardupdate_delayed_activation)
  * [`connexpay.card.update_lodged_card`](#connexpaycardupdate_lodged_card)
  * [`connexpay.card_issuance.create_virtual_card`](#connexpaycard_issuancecreate_virtual_card)
  * [`connexpay.card_issue.create_virtual_card_lite`](#connexpaycard_issuecreate_virtual_card_lite)
  * [`connexpay.funding.merchant_cash_balance`](#connexpayfundingmerchant_cash_balance)
  * [`connexpay.funding.transfer_merchant_cash_balance`](#connexpayfundingtransfer_merchant_cash_balance)
  * [`connexpay.funds.get_available_details`](#connexpayfundsget_available_details)
  * [`connexpay.merchant_payees.create_payee`](#connexpaymerchant_payeescreate_payee)
  * [`connexpay.merchant_payees.delete_payee`](#connexpaymerchant_payeesdelete_payee)
  * [`connexpay.merchant_payees.get_payee`](#connexpaymerchant_payeesget_payee)
  * [`connexpay.merchant_payees.get_payees`](#connexpaymerchant_payeesget_payees)
  * [`connexpay.merchant_payees.update_payee`](#connexpaymerchant_payeesupdate_payee)
  * [`connexpay.push_to_card.cancel_payments`](#connexpaypush_to_cardcancel_payments)
  * [`connexpay.push_to_card.create_payee`](#connexpaypush_to_cardcreate_payee)
  * [`connexpay.push_to_card.create_payout`](#connexpaypush_to_cardcreate_payout)
  * [`connexpay.push_to_card.get_authentication_token_async`](#connexpaypush_to_cardget_authentication_token_async)
  * [`connexpay.push_to_card.get_payee`](#connexpaypush_to_cardget_payee)
  * [`connexpay.push_to_card.get_payout_details`](#connexpaypush_to_cardget_payout_details)
  * [`connexpay.push_to_card.manage_payee`](#connexpaypush_to_cardmanage_payee)
  * [`connexpay.push_to_card.push_funds_to_card_async`](#connexpaypush_to_cardpush_funds_to_card_async)
  * [`connexpay.push_to_card.update_payee`](#connexpaypush_to_cardupdate_payee)
  * [`connexpay.replay.purchase_event_history_resend`](#connexpayreplaypurchase_event_history_resend)
  * [`connexpay.return.item_request`](#connexpayreturnitem_request)
  * [`connexpay.return.search_sale_returns`](#connexpayreturnsearch_sale_returns)
  * [`connexpay.sale.activate_delayed`](#connexpaysaleactivate_delayed)
  * [`connexpay.sale.create_transaction`](#connexpaysalecreate_transaction)
  * [`connexpay.sale.get_chargebacks_by_user`](#connexpaysaleget_chargebacks_by_user)
  * [`connexpay.sale.search_sales`](#connexpaysalesearch_sales)
  * [`connexpay.sale.update_delayed_activation`](#connexpaysaleupdate_delayed_activation)
  * [`connexpay.setting.tokenize_bank_account_info`](#connexpaysettingtokenize_bank_account_info)
  * [`connexpay.settlement.search_virtual_card_settlements`](#connexpaysettlementsearch_virtual_card_settlements)
  * [`connexpay.status_group.call_3ds_authentication_status`](#connexpaystatus_groupcall_3ds_authentication_status)
  * [`connexpay.token.generate_reporting_token`](#connexpaytokengenerate_reporting_token)
  * [`connexpay.token.issue_authentication_token`](#connexpaytokenissue_authentication_token)
  * [`connexpay.token.request_hpp_token`](#connexpaytokenrequest_hpp_token)
  * [`connexpay.transaction.capture_authorization`](#connexpaytransactioncapture_authorization)
  * [`connexpay.transaction.create_ach_credit_payment`](#connexpaytransactioncreate_ach_credit_payment)
  * [`connexpay.transaction.search_virtual_card_history`](#connexpaytransactionsearch_virtual_card_history)
  * [`connexpay.validation.search_verify_operation`](#connexpayvalidationsearch_verify_operation)
  * [`connexpay.verification.card_bank_account`](#connexpayverificationcard_bank_account)
  * [`connexpay.void.create_void`](#connexpayvoidcreate_void)
  * [`connexpay.void.search_voids`](#connexpayvoidsearch_voids)

<!-- tocstop -->

## Requirements<a id="requirements"></a>

Python >=3.7

## Installation<a id="installation"></a>
<div align="center">
  <a href="https://konfigthis.com/sdk-sign-up?company=ConnexPay&language=Python">
    <img src="https://raw.githubusercontent.com/konfig-dev/brand-assets/HEAD/cta-images/python-cta.png" width="70%">
  </a>
</div>

## Getting Started<a id="getting-started"></a>

```python
from pprint import pprint
from connex_pay_python_sdk import ConnexPay, ApiException

connexpay = ConnexPay(

    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

try:
    # Issue ACH Lite
    create_credit_payment_response = connexpay.ach.create_credit_payment(
        merchant_guid="string_example",
        amount=3.14,
        payee_name="string_example",
        account_holder={
        "business_name": "Default",
    },
        statement_company_name="Merchant Alias",
        description="string_example",
        order_number="7H2345",
        sequence_number="string_example",
        association_id="string_example",
    )
    print(create_credit_payment_response)
except ApiException as e:
    print("Exception when calling ACHApi.create_credit_payment: %s\n" % e)
    pprint(e.body)
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```

## Async<a id="async"></a>

`async` support is available by prepending `a` to any method.

```python

import asyncio
from pprint import pprint
from connex_pay_python_sdk import ConnexPay, ApiException

connexpay = ConnexPay(

    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

async def main():
    try:
        # Issue ACH Lite
        create_credit_payment_response = await connexpay.ach.acreate_credit_payment(
            merchant_guid="string_example",
            amount=3.14,
            payee_name="string_example",
            account_holder={
        "business_name": "Default",
    },
            statement_company_name="Merchant Alias",
            description="string_example",
            order_number="7H2345",
            sequence_number="string_example",
            association_id="string_example",
        )
        print(create_credit_payment_response)
    except ApiException as e:
        print("Exception when calling ACHApi.create_credit_payment: %s\n" % e)
        pprint(e.body)
        pprint(e.headers)
        pprint(e.status)
        pprint(e.reason)
        pprint(e.round_trip_time)

asyncio.run(main())
```

## Raw HTTP Response<a id="raw-http-response"></a>

To access raw HTTP response values, use the `.raw` namespace.

```python
from pprint import pprint
from connex_pay_python_sdk import ConnexPay, ApiException

connexpay = ConnexPay(

    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

try:
    # Issue ACH Lite
    create_credit_payment_response = connexpay.ach.raw.create_credit_payment(
        merchant_guid="string_example",
        amount=3.14,
        payee_name="string_example",
        account_holder={
        "business_name": "Default",
    },
        statement_company_name="Merchant Alias",
        description="string_example",
        order_number="7H2345",
        sequence_number="string_example",
        association_id="string_example",
    )
    pprint(create_credit_payment_response.body)
    pprint(create_credit_payment_response.body["description"])
    pprint(create_credit_payment_response.body["merchant_id"])
    pprint(create_credit_payment_response.body["incoming_transaction_code"])
    pprint(create_credit_payment_response.body["payment_id"])
    pprint(create_credit_payment_response.body["is_credit"])
    pprint(create_credit_payment_response.body["amount"])
    pprint(create_credit_payment_response.body["payee_name"])
    pprint(create_credit_payment_response.body["payment_status"])
    pprint(create_credit_payment_response.body["schedule_date"])
    pprint(create_credit_payment_response.body["receipt_date"])
    pprint(create_credit_payment_response.body["processing_date"])
    pprint(create_credit_payment_response.headers)
    pprint(create_credit_payment_response.status)
    pprint(create_credit_payment_response.round_trip_time)
except ApiException as e:
    print("Exception when calling ACHApi.create_credit_payment: %s\n" % e)
    pprint(e.body)
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```


## Reference<a id="reference"></a>
### `connexpay.ach.create_credit_payment`<a id="connexpayachcreate_credit_payment"></a>

This endpoint creates an ACH Credit payment that does not have an associated sale. This allows ConnexPay Lite clients to submit the issue payment call only.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_credit_payment_response = connexpay.ach.create_credit_payment(
    merchant_guid="string_example",
    amount=3.14,
    payee_name="string_example",
    account_holder={
        "business_name": "Default",
    },
    statement_company_name="Merchant Alias",
    description="string_example",
    order_number="7H2345",
    sequence_number="string_example",
    association_id="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### merchant_guid: `str`<a id="merchant_guid-str"></a>

Merchant's guid. Application level value that indicates the ACH payment is being requested for clients account. Value provided by ConnexPay.

##### amount: `Union[int, float]`<a id="amount-unionint-float"></a>

Payment amount with the minimum amount > 0.5.

##### payee_name: `str`<a id="payee_name-str"></a>

Payee name up to 100 characters.

##### account_holder: [`AchCreateCreditPaymentRequestAccountHolder`](./connex_pay_python_sdk/type/ach_create_credit_payment_request_account_holder.py)<a id="account_holder-achcreatecreditpaymentrequestaccountholderconnex_pay_python_sdktypeach_create_credit_payment_request_account_holderpy"></a>


##### statement_company_name: `str`<a id="statement_company_name-str"></a>

Company Name to display Bank Statement. The first 16 characters will display on the bank account holders statement.

##### description: `str`<a id="description-str"></a>

For banks who accept statement descriptors, the first 10 characters will display on the bank account holders statement.

##### order_number: `str`<a id="order_number-str"></a>

This is the most common number you'll see throughout the ConnexPay Portal.  Transaction ID within client environment associated with the order. The value is searchable and reportable in the ConnexPay portal. This value may be sent in multiple instances of the integration for multiple purposes. Customers in the travel space often send the Record Locator/PNR in this field.  The maximum length is 50 alpha-numeric characters.

##### sequence_number: `str`<a id="sequence_number-str"></a>

Transaction sequence number within client environment. Note: value is not searchable or reportable in ConnexPay portal.  Alphanumeric.

##### association_id: `str`<a id="association_id-str"></a>

This parameter allows you to input an up to 100 character association ID that can be used to tie this ACH Purchase to a sale (Association ID also needs to be included on the sale request). This is useful if you issue the ACH purchase prior to creating the sale that associates to it.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`AchCreateCreditPaymentRequest`](./connex_pay_python_sdk/type/ach_create_credit_payment_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`AchCreateCreditPaymentResponse`](./connex_pay_python_sdk/pydantic/ach_create_credit_payment_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/IssueACH/IssueLite` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `connexpay.accounting.get_daily_detail`<a id="connexpayaccountingget_daily_detail"></a>

This endpoint returns the paginated daily accounting detail items of a client for a given release date.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_daily_detail_response = connexpay.accounting.get_daily_detail(
    merchant_guid="ab0123f5-7648-4e27-8709-ad0f4e162c20",
    released_date="2022-12-31",
    page_number=1,
    page_size=10,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### merchant_guid: `str`<a id="merchant_guid-str"></a>

The client identifier for the requested transactions.

##### released_date: `date`<a id="released_date-date"></a>

Date on which the requested transactions were released to the client.

##### page_number: `int`<a id="page_number-int"></a>

##### page_size: `int`<a id="page_size-int"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`DailyAccountingDetailPaginatedItems`](./connex_pay_python_sdk/pydantic/daily_accounting_detail_paginated_items.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/Accounting/DailyDetail` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `connexpay.accounting.get_daily_summary`<a id="connexpayaccountingget_daily_summary"></a>

This endpoint returns the daily accounting summary of a merchant for a given release date.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_daily_summary_response = connexpay.accounting.get_daily_summary(
    merchant_guid="ab0123f5-7648-4e27-8709-ad0f4e162c20",
    released_date="2022-12-31",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### merchant_guid: `str`<a id="merchant_guid-str"></a>

The client identifier for the requested transactions.

##### released_date: `date`<a id="released_date-date"></a>

Date on which the requested transactions were released to the client.

#### 🔄 Return<a id="🔄-return"></a>

[`DailyAccountingSummary`](./connex_pay_python_sdk/pydantic/daily_accounting_summary.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/Accounting/DailySummary` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `connexpay.addendum.create_ach_purchase`<a id="connexpayaddendumcreate_ach_purchase"></a>

ACH Purchase Addendum

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_ach_purchase_response = connexpay.addendum.create_ach_purchase(
    item_guid="Mandatory",
    value="Mandatory",
    category="Optional",
    id_external="Optional",
    note="Optional",
    sequence="Optional",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### item_guid: `str`<a id="item_guid-str"></a>

Guid for the ACH Purchase you are attaching information to with this addendum request. This Guid was returned to client when the ACH Purchase was initially created.

##### value: `str`<a id="value-str"></a>

Character data to associate with the Virtual card.

##### category: `str`<a id="category-str"></a>

Can be used by client to specify a desired category for an Addenda item. Consistent category parameters will aid in reporting consistently. See note below regarding the \\\"MultipleSales\\\" category and how to use the category specifically to associate an ACH Purchase to an existing sale(s).

##### id_external: `str`<a id="id_external-str"></a>

Can be supplied by client to associate this addendum with an ID in client's data.

##### note: `str`<a id="note-str"></a>

Additional information to associate with this addendum, as desired.

##### sequence: `str`<a id="sequence-str"></a>

If client creates multiple addenda for a single ACH Purchase this sequence can be specified if a client desires.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`AddendumCreateAchPurchaseRequest`](./connex_pay_python_sdk/type/addendum_create_ach_purchase_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`AddendumCreateAchPurchaseResponse`](./connex_pay_python_sdk/pydantic/addendum_create_ach_purchase_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/Addendum/ACH` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `connexpay.addendum.create_virtual_card`<a id="connexpayaddendumcreate_virtual_card"></a>

Virtual Card Addendum

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_virtual_card_response = connexpay.addendum.create_virtual_card(
    item_guid="Mandatory",
    value="Mandatory",
    category="Optional",
    id_external="Optional",
    note="Optional",
    sequence="Optional",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### item_guid: `str`<a id="item_guid-str"></a>

Guid for the Virtual Card you are attaching information to with this addendum request. This Guid was returned to client when the Virtual Card was initially created.

##### value: `str`<a id="value-str"></a>

Character data to associate with the Virtual card.

##### category: `str`<a id="category-str"></a>

Can be used by client to specify a desired category for an Addenda item.

##### id_external: `str`<a id="id_external-str"></a>

Can be supplied by client to associate this addendum with an ID in client's data.

##### note: `str`<a id="note-str"></a>

Additional information to associate with this addendum, as desired.

##### sequence: `str`<a id="sequence-str"></a>

If client creates multiple addenda for a single Virtual Card this sequence can be specified if a client desires.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`AddendumCreateVirtualCardRequest`](./connex_pay_python_sdk/type/addendum_create_virtual_card_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`AddendumCreateVirtualCardResponse`](./connex_pay_python_sdk/pydantic/addendum_create_virtual_card_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/Addendum/VirtualCard` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `connexpay.addendum.delete_item`<a id="connexpayaddendumdelete_item"></a>

This endpoint deletes an Addendum information item from an object.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
delete_item_response = connexpay.addendum.delete_item(
    guid="Guid_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### guid: `str`<a id="guid-str"></a>

The Addendum guid to terminate.

#### 🔄 Return<a id="🔄-return"></a>

[`AddendumDeleteItemResponse`](./connex_pay_python_sdk/pydantic/addendum_delete_item_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/Addendum/Remove/&lt;guid&gt;` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `connexpay.authentication.acquire_client_authorization`<a id="connexpayauthenticationacquire_client_authorization"></a>

The Auth Only Endpoint is applicable to acquiring clients.  Call Auth Only when you want to process an Authorization only, which will not settle until it's Captured.  We do not allow you to Capture an Authorization after 5 business days have passed.Calling this endpoint will authorize the card, however, it will not be settled until the [Capture endpoint](https://docs.connexpay.com/reference/capture) is called. Authorizations expire after 5 days.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
acquire_client_authorization_response = connexpay.authentication.acquire_client_authorization(
    device_guid="string_example",
    amount=3.14,
    risk_data={
    },
    sequence_number="string_example",
    order_number="string_example",
    send_receipt=True,
    statement_description="string_example",
    customer_id="string_example",
    card={
        "is_recurring": False,
    },
    bank_account={
        "account_type": "account_type_example",
        "routing_number": "routing_number_example",
        "account_number": "account_number_example",
        "name_on_account": "name_on_account_example",
    },
    customer={
    },
    enhanced_data={
    },
    association_id="string_example",
    browser_data={
        "acceptance_header": "acceptance_header_example",
        "color_depth": 1,
        "java_enabled": True,
        "screen_height": 1,
        "screen_width": 1,
        "time_zone_offset": 1,
        "language": "language_example",
        "redirect_url": "redirect_url_example",
        "user_agent_header": "user_agent_header_example",
    },
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### device_guid: `str`<a id="device_guid-str"></a>

Device's Guid provided by ConnexPay.

##### amount: `Union[int, float]`<a id="amount-unionint-float"></a>

Amount of the transaction that will be processed. Note: this value is submitted multiple times (in different formats) within the integration to support different purposes i.e. risk analysis, merchant processing, etc.  The minimum amount is: $0.50.

##### risk_data: [`AuthenticationAcquireClientAuthorizationRequestRiskData`](./connex_pay_python_sdk/type/authentication_acquire_client_authorization_request_risk_data.py)<a id="risk_data-authenticationacquireclientauthorizationrequestriskdataconnex_pay_python_sdktypeauthentication_acquire_client_authorization_request_risk_datapy"></a>


##### sequence_number: `str`<a id="sequence_number-str"></a>

Transaction sequence number within client environment. Provide a unique SequenceNumber for each new request. If the same value is sent within 30 minutes it will be considered a duplicate request. Note: value is not searchable or reportable in ConnexPay portal.  Alphanumeric.

##### order_number: `str`<a id="order_number-str"></a>

This is the most common number you'll see throughout the ConnexPay Portal.  Transaction ID within client environment associated with the order. The value is searchable and reportable in the ConnexPay portal. This value may be sent in multiple instances of the integration for multiple purposes. Customers in the travel space often send the Record Locator/PNR in this field.  The maximum length is 50 alpha-numeric characters.

##### send_receipt: `bool`<a id="send_receipt-bool"></a>

Value determines whether or not a customer shall be emailed a receipt from the ConnexPay platform if the email address is provided in the API customer block. The default value is TRUE. Set to FALSE so that an email receipt is not sent to the customer. Set to TRUE or leave empty if you want e-mail to be sent. If TRUE, customer's email must be included in the \\\"Card.Customer.email\\\" parameter.

##### statement_description: `str`<a id="statement_description-str"></a>

US Clients only: The statement description allows a client to customize the Merchant name that appears on the cardholder statement such that the cardholder recognizes the transaction on their statement. ConnexPay recommends sending a recognizable DBA along with the PNR i.e. ABC Travel ABC123. Note: functionality not applicable for American Express OptBlue program.  The maximun length is 25 alpha-numeric characters.

##### customer_id: `str`<a id="customer_id-str"></a>

Transaction ID within client environment associated with the customer. This value acts as a secondary identifier in conjunction with OrderNumber. The value is searchable and reportable in the ConnexPay portal. This value may be sent in multiple times within the integration for multiple purposes.  The maximum length is 100 characters and is alpha-numeric.

##### card: [`AuthenticationAcquireClientAuthorizationRequestCard`](./connex_pay_python_sdk/type/authentication_acquire_client_authorization_request_card.py)<a id="card-authenticationacquireclientauthorizationrequestcardconnex_pay_python_sdktypeauthentication_acquire_client_authorization_request_cardpy"></a>


##### bank_account: [`AuthenticationAcquireClientAuthorizationRequestBankAccount`](./connex_pay_python_sdk/type/authentication_acquire_client_authorization_request_bank_account.py)<a id="bank_account-authenticationacquireclientauthorizationrequestbankaccountconnex_pay_python_sdktypeauthentication_acquire_client_authorization_request_bank_accountpy"></a>


##### customer: [`AuthenticationAcquireClientAuthorizationRequestCustomer`](./connex_pay_python_sdk/type/authentication_acquire_client_authorization_request_customer.py)<a id="customer-authenticationacquireclientauthorizationrequestcustomerconnex_pay_python_sdktypeauthentication_acquire_client_authorization_request_customerpy"></a>


##### enhanced_data: [`AuthenticationAcquireClientAuthorizationRequestEnhancedData`](./connex_pay_python_sdk/type/authentication_acquire_client_authorization_request_enhanced_data.py)<a id="enhanced_data-authenticationacquireclientauthorizationrequestenhanceddataconnex_pay_python_sdktypeauthentication_acquire_client_authorization_request_enhanced_datapy"></a>


##### association_id: `str`<a id="association_id-str"></a>

Utilize the Association ID field to tie a virtual card to a sale or sales. For example, if you have several sales and one virtual card payment to a supplier, you can add association ID to the sales and the virtual card for downstream reporting.

##### browser_data: [`AuthenticationAcquireClientAuthorizationRequestBrowserData`](./connex_pay_python_sdk/type/authentication_acquire_client_authorization_request_browser_data.py)<a id="browser_data-authenticationacquireclientauthorizationrequestbrowserdataconnex_pay_python_sdktypeauthentication_acquire_client_authorization_request_browser_datapy"></a>


#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`AuthenticationAcquireClientAuthorizationRequest`](./connex_pay_python_sdk/type/authentication_acquire_client_authorization_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`AuthenticationAcquireClientAuthorizationResponse`](./connex_pay_python_sdk/pydantic/authentication_acquire_client_authorization_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/authonlys` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `connexpay.authentication.obtain3d_secure_authentication`<a id="connexpayauthenticationobtain3d_secure_authentication"></a>

This endpoint can be used for obtaining 3D Secure Authentication separate from the Create Sale or Auth-Only calls.  This is recommended for our US and CA clients.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
obtain3d_secure_authentication_response = connexpay.authentication.obtain3d_secure_authentication(
    card={
        "is_recurring": False,
    },
    device_guid="{{deviceGuid}}",
    browser_data={
        "acceptance_header": "acceptance_header_example",
        "color_depth": 1,
        "java_enabled": True,
        "screen_height": 1,
        "screen_width": 1,
        "time_zone_offset": 1,
        "language": "language_example",
        "redirect_url": "redirect_url_example",
        "user_agent_header": "user_agent_header_example",
    },
    amount=3.14,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### card: [`AuthenticationObtain3DSecureAuthenticationRequestCard`](./connex_pay_python_sdk/type/authentication_obtain3_d_secure_authentication_request_card.py)<a id="card-authenticationobtain3dsecureauthenticationrequestcardconnex_pay_python_sdktypeauthentication_obtain3_d_secure_authentication_request_cardpy"></a>


##### device_guid: `str`<a id="device_guid-str"></a>

Device's Guid as assigned by ConnexPay.

##### browser_data: [`AuthenticationObtain3DSecureAuthenticationRequestBrowserData`](./connex_pay_python_sdk/type/authentication_obtain3_d_secure_authentication_request_browser_data.py)<a id="browser_data-authenticationobtain3dsecureauthenticationrequestbrowserdataconnex_pay_python_sdktypeauthentication_obtain3_d_secure_authentication_request_browser_datapy"></a>


##### amount: `Union[int, float]`<a id="amount-unionint-float"></a>

Amount of the transaction being 3DS authenticated

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`AuthenticationObtain3DSecureAuthenticationRequest`](./connex_pay_python_sdk/type/authentication_obtain3_d_secure_authentication_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`AuthenticationObtain3DSecureAuthenticationResponse`](./connex_pay_python_sdk/pydantic/authentication_obtain3_d_secure_authentication_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/3ds` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `connexpay.cancellation.entire_trip_cancellation`<a id="connexpaycancellationentire_trip_cancellation"></a>

The Cancel route should be used in the event the entire trip/booking (sale & purchase) require cancellation. In this case, the traveler/cardholder would be due a refund from the sale and the Virtual Card would be terminated to prevent the travel supplier from authorizing the Virtual Card.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
entire_trip_cancellation_response = connexpay.cancellation.entire_trip_cancellation(
    device_guid="string_example",
    sale_guid="string_example",
    sequence_number="string_example",
    void_reason="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### device_guid: `str`<a id="device_guid-str"></a>

Device's Guid provided by ConnexPay

##### sale_guid: `str`<a id="sale_guid-str"></a>

Sale transaction Guid

##### sequence_number: `str`<a id="sequence_number-str"></a>

Transaction sequence number within client environment. Provide a unique SequenceNumber for each new request. If the same value is sent within 30 minutes it will be considered a duplicate request. Note: value is not searchable or reportable in ConnexPay portal.  Alphanumeric.

##### void_reason: `str`<a id="void_reason-str"></a>

Indicates the reason the transaction was voided

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CancellationEntireTripCancellationRequest`](./connex_pay_python_sdk/type/cancellation_entire_trip_cancellation_request.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/cancel` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `connexpay.card.activate_delayed`<a id="connexpaycardactivate_delayed"></a>

Use this API to immediately activate a Virtual Card with a delayed activation date

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
activate_delayed_response = connexpay.card.activate_delayed()
```

#### 🔄 Return<a id="🔄-return"></a>

[`CardActivateDelayedResponse`](./connex_pay_python_sdk/pydantic/card_activate_delayed_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/IssueCard/ActivateDelayedCard/{{CardGuid}}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `connexpay.card.cancel_virtual_card`<a id="connexpaycardcancel_virtual_card"></a>

This endpoint should be called when you want to completely cancel a virtual card you created using the IssueLite endpoint.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
cancel_virtual_card_response = connexpay.card.cancel_virtual_card()
```

#### 🔄 Return<a id="🔄-return"></a>

[`CardCancelVirtualCardResponse`](./connex_pay_python_sdk/pydantic/card_cancel_virtual_card_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/IssueCard/Cancel/{{CardGuid}}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `connexpay.card.create_lodged_card`<a id="connexpaycardcreate_lodged_card"></a>

Use this endpoint to create a Lodged Card

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_lodged_card_response = connexpay.card.create_lodged_card(
    merchant_guid="string_example",
    first_name="string_example",
    last_name="string_example",
    amount_limit=3.14,
    limit_window="string_example",
    phone="string_example",
    address1="string_example",
    address2="string_example",
    city="string_example",
    state="string_example",
    zip_code="string_example",
    country="string_example",
    usage_limit=1,
    expiration_date="1970-01-01",
    terminate_date="1970-01-01",
    purchase_type="string_example",
    sequence_number="string_example",
    order_number="string_example",
    supplier_id="string_example",
    non_domestic_supplier=True,
    transmission={
    },
    return_card_data=True,
    customer_id="string_example",
    association_id="string_example",
    label_ids=[
        "string_example"
    ],
    custom_parameters=[
        {
        }
    ],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### merchant_guid: `str`<a id="merchant_guid-str"></a>

Merchant's guid. Application level value that indicates a virtual card is being requested for clients account. Value provided by ConnexPay.

##### first_name: `str`<a id="first_name-str"></a>

Cardholder's first name. This is the first name placed on the virtual card provided to the supplier. The value is also searchable in the ConnexPay portal.

##### last_name: `str`<a id="last_name-str"></a>

Cardholder's last name. This is the last name placed on the virtual card provided to the supplier. The value is also searchable in the ConnexPay portal.

##### amount_limit: `Union[int, float]`<a id="amount_limit-unionint-float"></a>

Security Control: Maximum dollar amount the card can be authorized and settled, which must be less than or equal to $1,000,000.00. The value must incorporate any anticipated overages such as currency conversion or taxes that a supplier may associate with the transaction. If a supplier attempts to authorize a card for more than the amount limit it will be declined.

##### limit_window: `str`<a id="limit_window-str"></a>

This is the time period that both the UsageLimit and the AmountLimit applies. Options are: Day, Week, Month, Lifetime. For example AmountLimit is $500 and LimitWindow is \\\"Week\\\" then the card can be approved for $500 per week.

##### phone: `str`<a id="phone-str"></a>

Cardholder's phone number. Phone number up to 20 character string, numbers and plus sign (+) allowed only. Telephone number of the user (including area code), prepended by the + symbol and the 1- to 3-digit country calling code. Do not include hyphens, spaces, or parentheses.

##### address1: `str`<a id="address1-str"></a>

Cardholder's address line 1. The street number is used by the supplier when submitting the transaction to perform an AVS check. Alphanumerics and [,.-'] are allowed.

##### address2: `str`<a id="address2-str"></a>

Cardholder's address line 2. Alphanumerics and [,.-'] are allowed.

##### city: `str`<a id="city-str"></a>

Cardholder's city.

##### state: `str`<a id="state-str"></a>

Cardholder's short name state.  The ISO 3166-2 CA and US state or province code of a user. Length = 2. If a non U.S. or Canadian value is submitted the virtual card request will not be processed and an error response returned.

##### zip_code: `str`<a id="zip_code-str"></a>

Cardholder's zipcode. The zip code is used by the supplier when submitting the transaction to perform an AVS check.  The Zipcode must be between 1 and 10 characters long, only numbers and letters are allowed.

##### country: `str`<a id="country-str"></a>

Cardholder's country.  Only alpha-2 digit country code allowed and numbers are not allowed.  See ISO-3166 country list of Alpha-2 country codes (https://www.iso.org/obp/ui/) .

##### usage_limit: `int`<a id="usage_limit-int"></a>

Security Control: Maximum number of times the card may be authorized. This is used in conjunction with the Limit Window: for example, if you specify a Usage Limit of 4 and a Limit Window of Monthly, the card can be authorized up to 4 times per month. The maximum allowed field value is 99, and if you do not provide a value the card will be considered unlimited. Authorization attempts exceeding the provided value will be declined.

##### expiration_date: `date`<a id="expiration_date-date"></a>

The ExpirationDate (YYYY-MM-DD) is the date to be provided to the supplier as the actual expiration date for the virtual card. The recommendation is to set the ExpirationDate one or two years in the future and set the TerminateDate just a day or two after the VCC is expected to be processed to avoid acceptance issues.  The expiration date cannot be more than 36 months in the future. If an expiration date is not provided, the expiration will default to issue date plus three years. For cards issued outside of the US/Canada, the expiration date will default to issue date plus three years and can not be overwritten - even if this parameter is included in the request. Note, Returns can still be processed on expired or terminated VCCs.

##### terminate_date: `date`<a id="terminate_date-date"></a>

The TerminateDate (YYYY-MM-DD format) is the date the Virtual Credit Card will be terminated by ConnexPay. TerminateDate is different than ExpirationDate in that TerminateDate indicates the actual date the card will no longer be active.  The recommendation is to set the ExpirationDate one or two years in the future and set the TerminateDate just a day or two after the VCC is expected to be processed. If a terminate date is not indicated, the card will be inactivated as of the expiration date. Note, Returns can still be processed on terminated VCCs.

##### purchase_type: `str`<a id="purchase_type-str"></a>

Security Control: The industry where the virtual card will be utilized. For example, if value set to airline and the card is used at hotel, it will be declined. Available purchase type values are: '01' (Airline), '02' (Hotels and Resorts), '03' (Car Rental), '04' (Cable, Satellite, Television, and Radio Services),  '05' (Cruise Lines), '11' (Medical Services and Health Practitioners), '21' (Advertising Services), '22' (Misc Advertising and Business Services), '23' (Ticketing), '31' (Insurance Sales, Underwriting, and Premiums), '91' (Restaurants and Food Services), and '93' (Tax Payments). Leave this blank if you plan to utilize MID level controls.

##### sequence_number: `str`<a id="sequence_number-str"></a>

Transaction sequence number within client environment. Provide a unique SequenceNumber for each new request. If the same value is sent within 30 minutes it will be considered a duplicate request. Note: value is not searchable or reportable in ConnexPay portal.  Alphanumeric.

##### order_number: `str`<a id="order_number-str"></a>

This is the most common number you'll see throughout the ConnexPay Portal.  Transaction ID within client environment associated with the order. The value is searchable and reportable in the ConnexPay portal. This value may be sent in multiple instances of the integration for multiple purposes. Customers in the travel space often send the Record Locator/PNR in this field.  The maximum length is 50 alpha-numeric characters and allows dashes and spaces (\\\"-\\\", \\\" \\\").

##### supplier_id: `str`<a id="supplier_id-str"></a>

The SupplierId is used to assist with Intelligent Routing functionality. In many cases, a Lodged Card is used at several different suppliers. In this case, there may be no reason to include SupplierId. However, if the Lodged Card will be used at a single supplier, we recommend sending in the SupplierId to assist with acceptance and rebate. The field accepts up to 100 alpha-numeric characters.

##### non_domestic_supplier: `bool`<a id="non_domestic_supplier-bool"></a>

We can issue the “Global VCC” if the Supplier accepting that VCC has an overseas merchant account. This is an optional field. Indicating true will result in issuing this Global VCC. Indicating false (or not including this property in your request) will result in receiving a VCC created for domestic use.

##### transmission: [`CardCreateLodgedCardRequestTransmission`](./connex_pay_python_sdk/type/card_create_lodged_card_request_transmission.py)<a id="transmission-cardcreatelodgedcardrequesttransmissionconnex_pay_python_sdktypecard_create_lodged_card_request_transmissionpy"></a>


##### return_card_data: `bool`<a id="return_card_data-bool"></a>

Optional field that may be set to true or false. When set to a value of true or if the field is not provided at all, card data is returned in the response. When set to a value of false, the Card Account Number and Security Code (CVV) will be excluded from the response.

##### customer_id: `str`<a id="customer_id-str"></a>

Transaction ID within client environment associated with the customer. This value acts as a secondary identifier in conjunction with OrderNumber. The value is searchable and reportable in the ConnexPay portal. This value may be sent in multiple times within the integration for multiple purposes.  The maximum length is 50 characters and is alpha-numeric.

##### association_id: `str`<a id="association_id-str"></a>

Utilize the Association ID field to tie a virtual card to a sale or sales. For example, if you have several sales and one virtual card payment to a supplier, you can add association ID to the sales and the virtual card for downstream reporting.

##### label_ids: [`CardCreateLodgedCardRequestLabelIDs`](./connex_pay_python_sdk/type/card_create_lodged_card_request_label_ids.py)<a id="label_ids-cardcreatelodgedcardrequestlabelidsconnex_pay_python_sdktypecard_create_lodged_card_request_label_idspy"></a>

##### custom_parameters: [`CardCreateLodgedCardRequestCustomParameters`](./connex_pay_python_sdk/type/card_create_lodged_card_request_custom_parameters.py)<a id="custom_parameters-cardcreatelodgedcardrequestcustomparametersconnex_pay_python_sdktypecard_create_lodged_card_request_custom_parameterspy"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CardCreateLodgedCardRequest`](./connex_pay_python_sdk/type/card_create_lodged_card_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`CardCreateLodgedCardResponse`](./connex_pay_python_sdk/pydantic/card_create_lodged_card_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/IssueCard/LodgedCard` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `connexpay.card.get_detail`<a id="connexpaycardget_detail"></a>

This Endpoint returns Virtual Credit Card details for a specific card guid.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_detail_response = connexpay.card.get_detail(
    card_guid="CardGuid_example",
    show_full_pan=True,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### card_guid: `str`<a id="card_guid-str"></a>

Global Unique Identifier for the VCC.

##### show_full_pan: `bool`<a id="show_full_pan-bool"></a>

Set to True to indicate whether the response should include the full account number.

#### 🔄 Return<a id="🔄-return"></a>

[`CardGetDetailResponse`](./connex_pay_python_sdk/pydantic/card_get_detail_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/Cards/{CardGuid}/{ShowFullPan}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `connexpay.card.resend_transmission_info`<a id="connexpaycardresend_transmission_info"></a>

This endpoint resends payment information to recipient. Or returns a URL you can use within your application to direct a user to a visual representation of the virtual card.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
resend_transmission_info_response = connexpay.card.resend_transmission_info(
    transmission_methods=[
        "string_example"
    ],
    card_guid="CardGuid_example",
    email_recipient="string_example",
    merchant_phone_number="string_example",
    email_from="string_example",
    recipient_name="string_example",
    subject="string_example",
    message="string_example",
    days_to_expire=1,
    fax_from="string_example",
    fax_recipient="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### transmission_methods: [`CardResendTransmissionInfoRequestTransmissionMethods`](./connex_pay_python_sdk/type/card_resend_transmission_info_request_transmission_methods.py)<a id="transmission_methods-cardresendtransmissioninforequesttransmissionmethodsconnex_pay_python_sdktypecard_resend_transmission_info_request_transmission_methodspy"></a>

##### card_guid: `str`<a id="card_guid-str"></a>

Global Unique Identififer for the Card.

##### email_recipient: `str`<a id="email_recipient-str"></a>

Mandatory when transmission is Email. Otherwise don't include. This is the email address of the intended recipient. 255 char max.

##### merchant_phone_number: `str`<a id="merchant_phone_number-str"></a>

This is the phone number that should display on the virtual card and is the number that should be used if the link has expired. Up to 15 characters. Numbers and plus sign (+) allowed only.

##### email_from: `str`<a id="email_from-str"></a>

For email transmissions, this will be the email address that populates the ‘reply to’ section of the email message. Do not include this parameter on other transmission method types. 255 char max.

##### recipient_name: `str`<a id="recipient_name-str"></a>

A descriptive name of the email or fax recipient. Does not apply to the Link transmission method type. 255 char max

##### subject: `str`<a id="subject-str"></a>

High-level subject line description of the transmission contents. Does not apply to the Link transmission method type. 255 char max.

##### message: `str`<a id="message-str"></a>

The message body of the email or fax. Does not apply to the Link transmission method type. 1024 char max.

##### days_to_expire: `int`<a id="days_to_expire-int"></a>

The number of days after card issuance until the link to the VC expires. Range: 1-999 days.

##### fax_from: `str`<a id="fax_from-str"></a>

Mandatory for fax transmission. This can be the client name or fax number the fax is coming from that populates the ‘FaxFrom’ section of the fax. 255 char max.

##### fax_recipient: `str`<a id="fax_recipient-str"></a>

Mandatory for fax transmissions.  The fax number of the intended recipient.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CardResendTransmissionInfoRequest`](./connex_pay_python_sdk/type/card_resend_transmission_info_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`CardResendTransmissionInfoResponse`](./connex_pay_python_sdk/pydantic/card_resend_transmission_info_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/IssueCard/SendPaymentInfo/{cardGuid}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `connexpay.card.search_issued_virtual_cards`<a id="connexpaycardsearch_issued_virtual_cards"></a>

This endpoint searches for Issued Virtual Cards.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
search_issued_virtual_cards_response = connexpay.card.search_issued_virtual_cards(
    merchant_guid="string_example",
    page_number=1,
    page_size=1,
    sale_guid="string_example",
    incoming_transaction_code="string_example",
    order_number="string_example",
    customer_id="string_example",
    time_stamp_from="1970-01-01",
    time_stamp_to="1970-01-01",
    issued_amount_from=3.14,
    issued_amount_to=3.14,
    outgoing_transaction_code="string_example",
    settled_amount_from=1,
    settled_amount_to=1,
    returned_amount_from=1,
    returned_amount_to=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### merchant_guid: `str`<a id="merchant_guid-str"></a>

Your assigned Merchant GUID.

##### page_number: `int`<a id="page_number-int"></a>

Number of page of the results. Default is 1.

##### page_size: `int`<a id="page_size-int"></a>

Size of each page of the results. Default is 1000.

##### sale_guid: `str`<a id="sale_guid-str"></a>

Sale GUID linked to the card you are searching.

##### incoming_transaction_code: `str`<a id="incoming_transaction_code-str"></a>

Incoming Transaction Code linked to the card you are searching.

##### order_number: `str`<a id="order_number-str"></a>

Order Number linked to the card you are searching.

##### customer_id: `str`<a id="customer_id-str"></a>

Order Number linked to the card you are searching.

##### time_stamp_from: `date`<a id="time_stamp_from-date"></a>

Starting Issued Date linked to the card(s) you are searching.

##### time_stamp_to: `date`<a id="time_stamp_to-date"></a>

Ending Issued Date linked to the card(s) you are searching.

##### issued_amount_from: `Union[int, float]`<a id="issued_amount_from-unionint-float"></a>

Start of Issued Amount range linked to the card(s) you are searching.

##### issued_amount_to: `Union[int, float]`<a id="issued_amount_to-unionint-float"></a>

End of Issued Amount range linked to the card(s) you are searching.

##### outgoing_transaction_code: `str`<a id="outgoing_transaction_code-str"></a>

Outgoing Transaction Code linked to the card(s) you are searching.

##### settled_amount_from: `int`<a id="settled_amount_from-int"></a>

Start of Settled Amount range linked to the card(s) you are searching.

##### settled_amount_to: `int`<a id="settled_amount_to-int"></a>

End of Settled Amount range linked to the card(s) you are searching.

##### returned_amount_from: `int`<a id="returned_amount_from-int"></a>

Start of Settled Returned Amount range linked to the card(s) you are searching.

##### returned_amount_to: `int`<a id="returned_amount_to-int"></a>

End of Settled Returned Amount range linked to the card(s) you are searching.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CardSearchIssuedVirtualCardsRequest`](./connex_pay_python_sdk/type/card_search_issued_virtual_cards_request.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/Search/IssuedCards` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `connexpay.card.terminate_by_date`<a id="connexpaycardterminate_by_date"></a>

The TerminateDate (YYYY-MM-DD format) is the date the Virtual Credit Card will be terminated by ConnexPay. TerminateDate is different than ExpirationDate in that TerminateDate indicates the actual date the card will no longer be active.  ExpirationDate is the month and year that will be applied to the actual VCC. Note, Returns can still be processed on terminated VCCs.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
terminate_by_date_response = connexpay.card.terminate_by_date(
    guid="guid_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### guid: `str`<a id="guid-str"></a>

Card’s guid to terminate

#### 🔄 Return<a id="🔄-return"></a>

[`CardTerminateByDateResponse`](./connex_pay_python_sdk/pydantic/card_terminate_by_date_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/TerminateCard/&lt;guid&gt;` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `connexpay.card.update_card_details`<a id="connexpaycardupdate_card_details"></a>

Update Card

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_card_details_response = connexpay.card.update_card_details(
    card_guid="CardGuid_example",
    purchase_type="string_example",
    mid_whitelist=[
        "string_example"
    ],
    mid_blacklist=[
        "string_example"
    ],
    usage_limit=1,
    association_id="string_example",
    terminate_date="1970-01-01",
    amount_limit=3.14,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### card_guid: `str`<a id="card_guid-str"></a>

Global Unique Identififer for the Card.

##### purchase_type: `str`<a id="purchase_type-str"></a>

Security Control: The industry where the virtual card will be utilized. For example, if value set to airline and the card is used at hotel, it will be declined. Available purchase type values are: '01' (Airline), '02' (Hotels and Resorts), '03' (Car Rental), '04' (Cable, Satellite, Television, and Radio Services),  '05' (Cruise Lines), '11' (Medical Services and Health Practitioners), '21' (Advertising Services), '22' (Misc Advertising and Business Services), '23' (Ticketing), '31' (Insurance Sales, Underwriting, and Premiums), '91' (Restaurants and Food Services), and '93' (Tax Payments). Leave this blank if you plan to utilize MID level controls.

##### mid_whitelist: [`CardUpdateCardDetailsRequestMidWhitelist`](./connex_pay_python_sdk/type/card_update_card_details_request_mid_whitelist.py)<a id="mid_whitelist-cardupdatecarddetailsrequestmidwhitelistconnex_pay_python_sdktypecard_update_card_details_request_mid_whitelistpy"></a>

##### mid_blacklist: [`CardUpdateCardDetailsRequestMidBlacklist`](./connex_pay_python_sdk/type/card_update_card_details_request_mid_blacklist.py)<a id="mid_blacklist-cardupdatecarddetailsrequestmidblacklistconnex_pay_python_sdktypecard_update_card_details_request_mid_blacklistpy"></a>

##### usage_limit: `int`<a id="usage_limit-int"></a>

Security Control: Maximum number of times the card may be authorized. The maximum allowed field value is 99, and if you do not provide a value the card will be considered unlimited. Authorization attempts exceeding the provided value will be declined. Even though a virtual card is often considered a “one-time-use” card, some suppliers may need to authorize a card multiple times (pre-authorizations, a purchase comprised of multiple tickets, etc.) and you may consider a value that is not overly restrictive to avoid unwanted declines.

##### association_id: `str`<a id="association_id-str"></a>

Utilize the Association ID field to tie a virtual card to a sale or sales. For example, if you have several sales and one virtual card payment to a supplier, you can add association ID to the sales and the virtual card for downstream reporting.

##### terminate_date: `date`<a id="terminate_date-date"></a>

The TerminateDate (YYYY-MM-DD format) is the date the Virtual Credit Card will be terminated by ConnexPay. TerminateDate is different than ExpirationDate in that TerminateDate indicates the actual date the card will no longer be active.  The recommendation is to set the ExpirationDate one or two years in the future and set the TerminateDate just a day or two after the VCC is expected to be processed. If a terminate date is not indicated, the card will be inactivated as of the expiration date. Note, Returns can still be processed on terminated VCCs.

##### amount_limit: `Union[int, float]`<a id="amount_limit-unionint-float"></a>

Security Control: Maximum dollar amount the card can be authorized and settled, which must be less than or equal to $1,000,000.00. The value must incorporate any anticipated overages such as currency conversion or taxes that a supplier may associate with the transaction. If a supplier attempts to authorize a card for more than the amount limit it will be declined.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CardUpdateCardDetailsRequest`](./connex_pay_python_sdk/type/card_update_card_details_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`CardUpdateCardDetailsResponse`](./connex_pay_python_sdk/pydantic/card_update_card_details_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/IssueCard/{cardGuid}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `connexpay.card.update_delayed_activation`<a id="connexpaycardupdate_delayed_activation"></a>

Request this endpoint to update the activation date or card limit of a virtual card with a future activation date.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_delayed_activation_response = connexpay.card.update_delayed_activation(
    merchant_guid="string_example",
    card_guid="CardGuid_example",
    activation_date="1970-01-01",
    amount_limit=3.14,
    terminate_date="1970-01-01",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### merchant_guid: `str`<a id="merchant_guid-str"></a>

Merchant's guid. Application level value that indicates a virtual card is being requested for clients account. Value provided by ConnexPay.

##### card_guid: `str`<a id="card_guid-str"></a>

Global Unique Identifier for the Card.

##### activation_date: `date`<a id="activation_date-date"></a>

Provide a future date, up to 600 days, if you wish to update the virtual card's activation date. Otherwise leave blank.

##### amount_limit: `Union[int, float]`<a id="amount_limit-unionint-float"></a>

Provide a card amount if you wish to update the amount limit for the virtual card, otherwise leave blank.

##### terminate_date: `date`<a id="terminate_date-date"></a>

The TerminateDate (YYYY-MM-DD format) is the date the Virtual Credit Card will be terminated by ConnexPay. TerminateDate is different than ExpirationDate in that TerminateDate indicates the actual date the card will no longer be active.  ExpirationDate is the month and year that will be applied to the actual VCC. The recommendation is to set the ExpirationDate one or two years in the future and set the TerminateDate just a day or two after the VCC is expected to be processed. Note, Returns can still be processed on terminated VCCs.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CardUpdateDelayedActivationRequest`](./connex_pay_python_sdk/type/card_update_delayed_activation_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`CardUpdateDelayedActivationResponse`](./connex_pay_python_sdk/pydantic/card_update_delayed_activation_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/IssueCard/UpdateDelayedCard/{{CardGuid}}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `connexpay.card.update_lodged_card`<a id="connexpaycardupdate_lodged_card"></a>

Update Lodged Card

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_lodged_card_response = connexpay.card.update_lodged_card(
    card_guid="CardGuid_example",
    usage_limit=1,
    amount_limit=3.14,
    limit_window="string_example",
    purchase_type="string_example",
    activated=True,
    association_id="string_example",
    terminate_date="1970-01-01",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### card_guid: `str`<a id="card_guid-str"></a>

Global Unique Identifier for the Card.

##### usage_limit: `int`<a id="usage_limit-int"></a>

Security Control: Maximum number of times the card may be authorized. This is used in conjunction with the Limit Window; for example, if you specify a Usage Limit of 4 and a Limit Window of Monthly, the card can be authorized up to 4 times per month. The maximum allowed field value is 99, and if you do not provide a value the card will be considered unlimited. Authorization attempts exceeding the provided value will be declined.

##### amount_limit: `Union[int, float]`<a id="amount_limit-unionint-float"></a>

Security Control: Maximum dollar amount the card can be authorized and settled, which must be less than or equal to $1,000,000.00. The value must incorporate any anticipated overages such as currency conversion or taxes that a supplier may associate with the transaction. If a supplier attempts to authorize a card for more than the amount limit it will be declined.

##### limit_window: `str`<a id="limit_window-str"></a>

This is the time period that both the UsageLimit and the AmountLimit applies. Options are: Day, Week, Month, Lifetime. For example AmountLimit is $500 and LimitWindow is \\\"Week\\\" then the card can be approved for $500 per week.

##### purchase_type: `str`<a id="purchase_type-str"></a>

Security Control: The industry where the virtual card will be utilized. For example, if value set to airline and the card is used at hotel, it will be declined. Available purchase type values are: '01' (Airline), '02' (Hotels and Resorts), '03' (Car Rental), '04' (Cable, Satellite, Television, and Radio Services),  '05' (Cruise Lines), '11' (Medical Services and Health Practitioners), '21' (Advertising Services), '22' (Misc Advertising and Business Services), '23' (Ticketing), '31' (Insurance Sales, Underwriting, and Premiums), '91' (Restaurants and Food Services), and '93' (Tax Payments). Leave this blank if you plan to utilize MID level controls.

##### activated: `bool`<a id="activated-bool"></a>

True activates a lodged card. False suspends a lodged card.

##### association_id: `str`<a id="association_id-str"></a>

Utilize the Association ID field to tie a lodged card to a sale or sales. For example, if you have several sales and one lodged card payment to a supplier, you can add association ID to the sales and the lodged card for downstream reporting.

##### terminate_date: `date`<a id="terminate_date-date"></a>

The TerminateDate (YYYY-MM-DD format) is the date the Lodged Card will be terminated by ConnexPay. TerminateDate is different than ExpirationDate in that TerminateDate indicates the actual date the card will no longer be active.  The recommendation is to set the ExpirationDate one or two years in the future and set the TerminateDate just a day or two after the Lodged Card is expected to be processed. If a terminate date is not indicated, the card will be inactivated as of the expiration date. Note, Returns can still be processed on terminated Lodged Cards.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CardUpdateLodgedCardRequest`](./connex_pay_python_sdk/type/card_update_lodged_card_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`CardUpdateLodgedCardResponse`](./connex_pay_python_sdk/pydantic/card_update_lodged_card_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/IssueCard/LodgedCard/{CardGuid}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `connexpay.card_issuance.create_virtual_card`<a id="connexpaycard_issuancecreate_virtual_card"></a>

Use this endpoint to issue virtual cards associated with a credit or ACH sale. Do not use this endpoint if you fund your virtual cards from cash and therefor don't have an associated sale. If you aren't sure which Issuance API to use, please contact your client support representative.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_virtual_card_response = connexpay.card_issuance.create_virtual_card(
    merchant_guid="string_example",
    first_name="string_example",
    last_name="string_example",
    amount_limit=3.14,
    purchase_type="string_example",
    phone="string_example",
    address1="string_example",
    address2="string_example",
    city="string_example",
    state="string_example",
    zip_code="string_example",
    country="string_example",
    usage_limit=1,
    expiration_date="1970-01-01",
    terminate_date="1970-01-01",
    mid_whitelist=[
        "string_example"
    ],
    mid_blacklist=[
        "string_example"
    ],
    sequence_number="string_example",
    order_number="{{OrderNumber}}",
    incoming_transaction_code="string_example",
    supplier_id="string_example",
    non_domestic_supplier=True,
    transmission={
    },
    return_card_data=True,
    customer_id="string_example",
    association_id="string_example",
    custom_parameters=[
        {
        }
    ],
    label_ids=[
        "string_example"
    ],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### merchant_guid: `str`<a id="merchant_guid-str"></a>

Merchant's Guid. Application-level value that indicates a virtual card is being requested for client's account. Value provided by ConnexPay.

##### first_name: `str`<a id="first_name-str"></a>

Cardholder's first name. This is the first name placed on the virtual card provided to the supplier. The value is also searchable in the ConnexPay portal.

##### last_name: `str`<a id="last_name-str"></a>

Cardholder's last name. This is the last name placed on the virtual card provided to the supplier. The value is also searchable in the ConnexPay portal.

##### amount_limit: `Union[int, float]`<a id="amount_limit-unionint-float"></a>

Security Control: Maximum dollar amount the card can be authorized and settled, which must be less than or equal to $1,000,000.00. The value must incorporate any anticipated overages such as currency conversion or taxes that a supplier may associate with the transaction. If a supplier attempts to authorize a card for more than the amount limit it will be declined.

##### purchase_type: `str`<a id="purchase_type-str"></a>

Security Control: The industry where the virtual card will be utilized. For example, if value set to airline and the card is used at hotel, it will be declined. Available purchase type values are: '01' (Airline), '02' (Hotels and Resorts), '03' (Car Rental), '04' (Cable, Satellite, Television, and Radio Services),  '05' (Cruise Lines), '11' (Medical Services and Health Practitioners), '21' (Advertising Services), '22' (Misc Advertising and Business Services), '23' (Ticketing), '31' (Insurance Sales, Underwriting, and Premiums), '91' (Restaurants and Food Services), and '93' (Tax Payments). Leave this blank if you plan to utilize MID level controls.

##### phone: `str`<a id="phone-str"></a>

Cardholder's phone number. Phone number up to 20 character string, numbers and plus sign (+) allowed only. Telephone number of the user (including area code), prepended by the + symbol and the 1- to 3-digit country calling code. Do not include hyphens, spaces, or parentheses.

##### address1: `str`<a id="address1-str"></a>

Cardholder's address line 1. The street number is used by the supplier when submitting the transaction to perform an AVS check. Alphanumerics and [,.-'] are allowed.

##### address2: `str`<a id="address2-str"></a>

Cardholder's address line 2. Alphanumerics and [,.-'] are allowed.

##### city: `str`<a id="city-str"></a>

Cardholder's city.

##### state: `str`<a id="state-str"></a>

Cardholder's short name state.  The ISO 3166-2 CA and US state or province code of a user. Length = 2. If a non U.S. or Canadian value is submitted the virtual card request will not be processed and an error response returned.

##### zip_code: `str`<a id="zip_code-str"></a>

Cardholder's zipcode. The zip code is used by the supplier when submitting the transaction to perform an AVS check.  The Zipcode must be between 1 and 10 characters long, only numbers and letters are allowed.

##### country: `str`<a id="country-str"></a>

Cardholder's country.  Only alpha-2 digit country code allowed and numbers are not allowed.  See ISO-3166 country list of Alpha-2 country codes (https://www.iso.org/obp/ui/) .

##### usage_limit: `int`<a id="usage_limit-int"></a>

Security Control: Maximum number of times the card may be authorized. The maximum allowed field value is 99, and if you do not provide a value the card will be considered unlimited. Authorization attempts exceeding the provided value will be declined. Even though a virtual card is often considered a “one-time-use” card, some suppliers may need to authorize a card multiple times (pre-authorizations, a purchase comprised of multiple tickets, etc.) and you may consider a value that is not overly restrictive to avoid unwanted declines.

##### expiration_date: `date`<a id="expiration_date-date"></a>

The ExpirationDate (YYYY-MM-DD) is the date to be provided to the supplier as the actual expiration date for the virtual card. The recommendation is to set the ExpirationDate one or two years in the future and set the TerminateDate just a day or two after the VCC is expected to be processed to avoid acceptance issues.  The expiration date cannot be more than 36 months in the future. If an expiration date is not provided, the expiration will default to issue date plus three years. For cards issued outside of the US/Canada, the expiration date will default to issue date plus three years and can not be overwritten - even if this parameter is included in the request. Note, Returns can still be processed on expired or terminated VCCs.

##### terminate_date: `date`<a id="terminate_date-date"></a>

The TerminateDate (YYYY-MM-DD format) is the date the Virtual Credit Card will be terminated by ConnexPay. TerminateDate is different than ExpirationDate in that TerminateDate indicates the actual date the card will no longer be active.  The recommendation is to set the ExpirationDate one or two years in the future and set the TerminateDate just a day or two after the VCC is expected to be processed. If a terminate date is not indicated, the card will be inactivated as of the expiration date. Note, Returns can still be processed on terminated VCCs.

##### mid_whitelist: [`CardIssuanceCreateVirtualCardRequestMidWhitelist`](./connex_pay_python_sdk/type/card_issuance_create_virtual_card_request_mid_whitelist.py)<a id="mid_whitelist-cardissuancecreatevirtualcardrequestmidwhitelistconnex_pay_python_sdktypecard_issuance_create_virtual_card_request_mid_whitelistpy"></a>

##### mid_blacklist: [`CardIssuanceCreateVirtualCardRequestMidBlacklist`](./connex_pay_python_sdk/type/card_issuance_create_virtual_card_request_mid_blacklist.py)<a id="mid_blacklist-cardissuancecreatevirtualcardrequestmidblacklistconnex_pay_python_sdktypecard_issuance_create_virtual_card_request_mid_blacklistpy"></a>

##### sequence_number: `str`<a id="sequence_number-str"></a>

Transaction sequence number within client environment. Note: value is not searchable or reportable in ConnexPay portal.  Alphanumeric.

##### order_number: `str`<a id="order_number-str"></a>

This is the most common number you'll see throughout the ConnexPay Portal. Transaction ID within client environment associated with the order. The value is searchable and reportable in the ConnexPay portal. This value may be sent in multiple instances of the integration for multiple purposes. Customers in the travel space often send the Record Locator/PNR in this field. The maximum length is 50 alpha-numeric characters and allows dashes ( - ).

##### incoming_transaction_code: `str`<a id="incoming_transaction_code-str"></a>

ITC for short Application level setting to associate the virtual card request with an original sale or sale group. The value is provided in the sale response of the original sale transaction, or in the Group Sale response of the group sale. All virtual card requests must be associated with an original sale or group transaction.

##### supplier_id: `str`<a id="supplier_id-str"></a>

The SupplierId is used to assist with Intelligent Routing functionality. The field accepts up to 100 alpha-numeric characters.  Alphanumeric with a max length of 100 characters

##### non_domestic_supplier: `bool`<a id="non_domestic_supplier-bool"></a>

We can issue the “Global VCC” if the Supplier accepting that VCC has an overseas merchant account. This is an optional field. Indicating true will result in issuing this Global VCC. Indicating false (or not including this property in your request) will result in receiving a VCC created for domestic use.

##### transmission: [`CardIssuanceCreateVirtualCardRequestTransmission`](./connex_pay_python_sdk/type/card_issuance_create_virtual_card_request_transmission.py)<a id="transmission-cardissuancecreatevirtualcardrequesttransmissionconnex_pay_python_sdktypecard_issuance_create_virtual_card_request_transmissionpy"></a>


##### return_card_data: `bool`<a id="return_card_data-bool"></a>

Optional field that may be set to true or false. When set to a value of true or if the field is not provided at all, card data is returned in the response. When set to a value of false, the Card Account Number and Security Code (CVV) will be excluded from the response.

##### customer_id: `str`<a id="customer_id-str"></a>

Transaction ID within client environment associated with the customer. This value acts as a secondary identifier in conjunction with OrderNumber. The value is searchable and reportable in the ConnexPay portal. This value may be sent in multiple times within the integration for multiple purposes.  The maximum length is 100 characters and is alpha-numeric.

##### association_id: `str`<a id="association_id-str"></a>

Utilize the Association ID field to tie a virtual card to a sale or sales. For example, if you have several sales and one virtual card payment to a supplier, you can add association ID to the sales and the virtual card for downstream reporting.

##### custom_parameters: [`CardIssuanceCreateVirtualCardRequestCustomParameters`](./connex_pay_python_sdk/type/card_issuance_create_virtual_card_request_custom_parameters.py)<a id="custom_parameters-cardissuancecreatevirtualcardrequestcustomparametersconnex_pay_python_sdktypecard_issuance_create_virtual_card_request_custom_parameterspy"></a>

##### label_ids: [`CardIssuanceCreateVirtualCardRequestLabelIDs`](./connex_pay_python_sdk/type/card_issuance_create_virtual_card_request_label_ids.py)<a id="label_ids-cardissuancecreatevirtualcardrequestlabelidsconnex_pay_python_sdktypecard_issuance_create_virtual_card_request_label_idspy"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CardIssuanceCreateVirtualCardRequest`](./connex_pay_python_sdk/type/card_issuance_create_virtual_card_request.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/IssueCard` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `connexpay.card_issue.create_virtual_card_lite`<a id="connexpaycard_issuecreate_virtual_card_lite"></a>

For our lite clients, we provide the ability to issue a VCC (Virtual Credit Card) via API without the requirement to process a sale first.  If you aren't sure which Issuance API to use, please contact your client support representative.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_virtual_card_lite_response = connexpay.card_issue.create_virtual_card_lite(
    merchant_guid="MerchantGuid",
    first_name="Jane",
    last_name="Doe",
    amount_limit=100,
    purchase_type="01",
    phone="1234567890",
    address1="123 Test Street",
    address2="Suite 185",
    city="Alpharetta",
    state="GA",
    zip_code="30004",
    country="US",
    usage_limit=1,
    expiration_date="1970-01-01",
    terminate_date="1970-01-01",
    mid_whitelist=[
        "string_example"
    ],
    mid_blacklist=[
        "string_example"
    ],
    sequence_number="987654321",
    supplier_id="DL",
    non_domestic_supplier=True,
    order_number="1234A",
    customer_id="string_example",
    transmission={
    },
    return_card_data=True,
    custom_parameters=[
        {
        }
    ],
    activation_date="1970-01-01",
    association_id="1234",
    label_ids=[
        "string_example"
    ],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### merchant_guid: `str`<a id="merchant_guid-str"></a>

Merchant's guid. Application level value that indicates a virtual card is being requested for clients account. Value provided by ConnexPay.

##### first_name: `str`<a id="first_name-str"></a>

Cardholder's first name. This is the first name placed on the virtual card provided to the supplier. The value is also searchable in the ConnexPay portal.

##### last_name: `str`<a id="last_name-str"></a>

Cardholder's last name. This is the last name placed on the virtual card provided to the supplier. The value is also searchable in the ConnexPay portal.

##### amount_limit: `Union[int, float]`<a id="amount_limit-unionint-float"></a>

Security Control: Maximum dollar amount the card can be authorized and settled, which must be less than or equal to $1,000,000.00. The value must incorporate any anticipated overages such as currency conversion or taxes that a supplier may associate with the transaction. If a supplier attempts to authorize a card for more than the amount limit it will be declined.

##### purchase_type: `str`<a id="purchase_type-str"></a>

Security Control: The industry where the virtual card will be utilized. For example, if value set to airline and the card is used at hotel, it will be declined. Available purchase type values are: '01' (Airline), '02' (Hotels and Resorts), '03' (Car Rental), '04' (Cable, Satellite, Television, and Radio Services),  '05' (Cruise Lines), '11' (Medical Services and Health Practitioners), '21' (Advertising Services), '22' (Misc Advertising and Business Services), '23' (Ticketing), '31' (Insurance Sales, Underwriting, and Premiums), '91' (Restaurants and Food Services), and '93' (Tax Payments). Leave this blank if you plan to utilize MID level controls.

##### phone: `str`<a id="phone-str"></a>

Cardholder's phone number.  Phone number up to 20 character string, numbers and plus sign (+) allowed only. Telephone number of the user (including area code), prepended by the + symbol and the 1- to 3-digit country calling code. Do not include hyphens, spaces, or parentheses.

##### address1: `str`<a id="address1-str"></a>

Cardholder's address line 1. The street number is used by the supplier when submitting the transaction to perform an AVS check. Alphanumerics and [,.-'] are allowed.

##### address2: `str`<a id="address2-str"></a>

Cardholder's address line 2. Alphanumerics and [,.-'] are allowed.

##### city: `str`<a id="city-str"></a>

Cardholder's city.

##### state: `str`<a id="state-str"></a>

Cardholder's short name state.  The ISO 3166-2 CA and US state or province code of a user. Length = 2. If a non U.S. or Canadian value is submitted the virtual card request will not be processed and an error response returned.

##### zip_code: `str`<a id="zip_code-str"></a>

Cardholder's zipcode. The zip code is used by the supplier when submitting the transaction to perform an AVS check.  The Zipcode must be between 1 and 10 characters long, only numbers and letters are allowed.

##### country: `str`<a id="country-str"></a>

Cardholder's country.  Only alpha-2 digit country code allowed and numbers are not allowed.  See ISO-3166 country list of Alpha-2 country codes (https://www.iso.org/obp/ui/) .

##### usage_limit: `int`<a id="usage_limit-int"></a>

Security Control: Maximum number of times the card may be authorized. The maximum allowed field value is 99, and if you do not provide a value the card will be considered unlimited. Authorization attempts exceeding the provided value will be declined. Even though a virtual card is often considered a “one-time-use” card, some suppliers may need to authorize a card multiple times (pre-authorizations, a purchase comprised of multiple tickets, etc.) and you may consider a value that is not overly restrictive to avoid unwanted declines.

##### expiration_date: `date`<a id="expiration_date-date"></a>

The ExpirationDate (YYYY-MM-DD) is the date to be provided to the supplier as the actual expiration date for the virtual card. The recommendation is to set the ExpirationDate one or two years in the future and set the TerminateDate just a day or two after the VCC is expected to be processed to avoid acceptance issues.  The expiration date cannot be more than 36 months in the future. If an expiration date is not provided, the expiration will default to issue date plus three years. For cards issued outside of the US/Canada, the expiration date will default to issue date plus three years and can not be overwritten - even if this parameter is included in the request. Note, Returns can still be processed on expired or terminated VCCs.

##### terminate_date: `date`<a id="terminate_date-date"></a>

The TerminateDate (YYYY-MM-DD format) is the date the Virtual Credit Card will be terminated by ConnexPay. TerminateDate is different than ExpirationDate in that TerminateDate indicates the actual date the card will no longer be active.  The recommendation is to set the ExpirationDate one or two years in the future and set the TerminateDate just a day or two after the VCC is expected to be processed. If a terminate date is not indicated, the card will be inactivated as of the expiration date. Note, Returns can still be processed on terminated VCCs.

##### mid_whitelist: [`CardIssueCreateVirtualCardLiteRequestMidWhitelist`](./connex_pay_python_sdk/type/card_issue_create_virtual_card_lite_request_mid_whitelist.py)<a id="mid_whitelist-cardissuecreatevirtualcardliterequestmidwhitelistconnex_pay_python_sdktypecard_issue_create_virtual_card_lite_request_mid_whitelistpy"></a>

##### mid_blacklist: [`CardIssueCreateVirtualCardLiteRequestMidBlacklist`](./connex_pay_python_sdk/type/card_issue_create_virtual_card_lite_request_mid_blacklist.py)<a id="mid_blacklist-cardissuecreatevirtualcardliterequestmidblacklistconnex_pay_python_sdktypecard_issue_create_virtual_card_lite_request_mid_blacklistpy"></a>

##### sequence_number: `str`<a id="sequence_number-str"></a>

Transaction sequence number within client environment. Provide a unique SequenceNumber for each new request. If a card request is made with all the same parameter information and the same sequence number, within 30 minutes, the request will be considered a duplicate and a new card will not be issued.  Note: value is not searchable or reportable in Bridge.  Alphanumeric.

##### supplier_id: `str`<a id="supplier_id-str"></a>

The SupplierId is used to assist with Intelligent Routing functionality. The field accepts up to 100 alpha-numeric characters.  Alphanumeric with a max length of 100 characters

##### non_domestic_supplier: `bool`<a id="non_domestic_supplier-bool"></a>

We can issue the “Global VCC” if the Supplier accepting that VCC has an overseas merchant account. This is an optional field. Indicating true will result in issuing this Global VCC. Indicating false (or not including this property in your request) will result in receiving a VCC created for domestic use.

##### order_number: `str`<a id="order_number-str"></a>

This is the most common number you'll see throughout the ConnexPay Portal.  Transaction ID within client environment associated with the order. The value is searchable and reportable in the ConnexPay portal. This value may be sent in multiple instances of the integration for multiple purposes. Customers in the travel space often send the Record Locator/PNR in this field.  The maximum length is 50 alpha-numeric characters and allows dashes and spaces  (\\\"-\\\", \\\" \\\").

##### customer_id: `str`<a id="customer_id-str"></a>

Transaction ID within client environment associated with the customer. This value acts as a secondary identifier in conjunction with OrderNumber. The value is searchable and reportable in the ConnexPay portal. This value may be sent in multiple times within the integration for multiple purposes.  The maximum length is 100 characters and is alpha-numeric.

##### transmission: [`CardIssueCreateVirtualCardLiteRequestTransmission`](./connex_pay_python_sdk/type/card_issue_create_virtual_card_lite_request_transmission.py)<a id="transmission-cardissuecreatevirtualcardliterequesttransmissionconnex_pay_python_sdktypecard_issue_create_virtual_card_lite_request_transmissionpy"></a>


##### return_card_data: `bool`<a id="return_card_data-bool"></a>

Optional field that may be set to true or false. When set to a value of true or if the field is not provided at all, card data is returned in the response. When set to a value of false, the Card Account Number and Security Code (CVV) will be excluded from the response.

##### custom_parameters: [`CardIssueCreateVirtualCardLiteRequestCustomParameters`](./connex_pay_python_sdk/type/card_issue_create_virtual_card_lite_request_custom_parameters.py)<a id="custom_parameters-cardissuecreatevirtualcardliterequestcustomparametersconnex_pay_python_sdktypecard_issue_create_virtual_card_lite_request_custom_parameterspy"></a>

##### activation_date: `date`<a id="activation_date-date"></a>

Future date that the card should be fully funded, at least one day from creation date and within 600 days. If no activation date is supplied the card will be funded immediately.

##### association_id: `str`<a id="association_id-str"></a>

Utilize the Association ID field to tie a virtual card to a sale or sales. For example, if you have several sales and one virtual card payment to a supplier, you can add association ID to the sales and the virtual card for downstream reporting.

##### label_ids: [`CardIssueCreateVirtualCardLiteRequestLabelIDs`](./connex_pay_python_sdk/type/card_issue_create_virtual_card_lite_request_label_ids.py)<a id="label_ids-cardissuecreatevirtualcardliterequestlabelidsconnex_pay_python_sdktypecard_issue_create_virtual_card_lite_request_label_idspy"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CardIssueCreateVirtualCardLiteRequest`](./connex_pay_python_sdk/type/card_issue_create_virtual_card_lite_request.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/IssueCard/IssueLite` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `connexpay.funding.merchant_cash_balance`<a id="connexpayfundingmerchant_cash_balance"></a>

Use this endpoint to fund or withdraw your merchant cash balance with your merchant bank account.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
merchant_cash_balance_response = connexpay.funding.merchant_cash_balance(
    merchant_guid="string_example",
    amount=3.14,
    is_fund_cash_balance=True,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### merchant_guid: `str`<a id="merchant_guid-str"></a>

The merchant's GUID. Value provided by ConnexPay.

##### amount: `Union[int, float]`<a id="amount-unionint-float"></a>

Self-service funding amount that will be processed. Maximum transaction and daily funding limits are set by ConnexPay.

##### is_fund_cash_balance: `bool`<a id="is_fund_cash_balance-bool"></a>

true: Fund your merchant cash balance from your merchant bank account. false: Withdraw your merchant cash balance and ConnexPay will credit your merchant bank account.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`FundingMerchantCashBalanceRequest`](./connex_pay_python_sdk/type/funding_merchant_cash_balance_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`FundingMerchantCashBalanceResponse`](./connex_pay_python_sdk/pydantic/funding_merchant_cash_balance_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/MerchantSelfServiceFunding` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `connexpay.funding.transfer_merchant_cash_balance`<a id="connexpayfundingtransfer_merchant_cash_balance"></a>

Use this endpoint to transfer funds between your merchant cash balances within the same Corporate entity.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
transfer_merchant_cash_balance_response = connexpay.funding.transfer_merchant_cash_balance(
    transferred_from="string_example",
    transferred_to="string_example",
    amount=3.14,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### transferred_from: `str`<a id="transferred_from-str"></a>

The merchant's GUID of the withdrawn account. Value provided by ConnexPay.

##### transferred_to: `str`<a id="transferred_to-str"></a>

The merchant's GUID of the deposited account. Value provided by ConnexPay.

##### amount: `Union[int, float]`<a id="amount-unionint-float"></a>

Transferred funding amount that will be processed. Maximum transaction and daily funding limits are set by ConnexPay.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`FundingTransferMerchantCashBalanceRequest`](./connex_pay_python_sdk/type/funding_transfer_merchant_cash_balance_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`FundingTransferMerchantCashBalanceResponse`](./connex_pay_python_sdk/pydantic/funding_transfer_merchant_cash_balance_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/MerchantFlexFunding/Funds/Transfer` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `connexpay.funds.get_available_details`<a id="connexpayfundsget_available_details"></a>

Use this endpoint to pull details regarding your Available Funds like cash balance, Available to Authorize (ATA) or Available to Issue (ATI), and the details that make up the final number.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_available_details_response = connexpay.funds.get_available_details(
    merchant_guid="MerchantGuid_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### merchant_guid: `str`<a id="merchant_guid-str"></a>

Merchant's Guid assigned by ConnexPay

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/Search/AvailableFunds/{merchantGuid}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `connexpay.merchant_payees.create_payee`<a id="connexpaymerchant_payeescreate_payee"></a>

Create a payee for a merchant

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_payee_response = connexpay.merchant_payees.create_payee(
    is_business=False,
    payee_id="payeeID01",
    preferred_payout_method="VCC",
    merchant_guid="merchantGuid_example",
    id_merchant=0,
    first_name="John",
    last_name="Doe",
    dba_name="",
    tax_id="12-3456789",
    customer_id="customerID01",
    email="test@test.com",
    address1="123 Main St",
    address2="",
    city="Anytown",
    state="",
    zip="12345",
    country="US",
    preferred_card_brand="Visa",
    preferred_card_class="CreditCommercial",
    purchase_type="01",
    guid="00000000-0000-0000-0000-000000000000",
    timestamp="1970-01-01T00:00:00.00Z",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### is_business: `bool`<a id="is_business-bool"></a>

##### payee_id: `str`<a id="payee_id-str"></a>

##### preferred_payout_method: `str`<a id="preferred_payout_method-str"></a>

##### merchant_guid: `str`<a id="merchant_guid-str"></a>

The merchant guid

##### id_merchant: `int`<a id="id_merchant-int"></a>

##### first_name: `str`<a id="first_name-str"></a>

##### last_name: `str`<a id="last_name-str"></a>

##### dba_name: `str`<a id="dba_name-str"></a>

##### tax_id: `str`<a id="tax_id-str"></a>

##### customer_id: `str`<a id="customer_id-str"></a>

##### email: `str`<a id="email-str"></a>

##### address1: `str`<a id="address1-str"></a>

##### address2: `str`<a id="address2-str"></a>

##### city: `str`<a id="city-str"></a>

##### state: `str`<a id="state-str"></a>

##### zip: `str`<a id="zip-str"></a>

##### country: `str`<a id="country-str"></a>

##### preferred_card_brand: `str`<a id="preferred_card_brand-str"></a>

##### preferred_card_class: `str`<a id="preferred_card_class-str"></a>

##### purchase_type: `str`<a id="purchase_type-str"></a>

##### guid: `str`<a id="guid-str"></a>

##### timestamp: `datetime`<a id="timestamp-datetime"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`MerchantPayeeDto`](./connex_pay_python_sdk/type/merchant_payee_dto.py)
The merchant payee dto

#### 🔄 Return<a id="🔄-return"></a>

[`MerchantPayeeDto`](./connex_pay_python_sdk/pydantic/merchant_payee_dto.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/Merchants/{merchantGuid}/Payees` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `connexpay.merchant_payees.delete_payee`<a id="connexpaymerchant_payeesdelete_payee"></a>

Delete a payee for a merchant by guid

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
connexpay.merchant_payees.delete_payee(
    merchant_guid="merchantGuid_example",
    payee_guid="payeeGuid_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### merchant_guid: `str`<a id="merchant_guid-str"></a>

The merchant guid

##### payee_guid: `str`<a id="payee_guid-str"></a>

The payee guid

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/Merchants/{merchantGuid}/Payees/{payeeGuid}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `connexpay.merchant_payees.get_payee`<a id="connexpaymerchant_payeesget_payee"></a>

Get a payee for a merchant by guid

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_payee_response = connexpay.merchant_payees.get_payee(
    merchant_guid="merchantGuid_example",
    payee_guid="payeeGuid_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### merchant_guid: `str`<a id="merchant_guid-str"></a>

The merchant guid

##### payee_guid: `str`<a id="payee_guid-str"></a>

The payee guid

#### 🔄 Return<a id="🔄-return"></a>

[`MerchantPayeeDto`](./connex_pay_python_sdk/pydantic/merchant_payee_dto.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/Merchants/{merchantGuid}/Payees/{payeeGuid}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `connexpay.merchant_payees.get_payees`<a id="connexpaymerchant_payeesget_payees"></a>

Get a list of payees for a merchant

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_payees_response = connexpay.merchant_payees.get_payees(
    merchant_guid="merchantGuid_example",
    page=1,
    pagesize=1,
    search_term="payeeID01",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### merchant_guid: `str`<a id="merchant_guid-str"></a>

The merchant guid

##### page: `int`<a id="page-int"></a>

The page number

##### pagesize: `int`<a id="pagesize-int"></a>

The number of records to return per page

##### search_term: `str`<a id="search_term-str"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`SearchMerchantPayeeDto`](./connex_pay_python_sdk/type/search_merchant_payee_dto.py)
A payload of search/filter parameters

#### 🔄 Return<a id="🔄-return"></a>

[`MerchantPayeePaginatedResponse`](./connex_pay_python_sdk/pydantic/merchant_payee_paginated_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/Merchants/{merchantGuid}/Payees/Search/{page}/{pagesize}` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `connexpay.merchant_payees.update_payee`<a id="connexpaymerchant_payeesupdate_payee"></a>

Update a payee for a merchant by guid

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
connexpay.merchant_payees.update_payee(
    is_business=False,
    payee_id="payeeID01",
    preferred_payout_method="VCC",
    merchant_guid="merchantGuid_example",
    payee_guid="payeeGuid_example",
    id_merchant=0,
    first_name="John",
    last_name="Doe",
    dba_name="",
    tax_id="12-3456789",
    customer_id="customerID01",
    email="test@test.com",
    address1="123 Main St",
    address2="",
    city="Anytown",
    state="",
    zip="12345",
    country="US",
    preferred_card_brand="Visa",
    preferred_card_class="CreditCommercial",
    purchase_type="01",
    guid="00000000-0000-0000-0000-000000000000",
    timestamp="1970-01-01T00:00:00.00Z",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### is_business: `bool`<a id="is_business-bool"></a>

##### payee_id: `str`<a id="payee_id-str"></a>

##### preferred_payout_method: `str`<a id="preferred_payout_method-str"></a>

##### merchant_guid: `str`<a id="merchant_guid-str"></a>

The merchant guid

##### payee_guid: `str`<a id="payee_guid-str"></a>

The payee guid

##### id_merchant: `int`<a id="id_merchant-int"></a>

##### first_name: `str`<a id="first_name-str"></a>

##### last_name: `str`<a id="last_name-str"></a>

##### dba_name: `str`<a id="dba_name-str"></a>

##### tax_id: `str`<a id="tax_id-str"></a>

##### customer_id: `str`<a id="customer_id-str"></a>

##### email: `str`<a id="email-str"></a>

##### address1: `str`<a id="address1-str"></a>

##### address2: `str`<a id="address2-str"></a>

##### city: `str`<a id="city-str"></a>

##### state: `str`<a id="state-str"></a>

##### zip: `str`<a id="zip-str"></a>

##### country: `str`<a id="country-str"></a>

##### preferred_card_brand: `str`<a id="preferred_card_brand-str"></a>

##### preferred_card_class: `str`<a id="preferred_card_class-str"></a>

##### purchase_type: `str`<a id="purchase_type-str"></a>

##### guid: `str`<a id="guid-str"></a>

##### timestamp: `datetime`<a id="timestamp-datetime"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`MerchantPayeeDto`](./connex_pay_python_sdk/type/merchant_payee_dto.py)
The merchant payee dto

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/Merchants/{merchantGuid}/Payees/{payeeGuid}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `connexpay.push_to_card.cancel_payments`<a id="connexpaypush_to_cardcancel_payments"></a>

Use this endpoint to cancel payments within a Payout.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
cancel_payments_response = connexpay.push_to_card.cancel_payments(
    merchant_guid="00000000-0000-0000-0000-000000000000",
    payments=[
        "046b6c7f-0b8a-43b9-b35d-6489e6daee91"
    ],
    payout_guid="payoutGuid_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### merchant_guid: `str`<a id="merchant_guid-str"></a>

Application-level value that indicates a Payout is being requested for client's account. Value provided by ConnexPay.

##### payments: [`CancelPaymentsDtoPayments`](./connex_pay_python_sdk/type/cancel_payments_dto_payments.py)<a id="payments-cancelpaymentsdtopaymentsconnex_pay_python_sdktypecancel_payments_dto_paymentspy"></a>

##### payout_guid: `str`<a id="payout_guid-str"></a>

Globally Unique Identifier for a the Payout that will be changed

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CancelPaymentsDto`](./connex_pay_python_sdk/type/cancel_payments_dto.py)
Indicator of which payments to cancel

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/PushToCard/Payouts/{payoutGuid}/Cancel` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `connexpay.push_to_card.create_payee`<a id="connexpaypush_to_cardcreate_payee"></a>

Use this endpoint to create a new Payee.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_payee_response = connexpay.push_to_card.create_payee(
    merchant_guid="00000000-0000-0000-0000-000000000000",
    first_name="",
    last_name="",
    email="2@[7.88.001.8]",
    phone="+10480728880",
    payee_guid="00000000-0000-0000-0000-000000000000",
    address1="",
    address2="",
    city="",
    state="",
    zip_code="",
    status="string_example",
    card_id="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### merchant_guid: `str`<a id="merchant_guid-str"></a>

Merchant guid for the Payee to be created.

##### first_name: `str`<a id="first_name-str"></a>

First name for the Payee to be created.

##### last_name: `str`<a id="last_name-str"></a>

Last name for the Payee to be created.

##### email: `str`<a id="email-str"></a>

Email address for the Payee.

##### phone: `str`<a id="phone-str"></a>

Phone number for the Payee, up to 10-character string.

##### payee_guid: `str`<a id="payee_guid-str"></a>

Guid for the created Payee that is returned by ConnexPay upon creation of a Payee. Ignored if provided in a Payee creation request.

##### address1: `str`<a id="address1-str"></a>

Postal address line 1 for the Payee. Alphanumerics and [,.-'] are allowed.

##### address2: `str`<a id="address2-str"></a>

Postal address line 2 for the Payee. Alphanumerics and [,.-'] are allowed.

##### city: `str`<a id="city-str"></a>

Postal address city for the Payee.

##### state: `str`<a id="state-str"></a>

Postal address state for the Payee.

##### zip_code: `str`<a id="zip_code-str"></a>

Postal code for the Payee.

##### status: `str`<a id="status-str"></a>

Status for the Payee.

##### card_id: `str`<a id="card_id-str"></a>

Unique identifier that refers to the card saved for a Payee when using the Payment Widget. It will be null when a Payee is created but will have a value once stored for the Payee using the Payment Widget.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`PayeeDto`](./connex_pay_python_sdk/type/payee_dto.py)
The data for the Payee that will be created

#### 🔄 Return<a id="🔄-return"></a>

[`PayeeDto`](./connex_pay_python_sdk/pydantic/payee_dto.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/PushToCard/Payees` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `connexpay.push_to_card.create_payout`<a id="connexpaypush_to_cardcreate_payout"></a>

Use this endpoint to create a new Payout.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_payout_response = connexpay.push_to_card.create_payout(
    merchant_guid="00000000-0000-0000-0000-000000000000",
    memo="",
    payments=[
        {
            "payee_guid": "00000000-0000-0000-0000-000000000000",
            "payment_guid": "00000000-0000-0000-0000-000000000000",
            "rid_guid": "00000000-0000-0000-0000-000000000000",
            "value": 3.14,
        }
    ],
    payout_guid="00000000-0000-0000-0000-000000000000",
    payout_reference_token="string_example",
    status="string_example",
    order_number="",
    customer_id="string_example",
    association_id="string_example",
    label_ids=[
        1
    ],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### merchant_guid: `str`<a id="merchant_guid-str"></a>

Application-level value that indicates a Payout is being requested for client's account. Value provided by ConnexPay.

##### memo: `str`<a id="memo-str"></a>

A brief description highlighting the reason for this Payout.

##### payments: List[`PaymentsDto`]<a id="payments-listpaymentsdto"></a>

##### payout_guid: `str`<a id="payout_guid-str"></a>

Guid assigned to the Payout by ConnexPay upon creation of a Payout.

##### payout_reference_token: `str`<a id="payout_reference_token-str"></a>

The Payout identifier that will be needed by ConnexPay support teams to research issues.

##### status: `str`<a id="status-str"></a>

Status of the Payout.

##### order_number: `str`<a id="order_number-str"></a>

The most common number used throughout the ConnexPay Portal. Transaction ID within client environment associated with the order. The value is searchable and reportable in the ConnexPay portal. This value may be sent in multiple instances of the integration for multiple purposes. The maximum length is 50 alpha-numeric characters and allows dashes ( - ).

##### customer_id: `str`<a id="customer_id-str"></a>

Transaction ID within the client environment associated with the customer. This value acts as a secondary identifier in conjunction with OrderNumber. The value is searchable and reportable in the ConnexPay portal. This value may be sent in multiple times within the integration for multiple purposes. The maximum length is 100 characters and is alpha-numeric.

##### association_id: `str`<a id="association_id-str"></a>

Association ID is used to tie a Payout to a sale or sales. For example, if you have several sales and one Payout to a Payee, association ID can be added to the sales and the Payout for downstream reporting.

##### label_ids: [`PayoutDtoLabelIds`](./connex_pay_python_sdk/type/payout_dto_label_ids.py)<a id="label_ids-payoutdtolabelidsconnex_pay_python_sdktypepayout_dto_label_idspy"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`PayoutDto`](./connex_pay_python_sdk/type/payout_dto.py)
The data for the Payout being created

#### 🔄 Return<a id="🔄-return"></a>

[`PayoutDto`](./connex_pay_python_sdk/pydantic/payout_dto.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/PushToCard/Payouts` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `connexpay.push_to_card.get_authentication_token_async`<a id="connexpaypush_to_cardget_authentication_token_async"></a>

Get Authentication Token for DropInUI

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_authentication_token_async_response = connexpay.push_to_card.get_authentication_token_async(
    payee_guid="string_example",
    payee_email_address="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### payee_guid: `str`<a id="payee_guid-str"></a>

Globally Unique Identifier for the Payee being authenticated.

##### payee_email_address: `str`<a id="payee_email_address-str"></a>

Email address of the Payee being retrieved

#### 🔄 Return<a id="🔄-return"></a>

[`PayoutAuthResponse`](./connex_pay_python_sdk/pydantic/payout_auth_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/PushToCard/AuthenticatePaymentWidget` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `connexpay.push_to_card.get_payee`<a id="connexpaypush_to_cardget_payee"></a>

Use this endpoint to retrieve a Payee for a specific Payee guid. One or both 'payeeGuid' or 'payeeEmailAddress' must be provided.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_payee_response = connexpay.push_to_card.get_payee(
    payee_guid="string_example",
    payee_email_address="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### payee_guid: `str`<a id="payee_guid-str"></a>

Globally Unique Identifier for the Payee being retrieved

##### payee_email_address: `str`<a id="payee_email_address-str"></a>

Email address of the Payee being retrieved

#### 🔄 Return<a id="🔄-return"></a>

[`PayeeDto`](./connex_pay_python_sdk/pydantic/payee_dto.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/PushToCard/Payees` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `connexpay.push_to_card.get_payout_details`<a id="connexpaypush_to_cardget_payout_details"></a>

Use this endpoint to retrieve the details for a Payout for a specific Payout guid.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_payout_details_response = connexpay.push_to_card.get_payout_details(
    payout_guid="payoutGuid_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### payout_guid: `str`<a id="payout_guid-str"></a>

Globally Unique Identifier for a the Payout that will be retrieved

#### 🔄 Return<a id="🔄-return"></a>

[`DtoPayout`](./connex_pay_python_sdk/pydantic/dto_payout.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/PushToCard/Payouts/{payoutGuid}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `connexpay.push_to_card.manage_payee`<a id="connexpaypush_to_cardmanage_payee"></a>

Use this endpoint to enable or disable a Payee.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
manage_payee_response = connexpay.push_to_card.manage_payee(
    payee_guid="payeeGuid_example",
    status="enable",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### payee_guid: `str`<a id="payee_guid-str"></a>

Globally Unique Identifier for the Payee that will be changed

##### status: `str`<a id="status-str"></a>

Must be 'enable' or 'disable'

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/PushToCard/Payees/{payeeGuid}/{status}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `connexpay.push_to_card.push_funds_to_card_async`<a id="connexpaypush_to_cardpush_funds_to_card_async"></a>

Push Funds to a Card

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
push_funds_to_card_async_response = connexpay.push_to_card.push_funds_to_card_async(
    rid_guid="ridGuid_example",
    card_id="cardId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### rid_guid: `str`<a id="rid_guid-str"></a>

For Payment Widget clients. A ridGuid will will be returned upon creation of a Payout. That must be saved and passed here to complete the process.

##### card_id: `str`<a id="card_id-str"></a>

For Payment Widget clients. The cardId is retrieved by calling the Get Payee endpoint.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/PushToCard/Payments/{ridGuid}/{cardId}` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `connexpay.push_to_card.update_payee`<a id="connexpaypush_to_cardupdate_payee"></a>

Use this endpoint to update data for a Payee.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_payee_response = connexpay.push_to_card.update_payee(
    payee_guid="payeeGuid_example",
    first_name="",
    last_name="",
    email="2@[7.88.001.8]",
    address1="",
    address2="",
    city="",
    state="",
    zip_code="",
    phone="+10480728880",
    status="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### payee_guid: `str`<a id="payee_guid-str"></a>

Globally Unique Identifier for a the Payee that will be updated

##### first_name: `str`<a id="first_name-str"></a>

First name for the Payee to be updated.

##### last_name: `str`<a id="last_name-str"></a>

Last name for the Payee to be updated.

##### email: `str`<a id="email-str"></a>

Email address for the Payee to be updated.

##### address1: `str`<a id="address1-str"></a>

Postal address line 1 for the Payee to be updated. Alphanumerics and [,.-'] are allowed.

##### address2: `str`<a id="address2-str"></a>

Postal address line 2 for the Payee to be updated. Alphanumerics and [,.-'] are allowed.

##### city: `str`<a id="city-str"></a>

Postal address city for the Payee to be updated.

##### state: `str`<a id="state-str"></a>

Postal address state for the Payee to be updated.

##### zip_code: `str`<a id="zip_code-str"></a>

Postal code for the Payee to be updated.

##### phone: `str`<a id="phone-str"></a>

Phone number for the Payee to be updated, up to 10-character string.

##### status: `str`<a id="status-str"></a>

Status for the Payee to be updated.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`UpdatePayeeDto`](./connex_pay_python_sdk/type/update_payee_dto.py)
The data for the Payee that will be updated

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/PushToCard/Payees/{payeeGuid}` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `connexpay.replay.purchase_event_history_resend`<a id="connexpayreplaypurchase_event_history_resend"></a>

Call this endpoint to receive VCC, Lodged Card, Physical Card or ACH purchase events either by unique Guid or for a specified date range. If you subscribe to webhooks and are concerned you may be missing events, this endpoint can retrieve past events.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
purchase_event_history_resend_response = connexpay.replay.purchase_event_history_resend(
    source_guid="string_example",
    merchant_guid="string_example",
    event_guid="string_example",
    from_date_time="1970-01-01",
    to_date_time="1970-01-01",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### source_guid: `str`<a id="source_guid-str"></a>

The unique GUID for a particular purchase.  This would be the Guid returned on your virtual card, lodged card, physical card or ACH issue call.

##### merchant_guid: `str`<a id="merchant_guid-str"></a>

Include your Merchant Guid instead of the Source Guid if you want to see all events for a given date range (you must also include the date range parameters)

##### event_guid: `str`<a id="event_guid-str"></a>

Transaction ID as displayed in Bridge

##### from_date_time: `date`<a id="from_date_time-date"></a>

From date

##### to_date_time: `date`<a id="to_date_time-date"></a>

To date

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ReplayPurchaseEventHistoryResendRequest`](./connex_pay_python_sdk/type/replay_purchase_event_history_resend_request.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/PurchaseEventHistory/Resend` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `connexpay.return.item_request`<a id="connexpayreturnitem_request"></a>

Return

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
item_request_response = connexpay.return.item_request(
    device_guid="string_example",
    amount=3.14,
    sale_guid="string_example",
    sale_reference_number=1,
    sequence_number="string_example",
    return_retry_card={
    },
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### device_guid: `str`<a id="device_guid-str"></a>

Device's Guid

##### amount: `Union[int, float]`<a id="amount-unionint-float"></a>

Transaction’s amount. Min. amt.: $0.50

##### sale_guid: `str`<a id="sale_guid-str"></a>

Mandatory when SaleReferenceNumber field is not sent. Sale's Guid.

##### sale_reference_number: `int`<a id="sale_reference_number-int"></a>

Mandatory when SaleGuid field is not sent. Sale's Reference Number

##### sequence_number: `str`<a id="sequence_number-str"></a>

Transaction sequence number within client environment. Provide a unique SequenceNumber for each new request. If the same value is sent within 30 minutes it will be considered a duplicate request. Note: value is not searchable or reportable in ConnexPay portal.  Alphanumeric.

##### return_retry_card: [`ReturnItemRequestRequestReturnRetryCard`](./connex_pay_python_sdk/type/return_item_request_request_return_retry_card.py)<a id="return_retry_card-returnitemrequestrequestreturnretrycardconnex_pay_python_sdktypereturn_item_request_request_return_retry_cardpy"></a>


#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ReturnItemRequestRequest`](./connex_pay_python_sdk/type/return_item_request_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`ReturnItemRequestResponse`](./connex_pay_python_sdk/pydantic/return_item_request_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/returns` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `connexpay.return.search_sale_returns`<a id="connexpayreturnsearch_sale_returns"></a>

This endpoint searches sale returns.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
search_sale_returns_response = connexpay.return.search_sale_returns(
    exportable="Mandatory",
    page_number=1,
    page_size="Optional",
    merchant_guid="Mandatory",
    amount_from=3.14,
    amount_to=3.14,
    card_holder_name="Optional",
    status="Optional",
    time_stamp_from="Optional",
    time_stamp_to="Optional",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### exportable: `str`<a id="exportable-str"></a>

True or False. It means if you want results exportable to CSV.

##### page_number: `int`<a id="page_number-int"></a>

Int. Number of page of the results. Default is 1 (Page size default is 500).

##### page_size: `str`<a id="page_size-str"></a>

Int. Size of each page of the results. Default is 500.

##### merchant_guid: `str`<a id="merchant_guid-str"></a>

Merchant’s Guid.

##### amount_from: `Union[int, float]`<a id="amount_from-unionint-float"></a>

Amount of the transaction. Min. amt.: $0.50

##### amount_to: `Union[int, float]`<a id="amount_to-unionint-float"></a>

Amount of the transaction. Min. amt.: $0.50

##### card_holder_name: `str`<a id="card_holder_name-str"></a>

Cardholder’s name. Providing information in this field allows a user of the ConnexPay portal to search for a transaction using the cardholder name.

##### status: `str`<a id="status-str"></a>

Return’s status.  Allowed values:  1. Transaction - Approved 2. Transaction - Declined 3. Transaction - Created - Local 4. Transaction - Created - Error: Processor not reached 5. Transaction - Processor Error 6. Transaction - Approved - Warning

##### time_stamp_from: `date`<a id="time_stamp_from-date"></a>

Return’s TimeStamp.

##### time_stamp_to: `date`<a id="time_stamp_to-date"></a>

Return’s TimeStamp.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ReturnSearchSaleReturnsRequest`](./connex_pay_python_sdk/type/return_search_sale_returns_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`ReturnSearchSaleReturnsResponse`](./connex_pay_python_sdk/pydantic/return_search_sale_returns_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/Search/Returns/{exportable}/{pageNumber}/{pageSize}` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `connexpay.sale.activate_delayed`<a id="connexpaysaleactivate_delayed"></a>

Activate a delayed activation sale independent of the activation date for which the sale was created.

A client can "Activate" a delayed activation sale this way at any time before ConnexPay will automatically activate it during the early hours of the supplied future date.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
activate_delayed_response = connexpay.sale.activate_delayed(
    sale_guid="SaleGuid_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### sale_guid: `str`<a id="sale_guid-str"></a>

The sale guid returned upon initial creation of the delayed activation sale.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/sales/Activate/{SaleGuid}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `connexpay.sale.create_transaction`<a id="connexpaysalecreate_transaction"></a>

The Create Sale Endpoint is used by acquiring clients. The Sale transaction is used to create a sale for your consumer. You can create a credit sale or an ACH sale (ACH sales apply to US Clients only). A credit sale will charge a consumer's credit card. The consumer's credit card will be authorized immediately when the Sales request is received and will automatically settle/batch that same night. In other words, this one Sale request is just like running an AuthOnly and a Capture in one request.You can postpone charging the consumer's credit card by providing a date in the 'ActivationDate' of your request. Doing so will delay the authorization and charge to the consumer's credit card until that future date.An ACH sale will create an ACH transaction that will debit the consumer's bank account. ACH sales received prior to 3:00 PM EST will process overnight. ACH Sales received after 3:00 PM EST will process the following night.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_transaction_response = connexpay.sale.create_transaction(
    device_guid="{{Device}}",
    amount=3.14,
    connex_pay_transaction={
        "expected_payments": 1,
    },
    risk_data={
    },
    tender_type="credit",
    sequence_number="{{SequenceNumber}}",
    order_number="{{OrderNumber}}",
    send_receipt=True,
    risk_processing_only=True,
    statement_description="{{StatementDescription}}",
    customer_id="string_example",
    activation_date="1970-01-01",
    request_ip="string_example",
    card={
        "is_recurring": False,
    },
    bank_account={
        "account_type": "account_type_example",
        "routing_number": "routing_number_example",
        "account_number": "account_number_example",
        "name_on_account": "name_on_account_example",
    },
    customer={
    },
    enhanced_data={
    },
    association_id="string_example",
    custom_parameters=[
        {
        }
    ],
    label_ids=[
        "string_example"
    ],
    browser_data={
        "acceptance_header": "acceptance_header_example",
        "color_depth": 1,
        "java_enabled": True,
        "screen_height": 1,
        "screen_width": 1,
        "time_zone_offset": 1,
        "language": "language_example",
        "redirect_url": "redirect_url_example",
        "user_agent_header": "user_agent_header_example",
    },
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### device_guid: `str`<a id="device_guid-str"></a>

Device's Guid provided by ConnexPay

##### amount: `Union[int, float]`<a id="amount-unionint-float"></a>

Amount of the transaction that will be processed. Note: this value is submitted multiple times (in different formats) within the integration to support different purposes i.e. risk analysis, merchant processing, etc.  The minimum amount is: $0.50.

##### connex_pay_transaction: [`SaleCreateTransactionRequestConnexPayTransaction`](./connex_pay_python_sdk/type/sale_create_transaction_request_connex_pay_transaction.py)<a id="connex_pay_transaction-salecreatetransactionrequestconnexpaytransactionconnex_pay_python_sdktypesale_create_transaction_request_connex_pay_transactionpy"></a>


##### risk_data: [`SaleCreateTransactionRequestRiskData`](./connex_pay_python_sdk/type/sale_create_transaction_request_risk_data.py)<a id="risk_data-salecreatetransactionrequestriskdataconnex_pay_python_sdktypesale_create_transaction_request_risk_datapy"></a>


##### tender_type: `str`<a id="tender_type-str"></a>

Allowed values:  \\\"credit\\\" (default if TenderType not provided) and \\\"ach\\\"

##### sequence_number: `str`<a id="sequence_number-str"></a>

Transaction sequence number within client environment. Provide a unique SequenceNumber for each new request. If a sale request with the same parameter data and the same sequence number is sent within 30 minutes it will be considered a duplicate request and the sale will not process. Note: value is not searchable or reportable in Bridge.  Alphanumeric.

##### order_number: `str`<a id="order_number-str"></a>

This is the most common number you'll see throughout the ConnexPay Portal.  Transaction ID within client environment associated with the order. The value is searchable and reportable in the ConnexPay portal. This value may be sent in multiple instances of the integration for multiple purposes. Customers in the travel space often send the Record Locator/PNR in this field.  The maximum length is 50 alpha-numeric characters and allows dashes ( - ).

##### send_receipt: `bool`<a id="send_receipt-bool"></a>

Value determines whether or not a customer shall be emailed a receipt from the ConnexPay platform if the email address is provided in the API customer block. The default value is TRUE. Set to FALSE so that an email receipt is not sent to the customer. Set to TRUE or leave empty if you want e-mail to be sent. If TRUE, customer's email must be included in the \\\"Card.Customer.email\\\" parameter.

##### risk_processing_only: `bool`<a id="risk_processing_only-bool"></a>

Indicator that determines if client would like to evaluate the transactions as risk only rather than process as merchant of record and create a virtual card. The allowed values:  1. Set to TRUE will only run risk validations. If TenderType is not set to Credit, setting TRUE will throw a validation error.  2. Set to FALSE will run risk validations and an authorization on the card. For this option a Processing Merchant account is required, contact ConnexPay support if any questions.  3. Set to NULL and your Merchant Level settings would apply.

##### statement_description: `str`<a id="statement_description-str"></a>

US Clients only: The statement description allows a client to customize the Merchant name that appears on the cardholder statement such that the cardholder recognizes the transaction on their statement. For US Merchants: ConnexPay recommends sending a recognizable DBA along with the PNR i.e. ABC Travel ABC123.  The maximum length is 25 alpha-numeric characters.  For EU Merchants: The maximum length of the description is 13 alphanumeric characters and the DBA Name and City will automatically be coded to appear as part of the statement description. Note: functionality not applicable for American Express program.

##### customer_id: `str`<a id="customer_id-str"></a>

Transaction ID within client environment associated with the customer. This value acts as a secondary identifier in conjunction with OrderNumber. The value is searchable and reportable in the ConnexPay portal. This value may be sent in multiple times within the integration for multiple purposes.  The maximum length is 100 characters and is alpha-numeric.

##### activation_date: `date`<a id="activation_date-date"></a>

Set a future date on which to run this sale, at least one day from creation date and within 600 days. If this parameter is supplied a record for this sale is created, supplied consumer card information is internally tokenized, but fraud check and authorization do not occur until ConnexPay processes it on the supplied ActivationDate. Alternatively, a client can force activation via the Activate API (see below). If this date is not supplied a sale is authorized and the consumer's credit card is charged immediately.

##### request_ip: `str`<a id="request_ip-str"></a>

Mandatory if TenderType is ACH. Customer's IP Address is a required parameter for all ACH Sales transactions to adhere to NACHA regulations.

##### card: [`SaleCreateTransactionRequestCard`](./connex_pay_python_sdk/type/sale_create_transaction_request_card.py)<a id="card-salecreatetransactionrequestcardconnex_pay_python_sdktypesale_create_transaction_request_cardpy"></a>


##### bank_account: [`SaleCreateTransactionRequestBankAccount`](./connex_pay_python_sdk/type/sale_create_transaction_request_bank_account.py)<a id="bank_account-salecreatetransactionrequestbankaccountconnex_pay_python_sdktypesale_create_transaction_request_bank_accountpy"></a>


##### customer: [`SaleCreateTransactionRequestCustomer`](./connex_pay_python_sdk/type/sale_create_transaction_request_customer.py)<a id="customer-salecreatetransactionrequestcustomerconnex_pay_python_sdktypesale_create_transaction_request_customerpy"></a>


##### enhanced_data: [`SaleCreateTransactionRequestEnhancedData`](./connex_pay_python_sdk/type/sale_create_transaction_request_enhanced_data.py)<a id="enhanced_data-salecreatetransactionrequestenhanceddataconnex_pay_python_sdktypesale_create_transaction_request_enhanced_datapy"></a>


##### association_id: `str`<a id="association_id-str"></a>

Utilize the Association ID field to tie a virtual card to a sale or sales. For example, if you have several sales and one virtual card payment to a supplier, you can add association ID to the sales and the virtual card for downstream reporting.

##### custom_parameters: [`SaleCreateTransactionRequestCustomParameters`](./connex_pay_python_sdk/type/sale_create_transaction_request_custom_parameters.py)<a id="custom_parameters-salecreatetransactionrequestcustomparametersconnex_pay_python_sdktypesale_create_transaction_request_custom_parameterspy"></a>

##### label_ids: [`SaleCreateTransactionRequestLabelIDs`](./connex_pay_python_sdk/type/sale_create_transaction_request_label_ids.py)<a id="label_ids-salecreatetransactionrequestlabelidsconnex_pay_python_sdktypesale_create_transaction_request_label_idspy"></a>

##### browser_data: [`SaleCreateTransactionRequestBrowserData`](./connex_pay_python_sdk/type/sale_create_transaction_request_browser_data.py)<a id="browser_data-salecreatetransactionrequestbrowserdataconnex_pay_python_sdktypesale_create_transaction_request_browser_datapy"></a>


#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`SaleCreateTransactionRequest`](./connex_pay_python_sdk/type/sale_create_transaction_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`SaleCreateTransactionResponse`](./connex_pay_python_sdk/pydantic/sale_create_transaction_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/sales` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `connexpay.sale.get_chargebacks_by_user`<a id="connexpaysaleget_chargebacks_by_user"></a>

Sales Chargebacks

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_chargebacks_by_user_response = connexpay.sale.get_chargebacks_by_user(
    get_by_userstart_date2016_12_01="/GetByUser?startDate=2016-12-01_example",
    get_by_userstart_date2016_12_01end_date2016_12_01="/GetByUser?startDate=2016-12-01&endDate=2016-12-01_example",
    get_by_resolved_datestart_date2019_09_20end_date2019_10_21="/GetByResolvedDate?startDate=2019-09-20&endDate=2019-10-21_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### get_by_userstart_date2016_12_01: `str`<a id="get_by_userstart_date2016_12_01-str"></a>

Return all chargebacks for the authenticated user with a start date

##### get_by_userstart_date2016_12_01end_date2016_12_01: `str`<a id="get_by_userstart_date2016_12_01end_date2016_12_01-str"></a>

Return all chargebacks for the authenticated user with a start and end date

##### get_by_resolved_datestart_date2019_09_20end_date2019_10_21: `str`<a id="get_by_resolved_datestart_date2019_09_20end_date2019_10_21-str"></a>

Return all chargebacks for the authenticated user with a start and end date based on resolved date

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/chargeback/GetByUser` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `connexpay.sale.search_sales`<a id="connexpaysalesearch_sales"></a>

This endpoint searches sales.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
search_sales_response = connexpay.sale.search_sales(
    exportable="Mandatory",
    page_number=1,
    page_size="Optional",
    merchant_guid="Mandatory",
    amount_from=3.14,
    amount_to=3.14,
    card_holder_name="Optional",
    card_last_four="Optional",
    card_type="Optional",
    invoice_number=1,
    order_number="Optional",
    order_date_from="Optional",
    order_date_to="Optional",
    time_stamp_from="Optional",
    time_stamp_to="Optional",
    status="Optional",
    merchant_customer_id="Optional",
    activated=False,
    activation_date_from="Optional",
    activation_date_to="Optional",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### exportable: `str`<a id="exportable-str"></a>

True or False. It means if you want results exportable to CSV.

##### page_number: `int`<a id="page_number-int"></a>

Int. Number of page of the results. Default is 1 (Page size default is 500).

##### page_size: `str`<a id="page_size-str"></a>

Int. Size of each page of the results. Default is 500.

##### merchant_guid: `str`<a id="merchant_guid-str"></a>

Merchant’s Guid.

##### amount_from: `Union[int, float]`<a id="amount_from-unionint-float"></a>

Amount of the transaction. Min. amt.: $0.50

##### amount_to: `Union[int, float]`<a id="amount_to-unionint-float"></a>

Amount of the transaction. Min. amt.: $0.50

##### card_holder_name: `str`<a id="card_holder_name-str"></a>

Cardholder’s name.

##### card_last_four: `str`<a id="card_last_four-str"></a>

Card last four number.

##### card_type: `str`<a id="card_type-str"></a>

Card type.

##### invoice_number: `int`<a id="invoice_number-int"></a>

Sale’s InvoiceNumber.

##### order_number: `str`<a id="order_number-str"></a>

Sale’s order number. Length = 17.

##### order_date_from: `date`<a id="order_date_from-date"></a>

Sale’s order Date.

##### order_date_to: `date`<a id="order_date_to-date"></a>

Sale’s order Date.

##### time_stamp_from: `date`<a id="time_stamp_from-date"></a>

Sale’s TimeStamp.

##### time_stamp_to: `date`<a id="time_stamp_to-date"></a>

Sale’s TimeStamp.

##### status: `str`<a id="status-str"></a>

Sale’s status. Allowed values:  1. Transaction - Approved 2. Transaction - Declined 3. Transaction - Created - Local 4. Transaction - Created - Error: Processor not reached 5. Transaction - Processor Error 6. Transaction - Approved - Warning

##### merchant_customer_id: `str`<a id="merchant_customer_id-str"></a>

Merchant Customer Id.

##### activated: `bool`<a id="activated-bool"></a>

Delayed Activation Sales to be included or not

##### activation_date_from: `date`<a id="activation_date_from-date"></a>

Activation Start Date. This field is applicable only when Activated flag is set to true.

##### activation_date_to: `date`<a id="activation_date_to-date"></a>

Activation End Date. This field is applicable only when Activated flag is set to true.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`SaleSearchSalesRequest`](./connex_pay_python_sdk/type/sale_search_sales_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`SaleSearchSalesResponse`](./connex_pay_python_sdk/pydantic/sale_search_sales_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/Search/Sales/{exportable}/{pageNumber}/{pageSize}` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `connexpay.sale.update_delayed_activation`<a id="connexpaysaleupdate_delayed_activation"></a>

Updates the sale amount or activation date on a delayed activation sale.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_delayed_activation_response = connexpay.sale.update_delayed_activation(
    device_guid="string_example",
    sale_guid="string_example",
    amount=3.14,
    activation_date="1970-01-01",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### device_guid: `str`<a id="device_guid-str"></a>

Device's Guid provided by ConnexPay.

##### sale_guid: `str`<a id="sale_guid-str"></a>

Sales's Guid that was provided by ConnexPay upon initial creation of the delayed activation sale.

##### amount: `Union[int, float]`<a id="amount-unionint-float"></a>

Amount of the transaction that will be processed. Note: this value is submitted multiple times (in different formats) within the integration to support different purposes i.e. risk analysis, merchant processing, etc.  The minimun amount is: $0.50.

##### activation_date: `date`<a id="activation_date-date"></a>

Set a future date on which to run this sale, at least one day from creation date and within 600 days.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`SaleUpdateDelayedActivationRequest`](./connex_pay_python_sdk/type/sale_update_delayed_activation_request.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/sales/UpdateFutureSale` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `connexpay.setting.tokenize_bank_account_info`<a id="connexpaysettingtokenize_bank_account_info"></a>

This endpoint allows you to create and tokenize a suppliers bank account information without actually making the Issue ACH call. That tokenized bank account can then be used in future Issue ACH or Issue ACH Lite API requests so you don't have to store the actual bank account information.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
tokenize_bank_account_info_response = connexpay.setting.tokenize_bank_account_info(
    merchant_guid="string_example",
    supplier_name="string_example",
    account_holder={
        "business_name": "Default",
    },
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### merchant_guid: `str`<a id="merchant_guid-str"></a>

Merchant's guid. Application level value that indicates the ACH payment is being requested for clients account. Value provided by ConnexPay.

##### supplier_name: `str`<a id="supplier_name-str"></a>

Name of supplier to whom payment will be made

##### account_holder: [`SettingTokenizeBankAccountInfoRequestAccountHolder`](./connex_pay_python_sdk/type/setting_tokenize_bank_account_info_request_account_holder.py)<a id="account_holder-settingtokenizebankaccountinforequestaccountholderconnex_pay_python_sdktypesetting_tokenize_bank_account_info_request_account_holderpy"></a>


#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`SettingTokenizeBankAccountInfoRequest`](./connex_pay_python_sdk/type/setting_tokenize_bank_account_info_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`SettingTokenizeBankAccountInfoResponse`](./connex_pay_python_sdk/pydantic/setting_tokenize_bank_account_info_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/merchantsupplier/settings` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `connexpay.settlement.search_virtual_card_settlements`<a id="connexpaysettlementsearch_virtual_card_settlements"></a>

This endpoint searches for Virtual Card Settlements.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
search_virtual_card_settlements_response = connexpay.settlement.search_virtual_card_settlements(
    merchant_guid="string_example",
    page_number=1,
    page_size=1,
    date_from="1970-01-01",
    date_to="1970-01-01",
    posted_date_from="1970-01-01",
    posted_date_to="1970-01-01",
    order_number="string_example",
    issued_amount_from=1,
    issued_amount_to=1,
    issued_card_last_four="string_example",
    posted_amount_from=3.14,
    posted_amount_to=3.14,
    expiration_date_from="1970-01-01",
    expiration_date_to="1970-01-01",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### merchant_guid: `str`<a id="merchant_guid-str"></a>

Merchant's Guid.

##### page_number: `int`<a id="page_number-int"></a>

Number of pages of results to return. Default is 1.

##### page_size: `int`<a id="page_size-int"></a>

Size of each page of results. Default is 1000.

##### date_from: `date`<a id="date_from-date"></a>

Card's Issued Date.

##### date_to: `date`<a id="date_to-date"></a>

Card's Issued Date.

##### posted_date_from: `date`<a id="posted_date_from-date"></a>

Card settlement post date.

##### posted_date_to: `date`<a id="posted_date_to-date"></a>

Card settlement post date.

##### order_number: `str`<a id="order_number-str"></a>

Order Number. Max. Length = 50.

##### issued_amount_from: `int`<a id="issued_amount_from-int"></a>

Issued Amount of the Card.

##### issued_amount_to: `int`<a id="issued_amount_to-int"></a>

Issued Amount of the Card.

##### issued_card_last_four: `str`<a id="issued_card_last_four-str"></a>

Card last four number.

##### posted_amount_from: `Union[int, float]`<a id="posted_amount_from-unionint-float"></a>

Posted Amount of the Card.

##### posted_amount_to: `Union[int, float]`<a id="posted_amount_to-unionint-float"></a>

Posted Amount of the Card.

##### expiration_date_from: `date`<a id="expiration_date_from-date"></a>

Card's expiration date.

##### expiration_date_to: `date`<a id="expiration_date_to-date"></a>

Card's expiration date.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`SettlementSearchVirtualCardSettlementsRequest`](./connex_pay_python_sdk/type/settlement_search_virtual_card_settlements_request.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/Search/Settlements` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `connexpay.status_group.call_3ds_authentication_status`<a id="connexpaystatus_groupcall_3ds_authentication_status"></a>

This endpoint returns the 3D Secure status of an authentication when a device fingerprint and/or cardholder challenge are required for 3D Secure Authentication.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
call_3ds_authentication_status_response = connexpay.status_group.call_3ds_authentication_status(
    guid="guid_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### guid: `str`<a id="guid-str"></a>

Replace the original guid value with the guid that was returned with the status response indicating a device fingerprint or cardholder challenge is required to complete 3DS authentication..

#### 🔄 Return<a id="🔄-return"></a>

[`StatusGroup3DsAuthenticationStatusResponse`](./connex_pay_python_sdk/pydantic/status_group3_ds_authentication_status_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/3ds/{GUID}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `connexpay.token.generate_reporting_token`<a id="connexpaytokengenerate_reporting_token"></a>

Reporting API requests require a combination of assigned Bridge user name, Bridge password, and a successfully generated authentication token. The Bridge credentials used are assigned separately from the Purchase and Sales API credentials. The received token for Reporting is valid for 60 minutes from issuance and may be used for all requests during its lifespan.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
generate_reporting_token_response = connexpay.token.generate_reporting_token(
    user_name="string_example",
    password="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### user_name: `str`<a id="user_name-str"></a>

Assigned username for CXP Bridge

##### password: `str`<a id="password-str"></a>

Assigned password for CXP Bridge

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`TokenGenerateReportingTokenRequest`](./connex_pay_python_sdk/type/token_generate_reporting_token_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`TokenGenerateReportingTokenResponse`](./connex_pay_python_sdk/pydantic/token_generate_reporting_token_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/authenticate` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `connexpay.token.issue_authentication_token`<a id="connexpaytokenissue_authentication_token"></a>

API requests require a combination of assigned user name, password, and successfully generated authentication token. The received token is valid for 24 hours from issuance and may be used for all requests during its lifespan.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
issue_authentication_token_response = connexpay.token.issue_authentication_token(
    grant_type="password",
    username="string_example",
    password="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### grant_type: `str`<a id="grant_type-str"></a>

##### username: `str`<a id="username-str"></a>

CXP provided username

##### password: `str`<a id="password-str"></a>

CXP provided password

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`TokenIssueAuthenticationTokenRequest`](./connex_pay_python_sdk/type/token_issue_authentication_token_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`TokenIssueAuthenticationTokenResponse`](./connex_pay_python_sdk/pydantic/token_issue_authentication_token_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/token` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `connexpay.token.request_hpp_token`<a id="connexpaytokenrequest_hpp_token"></a>

HPP Token Request

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
request_hpp_token_response = connexpay.token.request_hpp_token(
    merchant_name="string_example",
    sale={
        "device_guid": "device_guid_example",
        "amount": 1,
    },
    description="string_example",
    result_redirect_url="string_example",
    logo_url="string_example",
    tender_type_options=["Credit"],
    expiration="Current DateTime UTC",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### merchant_name: `str`<a id="merchant_name-str"></a>

Merchant Name. ConnexPay displays this on the Hosted Payment Page. The max length is 100 characters.

##### sale: [`TokenRequestHppTokenRequestSale`](./connex_pay_python_sdk/type/token_request_hpp_token_request_sale.py)<a id="sale-tokenrequesthpptokenrequestsaleconnex_pay_python_sdktypetoken_request_hpp_token_request_salepy"></a>


##### description: `str`<a id="description-str"></a>

Additional information ConnexPay can display in the Hosted Payment Page. The max length is 2048 characters.

##### result_redirect_url: `str`<a id="result_redirect_url-str"></a>

This is a ConnexPay CLIENT server route ConnexPay uses to (re)direct the consumer payment result back to our client upon payment success, failure or cancel. If this data is not set, then it will use the default one from ConnexPay.

##### logo_url: `str`<a id="logo_url-str"></a>

ConnexPay can display this instead of “MerchantName” in the payment dialog.

##### tender_type_options: [`TokenRequestHppTokenRequestTenderTypeOptions`](./connex_pay_python_sdk/type/token_request_hpp_token_request_tender_type_options.py)<a id="tender_type_options-tokenrequesthpptokenrequesttendertypeoptionsconnex_pay_python_sdktypetoken_request_hpp_token_request_tender_type_optionspy"></a>

##### expiration: `datetime`<a id="expiration-datetime"></a>

Client can request a specific expiration date to identify when the HPP Link will expire. Timestamps will be converted to UTC for consistency within the ConnexPay environment.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`TokenRequestHppTokenRequest`](./connex_pay_python_sdk/type/token_request_hpp_token_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`TokenRequestHppTokenResponse`](./connex_pay_python_sdk/pydantic/token_request_hpp_token_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/HostedPaymentPageRequests` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `connexpay.transaction.capture_authorization`<a id="connexpaytransactioncapture_authorization"></a>

Call this endpoint to Capture an Authorization so that it settles

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
capture_authorization_response = connexpay.transaction.capture_authorization(
    device_guid="string_example",
    auth_only_guid="string_example",
    sequence_number="string_example",
    connex_pay_transaction={
        "expected_payments": 1,
    },
    order_number="string_example",
    customer_id="string_example",
    association_id="string_example",
    custom_parameters=[
        {
        }
    ],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### device_guid: `str`<a id="device_guid-str"></a>

Device's Guid provided by ConnexPay.

##### auth_only_guid: `str`<a id="auth_only_guid-str"></a>

Guid received from the AuthOnly operation.

##### sequence_number: `str`<a id="sequence_number-str"></a>

Transaction sequence number within client environment. Provide a unique SequenceNumber for each new request. If the same value is sent within 30 minutes it will be considered a duplicate request. Note: value is not searchable or reportable in ConnexPay portal.  Alphanumeric.

##### connex_pay_transaction: [`TransactionCaptureAuthorizationRequestConnexPayTransaction`](./connex_pay_python_sdk/type/transaction_capture_authorization_request_connex_pay_transaction.py)<a id="connex_pay_transaction-transactioncaptureauthorizationrequestconnexpaytransactionconnex_pay_python_sdktypetransaction_capture_authorization_request_connex_pay_transactionpy"></a>


##### order_number: `str`<a id="order_number-str"></a>

This is the most common number you'll see throughout the ConnexPay Portal. Transaction ID within client environment associated with the order. The value is searchable and reportable in the ConnexPay portal. This value may be sent in multiple instances of the integration for multiple purposes. Customers in the travel space often send the Record Locator/PNR in this field. The maximum length is 50 alpha-numeric characters and allows dashes ( - ). If you provided an order number in the AUTH request it will be overwritten with the order number in the CAPTURE endpoint.

##### customer_id: `str`<a id="customer_id-str"></a>

Transaction ID within client environment associated with the customer. This value acts as a secondary identifier in conjunction with OrderNumber. The value is searchable and reportable in the ConnexPay portal. This value may be sent in multiple times within the integration for multiple purposes. The maximum length is 100 characters and is alpha-numeric.

##### association_id: `str`<a id="association_id-str"></a>

Utilize the Association ID field to tie a virtual card to a sale or sales. For example, if you have several sales and one virtual card payment to a supplier, you can add association ID to the sales and the virtual card for downstream reporting.

##### custom_parameters: [`TransactionCaptureAuthorizationRequestCustomParameters`](./connex_pay_python_sdk/type/transaction_capture_authorization_request_custom_parameters.py)<a id="custom_parameters-transactioncaptureauthorizationrequestcustomparametersconnex_pay_python_sdktypetransaction_capture_authorization_request_custom_parameterspy"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`TransactionCaptureAuthorizationRequest`](./connex_pay_python_sdk/type/transaction_capture_authorization_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`TransactionCaptureAuthorizationResponse`](./connex_pay_python_sdk/pydantic/transaction_capture_authorization_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/Captures` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `connexpay.transaction.create_ach_credit_payment`<a id="connexpaytransactioncreate_ach_credit_payment"></a>

This endpoint creates an ACH Credit payment.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_ach_credit_payment_response = connexpay.transaction.create_ach_credit_payment(
    merchant_guid="string_example",
    amount=3.14,
    payee_name="string_example",
    incoming_transaction_code="string_example",
    account_holder={
        "business_name": "Default",
    },
    statement_company_name="Merchant Alias",
    description="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### merchant_guid: `str`<a id="merchant_guid-str"></a>

Merchant's guid. Application level value that indicates the ACH payment is being requested for clients account. Value provided by ConnexPay.

##### amount: `Union[int, float]`<a id="amount-unionint-float"></a>

Payment amount. Minimum amount > 0.5.

##### payee_name: `str`<a id="payee_name-str"></a>

Payee name up to 100 characters.

##### incoming_transaction_code: `str`<a id="incoming_transaction_code-str"></a>

ITC for short Application level setting to associate the ACH payment request with an original sale or sale group. The value is provided in the sale response of the original sale transaction, or in the Group Sale response of the group sale. All ACH payment requests must be associated with an original sale or group transaction.

##### account_holder: [`TransactionCreateAchCreditPaymentRequestAccountHolder`](./connex_pay_python_sdk/type/transaction_create_ach_credit_payment_request_account_holder.py)<a id="account_holder-transactioncreateachcreditpaymentrequestaccountholderconnex_pay_python_sdktypetransaction_create_ach_credit_payment_request_account_holderpy"></a>


##### statement_company_name: `str`<a id="statement_company_name-str"></a>

Company Name to display Bank Statement. The first 16 characters will display on the bank account holders statement.

##### description: `str`<a id="description-str"></a>

For banks who accept statement descriptors, the first 10 characters will display on the bank account holders statement.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`TransactionCreateAchCreditPaymentRequest`](./connex_pay_python_sdk/type/transaction_create_ach_credit_payment_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`TransactionCreateAchCreditPaymentResponse`](./connex_pay_python_sdk/pydantic/transaction_create_ach_credit_payment_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/IssueACH` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `connexpay.transaction.search_virtual_card_history`<a id="connexpaytransactionsearch_virtual_card_history"></a>

This API allows you to pull back history of the Virtual Card. This is the same API (and data) that is used when clicking the “Transactions” button on the Virtual Card in the Portal to display the transaction history. The API will return the merchant name where the Virtual Card was used, the date and time, transaction type (auth, settlement, refund, void, etc.), the response/memo which correlates to the transaction type and the amount.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
search_virtual_card_history_response = connexpay.transaction.search_virtual_card_history(
    card_guid="CardGuid_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### card_guid: `str`<a id="card_guid-str"></a>

Global Unique Identifier for the Card. Required parameter.

#### 🔄 Return<a id="🔄-return"></a>

[`TransactionSearchVirtualCardHistoryResponse`](./connex_pay_python_sdk/pydantic/transaction_search_virtual_card_history_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/Cards/Transactions/{cardGuid}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `connexpay.validation.search_verify_operation`<a id="connexpayvalidationsearch_verify_operation"></a>

This endpoint search a verify.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
search_verify_operation_response = connexpay.validation.search_verify_operation(
    exportable="Mandatory",
    page_number=1,
    page_size="Optional",
    merchant_guid="Mandatory",
    card_last_four="Optional",
    card_holder_name="Optional",
    card_type="Optional",
    time_stamp_from="Optional",
    time_stamp_to="Optional",
    status="Optional",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### exportable: `str`<a id="exportable-str"></a>

True or False. It means if you want results exportable to CSV.

##### page_number: `int`<a id="page_number-int"></a>

Int. Number of page of the results. Default is 1 (Page size default is 500).

##### page_size: `str`<a id="page_size-str"></a>

Int. Size of each page of the results. Default is 500.

##### merchant_guid: `str`<a id="merchant_guid-str"></a>

Merchant’s Guid.

##### card_last_four: `str`<a id="card_last_four-str"></a>

Card last four number.

##### card_holder_name: `str`<a id="card_holder_name-str"></a>

Cardholder’s name. Providing information in this field allows a user of the ConnexPay portal to search for a transaction using the cardholder name.

##### card_type: `str`<a id="card_type-str"></a>

Card Type.

##### time_stamp_from: `date`<a id="time_stamp_from-date"></a>

Verify’s TimeStamp From.

##### time_stamp_to: `date`<a id="time_stamp_to-date"></a>

Verify’s TimeStamp To.

##### status: `str`<a id="status-str"></a>

Verify’s status.  Allowed values:  1. Transaction - Approved 2. Transaction - Declined 3. Transaction - Created - Local 4. Transaction - Created - Error: Processor not reached 5. Transaction - Processor Error 6. Transaction - Approved - Warning

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ValidationSearchVerifyOperationRequest`](./connex_pay_python_sdk/type/validation_search_verify_operation_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`ValidationSearchVerifyOperationResponse`](./connex_pay_python_sdk/pydantic/validation_search_verify_operation_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/Search/Verify/{exportable}/{pageNumber}/{pageSize}` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `connexpay.verification.card_bank_account`<a id="connexpayverificationcard_bank_account"></a>

Call to Verify Card or Bank Account

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
card_bank_account_response = connexpay.verification.card_bank_account(
    device_guid="{{Device}}",
    card={
        "is_recurring": False,
    },
    bank_account={
        "account_type": "account_type_example",
        "routing_number": "routing_number_example",
        "account_number": "account_number_example",
        "name_on_account": "name_on_account_example",
    },
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### device_guid: `str`<a id="device_guid-str"></a>

Device's Guid provided by ConnexPay.

##### card: [`VerificationCardBankAccountRequestCard`](./connex_pay_python_sdk/type/verification_card_bank_account_request_card.py)<a id="card-verificationcardbankaccountrequestcardconnex_pay_python_sdktypeverification_card_bank_account_request_cardpy"></a>


##### bank_account: [`VerificationCardBankAccountRequestBankAccount`](./connex_pay_python_sdk/type/verification_card_bank_account_request_bank_account.py)<a id="bank_account-verificationcardbankaccountrequestbankaccountconnex_pay_python_sdktypeverification_card_bank_account_request_bank_accountpy"></a>


#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`VerificationCardBankAccountRequest`](./connex_pay_python_sdk/type/verification_card_bank_account_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`VerificationCardBankAccountResponse`](./connex_pay_python_sdk/pydantic/verification_card_bank_account_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/verify` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `connexpay.void.create_void`<a id="connexpayvoidcreate_void"></a>

This endpoint creates a void.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_void_response = connexpay.void.create_void(
    device_guid="string_example",
    sale_guid="Conditional Mandatory when SaleReferenceNumber, AuthOnlyGuid and ReturnGuid parameters are not present",
    return_guid="Conditional Mandatory when SaleGuid, AuthOnlyGuid and SaleReferenceNumber parameters are not present",
    sale_reference_number=1,
    auth_only_guid="Conditional Mandatory when SaleGuid, SaleReferenceNumber and ReturnGuid parameters are not present",
    void_reason="Optional",
    amount=3.14,
    sequence_number="Optional",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### device_guid: `str`<a id="device_guid-str"></a>

Device’s Guid provided by ConnexPay.

##### sale_guid: `str`<a id="sale_guid-str"></a>

Sale Transaction Guid

##### return_guid: `str`<a id="return_guid-str"></a>

Return's Guid

##### sale_reference_number: `int`<a id="sale_reference_number-int"></a>

Sale Reference Number

##### auth_only_guid: `str`<a id="auth_only_guid-str"></a>

Guid to include in request when voiding an Auth Only request.

##### void_reason: `str`<a id="void_reason-str"></a>

Indicates the reason the transaction was voided.  Allowed values:  1. POST_AUTH_USER_DECLINE 2. DEVICE_TIMEOUT 3. DEVICE_UNAVAILABLE 4. PARTIAL_REVERSAL 5. TORN_TRANSACTIONS 6. POST_AUTH_CHIP_DECLINE

##### amount: `Union[int, float]`<a id="amount-unionint-float"></a>

Amount to be voided.  Note: Amount is be used once only for credit card Sales and should not exceed corresponding Sale’s Amount.

##### sequence_number: `str`<a id="sequence_number-str"></a>

Transaction sequence number within client environment. Provide a unique SequenceNumber for each new request. If the same value is sent within 30 minutes it will be considered a duplicate request. Note: value is not searchable or reportable in ConnexPay portal.  Alphanumeric.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`VoidCreateVoidRequest`](./connex_pay_python_sdk/type/void_create_void_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`VoidCreateVoidResponse`](./connex_pay_python_sdk/pydantic/void_create_void_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/void` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `connexpay.void.search_voids`<a id="connexpayvoidsearch_voids"></a>

This endpoint searches sales voids.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
search_voids_response = connexpay.void.search_voids(
    exportable="Mandatory",
    page_number=1,
    page_size="Optional",
    merchant_guid="Mandatory",
    void_reason="Optional",
    status="Optional",
    time_stamp_from="Optional",
    time_stamp_to="Optional",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### exportable: `str`<a id="exportable-str"></a>

True or False. It means if you want results exportable to CSV.

##### page_number: `int`<a id="page_number-int"></a>

Int. Number of page of the results. Default is 1 (Page size default is 500).

##### page_size: `str`<a id="page_size-str"></a>

Int. Size of each page of the results. Default is 500.

##### merchant_guid: `str`<a id="merchant_guid-str"></a>

Merchant’s Guid.

##### void_reason: `str`<a id="void_reason-str"></a>

Indicates the reason the transaction was voided.  Allowed values:  1. POST_AUTH_USER_DECLINE 2. DEVICE_TIMEOUT 3. DEVICE_UNAVAILABLE 4. PARTIAL_REVERSAL 5. TORN_TRANSACTIONS 6. POST_AUTH_CHIP_DECLINE

##### status: `str`<a id="status-str"></a>

Void’s status.  Allowed values:  1. Transaction - Approved 2. Transaction - Declined 3. Transaction - Created - Local 4. Transaction - Created - Error: Processor not reached 5. Transaction - Processor Error 6. Transaction - Approved - Warning

##### time_stamp_from: `date`<a id="time_stamp_from-date"></a>

Void’s TimeStamp.

##### time_stamp_to: `date`<a id="time_stamp_to-date"></a>

Void’s TimeStamp.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`VoidSearchVoidsRequest`](./connex_pay_python_sdk/type/void_search_voids_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`VoidSearchVoidsResponse`](./connex_pay_python_sdk/pydantic/void_search_voids_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/Search/Voids/{exportable}/{pageNumber}/{pageSize}` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---


## Author<a id="author"></a>
This Python package is automatically generated by [Konfig](https://konfigthis.com)
