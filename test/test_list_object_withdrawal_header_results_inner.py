# coding: utf-8

"""
    

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from openapi_client.models.list_object_withdrawal_header_results_inner import ListObjectWithdrawalHeaderResultsInner  # noqa: E501

class TestListObjectWithdrawalHeaderResultsInner(unittest.TestCase):
    """ListObjectWithdrawalHeaderResultsInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ListObjectWithdrawalHeaderResultsInner:
        """Test ListObjectWithdrawalHeaderResultsInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ListObjectWithdrawalHeaderResultsInner`
        """
        model = ListObjectWithdrawalHeaderResultsInner()  # noqa: E501
        if include_optional:
            return ListObjectWithdrawalHeaderResultsInner(
                links = openapi_client.models._withdrawals_post_201_response_links._withdrawals_post_201_response_links(
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
            return ListObjectWithdrawalHeaderResultsInner(
                links = openapi_client.models._withdrawals_post_201_response_links._withdrawals_post_201_response_links(
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

    def testListObjectWithdrawalHeaderResultsInner(self):
        """Test ListObjectWithdrawalHeaderResultsInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
