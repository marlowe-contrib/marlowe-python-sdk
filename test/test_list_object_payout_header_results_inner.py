# coding: utf-8

"""
    

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from openapi_client.models.list_object_payout_header_results_inner import ListObjectPayoutHeaderResultsInner  # noqa: E501

class TestListObjectPayoutHeaderResultsInner(unittest.TestCase):
    """ListObjectPayoutHeaderResultsInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ListObjectPayoutHeaderResultsInner:
        """Test ListObjectPayoutHeaderResultsInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ListObjectPayoutHeaderResultsInner`
        """
        model = ListObjectPayoutHeaderResultsInner()  # noqa: E501
        if include_optional:
            return ListObjectPayoutHeaderResultsInner(
                links = openapi_client.models.list_object_payout_header_results_inner_links.ListObject_PayoutHeader_results_inner_links(
                    payout = '', ),
                resource = openapi_client.models.payout_header.PayoutHeader(
                    contract_id = '98d601c9307dd43307cf68a03aad0086d4e07a789b66919ccf9f7f7676577eb7#1', 
                    payout_id = '98d601c9307dd43307cf68a03aad0086d4e07a789b66919ccf9f7f7676577eb7#1', 
                    role = openapi_client.models.asset_id.AssetId(
                        asset_name = '', 
                        policy_id = '2ECB020842930cc01FFCCf', ), 
                    status = 'available', 
                    withdrawal_id = '62ECB020842930cc01FFCCfeEe150AC32DcAEc8a83DDD7dBF7567C88195ffcea', )
            )
        else:
            return ListObjectPayoutHeaderResultsInner(
                links = openapi_client.models.list_object_payout_header_results_inner_links.ListObject_PayoutHeader_results_inner_links(
                    payout = '', ),
                resource = openapi_client.models.payout_header.PayoutHeader(
                    contract_id = '98d601c9307dd43307cf68a03aad0086d4e07a789b66919ccf9f7f7676577eb7#1', 
                    payout_id = '98d601c9307dd43307cf68a03aad0086d4e07a789b66919ccf9f7f7676577eb7#1', 
                    role = openapi_client.models.asset_id.AssetId(
                        asset_name = '', 
                        policy_id = '2ECB020842930cc01FFCCf', ), 
                    status = 'available', 
                    withdrawal_id = '62ECB020842930cc01FFCCfeEe150AC32DcAEc8a83DDD7dBF7567C88195ffcea', ),
        )
        """

    def testListObjectPayoutHeaderResultsInner(self):
        """Test ListObjectPayoutHeaderResultsInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()