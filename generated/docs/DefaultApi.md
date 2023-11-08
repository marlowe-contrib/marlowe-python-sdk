# openapi_client.DefaultApi

All URIs are relative to *https://marlowe-runtime-preprod-web.scdev.aws.iohkdev.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apply_inputs_to_contract**](DefaultApi.md#apply_inputs_to_contract) | **POST** /contracts/{contractId}/transactions | Apply inputs to contract
[**create_contract**](DefaultApi.md#create_contract) | **POST** /contracts | Create a new contract
[**create_contract_sources**](DefaultApi.md#create_contract_sources) | **POST** /contracts/sources | Upload contract sources
[**get_contract_by_id**](DefaultApi.md#get_contract_by_id) | **GET** /contracts/{contractId} | Get contract by ID
[**get_contract_source_adjacency**](DefaultApi.md#get_contract_source_adjacency) | **GET** /contracts/sources/{contractSourceId}/adjacency | Get adjacent contract source IDs by ID
[**get_contract_source_by_id**](DefaultApi.md#get_contract_source_by_id) | **GET** /contracts/sources/{contractSourceId} | Get contract source by ID
[**get_contract_source_closure**](DefaultApi.md#get_contract_source_closure) | **GET** /contracts/sources/{contractSourceId}/closure | Get contract source closure by ID
[**get_contract_transaction_by_id**](DefaultApi.md#get_contract_transaction_by_id) | **GET** /contracts/{contractId}/transactions/{transactionId} | Get contract transaction by ID
[**get_contracts**](DefaultApi.md#get_contracts) | **GET** /contracts | Get contracts
[**get_next_steps_for_contract**](DefaultApi.md#get_next_steps_for_contract) | **GET** /contracts/{contractId}/next | Get next contract steps
[**get_payout_by_id**](DefaultApi.md#get_payout_by_id) | **GET** /payouts/{payoutId} | Get payout by ID
[**get_payouts**](DefaultApi.md#get_payouts) | **GET** /payouts | Get role payouts
[**get_transactions_for_contract**](DefaultApi.md#get_transactions_for_contract) | **GET** /contracts/{contractId}/transactions | Get transactions for contract
[**get_withdrawal_by_id**](DefaultApi.md#get_withdrawal_by_id) | **GET** /withdrawals/{withdrawalId} | Get withdrawal by ID
[**get_withdrawals**](DefaultApi.md#get_withdrawals) | **GET** /withdrawals | Get withdrawals
[**healthcheck**](DefaultApi.md#healthcheck) | **GET** /healthcheck | Test server status
[**submit_contract**](DefaultApi.md#submit_contract) | **PUT** /contracts/{contractId} | Submit contract to chain
[**submit_contract_transaction**](DefaultApi.md#submit_contract_transaction) | **PUT** /contracts/{contractId}/transactions/{transactionId} | Submit contract input application
[**submit_withdrawal**](DefaultApi.md#submit_withdrawal) | **PUT** /withdrawals/{withdrawalId} | Submit payout withdrawal
[**withdraw_payouts**](DefaultApi.md#withdraw_payouts) | **POST** /withdrawals | Withdraw payouts


# **apply_inputs_to_contract**
> ApplyInputsResponse apply_inputs_to_contract(contract_id, x_change_address, x_address=x_address, x_collateral_utx_o=x_collateral_utx_o, post_transactions_request=post_transactions_request)

Apply inputs to contract

Build an unsigned (Cardano) transaction body which applies inputs to an open Marlowe contract. This unsigned transaction must be signed by a wallet (such as a CIP-30 or CIP-45 wallet) before being submitted. To submit the signed transaction, use the PUT /contracts/{contractId}/transactions/{transactionId} endpoint.

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.apply_inputs_response import ApplyInputsResponse
from openapi_client.models.post_transactions_request import PostTransactionsRequest
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://marlowe-runtime-preprod-web.scdev.aws.iohkdev.io
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://marlowe-runtime-preprod-web.scdev.aws.iohkdev.io"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    contract_id = '98d601c9307dd43307cf68a03aad0086d4e07a789b66919ccf9f7f7676577eb7%231' # str | 
    x_change_address = 'addr1w94f8ywk4fg672xasahtk4t9k6w3aql943uxz5rt62d4dvq8evxaf' # str | 
    x_address = 'x_address_example' # str |  (optional)
    x_collateral_utx_o = 'x_collateral_utx_o_example' # str |  (optional)
    post_transactions_request = openapi_client.PostTransactionsRequest() # PostTransactionsRequest |  (optional)

    try:
        # Apply inputs to contract
        api_response = api_instance.apply_inputs_to_contract(contract_id, x_change_address, x_address=x_address, x_collateral_utx_o=x_collateral_utx_o, post_transactions_request=post_transactions_request)
        print("The response of DefaultApi->apply_inputs_to_contract:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->apply_inputs_to_contract: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**|  | 
 **x_change_address** | **str**|  | 
 **x_address** | **str**|  | [optional] 
 **x_collateral_utx_o** | **str**|  | [optional] 
 **post_transactions_request** | [**PostTransactionsRequest**](PostTransactionsRequest.md)|  | [optional] 

### Return type

[**ApplyInputsResponse**](ApplyInputsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=utf-8
 - **Accept**: application/vendor.iog.marlowe-runtime.apply-inputs-tx-json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  * X-Network-Id -  <br>  * X-Node-Tip -  <br>  * X-Runtime-Chain-Tip -  <br>  * X-Runtime-Tip -  <br>  * X-Runtime-Version -  <br>  |
**400** | Invalid &#x60;X-Collateral-UTxO&#x60; or &#x60;X-Address&#x60; or &#x60;X-Change-Address&#x60; or &#x60;body&#x60; |  -  |
**404** | &#x60;contractId&#x60; not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_contract**
> CreateContractResponse create_contract(x_change_address, x_stake_address=x_stake_address, x_address=x_address, x_collateral_utx_o=x_collateral_utx_o, post_contracts_request=post_contracts_request)

Create a new contract

Build an unsigned (Cardano) transaction body which opens a new Marlowe contract. This unsigned transaction must be signed by a wallet (such as a CIP-30 or CIP-45 wallet) before being submitted. To submit the signed transaction, use the PUT /contracts/{contractId} endpoint.

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.create_contract_response import CreateContractResponse
from openapi_client.models.post_contracts_request import PostContractsRequest
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://marlowe-runtime-preprod-web.scdev.aws.iohkdev.io
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://marlowe-runtime-preprod-web.scdev.aws.iohkdev.io"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    x_change_address = 'addr1w94f8ywk4fg672xasahtk4t9k6w3aql943uxz5rt62d4dvq8evxaf' # str | 
    x_stake_address = 'stake1ux7lyy9nhecm033qsmel9awnr22up6jadlzkrxufr78w82gsfsn0d' # str | Where to send staking rewards for the Marlowe script outputs of this contract. (optional)
    x_address = 'x_address_example' # str |  (optional)
    x_collateral_utx_o = 'x_collateral_utx_o_example' # str |  (optional)
    post_contracts_request = openapi_client.PostContractsRequest() # PostContractsRequest |  (optional)

    try:
        # Create a new contract
        api_response = api_instance.create_contract(x_change_address, x_stake_address=x_stake_address, x_address=x_address, x_collateral_utx_o=x_collateral_utx_o, post_contracts_request=post_contracts_request)
        print("The response of DefaultApi->create_contract:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->create_contract: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_change_address** | **str**|  | 
 **x_stake_address** | **str**| Where to send staking rewards for the Marlowe script outputs of this contract. | [optional] 
 **x_address** | **str**|  | [optional] 
 **x_collateral_utx_o** | **str**|  | [optional] 
 **post_contracts_request** | [**PostContractsRequest**](PostContractsRequest.md)|  | [optional] 

### Return type

[**CreateContractResponse**](CreateContractResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=utf-8
 - **Accept**: application/vendor.iog.marlowe-runtime.contract-tx-json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  * X-Network-Id -  <br>  * X-Node-Tip -  <br>  * X-Runtime-Chain-Tip -  <br>  * X-Runtime-Tip -  <br>  * X-Runtime-Version -  <br>  |
**400** | Invalid &#x60;X-Collateral-UTxO&#x60; or &#x60;X-Address&#x60; or &#x60;X-Change-Address&#x60; or &#x60;body&#x60; or &#x60;X-Stake-Address&#x60; |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_contract_sources**
> PostContractSourceResponse create_contract_sources(main, labelled_object=labelled_object)

Upload contract sources

Upload a bundle of marlowe objects as contract sources. This API supports request body streaming, with newline framing between request bundles.

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.labelled_object import LabelledObject
from openapi_client.models.post_contract_source_response import PostContractSourceResponse
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://marlowe-runtime-preprod-web.scdev.aws.iohkdev.io
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://marlowe-runtime-preprod-web.scdev.aws.iohkdev.io"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    main = 'main_example' # str | The label of the top-level contract object in the bundle(s).
    labelled_object = [openapi_client.LabelledObject()] # List[LabelledObject] |  (optional)

    try:
        # Upload contract sources
        api_response = api_instance.create_contract_sources(main, labelled_object=labelled_object)
        print("The response of DefaultApi->create_contract_sources:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->create_contract_sources: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **main** | **str**| The label of the top-level contract object in the bundle(s). | 
 **labelled_object** | [**List[LabelledObject]**](LabelledObject.md)|  | [optional] 

### Return type

[**PostContractSourceResponse**](PostContractSourceResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/json;charset=utf-8
 - **Accept**: application/json;charset=utf-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  * X-Network-Id -  <br>  * X-Node-Tip -  <br>  * X-Runtime-Chain-Tip -  <br>  * X-Runtime-Tip -  <br>  * X-Runtime-Version -  <br>  |
**400** | Invalid &#x60;body&#x60; or &#x60;main&#x60; |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_contract_by_id**
> GetContractResponse get_contract_by_id(contract_id)

Get contract by ID

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.get_contract_response import GetContractResponse
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://marlowe-runtime-preprod-web.scdev.aws.iohkdev.io
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://marlowe-runtime-preprod-web.scdev.aws.iohkdev.io"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    contract_id = '98d601c9307dd43307cf68a03aad0086d4e07a789b66919ccf9f7f7676577eb7%231' # str | 

    try:
        # Get contract by ID
        api_response = api_instance.get_contract_by_id(contract_id)
        print("The response of DefaultApi->get_contract_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_contract_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**|  | 

### Return type

[**GetContractResponse**](GetContractResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=utf-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  * X-Network-Id -  <br>  * X-Node-Tip -  <br>  * X-Runtime-Chain-Tip -  <br>  * X-Runtime-Tip -  <br>  * X-Runtime-Version -  <br>  |
**404** | &#x60;contractId&#x60; not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_contract_source_adjacency**
> ContractSourceIds get_contract_source_adjacency(contract_source_id)

Get adjacent contract source IDs by ID

Get the contract source IDs which are adjacent to a contract source (they appear directly in the contract source).

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.contract_source_ids import ContractSourceIds
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://marlowe-runtime-preprod-web.scdev.aws.iohkdev.io
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://marlowe-runtime-preprod-web.scdev.aws.iohkdev.io"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    contract_source_id = 'contract_source_id_example' # str | 

    try:
        # Get adjacent contract source IDs by ID
        api_response = api_instance.get_contract_source_adjacency(contract_source_id)
        print("The response of DefaultApi->get_contract_source_adjacency:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_contract_source_adjacency: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_source_id** | **str**|  | 

### Return type

[**ContractSourceIds**](ContractSourceIds.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=utf-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  * X-Network-Id -  <br>  * X-Node-Tip -  <br>  * X-Runtime-Chain-Tip -  <br>  * X-Runtime-Tip -  <br>  * X-Runtime-Version -  <br>  |
**404** | &#x60;contractSourceId&#x60; not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_contract_source_by_id**
> Contract get_contract_source_by_id(contract_source_id, expand=expand)

Get contract source by ID

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.contract import Contract
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://marlowe-runtime-preprod-web.scdev.aws.iohkdev.io
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://marlowe-runtime-preprod-web.scdev.aws.iohkdev.io"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    contract_source_id = 'contract_source_id_example' # str | 
    expand = False # bool |  (optional) (default to False)

    try:
        # Get contract source by ID
        api_response = api_instance.get_contract_source_by_id(contract_source_id, expand=expand)
        print("The response of DefaultApi->get_contract_source_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_contract_source_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_source_id** | **str**|  | 
 **expand** | **bool**|  | [optional] [default to False]

### Return type

[**Contract**](Contract.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=utf-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  * X-Network-Id -  <br>  * X-Node-Tip -  <br>  * X-Runtime-Chain-Tip -  <br>  * X-Runtime-Tip -  <br>  * X-Runtime-Version -  <br>  |
**400** | Invalid &#x60;expand&#x60; |  -  |
**404** | &#x60;contractSourceId&#x60; not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_contract_source_closure**
> ContractSourceIds get_contract_source_closure(contract_source_id)

Get contract source closure by ID

Get the contract source IDs which appear in the full hierarchy of a contract source (including the ID of the contract source its self).

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.contract_source_ids import ContractSourceIds
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://marlowe-runtime-preprod-web.scdev.aws.iohkdev.io
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://marlowe-runtime-preprod-web.scdev.aws.iohkdev.io"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    contract_source_id = 'contract_source_id_example' # str | 

    try:
        # Get contract source closure by ID
        api_response = api_instance.get_contract_source_closure(contract_source_id)
        print("The response of DefaultApi->get_contract_source_closure:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_contract_source_closure: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_source_id** | **str**|  | 

### Return type

[**ContractSourceIds**](ContractSourceIds.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=utf-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  * X-Network-Id -  <br>  * X-Node-Tip -  <br>  * X-Runtime-Chain-Tip -  <br>  * X-Runtime-Tip -  <br>  * X-Runtime-Version -  <br>  |
**404** | &#x60;contractSourceId&#x60; not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_contract_transaction_by_id**
> GetTransactionResponse get_contract_transaction_by_id(contract_id, transaction_id)

Get contract transaction by ID

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.get_transaction_response import GetTransactionResponse
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://marlowe-runtime-preprod-web.scdev.aws.iohkdev.io
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://marlowe-runtime-preprod-web.scdev.aws.iohkdev.io"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    contract_id = '98d601c9307dd43307cf68a03aad0086d4e07a789b66919ccf9f7f7676577eb7%231' # str | 
    transaction_id = 'transaction_id_example' # str | 

    try:
        # Get contract transaction by ID
        api_response = api_instance.get_contract_transaction_by_id(contract_id, transaction_id)
        print("The response of DefaultApi->get_contract_transaction_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_contract_transaction_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**|  | 
 **transaction_id** | **str**|  | 

### Return type

[**GetTransactionResponse**](GetTransactionResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=utf-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  * X-Network-Id -  <br>  * X-Node-Tip -  <br>  * X-Runtime-Chain-Tip -  <br>  * X-Runtime-Tip -  <br>  * X-Runtime-Version -  <br>  |
**404** | &#x60;contractId&#x60; or &#x60;transactionId&#x60; not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_contracts**
> GetContractsResponse get_contracts(role_currency=role_currency, tag=tag, party_address=party_address, party_role=party_role, range=range)

Get contracts

Get contracts published on chain. Results are returned in pages, with paging being specified by request headers.

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.get_contracts_response import GetContractsResponse
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://marlowe-runtime-preprod-web.scdev.aws.iohkdev.io
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://marlowe-runtime-preprod-web.scdev.aws.iohkdev.io"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    role_currency = ['role_currency_example'] # List[str] |  (optional)
    tag = ['tag_example'] # List[str] |  (optional)
    party_address = ['party_address_example'] # List[str] |  (optional)
    party_role = ['party_role_example'] # List[str] |  (optional)
    range = 'range_example' # str |  (optional)

    try:
        # Get contracts
        api_response = api_instance.get_contracts(role_currency=role_currency, tag=tag, party_address=party_address, party_role=party_role, range=range)
        print("The response of DefaultApi->get_contracts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_contracts: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role_currency** | [**List[str]**](str.md)|  | [optional] 
 **tag** | [**List[str]**](str.md)|  | [optional] 
 **party_address** | [**List[str]**](str.md)|  | [optional] 
 **party_role** | [**List[str]**](str.md)|  | [optional] 
 **range** | **str**|  | [optional] 

### Return type

[**GetContractsResponse**](GetContractsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=utf-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**206** |  |  * Accept-Ranges -  <br>  * Content-Range -  <br>  * Next-Range -  <br>  * Total-Count -  <br>  * X-Network-Id -  <br>  * X-Node-Tip -  <br>  * X-Runtime-Chain-Tip -  <br>  * X-Runtime-Tip -  <br>  * X-Runtime-Version -  <br>  |
**400** | Invalid &#x60;Range&#x60; or &#x60;partyRole&#x60; or &#x60;partyAddress&#x60; or &#x60;tag&#x60; or &#x60;roleCurrency&#x60; |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_next_steps_for_contract**
> Next get_next_steps_for_contract(contract_id, validity_start, validity_end, party=party)

Get next contract steps

Get inputs which could be performed on a contract withing a time range by the requested parties.

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.next import Next
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://marlowe-runtime-preprod-web.scdev.aws.iohkdev.io
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://marlowe-runtime-preprod-web.scdev.aws.iohkdev.io"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    contract_id = '98d601c9307dd43307cf68a03aad0086d4e07a789b66919ccf9f7f7676577eb7%231' # str | 
    validity_start = 'validity_start_example' # str | The beginning of the validity range.
    validity_end = 'validity_end_example' # str | The end of the validity range.
    party = ['party_example'] # List[str] |  (optional)

    try:
        # Get next contract steps
        api_response = api_instance.get_next_steps_for_contract(contract_id, validity_start, validity_end, party=party)
        print("The response of DefaultApi->get_next_steps_for_contract:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_next_steps_for_contract: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**|  | 
 **validity_start** | **str**| The beginning of the validity range. | 
 **validity_end** | **str**| The end of the validity range. | 
 **party** | [**List[str]**](str.md)|  | [optional] 

### Return type

[**Next**](Next.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=utf-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  * X-Network-Id -  <br>  * X-Node-Tip -  <br>  * X-Runtime-Chain-Tip -  <br>  * X-Runtime-Tip -  <br>  * X-Runtime-Version -  <br>  |
**400** | Invalid &#x60;party&#x60; or &#x60;validityEnd&#x60; or &#x60;validityStart&#x60; |  -  |
**404** | &#x60;contractId&#x60; not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_payout_by_id**
> GetPayoutResponse get_payout_by_id(payout_id)

Get payout by ID

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.get_payout_response import GetPayoutResponse
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://marlowe-runtime-preprod-web.scdev.aws.iohkdev.io
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://marlowe-runtime-preprod-web.scdev.aws.iohkdev.io"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    payout_id = '98d601c9307dd43307cf68a03aad0086d4e07a789b66919ccf9f7f7676577eb7%231' # str | 

    try:
        # Get payout by ID
        api_response = api_instance.get_payout_by_id(payout_id)
        print("The response of DefaultApi->get_payout_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_payout_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payout_id** | **str**|  | 

### Return type

[**GetPayoutResponse**](GetPayoutResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=utf-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  * X-Network-Id -  <br>  * X-Node-Tip -  <br>  * X-Runtime-Chain-Tip -  <br>  * X-Runtime-Tip -  <br>  * X-Runtime-Version -  <br>  |
**404** | &#x60;payoutId&#x60; not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_payouts**
> GetContractsResponse get_payouts(contract_id=contract_id, role_token=role_token, status=status, range=range)

Get role payouts

Get payouts to parties from role-based contracts. Results are returned in pages, with paging being specified by request headers.

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.get_contracts_response import GetContractsResponse
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://marlowe-runtime-preprod-web.scdev.aws.iohkdev.io
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://marlowe-runtime-preprod-web.scdev.aws.iohkdev.io"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    contract_id = ['contract_id_example'] # List[str] |  (optional)
    role_token = ['role_token_example'] # List[str] |  (optional)
    status = 'status_example' # str | Whether to include available or withdrawn payouts in the results. (optional)
    range = 'range_example' # str |  (optional)

    try:
        # Get role payouts
        api_response = api_instance.get_payouts(contract_id=contract_id, role_token=role_token, status=status, range=range)
        print("The response of DefaultApi->get_payouts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_payouts: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | [**List[str]**](str.md)|  | [optional] 
 **role_token** | [**List[str]**](str.md)|  | [optional] 
 **status** | **str**| Whether to include available or withdrawn payouts in the results. | [optional] 
 **range** | **str**|  | [optional] 

### Return type

[**GetContractsResponse**](GetContractsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=utf-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**206** |  |  * Accept-Ranges -  <br>  * Content-Range -  <br>  * Next-Range -  <br>  * Total-Count -  <br>  * X-Network-Id -  <br>  * X-Node-Tip -  <br>  * X-Runtime-Chain-Tip -  <br>  * X-Runtime-Tip -  <br>  * X-Runtime-Version -  <br>  |
**400** | Invalid &#x60;Range&#x60; or &#x60;status&#x60; or &#x60;roleToken&#x60; or &#x60;contractId&#x60; |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_transactions_for_contract**
> GetContractsResponse get_transactions_for_contract(contract_id, range=range)

Get transactions for contract

Get published transactions for a contract. Results are returned in pages, with paging being specified by request headers.

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.get_contracts_response import GetContractsResponse
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://marlowe-runtime-preprod-web.scdev.aws.iohkdev.io
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://marlowe-runtime-preprod-web.scdev.aws.iohkdev.io"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    contract_id = '98d601c9307dd43307cf68a03aad0086d4e07a789b66919ccf9f7f7676577eb7%231' # str | 
    range = 'range_example' # str |  (optional)

    try:
        # Get transactions for contract
        api_response = api_instance.get_transactions_for_contract(contract_id, range=range)
        print("The response of DefaultApi->get_transactions_for_contract:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_transactions_for_contract: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**|  | 
 **range** | **str**|  | [optional] 

### Return type

[**GetContractsResponse**](GetContractsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=utf-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**206** |  |  * Accept-Ranges -  <br>  * Content-Range -  <br>  * Next-Range -  <br>  * Total-Count -  <br>  * X-Network-Id -  <br>  * X-Node-Tip -  <br>  * X-Runtime-Chain-Tip -  <br>  * X-Runtime-Tip -  <br>  * X-Runtime-Version -  <br>  |
**400** | Invalid &#x60;Range&#x60; |  -  |
**404** | &#x60;contractId&#x60; not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_withdrawal_by_id**
> Withdrawal get_withdrawal_by_id(withdrawal_id)

Get withdrawal by ID

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.withdrawal import Withdrawal
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://marlowe-runtime-preprod-web.scdev.aws.iohkdev.io
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://marlowe-runtime-preprod-web.scdev.aws.iohkdev.io"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    withdrawal_id = 'withdrawal_id_example' # str | 

    try:
        # Get withdrawal by ID
        api_response = api_instance.get_withdrawal_by_id(withdrawal_id)
        print("The response of DefaultApi->get_withdrawal_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_withdrawal_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **withdrawal_id** | **str**|  | 

### Return type

[**Withdrawal**](Withdrawal.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=utf-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  * X-Network-Id -  <br>  * X-Node-Tip -  <br>  * X-Runtime-Chain-Tip -  <br>  * X-Runtime-Tip -  <br>  * X-Runtime-Version -  <br>  |
**404** | &#x60;withdrawalId&#x60; not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_withdrawals**
> GetContractsResponse get_withdrawals(role_currency=role_currency, range=range)

Get withdrawals

Get published withdrawal transactions. Results are returned in pages, with paging being specified by request headers.

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.get_contracts_response import GetContractsResponse
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://marlowe-runtime-preprod-web.scdev.aws.iohkdev.io
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://marlowe-runtime-preprod-web.scdev.aws.iohkdev.io"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    role_currency = ['role_currency_example'] # List[str] |  (optional)
    range = 'range_example' # str |  (optional)

    try:
        # Get withdrawals
        api_response = api_instance.get_withdrawals(role_currency=role_currency, range=range)
        print("The response of DefaultApi->get_withdrawals:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_withdrawals: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role_currency** | [**List[str]**](str.md)|  | [optional] 
 **range** | **str**|  | [optional] 

### Return type

[**GetContractsResponse**](GetContractsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=utf-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**206** |  |  * Accept-Ranges -  <br>  * Content-Range -  <br>  * Next-Range -  <br>  * Total-Count -  <br>  * X-Network-Id -  <br>  * X-Node-Tip -  <br>  * X-Runtime-Chain-Tip -  <br>  * X-Runtime-Tip -  <br>  * X-Runtime-Version -  <br>  |
**400** | Invalid &#x60;Range&#x60; or &#x60;roleCurrency&#x60; |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **healthcheck**
> healthcheck()

Test server status

Check if the server is running and ready to respond to requests.

### Example

```python
import time
import os
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://marlowe-runtime-preprod-web.scdev.aws.iohkdev.io
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://marlowe-runtime-preprod-web.scdev.aws.iohkdev.io"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)

    try:
        # Test server status
        api_instance.healthcheck()
    except Exception as e:
        print("Exception when calling DefaultApi->healthcheck: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=utf-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  * X-Network-Id -  <br>  * X-Node-Tip -  <br>  * X-Runtime-Chain-Tip -  <br>  * X-Runtime-Tip -  <br>  * X-Runtime-Version -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **submit_contract**
> submit_contract(contract_id, text_envelope=text_envelope)

Submit contract to chain

Submit a signed (Cardano) transaction that opens a new Marlowe contract. The transaction must have originally been created by the POST /contracts endpoint. This endpoint will respond when the transaction is submitted successfully to the local node, which means it will not wait for the transaction to be published in a block. Use the GET /contracts/{contractId} endpoint to poll the on-chain status.

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.text_envelope import TextEnvelope
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://marlowe-runtime-preprod-web.scdev.aws.iohkdev.io
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://marlowe-runtime-preprod-web.scdev.aws.iohkdev.io"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    contract_id = '98d601c9307dd43307cf68a03aad0086d4e07a789b66919ccf9f7f7676577eb7%231' # str | 
    text_envelope = openapi_client.TextEnvelope() # TextEnvelope |  (optional)

    try:
        # Submit contract to chain
        api_instance.submit_contract(contract_id, text_envelope=text_envelope)
    except Exception as e:
        print("Exception when calling DefaultApi->submit_contract: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**|  | 
 **text_envelope** | [**TextEnvelope**](TextEnvelope.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=utf-8
 - **Accept**: application/json;charset=utf-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** |  |  * X-Network-Id -  <br>  * X-Node-Tip -  <br>  * X-Runtime-Chain-Tip -  <br>  * X-Runtime-Tip -  <br>  * X-Runtime-Version -  <br>  |
**400** | Invalid &#x60;body&#x60; |  -  |
**404** | &#x60;contractId&#x60; not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **submit_contract_transaction**
> submit_contract_transaction(contract_id, transaction_id, text_envelope=text_envelope)

Submit contract input application

Submit a signed (Cardano) transaction that applies inputs to an open Marlowe contract. The transaction must have originally been created by the POST /contracts/{contractId}/transactions endpoint. This endpoint will respond when the transaction is submitted successfully to the local node, which means it will not wait for the transaction to be published in a block. Use the GET /contracts/{contractId}/transactions/{transactionId} endpoint to poll the on-chain status.

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.text_envelope import TextEnvelope
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://marlowe-runtime-preprod-web.scdev.aws.iohkdev.io
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://marlowe-runtime-preprod-web.scdev.aws.iohkdev.io"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    contract_id = '98d601c9307dd43307cf68a03aad0086d4e07a789b66919ccf9f7f7676577eb7%231' # str | 
    transaction_id = 'transaction_id_example' # str | 
    text_envelope = openapi_client.TextEnvelope() # TextEnvelope |  (optional)

    try:
        # Submit contract input application
        api_instance.submit_contract_transaction(contract_id, transaction_id, text_envelope=text_envelope)
    except Exception as e:
        print("Exception when calling DefaultApi->submit_contract_transaction: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**|  | 
 **transaction_id** | **str**|  | 
 **text_envelope** | [**TextEnvelope**](TextEnvelope.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=utf-8
 - **Accept**: application/json;charset=utf-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** |  |  * X-Network-Id -  <br>  * X-Node-Tip -  <br>  * X-Runtime-Chain-Tip -  <br>  * X-Runtime-Tip -  <br>  * X-Runtime-Version -  <br>  |
**400** | Invalid &#x60;body&#x60; |  -  |
**404** | &#x60;contractId&#x60; or &#x60;transactionId&#x60; not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **submit_withdrawal**
> submit_withdrawal(withdrawal_id, text_envelope=text_envelope)

Submit payout withdrawal

Submit a signed (Cardano) transaction that withdraws available payouts from a role payout validator. The transaction must have originally been created by the POST /withdrawals endpoint. This endpoint will respond when the transaction is submitted successfully to the local node, which means it will not wait for the transaction to be published in a block. Use the GET /withdrawals/{withdrawalId} endpoint to poll the on-chain status.

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.text_envelope import TextEnvelope
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://marlowe-runtime-preprod-web.scdev.aws.iohkdev.io
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://marlowe-runtime-preprod-web.scdev.aws.iohkdev.io"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    withdrawal_id = 'withdrawal_id_example' # str | 
    text_envelope = openapi_client.TextEnvelope() # TextEnvelope |  (optional)

    try:
        # Submit payout withdrawal
        api_instance.submit_withdrawal(withdrawal_id, text_envelope=text_envelope)
    except Exception as e:
        print("Exception when calling DefaultApi->submit_withdrawal: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **withdrawal_id** | **str**|  | 
 **text_envelope** | [**TextEnvelope**](TextEnvelope.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=utf-8
 - **Accept**: application/json;charset=utf-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** |  |  * X-Network-Id -  <br>  * X-Node-Tip -  <br>  * X-Runtime-Chain-Tip -  <br>  * X-Runtime-Tip -  <br>  * X-Runtime-Version -  <br>  |
**400** | Invalid &#x60;body&#x60; |  -  |
**404** | &#x60;withdrawalId&#x60; not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **withdraw_payouts**
> WithdrawPayoutsResponse withdraw_payouts(x_change_address, x_address=x_address, x_collateral_utx_o=x_collateral_utx_o, post_withdrawals_request=post_withdrawals_request)

Withdraw payouts

Build an unsigned (Cardano) transaction body which withdraws available payouts from a role payout validator. This unsigned transaction must be signed by a wallet (such as a CIP-30 or CIP-45 wallet) before being submitted. To submit the signed transaction, use the PUT /withdrawals/{withdrawalId} endpoint.

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.post_withdrawals_request import PostWithdrawalsRequest
from openapi_client.models.withdraw_payouts_response import WithdrawPayoutsResponse
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://marlowe-runtime-preprod-web.scdev.aws.iohkdev.io
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://marlowe-runtime-preprod-web.scdev.aws.iohkdev.io"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    x_change_address = 'addr1w94f8ywk4fg672xasahtk4t9k6w3aql943uxz5rt62d4dvq8evxaf' # str | 
    x_address = 'x_address_example' # str |  (optional)
    x_collateral_utx_o = 'x_collateral_utx_o_example' # str |  (optional)
    post_withdrawals_request = openapi_client.PostWithdrawalsRequest() # PostWithdrawalsRequest |  (optional)

    try:
        # Withdraw payouts
        api_response = api_instance.withdraw_payouts(x_change_address, x_address=x_address, x_collateral_utx_o=x_collateral_utx_o, post_withdrawals_request=post_withdrawals_request)
        print("The response of DefaultApi->withdraw_payouts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->withdraw_payouts: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_change_address** | **str**|  | 
 **x_address** | **str**|  | [optional] 
 **x_collateral_utx_o** | **str**|  | [optional] 
 **post_withdrawals_request** | [**PostWithdrawalsRequest**](PostWithdrawalsRequest.md)|  | [optional] 

### Return type

[**WithdrawPayoutsResponse**](WithdrawPayoutsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=utf-8
 - **Accept**: application/vendor.iog.marlowe-runtime.withdraw-tx-json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  * X-Network-Id -  <br>  * X-Node-Tip -  <br>  * X-Runtime-Chain-Tip -  <br>  * X-Runtime-Tip -  <br>  * X-Runtime-Version -  <br>  |
**400** | Invalid &#x60;X-Collateral-UTxO&#x60; or &#x60;X-Address&#x60; or &#x60;X-Change-Address&#x60; or &#x60;body&#x60; |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

