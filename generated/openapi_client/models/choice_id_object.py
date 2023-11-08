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



from pydantic import BaseModel, Field, StrictStr
from openapi_client.models.party_object import PartyObject

class ChoiceIdObject(BaseModel):
    """
    Refers to a party by role name.  # noqa: E501
    """
    choice_name: StrictStr = Field(...)
    choice_owner: PartyObject = Field(...)
    __properties = ["choice_name", "choice_owner"]

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
    def from_json(cls, json_str: str) -> ChoiceIdObject:
        """Create an instance of ChoiceIdObject from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of choice_owner
        if self.choice_owner:
            _dict['choice_owner'] = self.choice_owner.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ChoiceIdObject:
        """Create an instance of ChoiceIdObject from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ChoiceIdObject.parse_obj(obj)

        _obj = ChoiceIdObject.parse_obj({
            "choice_name": obj.get("choice_name"),
            "choice_owner": PartyObject.from_dict(obj.get("choice_owner")) if obj.get("choice_owner") is not None else None
        })
        return _obj


