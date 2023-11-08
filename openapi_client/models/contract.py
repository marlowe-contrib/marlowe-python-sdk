# coding: utf-8

"""
    

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
from inspect import getfullargspec
import json
import pprint
import re  # noqa: F401

from typing import Any, List, Optional
from pydantic import BaseModel, Field, StrictStr, ValidationError, validator
from typing import Union, Any, List, TYPE_CHECKING
from pydantic import StrictStr, Field

CONTRACT_ONE_OF_SCHEMAS = ["ContractOneOf", "ContractOneOf1", "ContractOneOf2", "ContractOneOf3", "ContractOneOf4", "str"]

class Contract(BaseModel):
    """
    Contract terms specified in Marlowe
    """
    # data type: str
    oneof_schema_1_validator: Optional[StrictStr] = Field(None, description="No more payments will be sent and the balance of the contract is 0.")
    # data type: ContractOneOf
    oneof_schema_2_validator: Optional[ContractOneOf] = None
    # data type: ContractOneOf1
    oneof_schema_3_validator: Optional[ContractOneOf1] = None
    # data type: ContractOneOf2
    oneof_schema_4_validator: Optional[ContractOneOf2] = None
    # data type: ContractOneOf3
    oneof_schema_5_validator: Optional[ContractOneOf3] = None
    # data type: ContractOneOf4
    oneof_schema_6_validator: Optional[ContractOneOf4] = None
    if TYPE_CHECKING:
        actual_instance: Union[ContractOneOf, ContractOneOf1, ContractOneOf2, ContractOneOf3, ContractOneOf4, str]
    else:
        actual_instance: Any
    one_of_schemas: List[str] = Field(CONTRACT_ONE_OF_SCHEMAS, const=True)

    class Config:
        validate_assignment = True

    def __init__(self, *args, **kwargs) -> None:
        if args:
            if len(args) > 1:
                raise ValueError("If a position argument is used, only 1 is allowed to set `actual_instance`")
            if kwargs:
                raise ValueError("If a position argument is used, keyword arguments cannot be used.")
            super().__init__(actual_instance=args[0])
        else:
            super().__init__(**kwargs)

    @validator('actual_instance')
    def actual_instance_must_validate_oneof(cls, v):
        instance = Contract.construct()
        error_messages = []
        match = 0
        # validate data type: str
        try:
            instance.oneof_schema_1_validator = v
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # validate data type: ContractOneOf
        if not isinstance(v, ContractOneOf):
            error_messages.append(f"Error! Input type `{type(v)}` is not `ContractOneOf`")
        else:
            match += 1
        # validate data type: ContractOneOf1
        if not isinstance(v, ContractOneOf1):
            error_messages.append(f"Error! Input type `{type(v)}` is not `ContractOneOf1`")
        else:
            match += 1
        # validate data type: ContractOneOf2
        if not isinstance(v, ContractOneOf2):
            error_messages.append(f"Error! Input type `{type(v)}` is not `ContractOneOf2`")
        else:
            match += 1
        # validate data type: ContractOneOf3
        if not isinstance(v, ContractOneOf3):
            error_messages.append(f"Error! Input type `{type(v)}` is not `ContractOneOf3`")
        else:
            match += 1
        # validate data type: ContractOneOf4
        if not isinstance(v, ContractOneOf4):
            error_messages.append(f"Error! Input type `{type(v)}` is not `ContractOneOf4`")
        else:
            match += 1
        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when setting `actual_instance` in Contract with oneOf schemas: ContractOneOf, ContractOneOf1, ContractOneOf2, ContractOneOf3, ContractOneOf4, str. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when setting `actual_instance` in Contract with oneOf schemas: ContractOneOf, ContractOneOf1, ContractOneOf2, ContractOneOf3, ContractOneOf4, str. Details: " + ", ".join(error_messages))
        else:
            return v

    @classmethod
    def from_dict(cls, obj: dict) -> Contract:
        return cls.from_json(json.dumps(obj))

    @classmethod
    def from_json(cls, json_str: str) -> Contract:
        """Returns the object represented by the json string"""
        instance = Contract.construct()
        error_messages = []
        match = 0

        # deserialize data into str
        try:
            # validation
            instance.oneof_schema_1_validator = json.loads(json_str)
            # assign value to actual_instance
            instance.actual_instance = instance.oneof_schema_1_validator
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into ContractOneOf
        try:
            instance.actual_instance = ContractOneOf.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into ContractOneOf1
        try:
            instance.actual_instance = ContractOneOf1.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into ContractOneOf2
        try:
            instance.actual_instance = ContractOneOf2.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into ContractOneOf3
        try:
            instance.actual_instance = ContractOneOf3.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into ContractOneOf4
        try:
            instance.actual_instance = ContractOneOf4.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))

        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when deserializing the JSON string into Contract with oneOf schemas: ContractOneOf, ContractOneOf1, ContractOneOf2, ContractOneOf3, ContractOneOf4, str. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when deserializing the JSON string into Contract with oneOf schemas: ContractOneOf, ContractOneOf1, ContractOneOf2, ContractOneOf3, ContractOneOf4, str. Details: " + ", ".join(error_messages))
        else:
            return instance

    def to_json(self) -> str:
        """Returns the JSON representation of the actual instance"""
        if self.actual_instance is None:
            return "null"

        to_json = getattr(self.actual_instance, "to_json", None)
        if callable(to_json):
            return self.actual_instance.to_json()
        else:
            return json.dumps(self.actual_instance)

    def to_dict(self) -> dict:
        """Returns the dict representation of the actual instance"""
        if self.actual_instance is None:
            return None

        to_dict = getattr(self.actual_instance, "to_dict", None)
        if callable(to_dict):
            return self.actual_instance.to_dict()
        else:
            # primitive type
            return self.actual_instance

    def to_str(self) -> str:
        """Returns the string representation of the actual instance"""
        return pprint.pformat(self.dict())

from openapi_client.models.contract_one_of import ContractOneOf
from openapi_client.models.contract_one_of1 import ContractOneOf1
from openapi_client.models.contract_one_of2 import ContractOneOf2
from openapi_client.models.contract_one_of3 import ContractOneOf3
from openapi_client.models.contract_one_of4 import ContractOneOf4
Contract.update_forward_refs()

