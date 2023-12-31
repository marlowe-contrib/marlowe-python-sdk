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

from openapi_client.models.marlowe_state_accounts_inner_inner_one_of_inner import MarloweStateAccountsInnerInnerOneOfInner  # noqa: E501

class TestMarloweStateAccountsInnerInnerOneOfInner(unittest.TestCase):
    """MarloweStateAccountsInnerInnerOneOfInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> MarloweStateAccountsInnerInnerOneOfInner:
        """Test MarloweStateAccountsInnerInnerOneOfInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `MarloweStateAccountsInnerInnerOneOfInner`
        """
        model = MarloweStateAccountsInnerInnerOneOfInner()  # noqa: E501
        if include_optional:
            return MarloweStateAccountsInnerInnerOneOfInner(
                role_token = '',
                address = 'addr1w94f8ywk4fg672xasahtk4t9k6w3aql943uxz5rt62d4dvq8evxaf',
                currency_symbol = '',
                token_name = ''
            )
        else:
            return MarloweStateAccountsInnerInnerOneOfInner(
                role_token = '',
                address = 'addr1w94f8ywk4fg672xasahtk4t9k6w3aql943uxz5rt62d4dvq8evxaf',
                currency_symbol = '',
                token_name = '',
        )
        """

    def testMarloweStateAccountsInnerInnerOneOfInner(self):
        """Test MarloweStateAccountsInnerInnerOneOfInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
