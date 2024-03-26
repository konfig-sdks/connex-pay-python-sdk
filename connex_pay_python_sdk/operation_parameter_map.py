operation_parameter_map = {
    '/api/v1/IssueACH/IssueLite-POST': {
        'parameters': [
            {
                'name': 'MerchantGuid'
            },
            {
                'name': 'Amount'
            },
            {
                'name': 'PayeeName'
            },
            {
                'name': 'AccountHolder'
            },
            {
                'name': 'StatementCompanyName'
            },
            {
                'name': 'Description'
            },
            {
                'name': 'OrderNumber'
            },
            {
                'name': 'SequenceNumber'
            },
            {
                'name': 'AssociationId'
            },
        ]
    },
    '/api/v1/Accounting/DailyDetail-GET': {
        'parameters': [
            {
                'name': 'merchantGuid'
            },
            {
                'name': 'releasedDate'
            },
            {
                'name': 'pageNumber'
            },
            {
                'name': 'pageSize'
            },
        ]
    },
    '/api/v1/Accounting/DailySummary-GET': {
        'parameters': [
            {
                'name': 'merchantGuid'
            },
            {
                'name': 'releasedDate'
            },
        ]
    },
    '/api/v1/Addendum/ACH-POST': {
        'parameters': [
            {
                'name': 'ItemGuid'
            },
            {
                'name': 'Value'
            },
            {
                'name': 'Category'
            },
            {
                'name': 'IdExternal'
            },
            {
                'name': 'Note'
            },
            {
                'name': 'Sequence'
            },
        ]
    },
    '/api/v1/Addendum/VirtualCard-POST': {
        'parameters': [
            {
                'name': 'ItemGuid'
            },
            {
                'name': 'Value'
            },
            {
                'name': 'Category'
            },
            {
                'name': 'IdExternal'
            },
            {
                'name': 'Note'
            },
            {
                'name': 'Sequence'
            },
        ]
    },
    '/v1/Addendum/Remove/<guid>-POST': {
        'parameters': [
            {
                'name': 'Guid'
            },
        ]
    },
    '/api/v1/authonlys-POST': {
        'parameters': [
            {
                'name': 'DeviceGuid'
            },
            {
                'name': 'Amount'
            },
            {
                'name': 'RiskData'
            },
            {
                'name': 'SequenceNumber'
            },
            {
                'name': 'OrderNumber'
            },
            {
                'name': 'SendReceipt'
            },
            {
                'name': 'StatementDescription'
            },
            {
                'name': 'CustomerID'
            },
            {
                'name': 'Card'
            },
            {
                'name': 'BankAccount'
            },
            {
                'name': 'Customer'
            },
            {
                'name': 'EnhancedData'
            },
            {
                'name': 'AssociationID'
            },
            {
                'name': 'BrowserData'
            },
        ]
    },
    '/api/v1/3ds-POST': {
        'parameters': [
            {
                'name': 'Card'
            },
            {
                'name': 'DeviceGuid'
            },
            {
                'name': 'BrowserData'
            },
            {
                'name': 'Amount'
            },
        ]
    },
    '/api/v1/cancel-POST': {
        'parameters': [
            {
                'name': 'DeviceGuid'
            },
            {
                'name': 'SaleGuid'
            },
            {
                'name': 'SequenceNumber'
            },
            {
                'name': 'VoidReason'
            },
        ]
    },
    '/api/v1/IssueCard/ActivateDelayedCard/{{CardGuid}}-PUT': {
        'parameters': [
        ]
    },
    '/api/v1/IssueCard/Cancel/{{CardGuid}}-PUT': {
        'parameters': [
        ]
    },
    '/api/v1/IssueCard/LodgedCard-POST': {
        'parameters': [
            {
                'name': 'MerchantGuid'
            },
            {
                'name': 'FirstName'
            },
            {
                'name': 'LastName'
            },
            {
                'name': 'AmountLimit'
            },
            {
                'name': 'LimitWindow'
            },
            {
                'name': 'Phone'
            },
            {
                'name': 'Address1'
            },
            {
                'name': 'Address2'
            },
            {
                'name': 'City'
            },
            {
                'name': 'State'
            },
            {
                'name': 'ZipCode'
            },
            {
                'name': 'Country'
            },
            {
                'name': 'UsageLimit'
            },
            {
                'name': 'ExpirationDate'
            },
            {
                'name': 'TerminateDate'
            },
            {
                'name': 'PurchaseType'
            },
            {
                'name': 'SequenceNumber'
            },
            {
                'name': 'OrderNumber'
            },
            {
                'name': 'SupplierId'
            },
            {
                'name': 'NonDomesticSupplier'
            },
            {
                'name': 'Transmission'
            },
            {
                'name': 'ReturnCardData'
            },
            {
                'name': 'CustomerID'
            },
            {
                'name': 'AssociationId'
            },
            {
                'name': 'LabelIDs'
            },
            {
                'name': 'CustomParameters'
            },
        ]
    },
    '/api/v1/Cards/{CardGuid}/{ShowFullPan}-GET': {
        'parameters': [
            {
                'name': 'CardGuid'
            },
            {
                'name': 'ShowFullPan'
            },
        ]
    },
    '/api/v1/IssueCard/SendPaymentInfo/{cardGuid}-PUT': {
        'parameters': [
            {
                'name': 'TransmissionMethods'
            },
            {
                'name': 'CardGuid'
            },
            {
                'name': 'EmailRecipient'
            },
            {
                'name': 'MerchantPhoneNumber'
            },
            {
                'name': 'EmailFrom'
            },
            {
                'name': 'RecipientName'
            },
            {
                'name': 'Subject'
            },
            {
                'name': 'Message'
            },
            {
                'name': 'DaysToExpire'
            },
            {
                'name': 'FaxFrom'
            },
            {
                'name': 'FaxRecipient'
            },
        ]
    },
    '/api/v1/Search/IssuedCards-POST': {
        'parameters': [
            {
                'name': 'MerchantGuid'
            },
            {
                'name': 'PageNumber'
            },
            {
                'name': 'PageSize'
            },
            {
                'name': 'SaleGuid'
            },
            {
                'name': 'IncomingTransactionCode'
            },
            {
                'name': 'OrderNumber'
            },
            {
                'name': 'CustomerID'
            },
            {
                'name': 'TimeStampFrom'
            },
            {
                'name': 'TimeStampTo'
            },
            {
                'name': 'IssuedAmountFrom'
            },
            {
                'name': 'IssuedAmountTo'
            },
            {
                'name': 'OutgoingTransactionCode'
            },
            {
                'name': 'SettledAmountFrom'
            },
            {
                'name': 'SettledAmountTo'
            },
            {
                'name': 'ReturnedAmountFrom'
            },
            {
                'name': 'ReturnedAmountTo'
            },
        ]
    },
    '/api/v1/TerminateCard/<guid>-POST': {
        'parameters': [
            {
                'name': 'guid'
            },
        ]
    },
    '/api/v1/IssueCard/{cardGuid}-PUT': {
        'parameters': [
            {
                'name': 'CardGuid'
            },
            {
                'name': 'PurchaseType'
            },
            {
                'name': 'MIDWhitelist'
            },
            {
                'name': 'MIDBlacklist'
            },
            {
                'name': 'UsageLimit'
            },
            {
                'name': 'AssociationId'
            },
            {
                'name': 'TerminateDate'
            },
            {
                'name': 'AmountLimit'
            },
        ]
    },
    '/api/v1/IssueCard/UpdateDelayedCard/{{CardGuid}}-PUT': {
        'parameters': [
            {
                'name': 'MerchantGuid'
            },
            {
                'name': 'CardGuid'
            },
            {
                'name': 'ActivationDate'
            },
            {
                'name': 'AmountLimit'
            },
            {
                'name': 'TerminateDate'
            },
        ]
    },
    '/api/v1/IssueCard/LodgedCard/{CardGuid}-PUT': {
        'parameters': [
            {
                'name': 'CardGuid'
            },
            {
                'name': 'UsageLimit'
            },
            {
                'name': 'AmountLimit'
            },
            {
                'name': 'LimitWindow'
            },
            {
                'name': 'PurchaseType'
            },
            {
                'name': 'Activated'
            },
            {
                'name': 'AssociationId'
            },
            {
                'name': 'TerminateDate'
            },
        ]
    },
    '/api/v1/IssueCard-POST': {
        'parameters': [
            {
                'name': 'MerchantGuid'
            },
            {
                'name': 'FirstName'
            },
            {
                'name': 'LastName'
            },
            {
                'name': 'AmountLimit'
            },
            {
                'name': 'PurchaseType'
            },
            {
                'name': 'Phone'
            },
            {
                'name': 'Address1'
            },
            {
                'name': 'Address2'
            },
            {
                'name': 'City'
            },
            {
                'name': 'State'
            },
            {
                'name': 'ZipCode'
            },
            {
                'name': 'Country'
            },
            {
                'name': 'UsageLimit'
            },
            {
                'name': 'ExpirationDate'
            },
            {
                'name': 'TerminateDate'
            },
            {
                'name': 'MIDWhitelist'
            },
            {
                'name': 'MIDBlacklist'
            },
            {
                'name': 'SequenceNumber'
            },
            {
                'name': 'OrderNumber'
            },
            {
                'name': 'IncomingTransactionCode'
            },
            {
                'name': 'SupplierId'
            },
            {
                'name': 'NonDomesticSupplier'
            },
            {
                'name': 'Transmission'
            },
            {
                'name': 'ReturnCardData'
            },
            {
                'name': 'CustomerID'
            },
            {
                'name': 'AssociationId'
            },
            {
                'name': 'CustomParameters'
            },
            {
                'name': 'LabelIDs'
            },
        ]
    },
    '/api/v1/IssueCard/IssueLite-POST': {
        'parameters': [
            {
                'name': 'MerchantGuid'
            },
            {
                'name': 'FirstName'
            },
            {
                'name': 'LastName'
            },
            {
                'name': 'AmountLimit'
            },
            {
                'name': 'PurchaseType'
            },
            {
                'name': 'Phone'
            },
            {
                'name': 'Address1'
            },
            {
                'name': 'Address2'
            },
            {
                'name': 'City'
            },
            {
                'name': 'State'
            },
            {
                'name': 'ZipCode'
            },
            {
                'name': 'Country'
            },
            {
                'name': 'UsageLimit'
            },
            {
                'name': 'ExpirationDate'
            },
            {
                'name': 'TerminateDate'
            },
            {
                'name': 'MIDWhitelist'
            },
            {
                'name': 'MIDBlacklist'
            },
            {
                'name': 'SequenceNumber'
            },
            {
                'name': 'SupplierId'
            },
            {
                'name': 'NonDomesticSupplier'
            },
            {
                'name': 'OrderNumber'
            },
            {
                'name': 'CustomerID'
            },
            {
                'name': 'Transmission'
            },
            {
                'name': 'ReturnCardData'
            },
            {
                'name': 'CustomParameters'
            },
            {
                'name': 'ActivationDate'
            },
            {
                'name': 'AssociationId'
            },
            {
                'name': 'LabelIDs'
            },
        ]
    },
    '/api/v1/MerchantSelfServiceFunding-POST': {
        'parameters': [
            {
                'name': 'merchantGUID'
            },
            {
                'name': 'amount'
            },
            {
                'name': 'isFundCashBalance'
            },
        ]
    },
    '/api/v1/MerchantFlexFunding/Funds/Transfer-POST': {
        'parameters': [
            {
                'name': 'TransferredFrom'
            },
            {
                'name': 'TransferredTo'
            },
            {
                'name': 'Amount'
            },
        ]
    },
    '/api/v1/Search/AvailableFunds/{merchantGuid}-GET': {
        'parameters': [
            {
                'name': 'MerchantGuid'
            },
        ]
    },
    '/api/v1/Merchants/{merchantGuid}/Payees-POST': {
        'parameters': [
            {
                'name': 'isBusiness'
            },
            {
                'name': 'payeeId'
            },
            {
                'name': 'preferredPayoutMethod'
            },
            {
                'name': 'merchantGuid'
            },
            {
                'name': 'idMerchant'
            },
            {
                'name': 'firstName'
            },
            {
                'name': 'lastName'
            },
            {
                'name': 'dbaName'
            },
            {
                'name': 'taxId'
            },
            {
                'name': 'customerId'
            },
            {
                'name': 'email'
            },
            {
                'name': 'address1'
            },
            {
                'name': 'address2'
            },
            {
                'name': 'city'
            },
            {
                'name': 'state'
            },
            {
                'name': 'zip'
            },
            {
                'name': 'country'
            },
            {
                'name': 'preferredCardBrand'
            },
            {
                'name': 'preferredCardClass'
            },
            {
                'name': 'purchaseType'
            },
            {
                'name': 'guid'
            },
            {
                'name': 'timestamp'
            },
        ]
    },
    '/api/v1/Merchants/{merchantGuid}/Payees/{payeeGuid}-DELETE': {
        'parameters': [
            {
                'name': 'merchantGuid'
            },
            {
                'name': 'payeeGuid'
            },
        ]
    },
    '/api/v1/Merchants/{merchantGuid}/Payees/{payeeGuid}-GET': {
        'parameters': [
            {
                'name': 'merchantGuid'
            },
            {
                'name': 'payeeGuid'
            },
        ]
    },
    '/api/v1/Merchants/{merchantGuid}/Payees/Search/{page}/{pagesize}-POST': {
        'parameters': [
            {
                'name': 'merchantGuid'
            },
            {
                'name': 'page'
            },
            {
                'name': 'pagesize'
            },
            {
                'name': 'searchTerm'
            },
        ]
    },
    '/api/v1/Merchants/{merchantGuid}/Payees/{payeeGuid}-PUT': {
        'parameters': [
            {
                'name': 'isBusiness'
            },
            {
                'name': 'payeeId'
            },
            {
                'name': 'preferredPayoutMethod'
            },
            {
                'name': 'merchantGuid'
            },
            {
                'name': 'payeeGuid'
            },
            {
                'name': 'idMerchant'
            },
            {
                'name': 'firstName'
            },
            {
                'name': 'lastName'
            },
            {
                'name': 'dbaName'
            },
            {
                'name': 'taxId'
            },
            {
                'name': 'customerId'
            },
            {
                'name': 'email'
            },
            {
                'name': 'address1'
            },
            {
                'name': 'address2'
            },
            {
                'name': 'city'
            },
            {
                'name': 'state'
            },
            {
                'name': 'zip'
            },
            {
                'name': 'country'
            },
            {
                'name': 'preferredCardBrand'
            },
            {
                'name': 'preferredCardClass'
            },
            {
                'name': 'purchaseType'
            },
            {
                'name': 'guid'
            },
            {
                'name': 'timestamp'
            },
        ]
    },
    '/api/v1/PushToCard/Payouts/{payoutGuid}/Cancel-POST': {
        'parameters': [
            {
                'name': 'merchantGuid'
            },
            {
                'name': 'payments'
            },
            {
                'name': 'payoutGuid'
            },
        ]
    },
    '/api/v1/PushToCard/Payees-POST': {
        'parameters': [
            {
                'name': 'merchantGuid'
            },
            {
                'name': 'firstName'
            },
            {
                'name': 'lastName'
            },
            {
                'name': 'email'
            },
            {
                'name': 'phone'
            },
            {
                'name': 'payeeGuid'
            },
            {
                'name': 'address1'
            },
            {
                'name': 'address2'
            },
            {
                'name': 'city'
            },
            {
                'name': 'state'
            },
            {
                'name': 'zipCode'
            },
            {
                'name': 'status'
            },
            {
                'name': 'cardId'
            },
        ]
    },
    '/api/v1/PushToCard/Payouts-POST': {
        'parameters': [
            {
                'name': 'merchantGuid'
            },
            {
                'name': 'memo'
            },
            {
                'name': 'payments'
            },
            {
                'name': 'payoutGuid'
            },
            {
                'name': 'payoutReferenceToken'
            },
            {
                'name': 'status'
            },
            {
                'name': 'orderNumber'
            },
            {
                'name': 'customerId'
            },
            {
                'name': 'associationId'
            },
            {
                'name': 'labelIds'
            },
        ]
    },
    '/api/v1/PushToCard/AuthenticatePaymentWidget-GET': {
        'parameters': [
            {
                'name': 'payeeGuid'
            },
            {
                'name': 'payeeEmailAddress'
            },
        ]
    },
    '/api/v1/PushToCard/Payees-GET': {
        'parameters': [
            {
                'name': 'payeeGuid'
            },
            {
                'name': 'payeeEmailAddress'
            },
        ]
    },
    '/api/v1/PushToCard/Payouts/{payoutGuid}-GET': {
        'parameters': [
            {
                'name': 'payoutGuid'
            },
        ]
    },
    '/api/v1/PushToCard/Payees/{payeeGuid}/{status}-PUT': {
        'parameters': [
            {
                'name': 'payeeGuid'
            },
            {
                'name': 'status'
            },
        ]
    },
    '/api/v1/PushToCard/Payments/{ridGuid}/{cardId}-PATCH': {
        'parameters': [
            {
                'name': 'ridGuid'
            },
            {
                'name': 'cardId'
            },
        ]
    },
    '/api/v1/PushToCard/Payees/{payeeGuid}-PATCH': {
        'parameters': [
            {
                'name': 'payeeGuid'
            },
            {
                'name': 'firstName'
            },
            {
                'name': 'lastName'
            },
            {
                'name': 'email'
            },
            {
                'name': 'address1'
            },
            {
                'name': 'address2'
            },
            {
                'name': 'city'
            },
            {
                'name': 'state'
            },
            {
                'name': 'zipCode'
            },
            {
                'name': 'phone'
            },
            {
                'name': 'status'
            },
        ]
    },
    '/api/v1/PurchaseEventHistory/Resend-POST': {
        'parameters': [
            {
                'name': 'SourceGuid'
            },
            {
                'name': 'MerchantGuid'
            },
            {
                'name': 'EventGuid'
            },
            {
                'name': 'FromDateTime'
            },
            {
                'name': 'ToDateTime'
            },
        ]
    },
    '/api/v1/returns-POST': {
        'parameters': [
            {
                'name': 'DeviceGuid'
            },
            {
                'name': 'Amount'
            },
            {
                'name': 'SaleGuid'
            },
            {
                'name': 'SaleReferenceNumber'
            },
            {
                'name': 'SequenceNumber'
            },
            {
                'name': 'ReturnRetryCard'
            },
        ]
    },
    '/api/v1/Search/Returns/{exportable}/{pageNumber}/{pageSize}-POST': {
        'parameters': [
            {
                'name': 'Exportable'
            },
            {
                'name': 'PageNumber'
            },
            {
                'name': 'PageSize'
            },
            {
                'name': 'MerchantGuid'
            },
            {
                'name': 'AmountFrom'
            },
            {
                'name': 'AmountTo'
            },
            {
                'name': 'CardHolderName'
            },
            {
                'name': 'Status'
            },
            {
                'name': 'TimeStampFrom'
            },
            {
                'name': 'TimeStampTo'
            },
        ]
    },
    '/api/v1/sales/Activate/{SaleGuid}-PUT': {
        'parameters': [
            {
                'name': 'SaleGuid'
            },
        ]
    },
    '/api/v1/sales-POST': {
        'parameters': [
            {
                'name': 'DeviceGuid'
            },
            {
                'name': 'Amount'
            },
            {
                'name': 'ConnexPayTransaction'
            },
            {
                'name': 'RiskData'
            },
            {
                'name': 'TenderType'
            },
            {
                'name': 'SequenceNumber'
            },
            {
                'name': 'OrderNumber'
            },
            {
                'name': 'SendReceipt'
            },
            {
                'name': 'RiskProcessingOnly'
            },
            {
                'name': 'StatementDescription'
            },
            {
                'name': 'CustomerID'
            },
            {
                'name': 'ActivationDate'
            },
            {
                'name': 'RequestIp'
            },
            {
                'name': 'Card'
            },
            {
                'name': 'BankAccount'
            },
            {
                'name': 'Customer'
            },
            {
                'name': 'EnhancedData'
            },
            {
                'name': 'AssociationId'
            },
            {
                'name': 'CustomParameters'
            },
            {
                'name': 'LabelIDs'
            },
            {
                'name': 'BrowserData'
            },
        ]
    },
    '/api/chargeback/GetByUser-GET': {
        'parameters': [
            {
                'name': '/GetByUser?startDate=2016-12-01'
            },
            {
                'name': '/GetByUser?startDate=2016-12-01&endDate=2016-12-01'
            },
            {
                'name': '/GetByResolvedDate?startDate=2019-09-20&endDate=2019-10-21'
            },
        ]
    },
    '/api/v1/Search/Sales/{exportable}/{pageNumber}/{pageSize}-POST': {
        'parameters': [
            {
                'name': 'Exportable'
            },
            {
                'name': 'PageNumber'
            },
            {
                'name': 'PageSize'
            },
            {
                'name': 'MerchantGuid'
            },
            {
                'name': 'AmountFrom'
            },
            {
                'name': 'AmountTo'
            },
            {
                'name': 'CardHolderName'
            },
            {
                'name': 'CardLastFour'
            },
            {
                'name': 'CardType'
            },
            {
                'name': 'InvoiceNumber'
            },
            {
                'name': 'OrderNumber'
            },
            {
                'name': 'OrderDateFrom'
            },
            {
                'name': 'OrderDateTo'
            },
            {
                'name': 'TimeStampFrom'
            },
            {
                'name': 'TimeStampTo'
            },
            {
                'name': 'Status'
            },
            {
                'name': 'MerchantCustomerId'
            },
            {
                'name': 'Activated'
            },
            {
                'name': 'ActivationDateFrom'
            },
            {
                'name': 'ActivationDateTo'
            },
        ]
    },
    '/api/v1/sales/UpdateFutureSale-POST': {
        'parameters': [
            {
                'name': 'DeviceGuid'
            },
            {
                'name': 'SaleGuid'
            },
            {
                'name': 'Amount'
            },
            {
                'name': 'ActivationDate'
            },
        ]
    },
    '/api/v1/merchantsupplier/settings-POST': {
        'parameters': [
            {
                'name': 'MerchantGuid'
            },
            {
                'name': 'SupplierName'
            },
            {
                'name': 'AccountHolder'
            },
        ]
    },
    '/api/v1/Search/Settlements-POST': {
        'parameters': [
            {
                'name': 'MerchantGuid'
            },
            {
                'name': 'PageNumber'
            },
            {
                'name': 'PageSize'
            },
            {
                'name': 'DateFrom'
            },
            {
                'name': 'DateTo'
            },
            {
                'name': 'PostedDateFrom'
            },
            {
                'name': 'PostedDateTo'
            },
            {
                'name': 'OrderNumber'
            },
            {
                'name': 'IssuedAmountFrom'
            },
            {
                'name': 'IssuedAmountTo'
            },
            {
                'name': 'IssuedCardLastFour'
            },
            {
                'name': 'PostedAmountFrom'
            },
            {
                'name': 'PostedAmountTo'
            },
            {
                'name': 'ExpirationDateFrom'
            },
            {
                'name': 'ExpirationDateTo'
            },
        ]
    },
    '/api/v1/3ds/{GUID}-GET': {
        'parameters': [
            {
                'name': 'guid'
            },
        ]
    },
    '/api/v1/authenticate-POST': {
        'parameters': [
            {
                'name': 'UserName'
            },
            {
                'name': 'Password'
            },
        ]
    },
    '/api/v1/token-POST': {
        'parameters': [
            {
                'name': 'grant_type'
            },
            {
                'name': 'username'
            },
            {
                'name': 'password'
            },
        ]
    },
    '/api/v1/HostedPaymentPageRequests-POST': {
        'parameters': [
            {
                'name': 'MerchantName'
            },
            {
                'name': 'Sale'
            },
            {
                'name': 'Description'
            },
            {
                'name': 'ResultRedirectUrl'
            },
            {
                'name': 'LogoUrl'
            },
            {
                'name': 'TenderTypeOptions'
            },
            {
                'name': 'Expiration'
            },
        ]
    },
    '/api/v1/Captures-POST': {
        'parameters': [
            {
                'name': 'DeviceGuid'
            },
            {
                'name': 'AuthOnlyGuid'
            },
            {
                'name': 'SequenceNumber'
            },
            {
                'name': 'ConnexPayTransaction'
            },
            {
                'name': 'OrderNumber'
            },
            {
                'name': 'CustomerID'
            },
            {
                'name': 'AssociationID'
            },
            {
                'name': 'CustomParameters'
            },
        ]
    },
    '/api/v1/IssueACH-POST': {
        'parameters': [
            {
                'name': 'MerchantGuid'
            },
            {
                'name': 'Amount'
            },
            {
                'name': 'PayeeName'
            },
            {
                'name': 'IncomingTransactionCode'
            },
            {
                'name': 'AccountHolder'
            },
            {
                'name': 'StatementCompanyName'
            },
            {
                'name': 'Description'
            },
        ]
    },
    '/api/v1/Cards/Transactions/{cardGuid}-GET': {
        'parameters': [
            {
                'name': 'CardGuid'
            },
        ]
    },
    '/api/v1/Search/Verify/{exportable}/{pageNumber}/{pageSize}-POST': {
        'parameters': [
            {
                'name': 'Exportable'
            },
            {
                'name': 'PageNumber'
            },
            {
                'name': 'PageSize'
            },
            {
                'name': 'MerchantGuid'
            },
            {
                'name': 'CardLastFour'
            },
            {
                'name': 'CardHolderName'
            },
            {
                'name': 'CardType'
            },
            {
                'name': 'TimeStampFrom'
            },
            {
                'name': 'TimeStampTo'
            },
            {
                'name': 'Status'
            },
        ]
    },
    '/api/v1/verify-POST': {
        'parameters': [
            {
                'name': 'DeviceGuid'
            },
            {
                'name': 'Card'
            },
            {
                'name': 'BankAccount'
            },
        ]
    },
    '/api/v1/void-POST': {
        'parameters': [
            {
                'name': 'DeviceGuid'
            },
            {
                'name': 'SaleGuid'
            },
            {
                'name': 'ReturnGuid'
            },
            {
                'name': 'SaleReferenceNumber'
            },
            {
                'name': 'AuthOnlyGuid'
            },
            {
                'name': 'VoidReason'
            },
            {
                'name': 'Amount'
            },
            {
                'name': 'SequenceNumber'
            },
        ]
    },
    '/api/v1/Search/Voids/{exportable}/{pageNumber}/{pageSize}-POST': {
        'parameters': [
            {
                'name': 'Exportable'
            },
            {
                'name': 'PageNumber'
            },
            {
                'name': 'PageSize'
            },
            {
                'name': 'MerchantGuid'
            },
            {
                'name': 'VoidReason'
            },
            {
                'name': 'Status'
            },
            {
                'name': 'TimeStampFrom'
            },
            {
                'name': 'TimeStampTo'
            },
        ]
    },
};