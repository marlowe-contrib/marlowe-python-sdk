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

from openapi_client.models.payee_object import PayeeObject  # noqa: E501

class TestPayeeObject(unittest.TestCase):
    """PayeeObject unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PayeeObject:
        """Test PayeeObject
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PayeeObject`
        """
        model = PayeeObject()  # noqa: E501
        if include_optional:
            return PayeeObject(
                account = None,
                party = None
            )
        else:
            return PayeeObject(
                account = None,
                party = None,
        )
        """

    def testPayeeObject(self):
        """Test PayeeObject"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
