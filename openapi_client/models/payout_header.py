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


from typing import Optional
from pydantic import BaseModel, Field, constr, validator
from openapi_client.models.asset_id import AssetId
from openapi_client.models.payout_status import PayoutStatus

class PayoutHeader(BaseModel):
    """
    PayoutHeader
    """
    contract_id: constr(strict=True) = Field(..., alias="contractId", description="A reference to a transaction output with a transaction ID and index.")
    payout_id: constr(strict=True) = Field(..., alias="payoutId", description="A reference to a transaction output with a transaction ID and index.")
    role: AssetId = Field(...)
    status: PayoutStatus = Field(...)
    withdrawal_id: Optional[constr(strict=True)] = Field(None, alias="withdrawalId", description="The hex-encoded identifier of a Cardano transaction")
    __properties = ["contractId", "payoutId", "role", "status", "withdrawalId"]

    @validator('contract_id')
    def contract_id_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(r"^[a-fA-F0-9]{64}#[0-9]+$", value):
            raise ValueError(r"must validate the regular expression /^[a-fA-F0-9]{64}#[0-9]+$/")
        return value

    @validator('payout_id')
    def payout_id_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(r"^[a-fA-F0-9]{64}#[0-9]+$", value):
            raise ValueError(r"must validate the regular expression /^[a-fA-F0-9]{64}#[0-9]+$/")
        return value

    @validator('withdrawal_id')
    def withdrawal_id_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^[a-fA-F0-9]{64}$", value):
            raise ValueError(r"must validate the regular expression /^[a-fA-F0-9]{64}$/")
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
    def from_json(cls, json_str: str) -> PayoutHeader:
        """Create an instance of PayoutHeader from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of role
        if self.role:
            _dict['role'] = self.role.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> PayoutHeader:
        """Create an instance of PayoutHeader from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return PayoutHeader.parse_obj(obj)

        _obj = PayoutHeader.parse_obj({
            "contract_id": obj.get("contractId"),
            "payout_id": obj.get("payoutId"),
            "role": AssetId.from_dict(obj.get("role")) if obj.get("role") is not None else None,
            "status": obj.get("status"),
            "withdrawal_id": obj.get("withdrawalId")
        })
        return _obj


