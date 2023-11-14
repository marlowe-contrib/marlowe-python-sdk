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
from pydantic import BaseModel, StrictStr
from openapi_client.models.value_object import ValueObject
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class ContractObjectOneOf3(BaseModel):
    """
    Bind a value to a name within the scope of a sub-contract.
    """ # noqa: E501
    be: ValueObject
    let: StrictStr
    then: ContractObject
    __properties: ClassVar[List[str]] = ["be", "let", "then"]

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
        """Create an instance of ContractObjectOneOf3 from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of be
        if self.be:
            _dict['be'] = self.be.to_dict()
        # override the default output from pydantic by calling `to_dict()` of then
        if self.then:
            _dict['then'] = self.then.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of ContractObjectOneOf3 from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "be": ValueObject.from_dict(obj.get("be")) if obj.get("be") is not None else None,
            "let": obj.get("let"),
            "then": ContractObject.from_dict(obj.get("then")) if obj.get("then") is not None else None
        })
        return _obj

from openapi_client.models.contract_object import ContractObject
# TODO: Rewrite to not use raise_errors
ContractObjectOneOf3.model_rebuild(raise_errors=False)

