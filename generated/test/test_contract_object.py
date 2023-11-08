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

from openapi_client.models.contract_object import ContractObject  # noqa: E501

class TestContractObject(unittest.TestCase):
    """ContractObject unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ContractObject:
        """Test ContractObject
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ContractObject`
        """
        model = ContractObject()  # noqa: E501
        if include_optional:
            return ContractObject(
                from_account = None,
                pay = None,
                then = None,
                to = None,
                token = None,
                var_else = None,
                var_if = None,
                timeout = 56,
                timeout_continuation = None,
                when = [
                    null
                    ],
                be = None,
                let = '',
                var_assert = None,
                ref = ''
            )
        else:
            return ContractObject(
                from_account = None,
                pay = None,
                then = None,
                to = None,
                token = None,
                var_else = None,
                var_if = None,
                timeout = 56,
                timeout_continuation = None,
                when = [
                    null
                    ],
                be = None,
                let = '',
                var_assert = None,
                ref = '',
        )
        """

    def testContractObject(self):
        """Test ContractObject"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
