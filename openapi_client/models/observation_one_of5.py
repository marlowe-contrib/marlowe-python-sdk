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

class ObservationOneOf5(BaseModel):
    """
    ObservationOneOf5
    """
    gt: Value = Field(...)
    value: Value = Field(...)
    __properties = ["gt", "value"]

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
    def from_json(cls, json_str: str) -> ObservationOneOf5:
        """Create an instance of ObservationOneOf5 from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of gt
        if self.gt:
            _dict['gt'] = self.gt.to_dict()
        # override the default output from pydantic by calling `to_dict()` of value
        if self.value:
            _dict['value'] = self.value.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ObservationOneOf5:
        """Create an instance of ObservationOneOf5 from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ObservationOneOf5.parse_obj(obj)

        _obj = ObservationOneOf5.parse_obj({
            "gt": Value.from_dict(obj.get("gt")) if obj.get("gt") is not None else None,
            "value": Value.from_dict(obj.get("value")) if obj.get("value") is not None else None
        })
        return _obj

from openapi_client.models.value import Value
ObservationOneOf5.update_forward_refs()

