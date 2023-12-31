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


from typing import Union
from pydantic import BaseModel, Field, StrictFloat, StrictInt

class ExBudget(BaseModel):
    """
    ExBudget
    """
    ex_budget_cpu: Union[StrictFloat, StrictInt] = Field(..., alias="exBudgetCPU")
    ex_budget_memory: Union[StrictFloat, StrictInt] = Field(..., alias="exBudgetMemory")
    __properties = ["exBudgetCPU", "exBudgetMemory"]

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
    def from_json(cls, json_str: str) -> ExBudget:
        """Create an instance of ExBudget from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ExBudget:
        """Create an instance of ExBudget from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ExBudget.parse_obj(obj)

        _obj = ExBudget.parse_obj({
            "ex_budget_cpu": obj.get("exBudgetCPU"),
            "ex_budget_memory": obj.get("exBudgetMemory")
        })
        return _obj


