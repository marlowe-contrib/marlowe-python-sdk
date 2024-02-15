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

from openapi_client.models.equal import Equal  # noqa: E501

class TestEqual(unittest.TestCase):
    """Equal unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Equal:
        """Test Equal
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Equal`
        """
        model = Equal()  # noqa: E501
        if include_optional:
            return Equal(
                equal_to = None,
                value = None
            )
        else:
            return Equal(
                equal_to = None,
                value = None,
        )
        """

    def testEqual(self):
        """Test Equal"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
