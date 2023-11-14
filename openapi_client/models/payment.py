# coding: utf-8

"""
    Marlowe Runtime REST API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.0.5
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Any, ClassVar, Dict, List
from pydantic import BaseModel, StrictInt
from openapi_client.models.party import Party
from openapi_client.models.payee import Payee
from openapi_client.models.token import Token
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class Payment(BaseModel):
    """
    A Marlowe payment.
    """ # noqa: E501
    amount: StrictInt
    payment_from: Party
    to: Payee
    token: Token
    __properties: ClassVar[List[str]] = ["amount", "payment_from", "to", "token"]

    model_config = {
        "populate_by_name": True,
        "validate_assignment": True
    }


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of Payment from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        _dict = self.model_dump(
            by_alias=True,
            exclude={
            },
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of payment_from
        if self.payment_from:
            _dict['payment_from'] = self.payment_from.to_dict()
        # override the default output from pydantic by calling `to_dict()` of to
        if self.to:
            _dict['to'] = self.to.to_dict()
        # override the default output from pydantic by calling `to_dict()` of token
        if self.token:
            _dict['token'] = self.token.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of Payment from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "amount": obj.get("amount"),
            "payment_from": Party.from_dict(obj.get("payment_from")) if obj.get("payment_from") is not None else None,
            "to": Payee.from_dict(obj.get("to")) if obj.get("to") is not None else None,
            "token": Token.from_dict(obj.get("token")) if obj.get("token") is not None else None
        })
        return _obj


