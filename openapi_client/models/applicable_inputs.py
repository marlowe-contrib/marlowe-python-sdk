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


from typing import List, Optional
from pydantic import BaseModel, Field, conlist
from openapi_client.models.can_choose import CanChoose
from openapi_client.models.can_deposit import CanDeposit
from openapi_client.models.can_notify import CanNotify

class ApplicableInputs(BaseModel):
    """
    Applicable Inputs for a given contract  # noqa: E501
    """
    choices: conlist(CanChoose) = Field(...)
    deposits: conlist(CanDeposit) = Field(...)
    notify: Optional[CanNotify] = None
    __properties = ["choices", "deposits", "notify"]

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
    def from_json(cls, json_str: str) -> ApplicableInputs:
        """Create an instance of ApplicableInputs from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in choices (list)
        _items = []
        if self.choices:
            for _item in self.choices:
                if _item:
                    _items.append(_item.to_dict())
            _dict['choices'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in deposits (list)
        _items = []
        if self.deposits:
            for _item in self.deposits:
                if _item:
                    _items.append(_item.to_dict())
            _dict['deposits'] = _items
        # override the default output from pydantic by calling `to_dict()` of notify
        if self.notify:
            _dict['notify'] = self.notify.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ApplicableInputs:
        """Create an instance of ApplicableInputs from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ApplicableInputs.parse_obj(obj)

        _obj = ApplicableInputs.parse_obj({
            "choices": [CanChoose.from_dict(_item) for _item in obj.get("choices")] if obj.get("choices") is not None else None,
            "deposits": [CanDeposit.from_dict(_item) for _item in obj.get("deposits")] if obj.get("deposits") is not None else None,
            "notify": CanNotify.from_dict(obj.get("notify")) if obj.get("notify") is not None else None
        })
        return _obj


