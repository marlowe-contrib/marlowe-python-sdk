import unittest
import openapi_client


swap_contract = openapi_client.Contract(
    openapi_client.When(
        timeout=1704288420000,
        timeout_continuation=openapi_client.Contract(openapi_client.Close("close")),
        when=[
            openapi_client.Case(
                openapi_client.CaseThen(
                    case=openapi_client.Action(
                        openapi_client.DepositAction(
                            deposits=openapi_client.Value(3_000_000),
                            into_account=openapi_client.Party(
                                openapi_client.PartyRoleName(role_token="provider")
                            ),
                            of_token=openapi_client.Token(
                                currency_symbol="", token_name=""
                            ),
                            party=openapi_client.Party(
                                openapi_client.PartyRoleName(role_token="provider")
                            ),
                        )
                    ),
                    then=openapi_client.Contract(
                        openapi_client.When(
                            timeout=1704288420000,
                            timeout_continuation=openapi_client.Contract(
                                openapi_client.Pay(
                                    from_account=openapi_client.Party(
                                        openapi_client.PartyRoleName(
                                            role_token="provider"
                                        )
                                    ),
                                    pay=openapi_client.Value(3_000_000),
                                    then=openapi_client.Contract(
                                        openapi_client.Close("close")
                                    ),
                                    to=openapi_client.Payee(
                                        openapi_client.PayToParty(
                                            party=openapi_client.Party(
                                                openapi_client.PartyRoleName(
                                                    role_token="provider"
                                                )
                                            )
                                        )
                                    ),
                                    token=openapi_client.Token(
                                        currency_symbol="", token_name=""
                                    ),
                                )
                            ),
                            when=[
                                openapi_client.Case(
                                    openapi_client.CaseThen(
                                        case=openapi_client.Action(
                                            openapi_client.DepositAction(
                                                deposits=openapi_client.Value(
                                                    3_000_000
                                                ),
                                                into_account=openapi_client.Party(
                                                    openapi_client.PartyRoleName(
                                                        role_token="swapper"
                                                    )
                                                ),
                                                of_token=openapi_client.Token(
                                                    currency_symbol="",
                                                    token_name="",
                                                ),
                                                party=openapi_client.Party(
                                                    openapi_client.PartyRoleName(
                                                        role_token="swapper"
                                                    )
                                                ),
                                            ),
                                        ),
                                        then=openapi_client.Contract(
                                            openapi_client.Pay(
                                                from_account=openapi_client.Party(
                                                    openapi_client.PartyRoleName(
                                                        role_token="provider"
                                                    )
                                                ),
                                                pay=openapi_client.Value(3_000_000),
                                                then=openapi_client.Contract(
                                                    openapi_client.Pay(
                                                        from_account=openapi_client.Party(
                                                            openapi_client.PartyRoleName(
                                                                role_token="swapper"
                                                            )
                                                        ),
                                                        pay=openapi_client.Value(
                                                            3_000_000
                                                        ),
                                                        then=openapi_client.Contract(
                                                            openapi_client.Close(
                                                                "close"
                                                            )
                                                        ),
                                                        to=openapi_client.Payee(
                                                            openapi_client.PayToParty(
                                                                party=openapi_client.Party(
                                                                    openapi_client.PartyRoleName(
                                                                        role_token="provider"
                                                                    )
                                                                )
                                                            )
                                                        ),
                                                        token=openapi_client.Token(
                                                            currency_symbol="",
                                                            token_name="",
                                                        ),
                                                    )
                                                ),
                                                to=openapi_client.Payee(
                                                    openapi_client.PayToParty(
                                                        party=openapi_client.Party(
                                                            openapi_client.PartyRoleName(
                                                                role_token="swapper"
                                                            )
                                                        )
                                                    )
                                                ),
                                                token=openapi_client.Token(
                                                    currency_symbol="", token_name=""
                                                ),
                                            )
                                        ),
                                    )
                                )
                            ],
                        )
                    ),
                )
            )
        ],
    )
)


def upload_contract_sources(
    api_instance: openapi_client.DefaultApi,
) -> openapi_client.PostContractSourceResponse:
    return api_instance.create_contract_sources(
        main="swap_contract",
        labelled_object=[
            openapi_client.LabelledObject(
                label="swap_contract",
                type="contract",
                value=openapi_client.LabelledObjectValue(
                    openapi_client.ContractObject.from_dict(swap_contract.to_dict())
                ),
            )
        ],
    )


class TestParsingResponses:
    def setup_method(self):
        configuration = openapi_client.Configuration(
            host="https://marlowe-runtime-preprod-web.scdev.aws.iohkdev.io"
        )
        api_client = openapi_client.ApiClient(configuration)
        # Create an instance of the API class
        self.api_instance = openapi_client.DefaultApi(api_client)

    def test_get_contracts(self):
        api_response = self.api_instance.get_contracts()

    def test_create_contract(self):
        api_response = self.api_instance.create_contract(
            post_contracts_request=openapi_client.PostContractsRequest(
                contract=openapi_client.PostContractsRequestContract(swap_contract),
                metadata={},
                tags={},
                version=openapi_client.MarloweVersion.V1,
                minUTxODeposit=3_000_000,
                roles=openapi_client.RolesConfig(
                    {
                        "swapper": openapi_client.RoleTokenConfig(
                            "addr_test1vzuqvqzcnuy9pmrh2sy7tjucufmpwh8gzssz7v6scn0e04gxdvna9"
                        ),
                        "provider": openapi_client.RoleTokenConfig(
                            "addr_test1vzuqvqzcnuy9pmrh2sy7tjucufmpwh8gzssz7v6scn0e04gxdvna9"
                        ),
                    }
                ),
            ),
            x_change_address="addr_test1vzuqvqzcnuy9pmrh2sy7tjucufmpwh8gzssz7v6scn0e04gxdvna9",
        )

    def test_upload_contract_sources(self):
        uploaded_res = upload_contract_sources(self.api_instance)

    def test_get_contract_source_by_id(self):
        source_id_res = self.api_instance.get_contract_source_by_id(
            "705f33bb023b560f458a277c12130487f8dbca1b9e4dc50c4ed1596e00944996"
        )

    def test_get_contract_source_adjacency(self):
        source_adj_res = self.api_instance.get_contract_source_adjacency(
            "705f33bb023b560f458a277c12130487f8dbca1b9e4dc50c4ed1596e00944996"
        )

    def test_get_contract_source_closure(self):
        source_closure_res = self.api_instance.get_contract_source_closure(
            "705f33bb023b560f458a277c12130487f8dbca1b9e4dc50c4ed1596e00944996"
        )

    def test_get_contract_by_id(self):
        contract_by_id_res = self.api_instance.get_contract_by_id(
            "14a950e998711bb16c72fdd0bd707b4a306daf38bc1fc2e560aae3409dd30c25#1"
        )

    def test_get_next_steps(self):
        next_steps_res = self.api_instance.get_next_steps_for_contract(
            contract_id="26a9d99e3a014b7dafc21642c829b5f51edd8f74f45f13d965e967df182156eb#1",
            validity_start="1970-12-06T00:00:00.000Z",
            validity_end="2050-01-01T00:00:00.000Z",
        )

    def test_get_transactions_for_contract(self):
        transactions_res = self.api_instance.get_transactions_for_contract(
            contract_id="06fb28e1322bb2d366617e6fbaed22ed93a8ca2b813964ade5621c4b8fba1ee8#1",
        )
