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

from openapi_client.models.role_token_config_one_of1 import RoleTokenConfigOneOf1  # noqa: E501

class TestRoleTokenConfigOneOf1(unittest.TestCase):
    """RoleTokenConfigOneOf1 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RoleTokenConfigOneOf1:
        """Test RoleTokenConfigOneOf1
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RoleTokenConfigOneOf1`
        """
        model = RoleTokenConfigOneOf1()  # noqa: E501
        if include_optional:
            return RoleTokenConfigOneOf1(
                metadata = openapi_client.models.token_metadata.TokenMetadata(
                    description = '', 
                    files = [
                        openapi_client.models.token_metadata_file.TokenMetadataFile(
                            media_type = '', 
                            name = '', 
                            src = '', )
                        ], 
                    image = '', 
                    media_type = '', 
                    name = '', ),
                script = 'ThreadRole'
            )
        else:
            return RoleTokenConfigOneOf1(
                script = 'ThreadRole',
        )
        """

    def testRoleTokenConfigOneOf1(self):
        """Test RoleTokenConfigOneOf1"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()