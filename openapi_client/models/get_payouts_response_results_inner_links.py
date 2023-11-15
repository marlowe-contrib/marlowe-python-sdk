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


from typing import Optional
from pydantic import BaseModel, StrictStr

class GetPayoutsResponseResultsInnerLinks(BaseModel):
    """
    GetPayoutsResponseResultsInnerLinks
    """
    payout: Optional[StrictStr] = None
    __properties = ["payout"]

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
    def from_json(cls, json_str: str) -> GetPayoutsResponseResultsInnerLinks:
        """Create an instance of GetPayoutsResponseResultsInnerLinks from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> GetPayoutsResponseResultsInnerLinks:
        """Create an instance of GetPayoutsResponseResultsInnerLinks from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return GetPayoutsResponseResultsInnerLinks.parse_obj(obj)

        _obj = GetPayoutsResponseResultsInnerLinks.parse_obj({
            "payout": obj.get("payout")
        })
        return _obj

