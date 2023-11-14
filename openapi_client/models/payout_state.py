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


from typing import Any, ClassVar, Dict, List, Optional
from pydantic import BaseModel, StrictStr, field_validator
from pydantic import Field
from typing_extensions import Annotated
from openapi_client.models.asset_id import AssetId
from openapi_client.models.assets import Assets
from openapi_client.models.payout_status import PayoutStatus
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class PayoutState(BaseModel):
    """
    PayoutState
    """ # noqa: E501
    assets: Assets
    contract_id: Annotated[str, Field(strict=True)] = Field(description="A reference to a transaction output with a transaction ID and index.", alias="contractId")
    payout_id: Annotated[str, Field(strict=True)] = Field(description="A reference to a transaction output with a transaction ID and index.", alias="payoutId")
    payout_validator_address: StrictStr = Field(description="A cardano address", alias="payoutValidatorAddress")
    role: AssetId
    status: PayoutStatus
    withdrawal_id: Optional[Annotated[str, Field(strict=True)]] = Field(default=None, description="The hex-encoded identifier of a Cardano transaction", alias="withdrawalId")
    __properties: ClassVar[List[str]] = ["assets", "contractId", "payoutId", "payoutValidatorAddress", "role", "status", "withdrawalId"]

    @field_validator('contract_id')
    def contract_id_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(r"^[a-fA-F0-9]{64}#[0-9]+$", value):
            raise ValueError(r"must validate the regular expression /^[a-fA-F0-9]{64}#[0-9]+$/")
        return value

    @field_validator('payout_id')
    def payout_id_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(r"^[a-fA-F0-9]{64}#[0-9]+$", value):
            raise ValueError(r"must validate the regular expression /^[a-fA-F0-9]{64}#[0-9]+$/")
        return value

    @field_validator('withdrawal_id')
    def withdrawal_id_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^[a-fA-F0-9]{64}$", value):
            raise ValueError(r"must validate the regular expression /^[a-fA-F0-9]{64}$/")
        return value

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
        """Create an instance of PayoutState from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of assets
        if self.assets:
            _dict['assets'] = self.assets.to_dict()
        # override the default output from pydantic by calling `to_dict()` of role
        if self.role:
            _dict['role'] = self.role.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of PayoutState from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "assets": Assets.from_dict(obj.get("assets")) if obj.get("assets") is not None else None,
            "contractId": obj.get("contractId"),
            "payoutId": obj.get("payoutId"),
            "payoutValidatorAddress": obj.get("payoutValidatorAddress"),
            "role": AssetId.from_dict(obj.get("role")) if obj.get("role") is not None else None,
            "status": obj.get("status"),
            "withdrawalId": obj.get("withdrawalId")
        })
        return _obj


