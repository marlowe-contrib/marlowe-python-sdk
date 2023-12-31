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

from openapi_client.models.post_transactions_request import PostTransactionsRequest  # noqa: E501

class TestPostTransactionsRequest(unittest.TestCase):
    """PostTransactionsRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PostTransactionsRequest:
        """Test PostTransactionsRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PostTransactionsRequest`
        """
        model = PostTransactionsRequest()  # noqa: E501
        if include_optional:
            return PostTransactionsRequest(
                inputs = [
                    null
                    ],
                invalid_before = '2016-07-22T00:00:00Z',
                invalid_hereafter = '2016-07-22T00:00:00Z',
                metadata = {
                    'key' : null
                    },
                tags = {
                    'key' : null
                    },
                version = 'v1'
            )
        else:
            return PostTransactionsRequest(
                inputs = [
                    null
                    ],
                metadata = {
                    'key' : null
                    },
                tags = {
                    'key' : null
                    },
                version = 'v1',
        )
        """

    def testPostTransactionsRequest(self):
        """Test PostTransactionsRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
