# coding: utf-8

"""
    Marlowe Runtime REST API

    REST API for Marlowe Runtime

    The version of the OpenAPI document: 0.0.5.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.api.default_api import DefaultApi  # noqa: E501


class TestDefaultApi(unittest.TestCase):
    """DefaultApi unit test stubs"""

    def setUp(self) -> None:
        self.api = DefaultApi()  # noqa: E501

    def tearDown(self) -> None:
        pass

    def test_apply_inputs_to_contract(self) -> None:
        """Test case for apply_inputs_to_contract

        Apply inputs to contract  # noqa: E501
        """
        pass

    def test_create_contract(self) -> None:
        """Test case for create_contract

        Create a new contract  # noqa: E501
        """
        pass

    def test_create_contract_sources(self) -> None:
        """Test case for create_contract_sources

        Upload contract sources  # noqa: E501
        """
        pass

    def test_get_contract_by_id(self) -> None:
        """Test case for get_contract_by_id

        Get contract by ID  # noqa: E501
        """
        pass

    def test_get_contract_source_adjacency(self) -> None:
        """Test case for get_contract_source_adjacency

        Get adjacent contract source IDs by ID  # noqa: E501
        """
        pass

    def test_get_contract_source_by_id(self) -> None:
        """Test case for get_contract_source_by_id

        Get contract source by ID  # noqa: E501
        """
        pass

    def test_get_contract_source_closure(self) -> None:
        """Test case for get_contract_source_closure

        Get contract source closure by ID  # noqa: E501
        """
        pass

    def test_get_contract_transaction_by_id(self) -> None:
        """Test case for get_contract_transaction_by_id

        Get contract transaction by ID  # noqa: E501
        """
        pass

    def test_get_contracts(self) -> None:
        """Test case for get_contracts

        Get contracts  # noqa: E501
        """
        pass

    def test_get_next_steps_for_contract(self) -> None:
        """Test case for get_next_steps_for_contract

        Get next contract steps  # noqa: E501
        """
        pass

    def test_get_payout_by_id(self) -> None:
        """Test case for get_payout_by_id

        Get payout by ID  # noqa: E501
        """
        pass

    def test_get_payouts(self) -> None:
        """Test case for get_payouts

        Get role payouts  # noqa: E501
        """
        pass

    def test_get_transactions_for_contract(self) -> None:
        """Test case for get_transactions_for_contract

        Get transactions for contract  # noqa: E501
        """
        pass

    def test_get_withdrawal_by_id(self) -> None:
        """Test case for get_withdrawal_by_id

        Get withdrawal by ID  # noqa: E501
        """
        pass

    def test_get_withdrawals(self) -> None:
        """Test case for get_withdrawals

        Get withdrawals  # noqa: E501
        """
        pass

    def test_healthcheck(self) -> None:
        """Test case for healthcheck

        Test server status  # noqa: E501
        """
        pass

    def test_submit_contract(self) -> None:
        """Test case for submit_contract

        Submit contract to chain  # noqa: E501
        """
        pass

    def test_submit_contract_transaction(self) -> None:
        """Test case for submit_contract_transaction

        Submit contract input application  # noqa: E501
        """
        pass

    def test_submit_withdrawal(self) -> None:
        """Test case for submit_withdrawal

        Submit payout withdrawal  # noqa: E501
        """
        pass

    def test_withdraw_payouts(self) -> None:
        """Test case for withdraw_payouts

        Withdraw payouts  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
