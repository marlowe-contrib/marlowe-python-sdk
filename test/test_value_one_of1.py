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

from openapi_client.models.value_one_of1 import ValueOneOf1  # noqa: E501

class TestValueOneOf1(unittest.TestCase):
    """ValueOneOf1 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ValueOneOf1:
        """Test ValueOneOf1
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ValueOneOf1`
        """
        model = ValueOneOf1()  # noqa: E501
        if include_optional:
            return ValueOneOf1(
                negate = None
            )
        else:
            return ValueOneOf1(
                negate = None,
        )
        """

    def testValueOneOf1(self):
        """Test ValueOneOf1"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()