# coding: utf-8

"""
    Marlowe Runtime REST API

    REST API for Marlowe Runtime

    The version of the OpenAPI document: 0.0.5.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
from inspect import getfullargspec
import json
import pprint
import re  # noqa: F401

from typing import Any, List, Optional
from pydantic import BaseModel, Field, StrictInt, StrictStr, ValidationError, conlist, validator
from openapi_client.models.account_token_tuple_inner import AccountTokenTupleInner
from typing import Union, Any, List, TYPE_CHECKING
from pydantic import StrictStr, Field

MARLOWESTATEACCOUNTSINNERINNER_ONE_OF_SCHEMAS = ["List[AccountTokenTupleInner]", "int"]

class MarloweStateAccountsInnerInner(BaseModel):
    """
    MarloweStateAccountsInnerInner
    """
    # data type: List[AccountTokenTupleInner]
    oneof_schema_1_validator: Optional[conlist(AccountTokenTupleInner, max_items=2, min_items=2)] = None
    # data type: int
    oneof_schema_2_validator: Optional[StrictInt] = None
    if TYPE_CHECKING:
        actual_instance: Union[List[AccountTokenTupleInner], int]
    else:
        actual_instance: Any
    one_of_schemas: List[str] = Field(MARLOWESTATEACCOUNTSINNERINNER_ONE_OF_SCHEMAS, const=True)

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
        instance = MarloweStateAccountsInnerInner.construct()
        error_messages = []
        match = 0
        # validate data type: List[AccountTokenTupleInner]
        try:
            instance.oneof_schema_1_validator = v
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # validate data type: int
        try:
            instance.oneof_schema_2_validator = v
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when setting `actual_instance` in MarloweStateAccountsInnerInner with oneOf schemas: List[AccountTokenTupleInner], int. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when setting `actual_instance` in MarloweStateAccountsInnerInner with oneOf schemas: List[AccountTokenTupleInner], int. Details: " + ", ".join(error_messages))
        else:
            return v

    @classmethod
    def from_dict(cls, obj: dict) -> MarloweStateAccountsInnerInner:
        return cls.from_json(json.dumps(obj))

    @classmethod
    def from_json(cls, json_str: str) -> MarloweStateAccountsInnerInner:
        """Returns the object represented by the json string"""
        instance = MarloweStateAccountsInnerInner.construct()
        error_messages = []
        match = 0

        # deserialize data into List[AccountTokenTupleInner]
        try:
            # validation
            instance.oneof_schema_1_validator = json.loads(json_str)
            # assign value to actual_instance
            instance.actual_instance = instance.oneof_schema_1_validator
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into int
        try:
            # validation
            instance.oneof_schema_2_validator = json.loads(json_str)
            # assign value to actual_instance
            instance.actual_instance = instance.oneof_schema_2_validator
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))

        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when deserializing the JSON string into MarloweStateAccountsInnerInner with oneOf schemas: List[AccountTokenTupleInner], int. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when deserializing the JSON string into MarloweStateAccountsInnerInner with oneOf schemas: List[AccountTokenTupleInner], int. Details: " + ", ".join(error_messages))
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


