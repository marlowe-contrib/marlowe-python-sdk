# coding: utf-8

"""
    

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from openapi_client.models.list_object_contract_source_id import ListObjectContractSourceId  # noqa: E501

class TestListObjectContractSourceId(unittest.TestCase):
    """ListObjectContractSourceId unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ListObjectContractSourceId:
        """Test ListObjectContractSourceId
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ListObjectContractSourceId`
        """
        model = ListObjectContractSourceId()  # noqa: E501
        if include_optional:
            return ListObjectContractSourceId(
                results = [
                    '62ECB020842930cc01FFCCfeEe150AC32DcAEc8a83DDD7dBF7567C88195ffcea'
                    ]
            )
        else:
            return ListObjectContractSourceId(
                results = [
                    '62ECB020842930cc01FFCCfeEe150AC32DcAEc8a83DDD7dBF7567C88195ffcea'
                    ],
        )
        """

    def testListObjectContractSourceId(self):
        """Test ListObjectContractSourceId"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
