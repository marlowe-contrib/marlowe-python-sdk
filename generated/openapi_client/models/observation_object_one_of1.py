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

class ObservationObjectOneOf1(BaseModel):
    """
    ObservationObjectOneOf1
    """
    either: ObservationObject = Field(...)
    var_or: ObservationObject = Field(..., alias="or")
    __properties = ["either", "or"]

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
    def from_json(cls, json_str: str) -> ObservationObjectOneOf1:
        """Create an instance of ObservationObjectOneOf1 from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of either
        if self.either:
            _dict['either'] = self.either.to_dict()
        # override the default output from pydantic by calling `to_dict()` of var_or
        if self.var_or:
            _dict['or'] = self.var_or.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ObservationObjectOneOf1:
        """Create an instance of ObservationObjectOneOf1 from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ObservationObjectOneOf1.parse_obj(obj)

        _obj = ObservationObjectOneOf1.parse_obj({
            "either": ObservationObject.from_dict(obj.get("either")) if obj.get("either") is not None else None,
            "var_or": ObservationObject.from_dict(obj.get("or")) if obj.get("or") is not None else None
        })
        return _obj

from openapi_client.models.observation_object import ObservationObject
ObservationObjectOneOf1.update_forward_refs()

