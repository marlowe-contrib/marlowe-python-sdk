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

from openapi_client.models.contract_object_one_of3 import ContractObjectOneOf3  # noqa: E501

class TestContractObjectOneOf3(unittest.TestCase):
    """ContractObjectOneOf3 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ContractObjectOneOf3:
        """Test ContractObjectOneOf3
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ContractObjectOneOf3`
        """
        model = ContractObjectOneOf3()  # noqa: E501
        if include_optional:
            return ContractObjectOneOf3(
                be = None,
                let = '',
                then = None
            )
        else:
            return ContractObjectOneOf3(
                be = None,
                let = '',
                then = None,
        )
        """

    def testContractObjectOneOf3(self):
        """Test ContractObjectOneOf3"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
