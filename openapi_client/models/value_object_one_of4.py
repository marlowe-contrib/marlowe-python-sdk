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



from pydantic import BaseModel, Field

class ValueObjectOneOf4(BaseModel):
    """
    ValueObjectOneOf4
    """
    multiply: ValueObject = Field(...)
    times: ValueObject = Field(...)
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
    def from_json(cls, json_str: str) -> ValueObjectOneOf4:
        """Create an instance of ValueObjectOneOf4 from a JSON string"""
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
    def from_dict(cls, obj: dict) -> ValueObjectOneOf4:
        """Create an instance of ValueObjectOneOf4 from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ValueObjectOneOf4.parse_obj(obj)

        _obj = ValueObjectOneOf4.parse_obj({
            "multiply": ValueObject.from_dict(obj.get("multiply")) if obj.get("multiply") is not None else None,
            "times": ValueObject.from_dict(obj.get("times")) if obj.get("times") is not None else None
        })
        return _obj

from openapi_client.models.value_object import ValueObject
ValueObjectOneOf4.update_forward_refs()

