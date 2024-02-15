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

from openapi_client.models.withdraw_tx_envelope import WithdrawTxEnvelope  # noqa: E501

class TestWithdrawTxEnvelope(unittest.TestCase):
    """WithdrawTxEnvelope unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> WithdrawTxEnvelope:
        """Test WithdrawTxEnvelope
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `WithdrawTxEnvelope`
        """
        model = WithdrawTxEnvelope()  # noqa: E501
        if include_optional:
            return WithdrawTxEnvelope(
                tx = openapi_client.models.text_envelope.TextEnvelope(
                    cbor_hex = '', 
                    description = '', 
                    type = '', ),
                withdrawal_id = '62ECB020842930cc01FFCCfeEe150AC32DcAEc8a83DDD7dBF7567C88195ffcea'
            )
        else:
            return WithdrawTxEnvelope(
                tx = openapi_client.models.text_envelope.TextEnvelope(
                    cbor_hex = '', 
                    description = '', 
                    type = '', ),
                withdrawal_id = '62ECB020842930cc01FFCCfeEe150AC32DcAEc8a83DDD7dBF7567C88195ffcea',
        )
        """

    def testWithdrawTxEnvelope(self):
        """Test WithdrawTxEnvelope"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
