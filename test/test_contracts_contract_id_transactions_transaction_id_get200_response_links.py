# coding: utf-8

"""
    

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from openapi_client.models.contracts_contract_id_transactions_transaction_id_get200_response_links import ContractsContractIdTransactionsTransactionIdGet200ResponseLinks  # noqa: E501

class TestContractsContractIdTransactionsTransactionIdGet200ResponseLinks(unittest.TestCase):
    """ContractsContractIdTransactionsTransactionIdGet200ResponseLinks unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ContractsContractIdTransactionsTransactionIdGet200ResponseLinks:
        """Test ContractsContractIdTransactionsTransactionIdGet200ResponseLinks
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ContractsContractIdTransactionsTransactionIdGet200ResponseLinks`
        """
        model = ContractsContractIdTransactionsTransactionIdGet200ResponseLinks()  # noqa: E501
        if include_optional:
            return ContractsContractIdTransactionsTransactionIdGet200ResponseLinks(
                next = '',
                previous = ''
            )
        else:
            return ContractsContractIdTransactionsTransactionIdGet200ResponseLinks(
        )
        """

    def testContractsContractIdTransactionsTransactionIdGet200ResponseLinks(self):
        """Test ContractsContractIdTransactionsTransactionIdGet200ResponseLinks"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
