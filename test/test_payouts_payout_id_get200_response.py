# coding: utf-8

"""
    

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from openapi_client.models.payouts_payout_id_get200_response import PayoutsPayoutIdGet200Response  # noqa: E501

class TestPayoutsPayoutIdGet200Response(unittest.TestCase):
    """PayoutsPayoutIdGet200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PayoutsPayoutIdGet200Response:
        """Test PayoutsPayoutIdGet200Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PayoutsPayoutIdGet200Response`
        """
        model = PayoutsPayoutIdGet200Response()  # noqa: E501
        if include_optional:
            return PayoutsPayoutIdGet200Response(
                links = openapi_client.models._payouts__payout_id__get_200_response_links._payouts__payoutId__get_200_response_links(
                    contract = '', 
                    transaction = '', 
                    withdrawal = '', ),
                resource = openapi_client.models.payout_state.PayoutState(
                    assets = openapi_client.models.assets.Assets(
                        lovelace = 56, 
                        tokens = {
                            'key' : {
                                'key' : 56
                                }
                            }, ), 
                    contract_id = '98d601c9307dd43307cf68a03aad0086d4e07a789b66919ccf9f7f7676577eb7#1', 
                    payout_id = '98d601c9307dd43307cf68a03aad0086d4e07a789b66919ccf9f7f7676577eb7#1', 
                    payout_validator_address = 'addr1w94f8ywk4fg672xasahtk4t9k6w3aql943uxz5rt62d4dvq8evxaf', 
                    role = openapi_client.models.asset_id.AssetId(
                        asset_name = '', 
                        policy_id = '2ECB020842930cc01FFCCf', ), 
                    status = 'available', 
                    withdrawal_id = '62ECB020842930cc01FFCCfeEe150AC32DcAEc8a83DDD7dBF7567C88195ffcea', )
            )
        else:
            return PayoutsPayoutIdGet200Response(
                links = openapi_client.models._payouts__payout_id__get_200_response_links._payouts__payoutId__get_200_response_links(
                    contract = '', 
                    transaction = '', 
                    withdrawal = '', ),
                resource = openapi_client.models.payout_state.PayoutState(
                    assets = openapi_client.models.assets.Assets(
                        lovelace = 56, 
                        tokens = {
                            'key' : {
                                'key' : 56
                                }
                            }, ), 
                    contract_id = '98d601c9307dd43307cf68a03aad0086d4e07a789b66919ccf9f7f7676577eb7#1', 
                    payout_id = '98d601c9307dd43307cf68a03aad0086d4e07a789b66919ccf9f7f7676577eb7#1', 
                    payout_validator_address = 'addr1w94f8ywk4fg672xasahtk4t9k6w3aql943uxz5rt62d4dvq8evxaf', 
                    role = openapi_client.models.asset_id.AssetId(
                        asset_name = '', 
                        policy_id = '2ECB020842930cc01FFCCf', ), 
                    status = 'available', 
                    withdrawal_id = '62ECB020842930cc01FFCCfeEe150AC32DcAEc8a83DDD7dBF7567C88195ffcea', ),
        )
        """

    def testPayoutsPayoutIdGet200Response(self):
        """Test PayoutsPayoutIdGet200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
