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

from openapi_client.models.interval_error_one_of import IntervalErrorOneOf  # noqa: E501

class TestIntervalErrorOneOf(unittest.TestCase):
    """IntervalErrorOneOf unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> IntervalErrorOneOf:
        """Test IntervalErrorOneOf
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `IntervalErrorOneOf`
        """
        model = IntervalErrorOneOf()  # noqa: E501
        if include_optional:
            return IntervalErrorOneOf(
                invalid_interval = openapi_client.models.interval_error_one_of_invalid_interval.IntervalError_oneOf_invalidInterval(
                    from = 56, 
                    to = 56, )
            )
        else:
            return IntervalErrorOneOf(
                invalid_interval = openapi_client.models.interval_error_one_of_invalid_interval.IntervalError_oneOf_invalidInterval(
                    from = 56, 
                    to = 56, ),
        )
        """

    def testIntervalErrorOneOf(self):
        """Test IntervalErrorOneOf"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
