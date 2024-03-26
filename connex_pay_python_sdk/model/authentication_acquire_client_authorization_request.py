# coding: utf-8

"""
    ConnexPay Reporting API

    REST API for retrieving reporting data. Currently Daily Accounting data only.

    The version of the OpenAPI document: v1
    Created by: https://docs.connexpay.com
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from connex_pay_python_sdk import schemas  # noqa: F401


class AuthenticationAcquireClientAuthorizationRequest(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "DeviceGuid",
            "Amount",
            "RiskData",
        }
        
        class properties:
            DeviceGuid = schemas.StrSchema
            Amount = schemas.Float32Schema
        
            @staticmethod
            def RiskData() -> typing.Type['AuthenticationAcquireClientAuthorizationRequestRiskData']:
                return AuthenticationAcquireClientAuthorizationRequestRiskData
            SequenceNumber = schemas.StrSchema
            OrderNumber = schemas.StrSchema
            SendReceipt = schemas.BoolSchema
            StatementDescription = schemas.StrSchema
            CustomerID = schemas.StrSchema
        
            @staticmethod
            def Card() -> typing.Type['AuthenticationAcquireClientAuthorizationRequestCard']:
                return AuthenticationAcquireClientAuthorizationRequestCard
        
            @staticmethod
            def BankAccount() -> typing.Type['AuthenticationAcquireClientAuthorizationRequestBankAccount']:
                return AuthenticationAcquireClientAuthorizationRequestBankAccount
        
            @staticmethod
            def Customer() -> typing.Type['AuthenticationAcquireClientAuthorizationRequestCustomer']:
                return AuthenticationAcquireClientAuthorizationRequestCustomer
        
            @staticmethod
            def EnhancedData() -> typing.Type['AuthenticationAcquireClientAuthorizationRequestEnhancedData']:
                return AuthenticationAcquireClientAuthorizationRequestEnhancedData
            AssociationID = schemas.StrSchema
        
            @staticmethod
            def BrowserData() -> typing.Type['AuthenticationAcquireClientAuthorizationRequestBrowserData']:
                return AuthenticationAcquireClientAuthorizationRequestBrowserData
            __annotations__ = {
                "DeviceGuid": DeviceGuid,
                "Amount": Amount,
                "RiskData": RiskData,
                "SequenceNumber": SequenceNumber,
                "OrderNumber": OrderNumber,
                "SendReceipt": SendReceipt,
                "StatementDescription": StatementDescription,
                "CustomerID": CustomerID,
                "Card": Card,
                "BankAccount": BankAccount,
                "Customer": Customer,
                "EnhancedData": EnhancedData,
                "AssociationID": AssociationID,
                "BrowserData": BrowserData,
            }
    
    DeviceGuid: MetaOapg.properties.DeviceGuid
    Amount: MetaOapg.properties.Amount
    RiskData: 'AuthenticationAcquireClientAuthorizationRequestRiskData'
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["DeviceGuid"]) -> MetaOapg.properties.DeviceGuid: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Amount"]) -> MetaOapg.properties.Amount: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["RiskData"]) -> 'AuthenticationAcquireClientAuthorizationRequestRiskData': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["SequenceNumber"]) -> MetaOapg.properties.SequenceNumber: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["OrderNumber"]) -> MetaOapg.properties.OrderNumber: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["SendReceipt"]) -> MetaOapg.properties.SendReceipt: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["StatementDescription"]) -> MetaOapg.properties.StatementDescription: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["CustomerID"]) -> MetaOapg.properties.CustomerID: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Card"]) -> 'AuthenticationAcquireClientAuthorizationRequestCard': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["BankAccount"]) -> 'AuthenticationAcquireClientAuthorizationRequestBankAccount': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Customer"]) -> 'AuthenticationAcquireClientAuthorizationRequestCustomer': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["EnhancedData"]) -> 'AuthenticationAcquireClientAuthorizationRequestEnhancedData': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["AssociationID"]) -> MetaOapg.properties.AssociationID: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["BrowserData"]) -> 'AuthenticationAcquireClientAuthorizationRequestBrowserData': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["DeviceGuid", "Amount", "RiskData", "SequenceNumber", "OrderNumber", "SendReceipt", "StatementDescription", "CustomerID", "Card", "BankAccount", "Customer", "EnhancedData", "AssociationID", "BrowserData", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["DeviceGuid"]) -> MetaOapg.properties.DeviceGuid: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Amount"]) -> MetaOapg.properties.Amount: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["RiskData"]) -> 'AuthenticationAcquireClientAuthorizationRequestRiskData': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["SequenceNumber"]) -> typing.Union[MetaOapg.properties.SequenceNumber, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["OrderNumber"]) -> typing.Union[MetaOapg.properties.OrderNumber, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["SendReceipt"]) -> typing.Union[MetaOapg.properties.SendReceipt, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["StatementDescription"]) -> typing.Union[MetaOapg.properties.StatementDescription, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["CustomerID"]) -> typing.Union[MetaOapg.properties.CustomerID, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Card"]) -> typing.Union['AuthenticationAcquireClientAuthorizationRequestCard', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["BankAccount"]) -> typing.Union['AuthenticationAcquireClientAuthorizationRequestBankAccount', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Customer"]) -> typing.Union['AuthenticationAcquireClientAuthorizationRequestCustomer', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["EnhancedData"]) -> typing.Union['AuthenticationAcquireClientAuthorizationRequestEnhancedData', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["AssociationID"]) -> typing.Union[MetaOapg.properties.AssociationID, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["BrowserData"]) -> typing.Union['AuthenticationAcquireClientAuthorizationRequestBrowserData', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["DeviceGuid", "Amount", "RiskData", "SequenceNumber", "OrderNumber", "SendReceipt", "StatementDescription", "CustomerID", "Card", "BankAccount", "Customer", "EnhancedData", "AssociationID", "BrowserData", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        DeviceGuid: typing.Union[MetaOapg.properties.DeviceGuid, str, ],
        Amount: typing.Union[MetaOapg.properties.Amount, decimal.Decimal, int, float, ],
        RiskData: 'AuthenticationAcquireClientAuthorizationRequestRiskData',
        SequenceNumber: typing.Union[MetaOapg.properties.SequenceNumber, str, schemas.Unset] = schemas.unset,
        OrderNumber: typing.Union[MetaOapg.properties.OrderNumber, str, schemas.Unset] = schemas.unset,
        SendReceipt: typing.Union[MetaOapg.properties.SendReceipt, bool, schemas.Unset] = schemas.unset,
        StatementDescription: typing.Union[MetaOapg.properties.StatementDescription, str, schemas.Unset] = schemas.unset,
        CustomerID: typing.Union[MetaOapg.properties.CustomerID, str, schemas.Unset] = schemas.unset,
        Card: typing.Union['AuthenticationAcquireClientAuthorizationRequestCard', schemas.Unset] = schemas.unset,
        BankAccount: typing.Union['AuthenticationAcquireClientAuthorizationRequestBankAccount', schemas.Unset] = schemas.unset,
        Customer: typing.Union['AuthenticationAcquireClientAuthorizationRequestCustomer', schemas.Unset] = schemas.unset,
        EnhancedData: typing.Union['AuthenticationAcquireClientAuthorizationRequestEnhancedData', schemas.Unset] = schemas.unset,
        AssociationID: typing.Union[MetaOapg.properties.AssociationID, str, schemas.Unset] = schemas.unset,
        BrowserData: typing.Union['AuthenticationAcquireClientAuthorizationRequestBrowserData', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'AuthenticationAcquireClientAuthorizationRequest':
        return super().__new__(
            cls,
            *args,
            DeviceGuid=DeviceGuid,
            Amount=Amount,
            RiskData=RiskData,
            SequenceNumber=SequenceNumber,
            OrderNumber=OrderNumber,
            SendReceipt=SendReceipt,
            StatementDescription=StatementDescription,
            CustomerID=CustomerID,
            Card=Card,
            BankAccount=BankAccount,
            Customer=Customer,
            EnhancedData=EnhancedData,
            AssociationID=AssociationID,
            BrowserData=BrowserData,
            _configuration=_configuration,
            **kwargs,
        )

from connex_pay_python_sdk.model.authentication_acquire_client_authorization_request_bank_account import AuthenticationAcquireClientAuthorizationRequestBankAccount
from connex_pay_python_sdk.model.authentication_acquire_client_authorization_request_browser_data import AuthenticationAcquireClientAuthorizationRequestBrowserData
from connex_pay_python_sdk.model.authentication_acquire_client_authorization_request_card import AuthenticationAcquireClientAuthorizationRequestCard
from connex_pay_python_sdk.model.authentication_acquire_client_authorization_request_customer import AuthenticationAcquireClientAuthorizationRequestCustomer
from connex_pay_python_sdk.model.authentication_acquire_client_authorization_request_enhanced_data import AuthenticationAcquireClientAuthorizationRequestEnhancedData
from connex_pay_python_sdk.model.authentication_acquire_client_authorization_request_risk_data import AuthenticationAcquireClientAuthorizationRequestRiskData
