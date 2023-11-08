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

from openapi_client.models.transaction_warning_one_of import TransactionWarningOneOf  # noqa: E501

class TestTransactionWarningOneOf(unittest.TestCase):
    """TransactionWarningOneOf unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TransactionWarningOneOf:
        """Test TransactionWarningOneOf
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TransactionWarningOneOf`
        """
        model = TransactionWarningOneOf()  # noqa: E501
        if include_optional:
            return TransactionWarningOneOf(
                asked_to_deposit = 56,
                in_account = None,
                of_token = openapi_client.models.token.Token(
                    currency_symbol = '', 
                    token_name = '', ),
                party = None
            )
        else:
            return TransactionWarningOneOf(
                asked_to_deposit = 56,
                in_account = None,
                of_token = openapi_client.models.token.Token(
                    currency_symbol = '', 
                    token_name = '', ),
                party = None,
        )
        """

    def testTransactionWarningOneOf(self):
        """Test TransactionWarningOneOf"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
