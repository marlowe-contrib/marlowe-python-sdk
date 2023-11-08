# coding: utf-8

"""
    

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from openapi_client.models.contracts_contract_id_transactions_transaction_id_get200_response import ContractsContractIdTransactionsTransactionIdGet200Response  # noqa: E501

class TestContractsContractIdTransactionsTransactionIdGet200Response(unittest.TestCase):
    """ContractsContractIdTransactionsTransactionIdGet200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ContractsContractIdTransactionsTransactionIdGet200Response:
        """Test ContractsContractIdTransactionsTransactionIdGet200Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ContractsContractIdTransactionsTransactionIdGet200Response`
        """
        model = ContractsContractIdTransactionsTransactionIdGet200Response()  # noqa: E501
        if include_optional:
            return ContractsContractIdTransactionsTransactionIdGet200Response(
                links = openapi_client.models._contracts__contract_id__transactions__transaction_id__get_200_response_links._contracts__contractId__transactions__transactionId__get_200_response_links(
                    next = '', 
                    previous = '', ),
                resource = openapi_client.models.tx.Tx(
                    assets = openapi_client.models.assets.Assets(
                        lovelace = 56, 
                        tokens = {
                            'key' : {
                                'key' : 56
                                }
                            }, ), 
                    block = openapi_client.models.block_header.BlockHeader(
                        block_header_hash = '', 
                        block_no = 0, 
                        slot_no = 0, ), 
                    consuming_tx = '62ECB020842930cc01FFCCfeEe150AC32DcAEc8a83DDD7dBF7567C88195ffcea', 
                    continuations = '', 
                    contract_id = '98d601c9307dd43307cf68a03aad0086d4e07a789b66919ccf9f7f7676577eb7#1', 
                    input_utxo = '98d601c9307dd43307cf68a03aad0086d4e07a789b66919ccf9f7f7676577eb7#1', 
                    inputs = [
                        null
                        ], 
                    invalid_before = '2016-07-22T00:00:00Z', 
                    invalid_hereafter = '2016-07-22T00:00:00Z', 
                    metadata = {
                        'key' : null
                        }, 
                    output_contract = null, 
                    output_state = openapi_client.models.marlowe_state.MarloweState(
                        accounts = [
                            [
                                null
                                ]
                            ], 
                        bound_values = [
                            [
                                null
                                ]
                            ], 
                        choices = [
                            [
                                null
                                ]
                            ], 
                        min_time = 56, ), 
                    output_utxo = '98d601c9307dd43307cf68a03aad0086d4e07a789b66919ccf9f7f7676577eb7#1', 
                    payouts = [
                        openapi_client.models.payout.Payout(
                            assets = openapi_client.models.assets.Assets(
                                lovelace = 56, 
                                tokens = {
                                    'key' : {
                                        'key' : 56
                                        }
                                    }, ), 
                            payout_id = '98d601c9307dd43307cf68a03aad0086d4e07a789b66919ccf9f7f7676577eb7#1', 
                            role = '', )
                        ], 
                    status = 'unsigned', 
                    tags = {
                        'key' : null
                        }, 
                    transaction_id = '62ECB020842930cc01FFCCfeEe150AC32DcAEc8a83DDD7dBF7567C88195ffcea', 
                    tx_body = openapi_client.models.text_envelope.TextEnvelope(
                        cbor_hex = '', 
                        description = '', 
                        type = '', ), )
            )
        else:
            return ContractsContractIdTransactionsTransactionIdGet200Response(
                links = openapi_client.models._contracts__contract_id__transactions__transaction_id__get_200_response_links._contracts__contractId__transactions__transactionId__get_200_response_links(
                    next = '', 
                    previous = '', ),
                resource = openapi_client.models.tx.Tx(
                    assets = openapi_client.models.assets.Assets(
                        lovelace = 56, 
                        tokens = {
                            'key' : {
                                'key' : 56
                                }
                            }, ), 
                    block = openapi_client.models.block_header.BlockHeader(
                        block_header_hash = '', 
                        block_no = 0, 
                        slot_no = 0, ), 
                    consuming_tx = '62ECB020842930cc01FFCCfeEe150AC32DcAEc8a83DDD7dBF7567C88195ffcea', 
                    continuations = '', 
                    contract_id = '98d601c9307dd43307cf68a03aad0086d4e07a789b66919ccf9f7f7676577eb7#1', 
                    input_utxo = '98d601c9307dd43307cf68a03aad0086d4e07a789b66919ccf9f7f7676577eb7#1', 
                    inputs = [
                        null
                        ], 
                    invalid_before = '2016-07-22T00:00:00Z', 
                    invalid_hereafter = '2016-07-22T00:00:00Z', 
                    metadata = {
                        'key' : null
                        }, 
                    output_contract = null, 
                    output_state = openapi_client.models.marlowe_state.MarloweState(
                        accounts = [
                            [
                                null
                                ]
                            ], 
                        bound_values = [
                            [
                                null
                                ]
                            ], 
                        choices = [
                            [
                                null
                                ]
                            ], 
                        min_time = 56, ), 
                    output_utxo = '98d601c9307dd43307cf68a03aad0086d4e07a789b66919ccf9f7f7676577eb7#1', 
                    payouts = [
                        openapi_client.models.payout.Payout(
                            assets = openapi_client.models.assets.Assets(
                                lovelace = 56, 
                                tokens = {
                                    'key' : {
                                        'key' : 56
                                        }
                                    }, ), 
                            payout_id = '98d601c9307dd43307cf68a03aad0086d4e07a789b66919ccf9f7f7676577eb7#1', 
                            role = '', )
                        ], 
                    status = 'unsigned', 
                    tags = {
                        'key' : null
                        }, 
                    transaction_id = '62ECB020842930cc01FFCCfeEe150AC32DcAEc8a83DDD7dBF7567C88195ffcea', 
                    tx_body = openapi_client.models.text_envelope.TextEnvelope(
                        cbor_hex = '', 
                        description = '', 
                        type = '', ), ),
        )
        """

    def testContractsContractIdTransactionsTransactionIdGet200Response(self):
        """Test ContractsContractIdTransactionsTransactionIdGet200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
