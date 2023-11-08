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

from openapi_client.models.contract_header import ContractHeader  # noqa: E501

class TestContractHeader(unittest.TestCase):
    """ContractHeader unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ContractHeader:
        """Test ContractHeader
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ContractHeader`
        """
        model = ContractHeader()  # noqa: E501
        if include_optional:
            return ContractHeader(
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
                version = 'v1'
            )
        else:
            return ContractHeader(
                contract_id = '98d601c9307dd43307cf68a03aad0086d4e07a789b66919ccf9f7f7676577eb7#1',
                metadata = {
                    'key' : null
                    },
                role_token_minting_policy_id = '2ECB020842930cc01FFCCf',
                status = 'unsigned',
                tags = {
                    'key' : null
                    },
                version = 'v1',
        )
        """

    def testContractHeader(self):
        """Test ContractHeader"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
