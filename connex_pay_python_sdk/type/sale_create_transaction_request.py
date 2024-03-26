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

from connex_pay_python_sdk.type.sale_create_transaction_request_bank_account import SaleCreateTransactionRequestBankAccount
from connex_pay_python_sdk.type.sale_create_transaction_request_browser_data import SaleCreateTransactionRequestBrowserData
from connex_pay_python_sdk.type.sale_create_transaction_request_card import SaleCreateTransactionRequestCard
from connex_pay_python_sdk.type.sale_create_transaction_request_connex_pay_transaction import SaleCreateTransactionRequestConnexPayTransaction
from connex_pay_python_sdk.type.sale_create_transaction_request_custom_parameters import SaleCreateTransactionRequestCustomParameters
from connex_pay_python_sdk.type.sale_create_transaction_request_customer import SaleCreateTransactionRequestCustomer
from connex_pay_python_sdk.type.sale_create_transaction_request_enhanced_data import SaleCreateTransactionRequestEnhancedData
from connex_pay_python_sdk.type.sale_create_transaction_request_label_ids import SaleCreateTransactionRequestLabelIDs
from connex_pay_python_sdk.type.sale_create_transaction_request_risk_data import SaleCreateTransactionRequestRiskData

class RequiredSaleCreateTransactionRequest(TypedDict):
    # Device's Guid provided by ConnexPay
    DeviceGuid: str

    # Amount of the transaction that will be processed. Note: this value is submitted multiple times (in different formats) within the integration to support different purposes i.e. risk analysis, merchant processing, etc.  The minimum amount is: $0.50.
    Amount: typing.Union[int, float]

    ConnexPayTransaction: SaleCreateTransactionRequestConnexPayTransaction

    RiskData: SaleCreateTransactionRequestRiskData

class OptionalSaleCreateTransactionRequest(TypedDict, total=False):
    # Allowed values:  \"credit\" (default if TenderType not provided) and \"ach\"
    TenderType: str

    # Transaction sequence number within client environment. Provide a unique SequenceNumber for each new request. If a sale request with the same parameter data and the same sequence number is sent within 30 minutes it will be considered a duplicate request and the sale will not process. Note: value is not searchable or reportable in Bridge.  Alphanumeric.
    SequenceNumber: str

    # This is the most common number you'll see throughout the ConnexPay Portal.  Transaction ID within client environment associated with the order. The value is searchable and reportable in the ConnexPay portal. This value may be sent in multiple instances of the integration for multiple purposes. Customers in the travel space often send the Record Locator/PNR in this field.  The maximum length is 50 alpha-numeric characters and allows dashes ( - ).
    OrderNumber: str

    # Value determines whether or not a customer shall be emailed a receipt from the ConnexPay platform if the email address is provided in the API customer block. The default value is TRUE. Set to FALSE so that an email receipt is not sent to the customer. Set to TRUE or leave empty if you want e-mail to be sent. If TRUE, customer's email must be included in the \"Card.Customer.email\" parameter.
    SendReceipt: bool

    # Indicator that determines if client would like to evaluate the transactions as risk only rather than process as merchant of record and create a virtual card. The allowed values:  1. Set to TRUE will only run risk validations. If TenderType is not set to Credit, setting TRUE will throw a validation error.  2. Set to FALSE will run risk validations and an authorization on the card. For this option a Processing Merchant account is required, contact ConnexPay support if any questions.  3. Set to NULL and your Merchant Level settings would apply.
    RiskProcessingOnly: bool

    # US Clients only: The statement description allows a client to customize the Merchant name that appears on the cardholder statement such that the cardholder recognizes the transaction on their statement. For US Merchants: ConnexPay recommends sending a recognizable DBA along with the PNR i.e. ABC Travel ABC123.  The maximum length is 25 alpha-numeric characters.  For EU Merchants: The maximum length of the description is 13 alphanumeric characters and the DBA Name and City will automatically be coded to appear as part of the statement description. Note: functionality not applicable for American Express program.
    StatementDescription: str

    # Transaction ID within client environment associated with the customer. This value acts as a secondary identifier in conjunction with OrderNumber. The value is searchable and reportable in the ConnexPay portal. This value may be sent in multiple times within the integration for multiple purposes.  The maximum length is 100 characters and is alpha-numeric.
    CustomerID: str

    # Set a future date on which to run this sale, at least one day from creation date and within 600 days. If this parameter is supplied a record for this sale is created, supplied consumer card information is internally tokenized, but fraud check and authorization do not occur until ConnexPay processes it on the supplied ActivationDate. Alternatively, a client can force activation via the Activate API (see below). If this date is not supplied a sale is authorized and the consumer's credit card is charged immediately.
    ActivationDate: date

    # Mandatory if TenderType is ACH. Customer's IP Address is a required parameter for all ACH Sales transactions to adhere to NACHA regulations.
    RequestIp: str

    Card: SaleCreateTransactionRequestCard

    BankAccount: SaleCreateTransactionRequestBankAccount

    Customer: SaleCreateTransactionRequestCustomer

    EnhancedData: SaleCreateTransactionRequestEnhancedData

    # Utilize the Association ID field to tie a virtual card to a sale or sales. For example, if you have several sales and one virtual card payment to a supplier, you can add association ID to the sales and the virtual card for downstream reporting.
    AssociationId: str

    CustomParameters: SaleCreateTransactionRequestCustomParameters

    LabelIDs: SaleCreateTransactionRequestLabelIDs

    BrowserData: SaleCreateTransactionRequestBrowserData

class SaleCreateTransactionRequest(RequiredSaleCreateTransactionRequest, OptionalSaleCreateTransactionRequest):
    pass
