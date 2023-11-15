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

class ObservationOneOf(BaseModel):
    """
    ObservationOneOf
    """
    var_and: Observation = Field(..., alias="and")
    both: Observation = Field(...)
    __properties = ["and", "both"]

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
    def from_json(cls, json_str: str) -> ObservationOneOf:
        """Create an instance of ObservationOneOf from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of var_and
        if self.var_and:
            _dict['and'] = self.var_and.to_dict()
        # override the default output from pydantic by calling `to_dict()` of both
        if self.both:
            _dict['both'] = self.both.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ObservationOneOf:
        """Create an instance of ObservationOneOf from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ObservationOneOf.parse_obj(obj)

        _obj = ObservationOneOf.parse_obj({
            "var_and": Observation.from_dict(obj.get("and")) if obj.get("and") is not None else None,
            "both": Observation.from_dict(obj.get("both")) if obj.get("both") is not None else None
        })
        return _obj

from openapi_client.models.observation import Observation
ObservationOneOf.update_forward_refs()

