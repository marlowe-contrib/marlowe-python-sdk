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



from pydantic import BaseModel, Field, StrictInt
from openapi_client.models.party import Party
from openapi_client.models.payee import Payee
from openapi_client.models.token import Token

class NonPositivePayment(BaseModel):
    """
    A warning for a non-positive payment.  # noqa: E501
    """
    account: Party = Field(...)
    asked_to_pay: StrictInt = Field(...)
    of_token: Token = Field(...)
    to_payee: Payee = Field(...)
    __properties = ["account", "asked_to_pay", "of_token", "to_payee"]

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
    def from_json(cls, json_str: str) -> NonPositivePayment:
        """Create an instance of NonPositivePayment from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of account
        if self.account:
            _dict['account'] = self.account.to_dict()
        # override the default output from pydantic by calling `to_dict()` of of_token
        if self.of_token:
            _dict['of_token'] = self.of_token.to_dict()
        # override the default output from pydantic by calling `to_dict()` of to_payee
        if self.to_payee:
            _dict['to_payee'] = self.to_payee.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> NonPositivePayment:
        """Create an instance of NonPositivePayment from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return NonPositivePayment.parse_obj(obj)

        _obj = NonPositivePayment.parse_obj({
            "account": Party.from_dict(obj.get("account")) if obj.get("account") is not None else None,
            "asked_to_pay": obj.get("asked_to_pay"),
            "of_token": Token.from_dict(obj.get("of_token")) if obj.get("of_token") is not None else None,
            "to_payee": Payee.from_dict(obj.get("to_payee")) if obj.get("to_payee") is not None else None
        })
        return _obj


