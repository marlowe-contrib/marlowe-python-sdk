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



from pydantic import BaseModel, Field, StrictStr

class TextEnvelope(BaseModel):
    """
    TextEnvelope
    """
    cbor_hex: StrictStr = Field(..., alias="cborHex")
    description: StrictStr = Field(...)
    type: StrictStr = Field(..., description="What type of data is encoded in the CBOR Hex. Valid values include \"Tx <era>\", \"TxBody <era>\", and \"ShelleyTxWitness <era>\" where <era> is one of \"BabbageEra\", \"ConwayEra\".")
    __properties = ["cborHex", "description", "type"]

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
    def from_json(cls, json_str: str) -> TextEnvelope:
        """Create an instance of TextEnvelope from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> TextEnvelope:
        """Create an instance of TextEnvelope from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return TextEnvelope.parse_obj(obj)

        _obj = TextEnvelope.parse_obj({
            "cbor_hex": obj.get("cborHex"),
            "description": obj.get("description"),
            "type": obj.get("type")
        })
        return _obj


