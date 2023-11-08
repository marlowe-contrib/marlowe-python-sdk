# coding: utf-8

"""
    Marlowe Runtime REST API

    REST API for Marlowe Runtime

    The version of the OpenAPI document: 0.0.5.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import json
import pprint
import re  # noqa: F401
from aenum import Enum, no_arg





class PayoutStatus(str, Enum):
    """
    The status of a payout. Either it is available to be withdrawn, or it has already been withdrawn.
    """

    """
    allowed enum values
    """
    AVAILABLE = 'available'
    WITHDRAWN = 'withdrawn'

    @classmethod
    def from_json(cls, json_str: str) -> PayoutStatus:
        """Create an instance of PayoutStatus from a JSON string"""
        return PayoutStatus(json.loads(json_str))


