# coding: utf-8

"""
    

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from openapi_client.models.list_object_contract_header import ListObjectContractHeader  # noqa: E501

class TestListObjectContractHeader(unittest.TestCase):
    """ListObjectContractHeader unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ListObjectContractHeader:
        """Test ListObjectContractHeader
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ListObjectContractHeader`
        """
        model = ListObjectContractHeader()  # noqa: E501
        if include_optional:
            return ListObjectContractHeader(
                results = [
                    openapi_client.models.list_object_contract_header_results_inner.ListObject_ContractHeader_results_inner(
                        links = openapi_client.models.list_object_contract_header_results_inner_links.ListObject_ContractHeader_results_inner_links(
                            contract = '', 
                            transactions = '', ), 
                        resource = openapi_client.models.contract_header.ContractHeader(
                            block = openapi_client.models.block_header.BlockHeader(
                                block_header_hash = '', 
                                block_no = 0, 
                                slot_no = 0, ), 
                            continuations = '', 
                            contract_id = '98d601c9307dd43307cf68a03aad0086d4e07a789b66919ccf9f7f7676577eb7#1', 
                            metadata = {
                                'key' : null
                                }, 
                            role_token_minting_policy_id = '2ECB020842930cc01FFCCf', 
                            status = 'unsigned', 
                            tags = {
                                'key' : null
                                }, 
                            version = 'v1', ), )
                    ]
            )
        else:
            return ListObjectContractHeader(
                results = [
                    openapi_client.models.list_object_contract_header_results_inner.ListObject_ContractHeader_results_inner(
                        links = openapi_client.models.list_object_contract_header_results_inner_links.ListObject_ContractHeader_results_inner_links(
                            contract = '', 
                            transactions = '', ), 
                        resource = openapi_client.models.contract_header.ContractHeader(
                            block = openapi_client.models.block_header.BlockHeader(
                                block_header_hash = '', 
                                block_no = 0, 
                                slot_no = 0, ), 
                            continuations = '', 
                            contract_id = '98d601c9307dd43307cf68a03aad0086d4e07a789b66919ccf9f7f7676577eb7#1', 
                            metadata = {
                                'key' : null
                                }, 
                            role_token_minting_policy_id = '2ECB020842930cc01FFCCf', 
                            status = 'unsigned', 
                            tags = {
                                'key' : null
                                }, 
                            version = 'v1', ), )
                    ],
        )
        """

    def testListObjectContractHeader(self):
        """Test ListObjectContractHeader"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
