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

from openapi_client.models.case_merkleized_then_object import CaseMerkleizedThenObject  # noqa: E501

class TestCaseMerkleizedThenObject(unittest.TestCase):
    """CaseMerkleizedThenObject unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CaseMerkleizedThenObject:
        """Test CaseMerkleizedThenObject
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CaseMerkleizedThenObject`
        """
        model = CaseMerkleizedThenObject()  # noqa: E501
        if include_optional:
            return CaseMerkleizedThenObject(
                case = None,
                merkleized_then = ''
            )
        else:
            return CaseMerkleizedThenObject(
                case = None,
                merkleized_then = '',
        )
        """

    def testCaseMerkleizedThenObject(self):
        """Test CaseMerkleizedThenObject"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
