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

from openapi_client.models.value_object_one_of6 import ValueObjectOneOf6  # noqa: E501

class TestValueObjectOneOf6(unittest.TestCase):
    """ValueObjectOneOf6 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ValueObjectOneOf6:
        """Test ValueObjectOneOf6
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ValueObjectOneOf6`
        """
        model = ValueObjectOneOf6()  # noqa: E501
        if include_optional:
            return ValueObjectOneOf6(
                value_of_choice = openapi_client.models.choice_id_object.ChoiceIdObject(
                    choice_name = '', 
                    choice_owner = null, )
            )
        else:
            return ValueObjectOneOf6(
                value_of_choice = openapi_client.models.choice_id_object.ChoiceIdObject(
                    choice_name = '', 
                    choice_owner = null, ),
        )
        """

    def testValueObjectOneOf6(self):
        """Test ValueObjectOneOf6"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
