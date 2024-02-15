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

from openapi_client.models.let_object import LetObject  # noqa: E501

class TestLetObject(unittest.TestCase):
    """LetObject unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> LetObject:
        """Test LetObject
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `LetObject`
        """
        model = LetObject()  # noqa: E501
        if include_optional:
            return LetObject(
                be = None,
                let = '',
                then = None
            )
        else:
            return LetObject(
                be = None,
                let = '',
                then = None,
        )
        """

    def testLetObject(self):
        """Test LetObject"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
