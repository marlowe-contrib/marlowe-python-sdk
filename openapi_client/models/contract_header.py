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


from typing import Any, Dict, Optional
from pydantic import BaseModel, Field, StrictStr, constr, validator
from openapi_client.models.block_header import BlockHeader
from openapi_client.models.marlowe_version import MarloweVersion
from openapi_client.models.tx_status import TxStatus

class ContractHeader(BaseModel):
    """
    ContractHeader
    """
    block: Optional[BlockHeader] = None
    continuations: Optional[StrictStr] = None
    contract_id: constr(strict=True) = Field(..., alias="contractId", description="A reference to a transaction output with a transaction ID and index.")
    metadata: Dict[str, Any] = Field(...)
    role_token_minting_policy_id: constr(strict=True) = Field(..., alias="roleTokenMintingPolicyId", description="The hex-encoded minting policy ID for a native Cardano token")
    status: TxStatus = Field(...)
    tags: Dict[str, Any] = Field(...)
    version: MarloweVersion = Field(...)
    __properties = ["block", "continuations", "contractId", "metadata", "roleTokenMintingPolicyId", "status", "tags", "version"]

    @validator('contract_id')
    def contract_id_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(r"^[a-fA-F0-9]{64}#[0-9]+$", value):
            raise ValueError(r"must validate the regular expression /^[a-fA-F0-9]{64}#[0-9]+$/")
        return value

    @validator('role_token_minting_policy_id')
    def role_token_minting_policy_id_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(r"^[a-fA-F0-9]*$", value):
            raise ValueError(r"must validate the regular expression /^[a-fA-F0-9]*$/")
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
    def from_json(cls, json_str: str) -> ContractHeader:
        """Create an instance of ContractHeader from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of block
        if self.block:
            _dict['block'] = self.block.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ContractHeader:
        """Create an instance of ContractHeader from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ContractHeader.parse_obj(obj)

        _obj = ContractHeader.parse_obj({
            "block": BlockHeader.from_dict(obj.get("block")) if obj.get("block") is not None else None,
            "continuations": obj.get("continuations"),
            "contract_id": obj.get("contractId"),
            "metadata": obj.get("metadata"),
            "role_token_minting_policy_id": obj.get("roleTokenMintingPolicyId"),
            "status": obj.get("status"),
            "tags": obj.get("tags"),
            "version": obj.get("version")
        })
        return _obj


