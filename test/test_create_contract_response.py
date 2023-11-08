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

from openapi_client.models.create_contract_response import CreateContractResponse  # noqa: E501

class TestCreateContractResponse(unittest.TestCase):
    """CreateContractResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CreateContractResponse:
        """Test CreateContractResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CreateContractResponse`
        """
        model = CreateContractResponse()  # noqa: E501
        if include_optional:
            return CreateContractResponse(
                links = openapi_client.models.create_contract_response_links.CreateContractResponse_links(
                    contract = '', ),
                resource = openapi_client.models.apply_inputs_tx_envelope.ApplyInputsTxEnvelope(
                    tx = openapi_client.models.text_envelope.TextEnvelope(
                        cbor_hex = '', 
                        description = '', 
                        type = '', ), 
                    withdrawal_id = '62ECB020842930cc01FFCCfeEe150AC32DcAEc8a83DDD7dBF7567C88195ffcea', )
            )
        else:
            return CreateContractResponse(
                links = openapi_client.models.create_contract_response_links.CreateContractResponse_links(
                    contract = '', ),
                resource = openapi_client.models.apply_inputs_tx_envelope.ApplyInputsTxEnvelope(
                    tx = openapi_client.models.text_envelope.TextEnvelope(
                        cbor_hex = '', 
                        description = '', 
                        type = '', ), 
                    withdrawal_id = '62ECB020842930cc01FFCCfeEe150AC32DcAEc8a83DDD7dBF7567C88195ffcea', ),
        )
        """

    def testCreateContractResponse(self):
        """Test CreateContractResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
