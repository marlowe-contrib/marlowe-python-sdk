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

from openapi_client.models.contract_one_of4 import ContractOneOf4  # noqa: E501

class TestContractOneOf4(unittest.TestCase):
    """ContractOneOf4 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ContractOneOf4:
        """Test ContractOneOf4
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ContractOneOf4`
        """
        model = ContractOneOf4()  # noqa: E501
        if include_optional:
            return ContractOneOf4(
                var_assert = None,
                then = None
            )
        else:
            return ContractOneOf4(
                var_assert = None,
                then = None,
        )
        """

    def testContractOneOf4(self):
        """Test ContractOneOf4"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()