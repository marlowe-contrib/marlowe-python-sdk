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
from openapi_client.models.action import Action

class CaseOneOf(BaseModel):
    """
    CaseOneOf
    """
    case: Action = Field(...)
    then: Contract = Field(...)
    __properties = ["case", "then"]

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
    def from_json(cls, json_str: str) -> CaseOneOf:
        """Create an instance of CaseOneOf from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of case
        if self.case:
            _dict['case'] = self.case.to_dict()
        # override the default output from pydantic by calling `to_dict()` of then
        if self.then:
            _dict['then'] = self.then.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> CaseOneOf:
        """Create an instance of CaseOneOf from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return CaseOneOf.parse_obj(obj)

        _obj = CaseOneOf.parse_obj({
            "case": Action.from_dict(obj.get("case")) if obj.get("case") is not None else None,
            "then": Contract.from_dict(obj.get("then")) if obj.get("then") is not None else None
        })
        return _obj

from openapi_client.models.contract import Contract
CaseOneOf.update_forward_refs()

