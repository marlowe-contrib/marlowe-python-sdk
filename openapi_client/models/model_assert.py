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
from openapi_client.models.observation import Observation

class ModelAssert(BaseModel):
    """
    Check an observation and produce a warning if it is false.  # noqa: E501
    """
    var_assert: Observation = Field(..., alias="assert")
    then: Contract = Field(...)
    __properties = ["assert", "then"]

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
    def from_json(cls, json_str: str) -> ModelAssert:
        """Create an instance of ModelAssert from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of var_assert
        if self.var_assert:
            _dict['assert'] = self.var_assert.to_dict()
        # override the default output from pydantic by calling `to_dict()` of then
        if self.then:
            _dict['then'] = self.then.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ModelAssert:
        """Create an instance of ModelAssert from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ModelAssert.parse_obj(obj)

        _obj = ModelAssert.parse_obj({
            "var_assert": Observation.from_dict(obj.get("assert")) if obj.get("assert") is not None else None,
            "then": Contract.from_dict(obj.get("then")) if obj.get("then") is not None else None
        })
        return _obj

from openapi_client.models.contract import Contract
ModelAssert.update_forward_refs()

