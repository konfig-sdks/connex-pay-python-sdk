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


class CardIssueCreateVirtualCardLiteRequest(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "MerchantGuid",
            "PurchaseType",
            "FirstName",
            "LastName",
            "AmountLimit",
        }
        
        class properties:
            MerchantGuid = schemas.StrSchema
            FirstName = schemas.StrSchema
            LastName = schemas.StrSchema
            AmountLimit = schemas.Float32Schema
            PurchaseType = schemas.StrSchema
            Phone = schemas.StrSchema
            Address1 = schemas.StrSchema
            Address2 = schemas.StrSchema
            City = schemas.StrSchema
            State = schemas.StrSchema
            ZipCode = schemas.StrSchema
            Country = schemas.StrSchema
            UsageLimit = schemas.Int64Schema
            ExpirationDate = schemas.DateSchema
            TerminateDate = schemas.DateSchema
        
            @staticmethod
            def MIDWhitelist() -> typing.Type['CardIssueCreateVirtualCardLiteRequestMidWhitelist']:
                return CardIssueCreateVirtualCardLiteRequestMidWhitelist
        
            @staticmethod
            def MIDBlacklist() -> typing.Type['CardIssueCreateVirtualCardLiteRequestMidBlacklist']:
                return CardIssueCreateVirtualCardLiteRequestMidBlacklist
            SequenceNumber = schemas.StrSchema
            SupplierId = schemas.StrSchema
            NonDomesticSupplier = schemas.BoolSchema
            OrderNumber = schemas.StrSchema
            CustomerID = schemas.StrSchema
        
            @staticmethod
            def Transmission() -> typing.Type['CardIssueCreateVirtualCardLiteRequestTransmission']:
                return CardIssueCreateVirtualCardLiteRequestTransmission
            ReturnCardData = schemas.BoolSchema
        
            @staticmethod
            def CustomParameters() -> typing.Type['CardIssueCreateVirtualCardLiteRequestCustomParameters']:
                return CardIssueCreateVirtualCardLiteRequestCustomParameters
            ActivationDate = schemas.DateSchema
            AssociationId = schemas.StrSchema
        
            @staticmethod
            def LabelIDs() -> typing.Type['CardIssueCreateVirtualCardLiteRequestLabelIDs']:
                return CardIssueCreateVirtualCardLiteRequestLabelIDs
            __annotations__ = {
                "MerchantGuid": MerchantGuid,
                "FirstName": FirstName,
                "LastName": LastName,
                "AmountLimit": AmountLimit,
                "PurchaseType": PurchaseType,
                "Phone": Phone,
                "Address1": Address1,
                "Address2": Address2,
                "City": City,
                "State": State,
                "ZipCode": ZipCode,
                "Country": Country,
                "UsageLimit": UsageLimit,
                "ExpirationDate": ExpirationDate,
                "TerminateDate": TerminateDate,
                "MIDWhitelist": MIDWhitelist,
                "MIDBlacklist": MIDBlacklist,
                "SequenceNumber": SequenceNumber,
                "SupplierId": SupplierId,
                "NonDomesticSupplier": NonDomesticSupplier,
                "OrderNumber": OrderNumber,
                "CustomerID": CustomerID,
                "Transmission": Transmission,
                "ReturnCardData": ReturnCardData,
                "CustomParameters": CustomParameters,
                "ActivationDate": ActivationDate,
                "AssociationId": AssociationId,
                "LabelIDs": LabelIDs,
            }
    
    MerchantGuid: MetaOapg.properties.MerchantGuid
    PurchaseType: MetaOapg.properties.PurchaseType
    FirstName: MetaOapg.properties.FirstName
    LastName: MetaOapg.properties.LastName
    AmountLimit: MetaOapg.properties.AmountLimit
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["MerchantGuid"]) -> MetaOapg.properties.MerchantGuid: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["FirstName"]) -> MetaOapg.properties.FirstName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["LastName"]) -> MetaOapg.properties.LastName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["AmountLimit"]) -> MetaOapg.properties.AmountLimit: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["PurchaseType"]) -> MetaOapg.properties.PurchaseType: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Phone"]) -> MetaOapg.properties.Phone: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Address1"]) -> MetaOapg.properties.Address1: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Address2"]) -> MetaOapg.properties.Address2: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["City"]) -> MetaOapg.properties.City: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["State"]) -> MetaOapg.properties.State: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ZipCode"]) -> MetaOapg.properties.ZipCode: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Country"]) -> MetaOapg.properties.Country: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["UsageLimit"]) -> MetaOapg.properties.UsageLimit: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ExpirationDate"]) -> MetaOapg.properties.ExpirationDate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["TerminateDate"]) -> MetaOapg.properties.TerminateDate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["MIDWhitelist"]) -> 'CardIssueCreateVirtualCardLiteRequestMidWhitelist': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["MIDBlacklist"]) -> 'CardIssueCreateVirtualCardLiteRequestMidBlacklist': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["SequenceNumber"]) -> MetaOapg.properties.SequenceNumber: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["SupplierId"]) -> MetaOapg.properties.SupplierId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["NonDomesticSupplier"]) -> MetaOapg.properties.NonDomesticSupplier: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["OrderNumber"]) -> MetaOapg.properties.OrderNumber: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["CustomerID"]) -> MetaOapg.properties.CustomerID: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Transmission"]) -> 'CardIssueCreateVirtualCardLiteRequestTransmission': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ReturnCardData"]) -> MetaOapg.properties.ReturnCardData: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["CustomParameters"]) -> 'CardIssueCreateVirtualCardLiteRequestCustomParameters': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ActivationDate"]) -> MetaOapg.properties.ActivationDate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["AssociationId"]) -> MetaOapg.properties.AssociationId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["LabelIDs"]) -> 'CardIssueCreateVirtualCardLiteRequestLabelIDs': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["MerchantGuid", "FirstName", "LastName", "AmountLimit", "PurchaseType", "Phone", "Address1", "Address2", "City", "State", "ZipCode", "Country", "UsageLimit", "ExpirationDate", "TerminateDate", "MIDWhitelist", "MIDBlacklist", "SequenceNumber", "SupplierId", "NonDomesticSupplier", "OrderNumber", "CustomerID", "Transmission", "ReturnCardData", "CustomParameters", "ActivationDate", "AssociationId", "LabelIDs", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["MerchantGuid"]) -> MetaOapg.properties.MerchantGuid: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["FirstName"]) -> MetaOapg.properties.FirstName: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["LastName"]) -> MetaOapg.properties.LastName: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["AmountLimit"]) -> MetaOapg.properties.AmountLimit: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["PurchaseType"]) -> MetaOapg.properties.PurchaseType: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Phone"]) -> typing.Union[MetaOapg.properties.Phone, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Address1"]) -> typing.Union[MetaOapg.properties.Address1, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Address2"]) -> typing.Union[MetaOapg.properties.Address2, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["City"]) -> typing.Union[MetaOapg.properties.City, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["State"]) -> typing.Union[MetaOapg.properties.State, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ZipCode"]) -> typing.Union[MetaOapg.properties.ZipCode, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Country"]) -> typing.Union[MetaOapg.properties.Country, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["UsageLimit"]) -> typing.Union[MetaOapg.properties.UsageLimit, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ExpirationDate"]) -> typing.Union[MetaOapg.properties.ExpirationDate, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["TerminateDate"]) -> typing.Union[MetaOapg.properties.TerminateDate, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["MIDWhitelist"]) -> typing.Union['CardIssueCreateVirtualCardLiteRequestMidWhitelist', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["MIDBlacklist"]) -> typing.Union['CardIssueCreateVirtualCardLiteRequestMidBlacklist', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["SequenceNumber"]) -> typing.Union[MetaOapg.properties.SequenceNumber, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["SupplierId"]) -> typing.Union[MetaOapg.properties.SupplierId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["NonDomesticSupplier"]) -> typing.Union[MetaOapg.properties.NonDomesticSupplier, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["OrderNumber"]) -> typing.Union[MetaOapg.properties.OrderNumber, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["CustomerID"]) -> typing.Union[MetaOapg.properties.CustomerID, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Transmission"]) -> typing.Union['CardIssueCreateVirtualCardLiteRequestTransmission', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ReturnCardData"]) -> typing.Union[MetaOapg.properties.ReturnCardData, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["CustomParameters"]) -> typing.Union['CardIssueCreateVirtualCardLiteRequestCustomParameters', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ActivationDate"]) -> typing.Union[MetaOapg.properties.ActivationDate, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["AssociationId"]) -> typing.Union[MetaOapg.properties.AssociationId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["LabelIDs"]) -> typing.Union['CardIssueCreateVirtualCardLiteRequestLabelIDs', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["MerchantGuid", "FirstName", "LastName", "AmountLimit", "PurchaseType", "Phone", "Address1", "Address2", "City", "State", "ZipCode", "Country", "UsageLimit", "ExpirationDate", "TerminateDate", "MIDWhitelist", "MIDBlacklist", "SequenceNumber", "SupplierId", "NonDomesticSupplier", "OrderNumber", "CustomerID", "Transmission", "ReturnCardData", "CustomParameters", "ActivationDate", "AssociationId", "LabelIDs", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        MerchantGuid: typing.Union[MetaOapg.properties.MerchantGuid, str, ],
        PurchaseType: typing.Union[MetaOapg.properties.PurchaseType, str, ],
        FirstName: typing.Union[MetaOapg.properties.FirstName, str, ],
        LastName: typing.Union[MetaOapg.properties.LastName, str, ],
        AmountLimit: typing.Union[MetaOapg.properties.AmountLimit, decimal.Decimal, int, float, ],
        Phone: typing.Union[MetaOapg.properties.Phone, str, schemas.Unset] = schemas.unset,
        Address1: typing.Union[MetaOapg.properties.Address1, str, schemas.Unset] = schemas.unset,
        Address2: typing.Union[MetaOapg.properties.Address2, str, schemas.Unset] = schemas.unset,
        City: typing.Union[MetaOapg.properties.City, str, schemas.Unset] = schemas.unset,
        State: typing.Union[MetaOapg.properties.State, str, schemas.Unset] = schemas.unset,
        ZipCode: typing.Union[MetaOapg.properties.ZipCode, str, schemas.Unset] = schemas.unset,
        Country: typing.Union[MetaOapg.properties.Country, str, schemas.Unset] = schemas.unset,
        UsageLimit: typing.Union[MetaOapg.properties.UsageLimit, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        ExpirationDate: typing.Union[MetaOapg.properties.ExpirationDate, str, date, schemas.Unset] = schemas.unset,
        TerminateDate: typing.Union[MetaOapg.properties.TerminateDate, str, date, schemas.Unset] = schemas.unset,
        MIDWhitelist: typing.Union['CardIssueCreateVirtualCardLiteRequestMidWhitelist', schemas.Unset] = schemas.unset,
        MIDBlacklist: typing.Union['CardIssueCreateVirtualCardLiteRequestMidBlacklist', schemas.Unset] = schemas.unset,
        SequenceNumber: typing.Union[MetaOapg.properties.SequenceNumber, str, schemas.Unset] = schemas.unset,
        SupplierId: typing.Union[MetaOapg.properties.SupplierId, str, schemas.Unset] = schemas.unset,
        NonDomesticSupplier: typing.Union[MetaOapg.properties.NonDomesticSupplier, bool, schemas.Unset] = schemas.unset,
        OrderNumber: typing.Union[MetaOapg.properties.OrderNumber, str, schemas.Unset] = schemas.unset,
        CustomerID: typing.Union[MetaOapg.properties.CustomerID, str, schemas.Unset] = schemas.unset,
        Transmission: typing.Union['CardIssueCreateVirtualCardLiteRequestTransmission', schemas.Unset] = schemas.unset,
        ReturnCardData: typing.Union[MetaOapg.properties.ReturnCardData, bool, schemas.Unset] = schemas.unset,
        CustomParameters: typing.Union['CardIssueCreateVirtualCardLiteRequestCustomParameters', schemas.Unset] = schemas.unset,
        ActivationDate: typing.Union[MetaOapg.properties.ActivationDate, str, date, schemas.Unset] = schemas.unset,
        AssociationId: typing.Union[MetaOapg.properties.AssociationId, str, schemas.Unset] = schemas.unset,
        LabelIDs: typing.Union['CardIssueCreateVirtualCardLiteRequestLabelIDs', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'CardIssueCreateVirtualCardLiteRequest':
        return super().__new__(
            cls,
            *args,
            MerchantGuid=MerchantGuid,
            PurchaseType=PurchaseType,
            FirstName=FirstName,
            LastName=LastName,
            AmountLimit=AmountLimit,
            Phone=Phone,
            Address1=Address1,
            Address2=Address2,
            City=City,
            State=State,
            ZipCode=ZipCode,
            Country=Country,
            UsageLimit=UsageLimit,
            ExpirationDate=ExpirationDate,
            TerminateDate=TerminateDate,
            MIDWhitelist=MIDWhitelist,
            MIDBlacklist=MIDBlacklist,
            SequenceNumber=SequenceNumber,
            SupplierId=SupplierId,
            NonDomesticSupplier=NonDomesticSupplier,
            OrderNumber=OrderNumber,
            CustomerID=CustomerID,
            Transmission=Transmission,
            ReturnCardData=ReturnCardData,
            CustomParameters=CustomParameters,
            ActivationDate=ActivationDate,
            AssociationId=AssociationId,
            LabelIDs=LabelIDs,
            _configuration=_configuration,
            **kwargs,
        )

from connex_pay_python_sdk.model.card_issue_create_virtual_card_lite_request_custom_parameters import CardIssueCreateVirtualCardLiteRequestCustomParameters
from connex_pay_python_sdk.model.card_issue_create_virtual_card_lite_request_label_ids import CardIssueCreateVirtualCardLiteRequestLabelIDs
from connex_pay_python_sdk.model.card_issue_create_virtual_card_lite_request_mid_blacklist import CardIssueCreateVirtualCardLiteRequestMidBlacklist
from connex_pay_python_sdk.model.card_issue_create_virtual_card_lite_request_mid_whitelist import CardIssueCreateVirtualCardLiteRequestMidWhitelist
from connex_pay_python_sdk.model.card_issue_create_virtual_card_lite_request_transmission import CardIssueCreateVirtualCardLiteRequestTransmission
