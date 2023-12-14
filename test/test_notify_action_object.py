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

from openapi_client.models.notify_action_object import NotifyActionObject  # noqa: E501

class TestNotifyActionObject(unittest.TestCase):
    """NotifyActionObject unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> NotifyActionObject:
        """Test NotifyActionObject
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `NotifyActionObject`
        """
        model = NotifyActionObject()  # noqa: E501
        if include_optional:
            return NotifyActionObject(
                notify_if = None
            )
        else:
            return NotifyActionObject(
                notify_if = None,
        )
        """

    def testNotifyActionObject(self):
        """Test NotifyActionObject"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
