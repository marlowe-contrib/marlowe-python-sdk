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

from openapi_client.models.staking_hash import StakingHash  # noqa: E501

class TestStakingHash(unittest.TestCase):
    """StakingHash unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> StakingHash:
        """Test StakingHash
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `StakingHash`
        """
        model = StakingHash()  # noqa: E501
        if include_optional:
            return StakingHash(
                staking_hash = None
            )
        else:
            return StakingHash(
                staking_hash = None,
        )
        """

    def testStakingHash(self):
        """Test StakingHash"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
