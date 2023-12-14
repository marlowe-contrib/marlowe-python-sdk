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

from openapi_client.models.partial_payment import PartialPayment  # noqa: E501

class TestPartialPayment(unittest.TestCase):
    """PartialPayment unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PartialPayment:
        """Test PartialPayment
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PartialPayment`
        """
        model = PartialPayment()  # noqa: E501
        if include_optional:
            return PartialPayment(
                account = None,
                asked_to_pay = 56,
                but_only_paid = 56,
                of_token = openapi_client.models.token.Token(
                    currency_symbol = '', 
                    token_name = '', ),
                to_payee = None
            )
        else:
            return PartialPayment(
                account = None,
                asked_to_pay = 56,
                but_only_paid = 56,
                of_token = openapi_client.models.token.Token(
                    currency_symbol = '', 
                    token_name = '', ),
                to_payee = None,
        )
        """

    def testPartialPayment(self):
        """Test PartialPayment"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
