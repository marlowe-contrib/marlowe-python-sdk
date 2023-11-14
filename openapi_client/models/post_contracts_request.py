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
from pydantic import BaseModel
from pydantic import Field
from typing_extensions import Annotated
from openapi_client.models.marlowe_version import MarloweVersion
from openapi_client.models.post_contracts_request_contract import PostContractsRequestContract
from openapi_client.models.roles_config import RolesConfig
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class PostContractsRequest(BaseModel):
    """
    PostContractsRequest
    """ # noqa: E501
    contract: PostContractsRequestContract
    metadata: Dict[str, Any]
    min_utx_o_deposit: Annotated[int, Field(le=-1, strict=True, ge=0)] = Field(alias="minUTxODeposit")
    roles: Optional[RolesConfig] = None
    tags: Dict[str, Any]
    version: MarloweVersion
    __properties: ClassVar[List[str]] = ["contract", "metadata", "minUTxODeposit", "roles", "tags", "version"]

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
        """Create an instance of PostContractsRequest from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of contract
        if self.contract:
            _dict['contract'] = self.contract.to_dict()
        # override the default output from pydantic by calling `to_dict()` of roles
        if self.roles:
            _dict['roles'] = self.roles.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of PostContractsRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "contract": PostContractsRequestContract.from_dict(obj.get("contract")) if obj.get("contract") is not None else None,
            "metadata": obj.get("metadata"),
            "minUTxODeposit": obj.get("minUTxODeposit"),
            "roles": RolesConfig.from_dict(obj.get("roles")) if obj.get("roles") is not None else None,
            "tags": obj.get("tags"),
            "version": obj.get("version")
        })
        return _obj


