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
from openapi_client.models.input import Input
from openapi_client.models.transaction_input_tx_interval import TransactionInputTxInterval

class TransactionInput(BaseModel):
    """
    Marlowe transaction input.  # noqa: E501
    """
    tx_inputs: conlist(Input) = Field(...)
    tx_interval: TransactionInputTxInterval = Field(...)
    __properties = ["tx_inputs", "tx_interval"]

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
    def from_json(cls, json_str: str) -> TransactionInput:
        """Create an instance of TransactionInput from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in tx_inputs (list)
        _items = []
        if self.tx_inputs:
            for _item in self.tx_inputs:
                if _item:
                    _items.append(_item.to_dict())
            _dict['tx_inputs'] = _items
        # override the default output from pydantic by calling `to_dict()` of tx_interval
        if self.tx_interval:
            _dict['tx_interval'] = self.tx_interval.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> TransactionInput:
        """Create an instance of TransactionInput from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return TransactionInput.parse_obj(obj)

        _obj = TransactionInput.parse_obj({
            "tx_inputs": [Input.from_dict(_item) for _item in obj.get("tx_inputs")] if obj.get("tx_inputs") is not None else None,
            "tx_interval": TransactionInputTxInterval.from_dict(obj.get("tx_interval")) if obj.get("tx_interval") is not None else None
        })
        return _obj


