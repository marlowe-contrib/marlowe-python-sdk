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

from openapi_client.models.get_withdrawals_response_results_inner import GetWithdrawalsResponseResultsInner  # noqa: E501

class TestGetWithdrawalsResponseResultsInner(unittest.TestCase):
    """GetWithdrawalsResponseResultsInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetWithdrawalsResponseResultsInner:
        """Test GetWithdrawalsResponseResultsInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetWithdrawalsResponseResultsInner`
        """
        model = GetWithdrawalsResponseResultsInner()  # noqa: E501
        if include_optional:
            return GetWithdrawalsResponseResultsInner(
                links = openapi_client.models.get_withdrawals_response_results_inner_links.GetWithdrawalsResponse_results_inner_links(
                    withdrawal = '', ),
                resource = openapi_client.models.withdrawal_header.WithdrawalHeader(
                    block = openapi_client.models.block_header.BlockHeader(
                        block_header_hash = '', 
                        block_no = 0, 
                        slot_no = 0, ), 
                    status = 'unsigned', 
                    withdrawal_id = '62ECB020842930cc01FFCCfeEe150AC32DcAEc8a83DDD7dBF7567C88195ffcea', )
            )
        else:
            return GetWithdrawalsResponseResultsInner(
                links = openapi_client.models.get_withdrawals_response_results_inner_links.GetWithdrawalsResponse_results_inner_links(
                    withdrawal = '', ),
                resource = openapi_client.models.withdrawal_header.WithdrawalHeader(
                    block = openapi_client.models.block_header.BlockHeader(
                        block_header_hash = '', 
                        block_no = 0, 
                        slot_no = 0, ), 
                    status = 'unsigned', 
                    withdrawal_id = '62ECB020842930cc01FFCCfeEe150AC32DcAEc8a83DDD7dBF7567C88195ffcea', ),
        )
        """

    def testGetWithdrawalsResponseResultsInner(self):
        """Test GetWithdrawalsResponseResultsInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
