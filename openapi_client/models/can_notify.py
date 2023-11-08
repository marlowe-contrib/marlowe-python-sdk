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



from pydantic import BaseModel, Field, StrictBool, StrictInt

class CanNotify(BaseModel):
    """
    Notify Input tha can be applied for a given contract  # noqa: E501
    """
    case_index: StrictInt = Field(..., description="Index of a \"Case Action\" in a \"When\"")
    is_merkleized_continuation: StrictBool = Field(..., description="Indicates if a given contract continuation is merkleized")
    __properties = ["case_index", "is_merkleized_continuation"]

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
    def from_json(cls, json_str: str) -> CanNotify:
        """Create an instance of CanNotify from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> CanNotify:
        """Create an instance of CanNotify from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return CanNotify.parse_obj(obj)

        _obj = CanNotify.parse_obj({
            "case_index": obj.get("case_index"),
            "is_merkleized_continuation": obj.get("is_merkleized_continuation")
        })
        return _obj

