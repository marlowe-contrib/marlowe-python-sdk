# coding: utf-8

"""
    Marlowe Runtime REST API

    REST API for Marlowe Runtime

    The version of the OpenAPI document: 0.0.5.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from openapi_client.models.value_object_one_of3 import ValueObjectOneOf3  # noqa: E501

class TestValueObjectOneOf3(unittest.TestCase):
    """ValueObjectOneOf3 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ValueObjectOneOf3:
        """Test ValueObjectOneOf3
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ValueObjectOneOf3`
        """
        model = ValueObjectOneOf3()  # noqa: E501
        if include_optional:
            return ValueObjectOneOf3(
                minus = None,
                value = None
            )
        else:
            return ValueObjectOneOf3(
                minus = None,
                value = None,
        )
        """

    def testValueObjectOneOf3(self):
        """Test ValueObjectOneOf3"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()