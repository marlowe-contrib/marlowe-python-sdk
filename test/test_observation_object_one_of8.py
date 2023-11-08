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

from openapi_client.models.observation_object_one_of8 import ObservationObjectOneOf8  # noqa: E501

class TestObservationObjectOneOf8(unittest.TestCase):
    """ObservationObjectOneOf8 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ObservationObjectOneOf8:
        """Test ObservationObjectOneOf8
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ObservationObjectOneOf8`
        """
        model = ObservationObjectOneOf8()  # noqa: E501
        if include_optional:
            return ObservationObjectOneOf8(
                equal_to = None,
                value = None
            )
        else:
            return ObservationObjectOneOf8(
                equal_to = None,
                value = None,
        )
        """

    def testObservationObjectOneOf8(self):
        """Test ObservationObjectOneOf8"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
