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
from pydantic import BaseModel, Field, StrictInt, StrictStr, ValidationError, validator
from openapi_client.models.action_object_one_of import ActionObjectOneOf
from openapi_client.models.value_object_one_of import ValueObjectOneOf
from openapi_client.models.value_object_one_of6 import ValueObjectOneOf6
from openapi_client.models.value_one_of7 import ValueOneOf7
from typing import Union, Any, List, TYPE_CHECKING
from pydantic import StrictStr, Field

VALUEOBJECT_ONE_OF_SCHEMAS = ["ActionObjectOneOf", "ValueObjectOneOf", "ValueObjectOneOf1", "ValueObjectOneOf2", "ValueObjectOneOf3", "ValueObjectOneOf4", "ValueObjectOneOf5", "ValueObjectOneOf6", "ValueObjectOneOf7", "ValueOneOf7", "int", "str"]

class ValueObject(BaseModel):
    """
    A time-varying expression that evaluates to a boolean
    """
    # data type: ValueObjectOneOf
    oneof_schema_1_validator: Optional[ValueObjectOneOf] = None
    # data type: int
    oneof_schema_2_validator: Optional[StrictInt] = None
    # data type: ValueObjectOneOf1
    oneof_schema_3_validator: Optional[ValueObjectOneOf1] = None
    # data type: ValueObjectOneOf2
    oneof_schema_4_validator: Optional[ValueObjectOneOf2] = None
    # data type: ValueObjectOneOf3
    oneof_schema_5_validator: Optional[ValueObjectOneOf3] = None
    # data type: ValueObjectOneOf4
    oneof_schema_6_validator: Optional[ValueObjectOneOf4] = None
    # data type: ValueObjectOneOf5
    oneof_schema_7_validator: Optional[ValueObjectOneOf5] = None
    # data type: ValueObjectOneOf6
    oneof_schema_8_validator: Optional[ValueObjectOneOf6] = None
    # data type: str
    oneof_schema_9_validator: Optional[StrictStr] = None
    # data type: ValueOneOf7
    oneof_schema_10_validator: Optional[ValueOneOf7] = None
    # data type: ValueObjectOneOf7
    oneof_schema_11_validator: Optional[ValueObjectOneOf7] = None
    # data type: ActionObjectOneOf
    oneof_schema_12_validator: Optional[ActionObjectOneOf] = None
    if TYPE_CHECKING:
        actual_instance: Union[ActionObjectOneOf, ValueObjectOneOf, ValueObjectOneOf1, ValueObjectOneOf2, ValueObjectOneOf3, ValueObjectOneOf4, ValueObjectOneOf5, ValueObjectOneOf6, ValueObjectOneOf7, ValueOneOf7, int, str]
    else:
        actual_instance: Any
    one_of_schemas: List[str] = Field(VALUEOBJECT_ONE_OF_SCHEMAS, const=True)

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
        instance = ValueObject.construct()
        error_messages = []
        match = 0
        # validate data type: ValueObjectOneOf
        if not isinstance(v, ValueObjectOneOf):
            error_messages.append(f"Error! Input type `{type(v)}` is not `ValueObjectOneOf`")
        else:
            match += 1
        # validate data type: int
        try:
            instance.oneof_schema_2_validator = v
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # validate data type: ValueObjectOneOf1
        if not isinstance(v, ValueObjectOneOf1):
            error_messages.append(f"Error! Input type `{type(v)}` is not `ValueObjectOneOf1`")
        else:
            match += 1
        # validate data type: ValueObjectOneOf2
        if not isinstance(v, ValueObjectOneOf2):
            error_messages.append(f"Error! Input type `{type(v)}` is not `ValueObjectOneOf2`")
        else:
            match += 1
        # validate data type: ValueObjectOneOf3
        if not isinstance(v, ValueObjectOneOf3):
            error_messages.append(f"Error! Input type `{type(v)}` is not `ValueObjectOneOf3`")
        else:
            match += 1
        # validate data type: ValueObjectOneOf4
        if not isinstance(v, ValueObjectOneOf4):
            error_messages.append(f"Error! Input type `{type(v)}` is not `ValueObjectOneOf4`")
        else:
            match += 1
        # validate data type: ValueObjectOneOf5
        if not isinstance(v, ValueObjectOneOf5):
            error_messages.append(f"Error! Input type `{type(v)}` is not `ValueObjectOneOf5`")
        else:
            match += 1
        # validate data type: ValueObjectOneOf6
        if not isinstance(v, ValueObjectOneOf6):
            error_messages.append(f"Error! Input type `{type(v)}` is not `ValueObjectOneOf6`")
        else:
            match += 1
        # validate data type: str
        try:
            instance.oneof_schema_9_validator = v
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # validate data type: ValueOneOf7
        if not isinstance(v, ValueOneOf7):
            error_messages.append(f"Error! Input type `{type(v)}` is not `ValueOneOf7`")
        else:
            match += 1
        # validate data type: ValueObjectOneOf7
        if not isinstance(v, ValueObjectOneOf7):
            error_messages.append(f"Error! Input type `{type(v)}` is not `ValueObjectOneOf7`")
        else:
            match += 1
        # validate data type: ActionObjectOneOf
        if not isinstance(v, ActionObjectOneOf):
            error_messages.append(f"Error! Input type `{type(v)}` is not `ActionObjectOneOf`")
        else:
            match += 1
        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when setting `actual_instance` in ValueObject with oneOf schemas: ActionObjectOneOf, ValueObjectOneOf, ValueObjectOneOf1, ValueObjectOneOf2, ValueObjectOneOf3, ValueObjectOneOf4, ValueObjectOneOf5, ValueObjectOneOf6, ValueObjectOneOf7, ValueOneOf7, int, str. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when setting `actual_instance` in ValueObject with oneOf schemas: ActionObjectOneOf, ValueObjectOneOf, ValueObjectOneOf1, ValueObjectOneOf2, ValueObjectOneOf3, ValueObjectOneOf4, ValueObjectOneOf5, ValueObjectOneOf6, ValueObjectOneOf7, ValueOneOf7, int, str. Details: " + ", ".join(error_messages))
        else:
            return v

    @classmethod
    def from_dict(cls, obj: dict) -> ValueObject:
        return cls.from_json(json.dumps(obj))

    @classmethod
    def from_json(cls, json_str: str) -> ValueObject:
        """Returns the object represented by the json string"""
        instance = ValueObject.construct()
        error_messages = []
        match = 0

        # deserialize data into ValueObjectOneOf
        try:
            instance.actual_instance = ValueObjectOneOf.from_json(json_str)
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
        # deserialize data into ValueObjectOneOf1
        try:
            instance.actual_instance = ValueObjectOneOf1.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into ValueObjectOneOf2
        try:
            instance.actual_instance = ValueObjectOneOf2.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into ValueObjectOneOf3
        try:
            instance.actual_instance = ValueObjectOneOf3.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into ValueObjectOneOf4
        try:
            instance.actual_instance = ValueObjectOneOf4.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into ValueObjectOneOf5
        try:
            instance.actual_instance = ValueObjectOneOf5.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into ValueObjectOneOf6
        try:
            instance.actual_instance = ValueObjectOneOf6.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into str
        try:
            # validation
            instance.oneof_schema_9_validator = json.loads(json_str)
            # assign value to actual_instance
            instance.actual_instance = instance.oneof_schema_9_validator
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into ValueOneOf7
        try:
            instance.actual_instance = ValueOneOf7.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into ValueObjectOneOf7
        try:
            instance.actual_instance = ValueObjectOneOf7.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into ActionObjectOneOf
        try:
            instance.actual_instance = ActionObjectOneOf.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))

        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when deserializing the JSON string into ValueObject with oneOf schemas: ActionObjectOneOf, ValueObjectOneOf, ValueObjectOneOf1, ValueObjectOneOf2, ValueObjectOneOf3, ValueObjectOneOf4, ValueObjectOneOf5, ValueObjectOneOf6, ValueObjectOneOf7, ValueOneOf7, int, str. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when deserializing the JSON string into ValueObject with oneOf schemas: ActionObjectOneOf, ValueObjectOneOf, ValueObjectOneOf1, ValueObjectOneOf2, ValueObjectOneOf3, ValueObjectOneOf4, ValueObjectOneOf5, ValueObjectOneOf6, ValueObjectOneOf7, ValueOneOf7, int, str. Details: " + ", ".join(error_messages))
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

from openapi_client.models.value_object_one_of1 import ValueObjectOneOf1
from openapi_client.models.value_object_one_of2 import ValueObjectOneOf2
from openapi_client.models.value_object_one_of3 import ValueObjectOneOf3
from openapi_client.models.value_object_one_of4 import ValueObjectOneOf4
from openapi_client.models.value_object_one_of5 import ValueObjectOneOf5
from openapi_client.models.value_object_one_of7 import ValueObjectOneOf7
ValueObject.update_forward_refs()
