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

class ObservationObjectOneOf6(BaseModel):
    """
    ObservationObjectOneOf6
    """
    lt: ValueObject = Field(...)
    value: ValueObject = Field(...)
    __properties = ["lt", "value"]

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
    def from_json(cls, json_str: str) -> ObservationObjectOneOf6:
        """Create an instance of ObservationObjectOneOf6 from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of lt
        if self.lt:
            _dict['lt'] = self.lt.to_dict()
        # override the default output from pydantic by calling `to_dict()` of value
        if self.value:
            _dict['value'] = self.value.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ObservationObjectOneOf6:
        """Create an instance of ObservationObjectOneOf6 from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ObservationObjectOneOf6.parse_obj(obj)

        _obj = ObservationObjectOneOf6.parse_obj({
            "lt": ValueObject.from_dict(obj.get("lt")) if obj.get("lt") is not None else None,
            "value": ValueObject.from_dict(obj.get("value")) if obj.get("value") is not None else None
        })
        return _obj

from openapi_client.models.value_object import ValueObject
ObservationObjectOneOf6.update_forward_refs()

