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

from openapi_client.models.interval_error_one_of1_interval_in_past_error import IntervalErrorOneOf1IntervalInPastError  # noqa: E501

class TestIntervalErrorOneOf1IntervalInPastError(unittest.TestCase):
    """IntervalErrorOneOf1IntervalInPastError unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> IntervalErrorOneOf1IntervalInPastError:
        """Test IntervalErrorOneOf1IntervalInPastError
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `IntervalErrorOneOf1IntervalInPastError`
        """
        model = IntervalErrorOneOf1IntervalInPastError()  # noqa: E501
        if include_optional:
            return IntervalErrorOneOf1IntervalInPastError(
                var_from = 56,
                min_time = 56,
                to = 56
            )
        else:
            return IntervalErrorOneOf1IntervalInPastError(
                var_from = 56,
                min_time = 56,
                to = 56,
        )
        """

    def testIntervalErrorOneOf1IntervalInPastError(self):
        """Test IntervalErrorOneOf1IntervalInPastError"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
