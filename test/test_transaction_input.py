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

from openapi_client.models.transaction_input import TransactionInput  # noqa: E501

class TestTransactionInput(unittest.TestCase):
    """TransactionInput unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TransactionInput:
        """Test TransactionInput
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TransactionInput`
        """
        model = TransactionInput()  # noqa: E501
        if include_optional:
            return TransactionInput(
                tx_inputs = [
                    null
                    ],
                tx_interval = openapi_client.models.transaction_input_tx_interval.TransactionInput_tx_interval(
                    from = 56, 
                    to = 56, )
            )
        else:
            return TransactionInput(
                tx_inputs = [
                    null
                    ],
                tx_interval = openapi_client.models.transaction_input_tx_interval.TransactionInput_tx_interval(
                    from = 56, 
                    to = 56, ),
        )
        """

    def testTransactionInput(self):
        """Test TransactionInput"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
