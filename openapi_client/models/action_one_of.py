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
from openapi_client.models.party import Party
from openapi_client.models.token import Token
from openapi_client.models.value import Value

class ActionOneOf(BaseModel):
    """
    ActionOneOf
    """
    deposits: Value = Field(...)
    into_account: Party = Field(...)
    of_token: Token = Field(...)
    party: Party = Field(...)
    __properties = ["deposits", "into_account", "of_token", "party"]

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
    def from_json(cls, json_str: str) -> ActionOneOf:
        """Create an instance of ActionOneOf from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of deposits
        if self.deposits:
            _dict['deposits'] = self.deposits.to_dict()
        # override the default output from pydantic by calling `to_dict()` of into_account
        if self.into_account:
            _dict['into_account'] = self.into_account.to_dict()
        # override the default output from pydantic by calling `to_dict()` of of_token
        if self.of_token:
            _dict['of_token'] = self.of_token.to_dict()
        # override the default output from pydantic by calling `to_dict()` of party
        if self.party:
            _dict['party'] = self.party.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ActionOneOf:
        """Create an instance of ActionOneOf from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ActionOneOf.parse_obj(obj)

        _obj = ActionOneOf.parse_obj({
            "deposits": Value.from_dict(obj.get("deposits")) if obj.get("deposits") is not None else None,
            "into_account": Party.from_dict(obj.get("into_account")) if obj.get("into_account") is not None else None,
            "of_token": Token.from_dict(obj.get("of_token")) if obj.get("of_token") is not None else None,
            "party": Party.from_dict(obj.get("party")) if obj.get("party") is not None else None
        })
        return _obj


