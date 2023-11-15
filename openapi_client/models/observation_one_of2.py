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

class ObservationOneOf2(BaseModel):
    """
    ObservationOneOf2
    """
    var_not: Observation = Field(..., alias="not")
    __properties = ["not"]

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
    def from_json(cls, json_str: str) -> ObservationOneOf2:
        """Create an instance of ObservationOneOf2 from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of var_not
        if self.var_not:
            _dict['not'] = self.var_not.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ObservationOneOf2:
        """Create an instance of ObservationOneOf2 from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ObservationOneOf2.parse_obj(obj)

        _obj = ObservationOneOf2.parse_obj({
            "var_not": Observation.from_dict(obj.get("not")) if obj.get("not") is not None else None
        })
        return _obj

from openapi_client.models.observation import Observation
ObservationOneOf2.update_forward_refs()

