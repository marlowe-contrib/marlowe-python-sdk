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
from openapi_client.models.party_object import PartyObject
from openapi_client.models.payee_object import PayeeObject
from openapi_client.models.token_object import TokenObject
from openapi_client.models.value_object import ValueObject

class PayObject(BaseModel):
    """
    A payment will be sent from an account to a payee.  # noqa: E501
    """
    from_account: PartyObject = Field(...)
    pay: ValueObject = Field(...)
    then: ContractObject = Field(...)
    to: PayeeObject = Field(...)
    token: TokenObject = Field(...)
    __properties = ["from_account", "pay", "then", "to", "token"]

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
    def from_json(cls, json_str: str) -> PayObject:
        """Create an instance of PayObject from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of from_account
        if self.from_account:
            _dict['from_account'] = self.from_account.to_dict()
        # override the default output from pydantic by calling `to_dict()` of pay
        if self.pay:
            _dict['pay'] = self.pay.to_dict()
        # override the default output from pydantic by calling `to_dict()` of then
        if self.then:
            _dict['then'] = self.then.to_dict()
        # override the default output from pydantic by calling `to_dict()` of to
        if self.to:
            _dict['to'] = self.to.to_dict()
        # override the default output from pydantic by calling `to_dict()` of token
        if self.token:
            _dict['token'] = self.token.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> PayObject:
        """Create an instance of PayObject from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return PayObject.parse_obj(obj)

        _obj = PayObject.parse_obj({
            "from_account": PartyObject.from_dict(obj.get("from_account")) if obj.get("from_account") is not None else None,
            "pay": ValueObject.from_dict(obj.get("pay")) if obj.get("pay") is not None else None,
            "then": ContractObject.from_dict(obj.get("then")) if obj.get("then") is not None else None,
            "to": PayeeObject.from_dict(obj.get("to")) if obj.get("to") is not None else None,
            "token": TokenObject.from_dict(obj.get("token")) if obj.get("token") is not None else None
        })
        return _obj

from openapi_client.models.contract_object import ContractObject
PayObject.update_forward_refs()

