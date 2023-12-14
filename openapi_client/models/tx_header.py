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


from typing import Dict, Optional
from pydantic import BaseModel, Field, StrictStr, constr, validator
from openapi_client.models.block_header import BlockHeader
from openapi_client.models.metadata import Metadata
from openapi_client.models.tx_status import TxStatus

class TxHeader(BaseModel):
    """
    TxHeader
    """
    block: Optional[BlockHeader] = None
    continuations: Optional[StrictStr] = None
    contract_id: constr(strict=True) = Field(..., alias="contractId", description="A reference to a transaction output with a transaction ID and index.")
    metadata: Dict[str, Metadata] = Field(...)
    status: TxStatus = Field(...)
    tags: Dict[str, Metadata] = Field(...)
    transaction_id: constr(strict=True) = Field(..., alias="transactionId", description="The hex-encoded identifier of a Cardano transaction")
    utxo: Optional[constr(strict=True)] = Field(None, description="A reference to a transaction output with a transaction ID and index.")
    __properties = ["block", "continuations", "contractId", "metadata", "status", "tags", "transactionId", "utxo"]

    @validator('contract_id')
    def contract_id_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(r"^[a-fA-F0-9]{64}#[0-9]+$", value):
            raise ValueError(r"must validate the regular expression /^[a-fA-F0-9]{64}#[0-9]+$/")
        return value

    @validator('transaction_id')
    def transaction_id_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(r"^[a-fA-F0-9]{64}$", value):
            raise ValueError(r"must validate the regular expression /^[a-fA-F0-9]{64}$/")
        return value

    @validator('utxo')
    def utxo_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

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
    def from_json(cls, json_str: str) -> TxHeader:
        """Create an instance of TxHeader from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each value in metadata (dict)
        _field_dict = {}
        if self.metadata:
            for _key in self.metadata:
                if self.metadata[_key]:
                    _field_dict[_key] = self.metadata[_key].to_dict()
            _dict['metadata'] = _field_dict
        # override the default output from pydantic by calling `to_dict()` of each value in tags (dict)
        _field_dict = {}
        if self.tags:
            for _key in self.tags:
                if self.tags[_key]:
                    _field_dict[_key] = self.tags[_key].to_dict()
            _dict['tags'] = _field_dict
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> TxHeader:
        """Create an instance of TxHeader from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return TxHeader.parse_obj(obj)

        _obj = TxHeader.parse_obj({
            "block": BlockHeader.from_dict(obj.get("block")) if obj.get("block") is not None else None,
            "continuations": obj.get("continuations"),
            "contract_id": obj.get("contractId"),
            "metadata": dict(
                (_k, Metadata.from_dict(_v))
                for _k, _v in obj.get("metadata").items()
            )
            if obj.get("metadata") is not None
            else None,
            "status": obj.get("status"),
            "tags": dict(
                (_k, Metadata.from_dict(_v))
                for _k, _v in obj.get("tags").items()
            )
            if obj.get("tags") is not None
            else None,
            "transaction_id": obj.get("transactionId"),
            "utxo": obj.get("utxo")
        })
        return _obj


