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


from typing import Any, Dict, List, Optional
from pydantic import BaseModel, Field, StrictStr, conlist, constr, validator
from openapi_client.models.assets import Assets
from openapi_client.models.block_header import BlockHeader
from openapi_client.models.contract import Contract
from openapi_client.models.input import Input
from openapi_client.models.marlowe_state import MarloweState
from openapi_client.models.payout import Payout
from openapi_client.models.text_envelope import TextEnvelope
from openapi_client.models.tx_status import TxStatus

class Tx(BaseModel):
    """
    Tx
    """
    assets: Assets = Field(...)
    block: Optional[BlockHeader] = None
    consuming_tx: Optional[constr(strict=True)] = Field(None, alias="consumingTx", description="The hex-encoded identifier of a Cardano transaction")
    continuations: Optional[StrictStr] = None
    contract_id: constr(strict=True) = Field(..., alias="contractId", description="A reference to a transaction output with a transaction ID and index.")
    input_utxo: constr(strict=True) = Field(..., alias="inputUtxo", description="A reference to a transaction output with a transaction ID and index.")
    inputs: conlist(Input) = Field(...)
    invalid_before: StrictStr = Field(..., alias="invalidBefore")
    invalid_hereafter: StrictStr = Field(..., alias="invalidHereafter")
    metadata: Dict[str, Any] = Field(...)
    output_contract: Optional[Contract] = Field(None, alias="outputContract")
    output_state: Optional[MarloweState] = Field(None, alias="outputState")
    output_utxo: Optional[constr(strict=True)] = Field(None, alias="outputUtxo", description="A reference to a transaction output with a transaction ID and index.")
    payouts: conlist(Payout) = Field(...)
    status: TxStatus = Field(...)
    tags: Dict[str, Any] = Field(...)
    transaction_id: constr(strict=True) = Field(..., alias="transactionId", description="The hex-encoded identifier of a Cardano transaction")
    tx_body: Optional[TextEnvelope] = Field(None, alias="txBody")
    __properties = ["assets", "block", "consumingTx", "continuations", "contractId", "inputUtxo", "inputs", "invalidBefore", "invalidHereafter", "metadata", "outputContract", "outputState", "outputUtxo", "payouts", "status", "tags", "transactionId", "txBody"]

    @validator('consuming_tx')
    def consuming_tx_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^[a-fA-F0-9]{64}$", value):
            raise ValueError(r"must validate the regular expression /^[a-fA-F0-9]{64}$/")
        return value

    @validator('contract_id')
    def contract_id_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(r"^[a-fA-F0-9]{64}#[0-9]+$", value):
            raise ValueError(r"must validate the regular expression /^[a-fA-F0-9]{64}#[0-9]+$/")
        return value

    @validator('input_utxo')
    def input_utxo_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(r"^[a-fA-F0-9]{64}#[0-9]+$", value):
            raise ValueError(r"must validate the regular expression /^[a-fA-F0-9]{64}#[0-9]+$/")
        return value

    @validator('output_utxo')
    def output_utxo_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^[a-fA-F0-9]{64}#[0-9]+$", value):
            raise ValueError(r"must validate the regular expression /^[a-fA-F0-9]{64}#[0-9]+$/")
        return value

    @validator('transaction_id')
    def transaction_id_validate_regular_expression(cls, value):
        """Validates the regular expression"""
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
    def from_json(cls, json_str: str) -> Tx:
        """Create an instance of Tx from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of assets
        if self.assets:
            _dict['assets'] = self.assets.to_dict()
        # override the default output from pydantic by calling `to_dict()` of block
        if self.block:
            _dict['block'] = self.block.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in inputs (list)
        _items = []
        if self.inputs:
            for _item in self.inputs:
                if _item:
                    _items.append(_item.to_dict())
            _dict['inputs'] = _items
        # override the default output from pydantic by calling `to_dict()` of output_contract
        if self.output_contract:
            _dict['outputContract'] = self.output_contract.to_dict()
        # override the default output from pydantic by calling `to_dict()` of output_state
        if self.output_state:
            _dict['outputState'] = self.output_state.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in payouts (list)
        _items = []
        if self.payouts:
            for _item in self.payouts:
                if _item:
                    _items.append(_item.to_dict())
            _dict['payouts'] = _items
        # override the default output from pydantic by calling `to_dict()` of tx_body
        if self.tx_body:
            _dict['txBody'] = self.tx_body.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Tx:
        """Create an instance of Tx from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return Tx.parse_obj(obj)

        _obj = Tx.parse_obj({
            "assets": Assets.from_dict(obj.get("assets")) if obj.get("assets") is not None else None,
            "block": BlockHeader.from_dict(obj.get("block")) if obj.get("block") is not None else None,
            "consuming_tx": obj.get("consumingTx"),
            "continuations": obj.get("continuations"),
            "contract_id": obj.get("contractId"),
            "input_utxo": obj.get("inputUtxo"),
            "inputs": [Input.from_dict(_item) for _item in obj.get("inputs")] if obj.get("inputs") is not None else None,
            "invalid_before": obj.get("invalidBefore"),
            "invalid_hereafter": obj.get("invalidHereafter"),
            "metadata": obj.get("metadata"),
            "output_contract": Contract.from_dict(obj.get("outputContract")) if obj.get("outputContract") is not None else None,
            "output_state": MarloweState.from_dict(obj.get("outputState")) if obj.get("outputState") is not None else None,
            "output_utxo": obj.get("outputUtxo"),
            "payouts": [Payout.from_dict(_item) for _item in obj.get("payouts")] if obj.get("payouts") is not None else None,
            "status": obj.get("status"),
            "tags": obj.get("tags"),
            "transaction_id": obj.get("transactionId"),
            "tx_body": TextEnvelope.from_dict(obj.get("txBody")) if obj.get("txBody") is not None else None
        })
        return _obj


