# coding: utf-8

"""
    

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import List
from pydantic import BaseModel, Field, StrictBool, StrictInt, conlist
from openapi_client.models.bound import Bound
from openapi_client.models.choice_id import ChoiceId

class CanChoose(BaseModel):
    """
    Choice Inputs that can be applied for a given contract  # noqa: E501
    """
    can_choose_between: conlist(Bound) = Field(...)
    case_index: StrictInt = Field(..., description="Index of a \"Case Action\" in a \"When\"")
    for_choice: ChoiceId = Field(...)
    is_merkleized_continuation: StrictBool = Field(..., description="Indicates if a given contract continuation is merkleized")
    __properties = ["can_choose_between", "case_index", "for_choice", "is_merkleized_continuation"]

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
    def from_json(cls, json_str: str) -> CanChoose:
        """Create an instance of CanChoose from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in can_choose_between (list)
        _items = []
        if self.can_choose_between:
            for _item in self.can_choose_between:
                if _item:
                    _items.append(_item.to_dict())
            _dict['can_choose_between'] = _items
        # override the default output from pydantic by calling `to_dict()` of for_choice
        if self.for_choice:
            _dict['for_choice'] = self.for_choice.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> CanChoose:
        """Create an instance of CanChoose from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return CanChoose.parse_obj(obj)

        _obj = CanChoose.parse_obj({
            "can_choose_between": [Bound.from_dict(_item) for _item in obj.get("can_choose_between")] if obj.get("can_choose_between") is not None else None,
            "case_index": obj.get("case_index"),
            "for_choice": ChoiceId.from_dict(obj.get("for_choice")) if obj.get("for_choice") is not None else None,
            "is_merkleized_continuation": obj.get("is_merkleized_continuation")
        })
        return _obj


