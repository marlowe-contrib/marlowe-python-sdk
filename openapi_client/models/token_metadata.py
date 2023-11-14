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
from pydantic import BaseModel, StrictStr
from pydantic import Field
from openapi_client.models.token_metadata_file import TokenMetadataFile
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class TokenMetadata(BaseModel):
    """
    Metadata for an NFT, as described by https://cips.cardano.org/cips/cip25/
    """ # noqa: E501
    description: Optional[StrictStr] = None
    files: Optional[List[TokenMetadataFile]] = None
    image: StrictStr
    media_type: Optional[StrictStr] = Field(default=None, alias="mediaType")
    name: StrictStr
    __properties: ClassVar[List[str]] = ["description", "files", "image", "mediaType", "name"]

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
        """Create an instance of TokenMetadata from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in files (list)
        _items = []
        if self.files:
            for _item in self.files:
                if _item:
                    _items.append(_item.to_dict())
            _dict['files'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of TokenMetadata from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "description": obj.get("description"),
            "files": [TokenMetadataFile.from_dict(_item) for _item in obj.get("files")] if obj.get("files") is not None else None,
            "image": obj.get("image"),
            "mediaType": obj.get("mediaType"),
            "name": obj.get("name")
        })
        return _obj


