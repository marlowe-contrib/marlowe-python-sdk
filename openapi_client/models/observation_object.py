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
from pydantic import BaseModel, Field, StrictBool, StrictStr, ValidationError, field_validator
from openapi_client.models.observation_object_one_of3 import ObservationObjectOneOf3
from openapi_client.models.value_object_one_of8 import ValueObjectOneOf8
from typing import Union, Any, List, TYPE_CHECKING, Optional, Dict
from typing_extensions import Literal
from pydantic import StrictStr, Field
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

OBSERVATIONOBJECT_ONE_OF_SCHEMAS = ["ObservationObjectOneOf", "ObservationObjectOneOf1", "ObservationObjectOneOf2", "ObservationObjectOneOf3", "ObservationObjectOneOf4", "ObservationObjectOneOf5", "ObservationObjectOneOf6", "ObservationObjectOneOf7", "ObservationObjectOneOf8", "ValueObjectOneOf8", "bool"]

class ObservationObject(BaseModel):
    """
    A time-varying expression that evaluates to an integer
    """
    # data type: bool
    oneof_schema_1_validator: Optional[StrictBool] = None
    # data type: ObservationObjectOneOf
    oneof_schema_2_validator: Optional[ObservationObjectOneOf] = None
    # data type: ObservationObjectOneOf1
    oneof_schema_3_validator: Optional[ObservationObjectOneOf1] = None
    # data type: ObservationObjectOneOf2
    oneof_schema_4_validator: Optional[ObservationObjectOneOf2] = None
    # data type: ObservationObjectOneOf3
    oneof_schema_5_validator: Optional[ObservationObjectOneOf3] = None
    # data type: ObservationObjectOneOf4
    oneof_schema_6_validator: Optional[ObservationObjectOneOf4] = None
    # data type: ObservationObjectOneOf5
    oneof_schema_7_validator: Optional[ObservationObjectOneOf5] = None
    # data type: ObservationObjectOneOf6
    oneof_schema_8_validator: Optional[ObservationObjectOneOf6] = None
    # data type: ObservationObjectOneOf7
    oneof_schema_9_validator: Optional[ObservationObjectOneOf7] = None
    # data type: ObservationObjectOneOf8
    oneof_schema_10_validator: Optional[ObservationObjectOneOf8] = None
    # data type: ValueObjectOneOf8
    oneof_schema_11_validator: Optional[ValueObjectOneOf8] = None
    actual_instance: Optional[Union[ObservationObjectOneOf, ObservationObjectOneOf1, ObservationObjectOneOf2, ObservationObjectOneOf3, ObservationObjectOneOf4, ObservationObjectOneOf5, ObservationObjectOneOf6, ObservationObjectOneOf7, ObservationObjectOneOf8, ValueObjectOneOf8, bool]] = None
    one_of_schemas: List[str] = Literal["ObservationObjectOneOf", "ObservationObjectOneOf1", "ObservationObjectOneOf2", "ObservationObjectOneOf3", "ObservationObjectOneOf4", "ObservationObjectOneOf5", "ObservationObjectOneOf6", "ObservationObjectOneOf7", "ObservationObjectOneOf8", "ValueObjectOneOf8", "bool"]

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
        instance = ObservationObject.model_construct()
        error_messages = []
        match = 0
        # validate data type: bool
        try:
            instance.oneof_schema_1_validator = v
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # validate data type: ObservationObjectOneOf
        if not isinstance(v, ObservationObjectOneOf):
            error_messages.append(f"Error! Input type `{type(v)}` is not `ObservationObjectOneOf`")
        else:
            match += 1
        # validate data type: ObservationObjectOneOf1
        if not isinstance(v, ObservationObjectOneOf1):
            error_messages.append(f"Error! Input type `{type(v)}` is not `ObservationObjectOneOf1`")
        else:
            match += 1
        # validate data type: ObservationObjectOneOf2
        if not isinstance(v, ObservationObjectOneOf2):
            error_messages.append(f"Error! Input type `{type(v)}` is not `ObservationObjectOneOf2`")
        else:
            match += 1
        # validate data type: ObservationObjectOneOf3
        if not isinstance(v, ObservationObjectOneOf3):
            error_messages.append(f"Error! Input type `{type(v)}` is not `ObservationObjectOneOf3`")
        else:
            match += 1
        # validate data type: ObservationObjectOneOf4
        if not isinstance(v, ObservationObjectOneOf4):
            error_messages.append(f"Error! Input type `{type(v)}` is not `ObservationObjectOneOf4`")
        else:
            match += 1
        # validate data type: ObservationObjectOneOf5
        if not isinstance(v, ObservationObjectOneOf5):
            error_messages.append(f"Error! Input type `{type(v)}` is not `ObservationObjectOneOf5`")
        else:
            match += 1
        # validate data type: ObservationObjectOneOf6
        if not isinstance(v, ObservationObjectOneOf6):
            error_messages.append(f"Error! Input type `{type(v)}` is not `ObservationObjectOneOf6`")
        else:
            match += 1
        # validate data type: ObservationObjectOneOf7
        if not isinstance(v, ObservationObjectOneOf7):
            error_messages.append(f"Error! Input type `{type(v)}` is not `ObservationObjectOneOf7`")
        else:
            match += 1
        # validate data type: ObservationObjectOneOf8
        if not isinstance(v, ObservationObjectOneOf8):
            error_messages.append(f"Error! Input type `{type(v)}` is not `ObservationObjectOneOf8`")
        else:
            match += 1
        # validate data type: ValueObjectOneOf8
        if not isinstance(v, ValueObjectOneOf8):
            error_messages.append(f"Error! Input type `{type(v)}` is not `ValueObjectOneOf8`")
        else:
            match += 1
        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when setting `actual_instance` in ObservationObject with oneOf schemas: ObservationObjectOneOf, ObservationObjectOneOf1, ObservationObjectOneOf2, ObservationObjectOneOf3, ObservationObjectOneOf4, ObservationObjectOneOf5, ObservationObjectOneOf6, ObservationObjectOneOf7, ObservationObjectOneOf8, ValueObjectOneOf8, bool. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when setting `actual_instance` in ObservationObject with oneOf schemas: ObservationObjectOneOf, ObservationObjectOneOf1, ObservationObjectOneOf2, ObservationObjectOneOf3, ObservationObjectOneOf4, ObservationObjectOneOf5, ObservationObjectOneOf6, ObservationObjectOneOf7, ObservationObjectOneOf8, ValueObjectOneOf8, bool. Details: " + ", ".join(error_messages))
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

        # deserialize data into bool
        try:
            # validation
            instance.oneof_schema_1_validator = json.loads(json_str)
            # assign value to actual_instance
            instance.actual_instance = instance.oneof_schema_1_validator
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into ObservationObjectOneOf
        try:
            instance.actual_instance = ObservationObjectOneOf.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into ObservationObjectOneOf1
        try:
            instance.actual_instance = ObservationObjectOneOf1.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into ObservationObjectOneOf2
        try:
            instance.actual_instance = ObservationObjectOneOf2.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into ObservationObjectOneOf3
        try:
            instance.actual_instance = ObservationObjectOneOf3.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into ObservationObjectOneOf4
        try:
            instance.actual_instance = ObservationObjectOneOf4.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into ObservationObjectOneOf5
        try:
            instance.actual_instance = ObservationObjectOneOf5.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into ObservationObjectOneOf6
        try:
            instance.actual_instance = ObservationObjectOneOf6.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into ObservationObjectOneOf7
        try:
            instance.actual_instance = ObservationObjectOneOf7.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into ObservationObjectOneOf8
        try:
            instance.actual_instance = ObservationObjectOneOf8.from_json(json_str)
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
            raise ValueError("Multiple matches found when deserializing the JSON string into ObservationObject with oneOf schemas: ObservationObjectOneOf, ObservationObjectOneOf1, ObservationObjectOneOf2, ObservationObjectOneOf3, ObservationObjectOneOf4, ObservationObjectOneOf5, ObservationObjectOneOf6, ObservationObjectOneOf7, ObservationObjectOneOf8, ValueObjectOneOf8, bool. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when deserializing the JSON string into ObservationObject with oneOf schemas: ObservationObjectOneOf, ObservationObjectOneOf1, ObservationObjectOneOf2, ObservationObjectOneOf3, ObservationObjectOneOf4, ObservationObjectOneOf5, ObservationObjectOneOf6, ObservationObjectOneOf7, ObservationObjectOneOf8, ValueObjectOneOf8, bool. Details: " + ", ".join(error_messages))
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

from openapi_client.models.observation_object_one_of import ObservationObjectOneOf
from openapi_client.models.observation_object_one_of1 import ObservationObjectOneOf1
from openapi_client.models.observation_object_one_of2 import ObservationObjectOneOf2
from openapi_client.models.observation_object_one_of4 import ObservationObjectOneOf4
from openapi_client.models.observation_object_one_of5 import ObservationObjectOneOf5
from openapi_client.models.observation_object_one_of6 import ObservationObjectOneOf6
from openapi_client.models.observation_object_one_of7 import ObservationObjectOneOf7
from openapi_client.models.observation_object_one_of8 import ObservationObjectOneOf8
# TODO: Rewrite to not use raise_errors
ObservationObject.model_rebuild(raise_errors=False)

