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

from openapi_client.models.variable_shadowing import VariableShadowing  # noqa: E501

class TestVariableShadowing(unittest.TestCase):
    """VariableShadowing unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> VariableShadowing:
        """Test VariableShadowing
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `VariableShadowing`
        """
        model = VariableShadowing()  # noqa: E501
        if include_optional:
            return VariableShadowing(
                had_value = 56,
                is_now_assigned = 56,
                value_id = ''
            )
        else:
            return VariableShadowing(
                had_value = 56,
                is_now_assigned = 56,
                value_id = '',
        )
        """

    def testVariableShadowing(self):
        """Test VariableShadowing"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()