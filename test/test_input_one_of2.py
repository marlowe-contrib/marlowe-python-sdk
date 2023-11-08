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

from openapi_client.models.input_one_of2 import InputOneOf2  # noqa: E501

class TestInputOneOf2(unittest.TestCase):
    """InputOneOf2 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> InputOneOf2:
        """Test InputOneOf2
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `InputOneOf2`
        """
        model = InputOneOf2()  # noqa: E501
        if include_optional:
            return InputOneOf2(
                for_choice_id = openapi_client.models.choice_id.ChoiceId(
                    choice_name = '', 
                    choice_owner = null, ),
                input_that_chooses_num = 56
            )
        else:
            return InputOneOf2(
                for_choice_id = openapi_client.models.choice_id.ChoiceId(
                    choice_name = '', 
                    choice_owner = null, ),
                input_that_chooses_num = 56,
        )
        """

    def testInputOneOf2(self):
        """Test InputOneOf2"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()