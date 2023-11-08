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



from pydantic import BaseModel, Field, StrictInt
from openapi_client.models.party import Party
from openapi_client.models.token import Token

class InputOneOf4(BaseModel):
    """
    Deposit funds into an account in a contract  # noqa: E501
    """
    input_from_party: Party = Field(...)
    into_account: Party = Field(...)
    of_token: Token = Field(...)
    that_deposits: StrictInt = Field(...)
    __properties = ["input_from_party", "into_account", "of_token", "that_deposits"]

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
    def from_json(cls, json_str: str) -> InputOneOf4:
        """Create an instance of InputOneOf4 from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of input_from_party
        if self.input_from_party:
            _dict['input_from_party'] = self.input_from_party.to_dict()
        # override the default output from pydantic by calling `to_dict()` of into_account
        if self.into_account:
            _dict['into_account'] = self.into_account.to_dict()
        # override the default output from pydantic by calling `to_dict()` of of_token
        if self.of_token:
            _dict['of_token'] = self.of_token.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> InputOneOf4:
        """Create an instance of InputOneOf4 from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return InputOneOf4.parse_obj(obj)

        _obj = InputOneOf4.parse_obj({
            "input_from_party": Party.from_dict(obj.get("input_from_party")) if obj.get("input_from_party") is not None else None,
            "into_account": Party.from_dict(obj.get("into_account")) if obj.get("into_account") is not None else None,
            "of_token": Token.from_dict(obj.get("of_token")) if obj.get("of_token") is not None else None,
            "that_deposits": obj.get("that_deposits")
        })
        return _obj


