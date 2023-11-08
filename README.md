# openapi-client
No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 
- Package version: 1.0.0
- Build package: org.openapitools.codegen.languages.PythonClientCodegen

## Requirements.

Python 3.7+

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import openapi_client
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import openapi_client
```

### Tests

Execute `pytest` to run the tests.

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python

import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)



# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    contract_id = '98d601c9307dd43307cf68a03aad0086d4e07a789b66919ccf9f7f7676577eb7%231' # str | 

    try:
        api_response = api_instance.contracts_contract_id_get(contract_id)
        print("The response of DefaultApi->contracts_contract_id_get:\n")
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->contracts_contract_id_get: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *http://localhost*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*DefaultApi* | [**contracts_contract_id_get**](docs/DefaultApi.md#contracts_contract_id_get) | **GET** /contracts/{contractId} | 
*DefaultApi* | [**contracts_contract_id_next_get**](docs/DefaultApi.md#contracts_contract_id_next_get) | **GET** /contracts/{contractId}/next | 
*DefaultApi* | [**contracts_contract_id_put**](docs/DefaultApi.md#contracts_contract_id_put) | **PUT** /contracts/{contractId} | 
*DefaultApi* | [**contracts_contract_id_transactions_get**](docs/DefaultApi.md#contracts_contract_id_transactions_get) | **GET** /contracts/{contractId}/transactions | 
*DefaultApi* | [**contracts_contract_id_transactions_post**](docs/DefaultApi.md#contracts_contract_id_transactions_post) | **POST** /contracts/{contractId}/transactions | 
*DefaultApi* | [**contracts_contract_id_transactions_transaction_id_get**](docs/DefaultApi.md#contracts_contract_id_transactions_transaction_id_get) | **GET** /contracts/{contractId}/transactions/{transactionId} | 
*DefaultApi* | [**contracts_contract_id_transactions_transaction_id_put**](docs/DefaultApi.md#contracts_contract_id_transactions_transaction_id_put) | **PUT** /contracts/{contractId}/transactions/{transactionId} | 
*DefaultApi* | [**contracts_get**](docs/DefaultApi.md#contracts_get) | **GET** /contracts | 
*DefaultApi* | [**contracts_post**](docs/DefaultApi.md#contracts_post) | **POST** /contracts | 
*DefaultApi* | [**contracts_sources_contract_source_id_adjacency_get**](docs/DefaultApi.md#contracts_sources_contract_source_id_adjacency_get) | **GET** /contracts/sources/{contractSourceId}/adjacency | 
*DefaultApi* | [**contracts_sources_contract_source_id_closure_get**](docs/DefaultApi.md#contracts_sources_contract_source_id_closure_get) | **GET** /contracts/sources/{contractSourceId}/closure | 
*DefaultApi* | [**contracts_sources_contract_source_id_get**](docs/DefaultApi.md#contracts_sources_contract_source_id_get) | **GET** /contracts/sources/{contractSourceId} | 
*DefaultApi* | [**contracts_sources_post**](docs/DefaultApi.md#contracts_sources_post) | **POST** /contracts/sources | 
*DefaultApi* | [**healthcheck_get**](docs/DefaultApi.md#healthcheck_get) | **GET** /healthcheck | 
*DefaultApi* | [**payouts_get**](docs/DefaultApi.md#payouts_get) | **GET** /payouts | 
*DefaultApi* | [**payouts_payout_id_get**](docs/DefaultApi.md#payouts_payout_id_get) | **GET** /payouts/{payoutId} | 
*DefaultApi* | [**withdrawals_get**](docs/DefaultApi.md#withdrawals_get) | **GET** /withdrawals | 
*DefaultApi* | [**withdrawals_post**](docs/DefaultApi.md#withdrawals_post) | **POST** /withdrawals | 
*DefaultApi* | [**withdrawals_withdrawal_id_get**](docs/DefaultApi.md#withdrawals_withdrawal_id_get) | **GET** /withdrawals/{withdrawalId} | 
*DefaultApi* | [**withdrawals_withdrawal_id_put**](docs/DefaultApi.md#withdrawals_withdrawal_id_put) | **PUT** /withdrawals/{withdrawalId} | 


## Documentation For Models

 - [Action](docs/Action.md)
 - [ActionObject](docs/ActionObject.md)
 - [ActionOneOf](docs/ActionOneOf.md)
 - [ActionOneOf1](docs/ActionOneOf1.md)
 - [ActionOneOf2](docs/ActionOneOf2.md)
 - [ApplicableInputs](docs/ApplicableInputs.md)
 - [ApplyInputsTxEnvelope](docs/ApplyInputsTxEnvelope.md)
 - [AssetId](docs/AssetId.md)
 - [Assets](docs/Assets.md)
 - [BlockHeader](docs/BlockHeader.md)
 - [Bound](docs/Bound.md)
 - [CanChoose](docs/CanChoose.md)
 - [CanDeposit](docs/CanDeposit.md)
 - [CanNotify](docs/CanNotify.md)
 - [Case](docs/Case.md)
 - [CaseObject](docs/CaseObject.md)
 - [CaseObjectOneOf](docs/CaseObjectOneOf.md)
 - [CaseObjectOneOf1](docs/CaseObjectOneOf1.md)
 - [CaseOneOf](docs/CaseOneOf.md)
 - [CaseOneOf1](docs/CaseOneOf1.md)
 - [ChoiceId](docs/ChoiceId.md)
 - [ChoiceIdObject](docs/ChoiceIdObject.md)
 - [Contract](docs/Contract.md)
 - [ContractHeader](docs/ContractHeader.md)
 - [ContractObject](docs/ContractObject.md)
 - [ContractObjectOneOf](docs/ContractObjectOneOf.md)
 - [ContractObjectOneOf1](docs/ContractObjectOneOf1.md)
 - [ContractObjectOneOf2](docs/ContractObjectOneOf2.md)
 - [ContractObjectOneOf3](docs/ContractObjectOneOf3.md)
 - [ContractObjectOneOf4](docs/ContractObjectOneOf4.md)
 - [ContractOneOf](docs/ContractOneOf.md)
 - [ContractOneOf1](docs/ContractOneOf1.md)
 - [ContractOneOf2](docs/ContractOneOf2.md)
 - [ContractOneOf3](docs/ContractOneOf3.md)
 - [ContractOneOf4](docs/ContractOneOf4.md)
 - [ContractState](docs/ContractState.md)
 - [ContractsContractIdGet200Response](docs/ContractsContractIdGet200Response.md)
 - [ContractsContractIdGet200ResponseLinks](docs/ContractsContractIdGet200ResponseLinks.md)
 - [ContractsContractIdTransactionsPost201Response](docs/ContractsContractIdTransactionsPost201Response.md)
 - [ContractsContractIdTransactionsPost201ResponseLinks](docs/ContractsContractIdTransactionsPost201ResponseLinks.md)
 - [ContractsContractIdTransactionsTransactionIdGet200Response](docs/ContractsContractIdTransactionsTransactionIdGet200Response.md)
 - [ContractsContractIdTransactionsTransactionIdGet200ResponseLinks](docs/ContractsContractIdTransactionsTransactionIdGet200ResponseLinks.md)
 - [ContractsPost201Response](docs/ContractsPost201Response.md)
 - [ContractsPost201ResponseLinks](docs/ContractsPost201ResponseLinks.md)
 - [ExBudget](docs/ExBudget.md)
 - [Input](docs/Input.md)
 - [InputOneOf](docs/InputOneOf.md)
 - [InputOneOf1](docs/InputOneOf1.md)
 - [InputOneOf2](docs/InputOneOf2.md)
 - [InputOneOf3](docs/InputOneOf3.md)
 - [InputOneOf4](docs/InputOneOf4.md)
 - [IntervalError](docs/IntervalError.md)
 - [IntervalErrorOneOf](docs/IntervalErrorOneOf.md)
 - [IntervalErrorOneOf1](docs/IntervalErrorOneOf1.md)
 - [IntervalErrorOneOf1IntervalInPastError](docs/IntervalErrorOneOf1IntervalInPastError.md)
 - [IntervalErrorOneOfInvalidInterval](docs/IntervalErrorOneOfInvalidInterval.md)
 - [LabelledObject](docs/LabelledObject.md)
 - [LabelledObjectValue](docs/LabelledObjectValue.md)
 - [ListObjectContractHeader](docs/ListObjectContractHeader.md)
 - [ListObjectContractHeaderResultsInner](docs/ListObjectContractHeaderResultsInner.md)
 - [ListObjectContractHeaderResultsInnerLinks](docs/ListObjectContractHeaderResultsInnerLinks.md)
 - [ListObjectContractSourceId](docs/ListObjectContractSourceId.md)
 - [ListObjectPayoutHeader](docs/ListObjectPayoutHeader.md)
 - [ListObjectPayoutHeaderResultsInner](docs/ListObjectPayoutHeaderResultsInner.md)
 - [ListObjectPayoutHeaderResultsInnerLinks](docs/ListObjectPayoutHeaderResultsInnerLinks.md)
 - [ListObjectTxHeader](docs/ListObjectTxHeader.md)
 - [ListObjectTxHeaderResultsInner](docs/ListObjectTxHeaderResultsInner.md)
 - [ListObjectWithdrawalHeader](docs/ListObjectWithdrawalHeader.md)
 - [ListObjectWithdrawalHeaderResultsInner](docs/ListObjectWithdrawalHeaderResultsInner.md)
 - [MarloweState](docs/MarloweState.md)
 - [MarloweStateAccountsInnerInner](docs/MarloweStateAccountsInnerInner.md)
 - [MarloweStateAccountsInnerInnerOneOfInner](docs/MarloweStateAccountsInnerInnerOneOfInner.md)
 - [MarloweStateBoundValuesInnerInner](docs/MarloweStateBoundValuesInnerInner.md)
 - [MarloweStateChoicesInnerInner](docs/MarloweStateChoicesInnerInner.md)
 - [MarloweVersion](docs/MarloweVersion.md)
 - [Next](docs/Next.md)
 - [Observation](docs/Observation.md)
 - [ObservationObject](docs/ObservationObject.md)
 - [ObservationObjectOneOf](docs/ObservationObjectOneOf.md)
 - [ObservationObjectOneOf1](docs/ObservationObjectOneOf1.md)
 - [ObservationObjectOneOf2](docs/ObservationObjectOneOf2.md)
 - [ObservationObjectOneOf3](docs/ObservationObjectOneOf3.md)
 - [ObservationObjectOneOf4](docs/ObservationObjectOneOf4.md)
 - [ObservationObjectOneOf5](docs/ObservationObjectOneOf5.md)
 - [ObservationObjectOneOf6](docs/ObservationObjectOneOf6.md)
 - [ObservationObjectOneOf7](docs/ObservationObjectOneOf7.md)
 - [ObservationObjectOneOf8](docs/ObservationObjectOneOf8.md)
 - [ObservationOneOf](docs/ObservationOneOf.md)
 - [ObservationOneOf1](docs/ObservationOneOf1.md)
 - [ObservationOneOf2](docs/ObservationOneOf2.md)
 - [ObservationOneOf3](docs/ObservationOneOf3.md)
 - [ObservationOneOf4](docs/ObservationOneOf4.md)
 - [ObservationOneOf5](docs/ObservationOneOf5.md)
 - [ObservationOneOf6](docs/ObservationOneOf6.md)
 - [ObservationOneOf7](docs/ObservationOneOf7.md)
 - [ObservationOneOf8](docs/ObservationOneOf8.md)
 - [Party](docs/Party.md)
 - [PartyObject](docs/PartyObject.md)
 - [PartyOneOf](docs/PartyOneOf.md)
 - [PartyOneOf1](docs/PartyOneOf1.md)
 - [Payee](docs/Payee.md)
 - [PayeeObject](docs/PayeeObject.md)
 - [PayeeObjectOneOf](docs/PayeeObjectOneOf.md)
 - [PayeeObjectOneOf1](docs/PayeeObjectOneOf1.md)
 - [PayeeOneOf](docs/PayeeOneOf.md)
 - [PayeeOneOf1](docs/PayeeOneOf1.md)
 - [Payment](docs/Payment.md)
 - [Payout](docs/Payout.md)
 - [PayoutHeader](docs/PayoutHeader.md)
 - [PayoutState](docs/PayoutState.md)
 - [PayoutStatus](docs/PayoutStatus.md)
 - [PayoutsPayoutIdGet200Response](docs/PayoutsPayoutIdGet200Response.md)
 - [PayoutsPayoutIdGet200ResponseLinks](docs/PayoutsPayoutIdGet200ResponseLinks.md)
 - [PlutusAddress](docs/PlutusAddress.md)
 - [PlutusCredential](docs/PlutusCredential.md)
 - [PlutusCredentialOneOf](docs/PlutusCredentialOneOf.md)
 - [PlutusCredentialOneOf1](docs/PlutusCredentialOneOf1.md)
 - [PlutusStakingCredential](docs/PlutusStakingCredential.md)
 - [PlutusStakingCredentialOneOf](docs/PlutusStakingCredentialOneOf.md)
 - [PlutusStakingCredentialOneOf1](docs/PlutusStakingCredentialOneOf1.md)
 - [PlutusStakingCredentialOneOf1StakingHashInner](docs/PlutusStakingCredentialOneOf1StakingHashInner.md)
 - [PostContractSourceResponse](docs/PostContractSourceResponse.md)
 - [PostContractsRequest](docs/PostContractsRequest.md)
 - [PostContractsRequestContract](docs/PostContractsRequestContract.md)
 - [PostTransactionsRequest](docs/PostTransactionsRequest.md)
 - [PostWithdrawalsRequest](docs/PostWithdrawalsRequest.md)
 - [RoleTokenConfig](docs/RoleTokenConfig.md)
 - [RoleTokenConfigOneOf](docs/RoleTokenConfigOneOf.md)
 - [RolesConfig](docs/RolesConfig.md)
 - [SafetyError](docs/SafetyError.md)
 - [TextEnvelope](docs/TextEnvelope.md)
 - [Token](docs/Token.md)
 - [TokenMetadata](docs/TokenMetadata.md)
 - [TokenMetadataFile](docs/TokenMetadataFile.md)
 - [TokenObject](docs/TokenObject.md)
 - [Transaction](docs/Transaction.md)
 - [TransactionError](docs/TransactionError.md)
 - [TransactionErrorOneOf](docs/TransactionErrorOneOf.md)
 - [TransactionInput](docs/TransactionInput.md)
 - [TransactionInputTxInterval](docs/TransactionInputTxInterval.md)
 - [TransactionOutput](docs/TransactionOutput.md)
 - [TransactionOutputOneOf](docs/TransactionOutputOneOf.md)
 - [TransactionOutputOneOf1](docs/TransactionOutputOneOf1.md)
 - [TransactionWarning](docs/TransactionWarning.md)
 - [TransactionWarningOneOf](docs/TransactionWarningOneOf.md)
 - [TransactionWarningOneOf1](docs/TransactionWarningOneOf1.md)
 - [TransactionWarningOneOf2](docs/TransactionWarningOneOf2.md)
 - [TransactionWarningOneOf3](docs/TransactionWarningOneOf3.md)
 - [Tx](docs/Tx.md)
 - [TxHeader](docs/TxHeader.md)
 - [TxStatus](docs/TxStatus.md)
 - [Value](docs/Value.md)
 - [ValueObject](docs/ValueObject.md)
 - [ValueObjectOneOf](docs/ValueObjectOneOf.md)
 - [ValueObjectOneOf1](docs/ValueObjectOneOf1.md)
 - [ValueObjectOneOf2](docs/ValueObjectOneOf2.md)
 - [ValueObjectOneOf3](docs/ValueObjectOneOf3.md)
 - [ValueObjectOneOf4](docs/ValueObjectOneOf4.md)
 - [ValueObjectOneOf5](docs/ValueObjectOneOf5.md)
 - [ValueObjectOneOf6](docs/ValueObjectOneOf6.md)
 - [ValueObjectOneOf7](docs/ValueObjectOneOf7.md)
 - [ValueObjectOneOf8](docs/ValueObjectOneOf8.md)
 - [ValueOneOf](docs/ValueOneOf.md)
 - [ValueOneOf1](docs/ValueOneOf1.md)
 - [ValueOneOf2](docs/ValueOneOf2.md)
 - [ValueOneOf3](docs/ValueOneOf3.md)
 - [ValueOneOf4](docs/ValueOneOf4.md)
 - [ValueOneOf5](docs/ValueOneOf5.md)
 - [ValueOneOf6](docs/ValueOneOf6.md)
 - [ValueOneOf7](docs/ValueOneOf7.md)
 - [ValueOneOf8](docs/ValueOneOf8.md)
 - [Withdrawal](docs/Withdrawal.md)
 - [WithdrawalHeader](docs/WithdrawalHeader.md)
 - [WithdrawalsPost201Response](docs/WithdrawalsPost201Response.md)
 - [WithdrawalsPost201ResponseLinks](docs/WithdrawalsPost201ResponseLinks.md)


<a id="documentation-for-authorization"></a>
## Documentation For Authorization

Endpoints do not require authorization.


## Author




