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

from openapi_client.models.contract_object_one_of2 import ContractObjectOneOf2  # noqa: E501

class TestContractObjectOneOf2(unittest.TestCase):
    """ContractObjectOneOf2 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ContractObjectOneOf2:
        """Test ContractObjectOneOf2
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ContractObjectOneOf2`
        """
        model = ContractObjectOneOf2()  # noqa: E501
        if include_optional:
            return ContractObjectOneOf2(
                timeout = 56,
                timeout_continuation = None,
                when = [
                    null
                    ]
            )
        else:
            return ContractObjectOneOf2(
                timeout = 56,
                timeout_continuation = None,
                when = [
                    null
                    ],
        )
        """

    def testContractObjectOneOf2(self):
        """Test ContractObjectOneOf2"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()