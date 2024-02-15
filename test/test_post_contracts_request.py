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

from openapi_client.models.post_contracts_request import PostContractsRequest  # noqa: E501

class TestPostContractsRequest(unittest.TestCase):
    """PostContractsRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PostContractsRequest:
        """Test PostContractsRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PostContractsRequest`
        """
        model = PostContractsRequest()  # noqa: E501
        if include_optional:
            return PostContractsRequest(
                contract = None,
                metadata = {
                    'key' : null
                    },
                min_utx_o_deposit = 0,
                roles = None,
                tags = {
                    'key' : null
                    },
                thread_token_name = '',
                version = 'v1'
            )
        else:
            return PostContractsRequest(
                contract = None,
                metadata = {
                    'key' : null
                    },
                tags = {
                    'key' : null
                    },
                version = 'v1',
        )
        """

    def testPostContractsRequest(self):
        """Test PostContractsRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
