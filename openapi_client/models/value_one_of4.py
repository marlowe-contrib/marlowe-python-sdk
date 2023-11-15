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



from pydantic import BaseModel, Field

class ValueOneOf4(BaseModel):
    """
    ValueOneOf4
    """
    multiply: Value = Field(...)
    times: Value = Field(...)
    __properties = ["multiply", "times"]

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
    def from_json(cls, json_str: str) -> ValueOneOf4:
        """Create an instance of ValueOneOf4 from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of multiply
        if self.multiply:
            _dict['multiply'] = self.multiply.to_dict()
        # override the default output from pydantic by calling `to_dict()` of times
        if self.times:
            _dict['times'] = self.times.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ValueOneOf4:
        """Create an instance of ValueOneOf4 from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ValueOneOf4.parse_obj(obj)

        _obj = ValueOneOf4.parse_obj({
            "multiply": Value.from_dict(obj.get("multiply")) if obj.get("multiply") is not None else None,
            "times": Value.from_dict(obj.get("times")) if obj.get("times") is not None else None
        })
        return _obj

from openapi_client.models.value import Value
ValueOneOf4.update_forward_refs()

