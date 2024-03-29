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
from pydantic import BaseModel, Field, StrictInt, conlist

class WhenObject(BaseModel):
    """
    Wait for an action to be performed and apply the matching contract when it does. Apply the timeout contract if no actions have been performed in the timeout period.  # noqa: E501
    """
    timeout: StrictInt = Field(...)
    timeout_continuation: ContractObject = Field(...)
    when: conlist(CaseObject) = Field(...)
    __properties = ["timeout", "timeout_continuation", "when"]

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
    def from_json(cls, json_str: str) -> WhenObject:
        """Create an instance of WhenObject from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of timeout_continuation
        if self.timeout_continuation:
            _dict['timeout_continuation'] = self.timeout_continuation.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in when (list)
        _items = []
        if self.when:
            for _item in self.when:
                if _item:
                    _items.append(_item.to_dict())
            _dict['when'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> WhenObject:
        """Create an instance of WhenObject from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return WhenObject.parse_obj(obj)

        _obj = WhenObject.parse_obj({
            "timeout": obj.get("timeout"),
            "timeout_continuation": ContractObject.from_dict(obj.get("timeout_continuation")) if obj.get("timeout_continuation") is not None else None,
            "when": [CaseObject.from_dict(_item) for _item in obj.get("when")] if obj.get("when") is not None else None
        })
        return _obj

from openapi_client.models.case_object import CaseObject
from openapi_client.models.contract_object import ContractObject
WhenObject.update_forward_refs()

