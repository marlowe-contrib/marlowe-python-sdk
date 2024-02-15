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

from openapi_client.models.post_contracts_request_contract import PostContractsRequestContract  # noqa: E501

class TestPostContractsRequestContract(unittest.TestCase):
    """PostContractsRequestContract unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PostContractsRequestContract:
        """Test PostContractsRequestContract
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PostContractsRequestContract`
        """
        model = PostContractsRequestContract()  # noqa: E501
        if include_optional:
            return PostContractsRequestContract(
                from_account = None,
                pay = None,
                then = None,
                to = None,
                token = openapi_client.models.token.Token(
                    currency_symbol = '', 
                    token_name = '', ),
                var_else = None,
                var_if = None,
                timeout = 56,
                timeout_continuation = None,
                when = [
                    null
                    ],
                be = None,
                let = '',
                var_assert = None
            )
        else:
            return PostContractsRequestContract(
                from_account = None,
                pay = None,
                then = None,
                to = None,
                token = openapi_client.models.token.Token(
                    currency_symbol = '', 
                    token_name = '', ),
                var_else = None,
                var_if = None,
                timeout = 56,
                timeout_continuation = None,
                when = [
                    null
                    ],
                be = None,
                let = '',
                var_assert = None,
        )
        """

    def testPostContractsRequestContract(self):
        """Test PostContractsRequestContract"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
