# coding: utf-8

"""
    Marlowe Runtime REST API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.0.5
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
from inspect import getfullargspec
import json
import pprint
import re  # noqa: F401

from typing import Any, List, Optional
from pydantic import BaseModel, Field, StrictStr, ValidationError, field_validator
from openapi_client.models.action_one_of import ActionOneOf
from openapi_client.models.action_one_of1 import ActionOneOf1
from openapi_client.models.action_one_of2 import ActionOneOf2
from openapi_client.models.value_object_one_of8 import ValueObjectOneOf8
from typing import Union, Any, List, TYPE_CHECKING, Optional, Dict
from typing_extensions import Literal
from pydantic import StrictStr, Field
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

ACTIONOBJECT_ONE_OF_SCHEMAS = ["ActionOneOf", "ActionOneOf1", "ActionOneOf2", "ValueObjectOneOf8"]

class ActionObject(BaseModel):
    """
    A contract which becomes active when an action occurs.
    """
    # data type: ActionOneOf
    oneof_schema_1_validator: Optional[ActionOneOf] = None
    # data type: ActionOneOf1
    oneof_schema_2_validator: Optional[ActionOneOf1] = None
    # data type: ActionOneOf2
    oneof_schema_3_validator: Optional[ActionOneOf2] = None
    # data type: ValueObjectOneOf8
    oneof_schema_4_validator: Optional[ValueObjectOneOf8] = None
    actual_instance: Optional[Union[ActionOneOf, ActionOneOf1, ActionOneOf2, ValueObjectOneOf8]] = None
    one_of_schemas: List[str] = Literal["ActionOneOf", "ActionOneOf1", "ActionOneOf2", "ValueObjectOneOf8"]

    model_config = {
        "validate_assignment": True
    }


    def __init__(self, *args, **kwargs) -> None:
        if args:
            if len(args) > 1:
                raise ValueError("If a position argument is used, only 1 is allowed to set `actual_instance`")
            if kwargs:
                raise ValueError("If a position argument is used, keyword arguments cannot be used.")
            super().__init__(actual_instance=args[0])
        else:
            super().__init__(**kwargs)

    @field_validator('actual_instance')
    def actual_instance_must_validate_oneof(cls, v):
        instance = ActionObject.model_construct()
        error_messages = []
        match = 0
        # validate data type: ActionOneOf
        if not isinstance(v, ActionOneOf):
            error_messages.append(f"Error! Input type `{type(v)}` is not `ActionOneOf`")
        else:
            match += 1
        # validate data type: ActionOneOf1
        if not isinstance(v, ActionOneOf1):
            error_messages.append(f"Error! Input type `{type(v)}` is not `ActionOneOf1`")
        else:
            match += 1
        # validate data type: ActionOneOf2
        if not isinstance(v, ActionOneOf2):
            error_messages.append(f"Error! Input type `{type(v)}` is not `ActionOneOf2`")
        else:
            match += 1
        # validate data type: ValueObjectOneOf8
        if not isinstance(v, ValueObjectOneOf8):
            error_messages.append(f"Error! Input type `{type(v)}` is not `ValueObjectOneOf8`")
        else:
            match += 1
        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when setting `actual_instance` in ActionObject with oneOf schemas: ActionOneOf, ActionOneOf1, ActionOneOf2, ValueObjectOneOf8. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when setting `actual_instance` in ActionObject with oneOf schemas: ActionOneOf, ActionOneOf1, ActionOneOf2, ValueObjectOneOf8. Details: " + ", ".join(error_messages))
        else:
            return v

    @classmethod
    def from_dict(cls, obj: dict) -> Self:
        return cls.from_json(json.dumps(obj))

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Returns the object represented by the json string"""
        instance = cls.model_construct()
        error_messages = []
        match = 0

        # deserialize data into ActionOneOf
        try:
            instance.actual_instance = ActionOneOf.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into ActionOneOf1
        try:
            instance.actual_instance = ActionOneOf1.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into ActionOneOf2
        try:
            instance.actual_instance = ActionOneOf2.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into ValueObjectOneOf8
        try:
            instance.actual_instance = ValueObjectOneOf8.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))

        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when deserializing the JSON string into ActionObject with oneOf schemas: ActionOneOf, ActionOneOf1, ActionOneOf2, ValueObjectOneOf8. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when deserializing the JSON string into ActionObject with oneOf schemas: ActionOneOf, ActionOneOf1, ActionOneOf2, ValueObjectOneOf8. Details: " + ", ".join(error_messages))
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

    def to_dict(self) -> Dict:
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
        return pprint.pformat(self.model_dump())


