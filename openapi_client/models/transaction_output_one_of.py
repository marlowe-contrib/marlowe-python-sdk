# coding: utf-8

"""
    Marlowe Runtime REST API

    REST API for Marlowe Runtime

    The version of the OpenAPI document: 0.0.5.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import List
from pydantic import BaseModel, Field, conlist
from openapi_client.models.contract import Contract
from openapi_client.models.marlowe_state import MarloweState
from openapi_client.models.payment import Payment
from openapi_client.models.transaction_warning import TransactionWarning

class TransactionOutputOneOf(BaseModel):
    """
    Marlowe transaction output information.  # noqa: E501
    """
    contract: Contract = Field(...)
    payments: conlist(Payment) = Field(...)
    state: MarloweState = Field(...)
    warnings: conlist(TransactionWarning) = Field(...)
    __properties = ["contract", "payments", "state", "warnings"]

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> TransactionOutputOneOf:
        """Create an instance of TransactionOutputOneOf from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of contract
        if self.contract:
            _dict['contract'] = self.contract.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in payments (list)
        _items = []
        if self.payments:
            for _item in self.payments:
                if _item:
                    _items.append(_item.to_dict())
            _dict['payments'] = _items
        # override the default output from pydantic by calling `to_dict()` of state
        if self.state:
            _dict['state'] = self.state.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in warnings (list)
        _items = []
        if self.warnings:
            for _item in self.warnings:
                if _item:
                    _items.append(_item.to_dict())
            _dict['warnings'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> TransactionOutputOneOf:
        """Create an instance of TransactionOutputOneOf from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return TransactionOutputOneOf.parse_obj(obj)

        _obj = TransactionOutputOneOf.parse_obj({
            "contract": Contract.from_dict(obj.get("contract")) if obj.get("contract") is not None else None,
            "payments": [Payment.from_dict(_item) for _item in obj.get("payments")] if obj.get("payments") is not None else None,
            "state": MarloweState.from_dict(obj.get("state")) if obj.get("state") is not None else None,
            "warnings": [TransactionWarning.from_dict(_item) for _item in obj.get("warnings")] if obj.get("warnings") is not None else None
        })
        return _obj


