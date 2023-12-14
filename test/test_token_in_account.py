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

from openapi_client.models.token_in_account import TokenInAccount  # noqa: E501

class TestTokenInAccount(unittest.TestCase):
    """TokenInAccount unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TokenInAccount:
        """Test TokenInAccount
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TokenInAccount`
        """
        model = TokenInAccount()  # noqa: E501
        if include_optional:
            return TokenInAccount(
                amount_of_token = openapi_client.models.token.Token(
                    currency_symbol = '', 
                    token_name = '', ),
                in_account = None
            )
        else:
            return TokenInAccount(
                amount_of_token = openapi_client.models.token.Token(
                    currency_symbol = '', 
                    token_name = '', ),
                in_account = None,
        )
        """

    def testTokenInAccount(self):
        """Test TokenInAccount"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
