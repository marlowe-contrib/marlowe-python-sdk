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

from openapi_client.models.value_one_of3 import ValueOneOf3  # noqa: E501

class TestValueOneOf3(unittest.TestCase):
    """ValueOneOf3 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ValueOneOf3:
        """Test ValueOneOf3
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ValueOneOf3`
        """
        model = ValueOneOf3()  # noqa: E501
        if include_optional:
            return ValueOneOf3(
                minus = None,
                value = None
            )
        else:
            return ValueOneOf3(
                minus = None,
                value = None,
        )
        """

    def testValueOneOf3(self):
        """Test ValueOneOf3"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
