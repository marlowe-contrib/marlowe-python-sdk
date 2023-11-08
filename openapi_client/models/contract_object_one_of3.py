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



from pydantic import BaseModel, Field, StrictStr
from openapi_client.models.value_object import ValueObject

class ContractObjectOneOf3(BaseModel):
    """
    Bind a value to a name within the scope of a sub-contract.  # noqa: E501
    """
    be: ValueObject = Field(...)
    let: StrictStr = Field(...)
    then: ContractObject = Field(...)
    __properties = ["be", "let", "then"]

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
    def from_json(cls, json_str: str) -> ContractObjectOneOf3:
        """Create an instance of ContractObjectOneOf3 from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of be
        if self.be:
            _dict['be'] = self.be.to_dict()
        # override the default output from pydantic by calling `to_dict()` of then
        if self.then:
            _dict['then'] = self.then.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ContractObjectOneOf3:
        """Create an instance of ContractObjectOneOf3 from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ContractObjectOneOf3.parse_obj(obj)

        _obj = ContractObjectOneOf3.parse_obj({
            "be": ValueObject.from_dict(obj.get("be")) if obj.get("be") is not None else None,
            "let": obj.get("let"),
            "then": ContractObject.from_dict(obj.get("then")) if obj.get("then") is not None else None
        })
        return _obj

from openapi_client.models.contract_object import ContractObject
ContractObjectOneOf3.update_forward_refs()

