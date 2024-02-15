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

from openapi_client.models.create_contract_response_links import CreateContractResponseLinks  # noqa: E501

class TestCreateContractResponseLinks(unittest.TestCase):
    """CreateContractResponseLinks unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CreateContractResponseLinks:
        """Test CreateContractResponseLinks
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CreateContractResponseLinks`
        """
        model = CreateContractResponseLinks()  # noqa: E501
        if include_optional:
            return CreateContractResponseLinks(
                contract = ''
            )
        else:
            return CreateContractResponseLinks(
        )
        """

    def testCreateContractResponseLinks(self):
        """Test CreateContractResponseLinks"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
