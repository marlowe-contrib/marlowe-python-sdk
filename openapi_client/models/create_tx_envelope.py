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


from typing import List, Optional
from pydantic import BaseModel, Field, conlist, constr, validator
from openapi_client.models.safety_error import SafetyError
from openapi_client.models.text_envelope import TextEnvelope

class CreateTxEnvelope(BaseModel):
    """
    The \"type\" property of \"tx\" must be \"Tx BabbageEra\" or \"Tx ConwayEra\"  # noqa: E501
    """
    contract_id: constr(strict=True) = Field(..., alias="contractId", description="A reference to a transaction output with a transaction ID and index.")
    safety_errors: Optional[conlist(SafetyError)] = Field(None, alias="safetyErrors")
    tx: TextEnvelope = Field(...)
    __properties = ["contractId", "safetyErrors", "tx"]

    @validator('contract_id')
    def contract_id_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(r"^[a-fA-F0-9]{64}#[0-9]+$", value):
            raise ValueError(r"must validate the regular expression /^[a-fA-F0-9]{64}#[0-9]+$/")
        return value

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
    def from_json(cls, json_str: str) -> CreateTxEnvelope:
        """Create an instance of CreateTxEnvelope from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in safety_errors (list)
        _items = []
        if self.safety_errors:
            for _item in self.safety_errors:
                if _item:
                    _items.append(_item.to_dict())
            _dict['safetyErrors'] = _items
        # override the default output from pydantic by calling `to_dict()` of tx
        if self.tx:
            _dict['tx'] = self.tx.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> CreateTxEnvelope:
        """Create an instance of CreateTxEnvelope from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return CreateTxEnvelope.parse_obj(obj)

        _obj = CreateTxEnvelope.parse_obj({
            "contract_id": obj.get("contractId"),
            "safety_errors": [SafetyError.from_dict(_item) for _item in obj.get("safetyErrors")] if obj.get("safetyErrors") is not None else None,
            "tx": TextEnvelope.from_dict(obj.get("tx")) if obj.get("tx") is not None else None
        })
        return _obj

