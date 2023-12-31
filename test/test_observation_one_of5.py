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

from openapi_client.models.observation_one_of5 import ObservationOneOf5  # noqa: E501

class TestObservationOneOf5(unittest.TestCase):
    """ObservationOneOf5 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ObservationOneOf5:
        """Test ObservationOneOf5
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ObservationOneOf5`
        """
        model = ObservationOneOf5()  # noqa: E501
        if include_optional:
            return ObservationOneOf5(
                gt = None,
                value = None
            )
        else:
            return ObservationOneOf5(
                gt = None,
                value = None,
        )
        """

    def testObservationOneOf5(self):
        """Test ObservationOneOf5"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
