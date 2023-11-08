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



from pydantic import BaseModel, Field, StrictInt, StrictStr
from openapi_client.models.choice_id import ChoiceId
from openapi_client.models.contract import Contract

class InputOneOf1(BaseModel):
    """
    Make a choice in a contract and provide the continuation of the contract  # noqa: E501
    """
    continuation_hash: StrictStr = Field(...)
    for_choice_id: ChoiceId = Field(...)
    input_that_chooses_num: StrictInt = Field(...)
    merkleized_continuation: Contract = Field(...)
    __properties = ["continuation_hash", "for_choice_id", "input_that_chooses_num", "merkleized_continuation"]

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
    def from_json(cls, json_str: str) -> InputOneOf1:
        """Create an instance of InputOneOf1 from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of for_choice_id
        if self.for_choice_id:
            _dict['for_choice_id'] = self.for_choice_id.to_dict()
        # override the default output from pydantic by calling `to_dict()` of merkleized_continuation
        if self.merkleized_continuation:
            _dict['merkleized_continuation'] = self.merkleized_continuation.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> InputOneOf1:
        """Create an instance of InputOneOf1 from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return InputOneOf1.parse_obj(obj)

        _obj = InputOneOf1.parse_obj({
            "continuation_hash": obj.get("continuation_hash"),
            "for_choice_id": ChoiceId.from_dict(obj.get("for_choice_id")) if obj.get("for_choice_id") is not None else None,
            "input_that_chooses_num": obj.get("input_that_chooses_num"),
            "merkleized_continuation": Contract.from_dict(obj.get("merkleized_continuation")) if obj.get("merkleized_continuation") is not None else None
        })
        return _obj


