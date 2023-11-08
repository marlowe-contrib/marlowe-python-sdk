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

from openapi_client.models.apply_inputs_tx_envelope import ApplyInputsTxEnvelope  # noqa: E501

class TestApplyInputsTxEnvelope(unittest.TestCase):
    """ApplyInputsTxEnvelope unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ApplyInputsTxEnvelope:
        """Test ApplyInputsTxEnvelope
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ApplyInputsTxEnvelope`
        """
        model = ApplyInputsTxEnvelope()  # noqa: E501
        if include_optional:
            return ApplyInputsTxEnvelope(
                tx = openapi_client.models.text_envelope.TextEnvelope(
                    cbor_hex = '', 
                    description = '', 
                    type = '', ),
                withdrawal_id = '62ECB020842930cc01FFCCfeEe150AC32DcAEc8a83DDD7dBF7567C88195ffcea'
            )
        else:
            return ApplyInputsTxEnvelope(
                tx = openapi_client.models.text_envelope.TextEnvelope(
                    cbor_hex = '', 
                    description = '', 
                    type = '', ),
                withdrawal_id = '62ECB020842930cc01FFCCfeEe150AC32DcAEc8a83DDD7dBF7567C88195ffcea',
        )
        """

    def testApplyInputsTxEnvelope(self):
        """Test ApplyInputsTxEnvelope"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()