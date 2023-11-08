# openapi_client.DefaultApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**contracts_contract_id_get**](DefaultApi.md#contracts_contract_id_get) | **GET** /contracts/{contractId} | 
[**contracts_contract_id_next_get**](DefaultApi.md#contracts_contract_id_next_get) | **GET** /contracts/{contractId}/next | 
[**contracts_contract_id_put**](DefaultApi.md#contracts_contract_id_put) | **PUT** /contracts/{contractId} | 
[**contracts_contract_id_transactions_get**](DefaultApi.md#contracts_contract_id_transactions_get) | **GET** /contracts/{contractId}/transactions | 
[**contracts_contract_id_transactions_post**](DefaultApi.md#contracts_contract_id_transactions_post) | **POST** /contracts/{contractId}/transactions | 
[**contracts_contract_id_transactions_transaction_id_get**](DefaultApi.md#contracts_contract_id_transactions_transaction_id_get) | **GET** /contracts/{contractId}/transactions/{transactionId} | 
[**contracts_contract_id_transactions_transaction_id_put**](DefaultApi.md#contracts_contract_id_transactions_transaction_id_put) | **PUT** /contracts/{contractId}/transactions/{transactionId} | 
[**contracts_get**](DefaultApi.md#contracts_get) | **GET** /contracts | 
[**contracts_post**](DefaultApi.md#contracts_post) | **POST** /contracts | 
[**contracts_sources_contract_source_id_adjacency_get**](DefaultApi.md#contracts_sources_contract_source_id_adjacency_get) | **GET** /contracts/sources/{contractSourceId}/adjacency | 
[**contracts_sources_contract_source_id_closure_get**](DefaultApi.md#contracts_sources_contract_source_id_closure_get) | **GET** /contracts/sources/{contractSourceId}/closure | 
[**contracts_sources_contract_source_id_get**](DefaultApi.md#contracts_sources_contract_source_id_get) | **GET** /contracts/sources/{contractSourceId} | 
[**contracts_sources_post**](DefaultApi.md#contracts_sources_post) | **POST** /contracts/sources | 
[**healthcheck_get**](DefaultApi.md#healthcheck_get) | **GET** /healthcheck | 
[**payouts_get**](DefaultApi.md#payouts_get) | **GET** /payouts | 
[**payouts_payout_id_get**](DefaultApi.md#payouts_payout_id_get) | **GET** /payouts/{payoutId} | 
[**withdrawals_get**](DefaultApi.md#withdrawals_get) | **GET** /withdrawals | 
[**withdrawals_post**](DefaultApi.md#withdrawals_post) | **POST** /withdrawals | 
[**withdrawals_withdrawal_id_get**](DefaultApi.md#withdrawals_withdrawal_id_get) | **GET** /withdrawals/{withdrawalId} | 
[**withdrawals_withdrawal_id_put**](DefaultApi.md#withdrawals_withdrawal_id_put) | **PUT** /withdrawals/{withdrawalId} | 


# **contracts_contract_id_get**
> ContractsContractIdGet200Response contracts_contract_id_get(contract_id)



### Example

```python
import time
import os
import openapi_client
from openapi_client.models.contracts_contract_id_get200_response import ContractsContractIdGet200Response
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
    except Exception as e:
        print("Exception when calling DefaultApi->contracts_contract_id_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**|  | 

### Return type

[**ContractsContractIdGet200Response**](ContractsContractIdGet200Response.md)

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

# **contracts_contract_id_next_get**
> Next contracts_contract_id_next_get(contract_id, validity_start, validity_end, party=party)



### Example

```python
import time
import os
import openapi_client
from openapi_client.models.next import Next
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
    validity_start = 'validity_start_example' # str | 
    validity_end = 'validity_end_example' # str | 
    party = ['party_example'] # List[str] |  (optional)

    try:
        api_response = api_instance.contracts_contract_id_next_get(contract_id, validity_start, validity_end, party=party)
        print("The response of DefaultApi->contracts_contract_id_next_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->contracts_contract_id_next_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**|  | 
 **validity_start** | **str**|  | 
 **validity_end** | **str**|  | 
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

# **contracts_contract_id_put**
> contracts_contract_id_put(contract_id, text_envelope=text_envelope)



### Example

```python
import time
import os
import openapi_client
from openapi_client.models.text_envelope import TextEnvelope
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
    text_envelope = openapi_client.TextEnvelope() # TextEnvelope |  (optional)

    try:
        api_instance.contracts_contract_id_put(contract_id, text_envelope=text_envelope)
    except Exception as e:
        print("Exception when calling DefaultApi->contracts_contract_id_put: %s\n" % e)
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

# **contracts_contract_id_transactions_get**
> ListObjectTxHeader contracts_contract_id_transactions_get(contract_id, range=range)



### Example

```python
import time
import os
import openapi_client
from openapi_client.models.list_object_tx_header import ListObjectTxHeader
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
    range = 'range_example' # str |  (optional)

    try:
        api_response = api_instance.contracts_contract_id_transactions_get(contract_id, range=range)
        print("The response of DefaultApi->contracts_contract_id_transactions_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->contracts_contract_id_transactions_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**|  | 
 **range** | **str**|  | [optional] 

### Return type

[**ListObjectTxHeader**](ListObjectTxHeader.md)

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

# **contracts_contract_id_transactions_post**
> ContractsContractIdTransactionsPost201Response contracts_contract_id_transactions_post(contract_id, x_change_address, x_address=x_address, x_collateral_utx_o=x_collateral_utx_o, post_transactions_request=post_transactions_request)



### Example

```python
import time
import os
import openapi_client
from openapi_client.models.contracts_contract_id_transactions_post201_response import ContractsContractIdTransactionsPost201Response
from openapi_client.models.post_transactions_request import PostTransactionsRequest
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
    x_change_address = 'addr1w94f8ywk4fg672xasahtk4t9k6w3aql943uxz5rt62d4dvq8evxaf' # str | 
    x_address = 'x_address_example' # str |  (optional)
    x_collateral_utx_o = 'x_collateral_utx_o_example' # str |  (optional)
    post_transactions_request = openapi_client.PostTransactionsRequest() # PostTransactionsRequest |  (optional)

    try:
        api_response = api_instance.contracts_contract_id_transactions_post(contract_id, x_change_address, x_address=x_address, x_collateral_utx_o=x_collateral_utx_o, post_transactions_request=post_transactions_request)
        print("The response of DefaultApi->contracts_contract_id_transactions_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->contracts_contract_id_transactions_post: %s\n" % e)
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

[**ContractsContractIdTransactionsPost201Response**](ContractsContractIdTransactionsPost201Response.md)

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

# **contracts_contract_id_transactions_transaction_id_get**
> ContractsContractIdTransactionsTransactionIdGet200Response contracts_contract_id_transactions_transaction_id_get(contract_id, transaction_id)



### Example

```python
import time
import os
import openapi_client
from openapi_client.models.contracts_contract_id_transactions_transaction_id_get200_response import ContractsContractIdTransactionsTransactionIdGet200Response
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
    transaction_id = 'transaction_id_example' # str | 

    try:
        api_response = api_instance.contracts_contract_id_transactions_transaction_id_get(contract_id, transaction_id)
        print("The response of DefaultApi->contracts_contract_id_transactions_transaction_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->contracts_contract_id_transactions_transaction_id_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**|  | 
 **transaction_id** | **str**|  | 

### Return type

[**ContractsContractIdTransactionsTransactionIdGet200Response**](ContractsContractIdTransactionsTransactionIdGet200Response.md)

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

# **contracts_contract_id_transactions_transaction_id_put**
> contracts_contract_id_transactions_transaction_id_put(contract_id, transaction_id, text_envelope=text_envelope)



### Example

```python
import time
import os
import openapi_client
from openapi_client.models.text_envelope import TextEnvelope
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
    transaction_id = 'transaction_id_example' # str | 
    text_envelope = openapi_client.TextEnvelope() # TextEnvelope |  (optional)

    try:
        api_instance.contracts_contract_id_transactions_transaction_id_put(contract_id, transaction_id, text_envelope=text_envelope)
    except Exception as e:
        print("Exception when calling DefaultApi->contracts_contract_id_transactions_transaction_id_put: %s\n" % e)
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

# **contracts_get**
> ListObjectContractHeader contracts_get(role_currency=role_currency, tag=tag, party_address=party_address, party_role=party_role, range=range)



### Example

```python
import time
import os
import openapi_client
from openapi_client.models.list_object_contract_header import ListObjectContractHeader
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
    role_currency = ['role_currency_example'] # List[str] |  (optional)
    tag = ['tag_example'] # List[str] |  (optional)
    party_address = ['party_address_example'] # List[str] |  (optional)
    party_role = ['party_role_example'] # List[str] |  (optional)
    range = 'range_example' # str |  (optional)

    try:
        api_response = api_instance.contracts_get(role_currency=role_currency, tag=tag, party_address=party_address, party_role=party_role, range=range)
        print("The response of DefaultApi->contracts_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->contracts_get: %s\n" % e)
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

[**ListObjectContractHeader**](ListObjectContractHeader.md)

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

# **contracts_post**
> ContractsPost201Response contracts_post(x_change_address, x_stake_address=x_stake_address, x_address=x_address, x_collateral_utx_o=x_collateral_utx_o, post_contracts_request=post_contracts_request)



### Example

```python
import time
import os
import openapi_client
from openapi_client.models.contracts_post201_response import ContractsPost201Response
from openapi_client.models.post_contracts_request import PostContractsRequest
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
    x_change_address = 'addr1w94f8ywk4fg672xasahtk4t9k6w3aql943uxz5rt62d4dvq8evxaf' # str | 
    x_stake_address = 'stake1ux7lyy9nhecm033qsmel9awnr22up6jadlzkrxufr78w82gsfsn0d' # str |  (optional)
    x_address = 'x_address_example' # str |  (optional)
    x_collateral_utx_o = 'x_collateral_utx_o_example' # str |  (optional)
    post_contracts_request = openapi_client.PostContractsRequest() # PostContractsRequest |  (optional)

    try:
        api_response = api_instance.contracts_post(x_change_address, x_stake_address=x_stake_address, x_address=x_address, x_collateral_utx_o=x_collateral_utx_o, post_contracts_request=post_contracts_request)
        print("The response of DefaultApi->contracts_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->contracts_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_change_address** | **str**|  | 
 **x_stake_address** | **str**|  | [optional] 
 **x_address** | **str**|  | [optional] 
 **x_collateral_utx_o** | **str**|  | [optional] 
 **post_contracts_request** | [**PostContractsRequest**](PostContractsRequest.md)|  | [optional] 

### Return type

[**ContractsPost201Response**](ContractsPost201Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=utf-8
 - **Accept**: application/vendor.iog.marlowe-runtime.contract-tx-json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  * X-Network-Id -  <br>  * X-Node-Tip -  <br>  * X-Runtime-Chain-Tip -  <br>  * X-Runtime-Tip -  <br>  * X-Runtime-Version -  <br>  |
**400** | Invalid &#x60;X-Collateral-UTxO&#x60; or &#x60;X-Address&#x60; or &#x60;X-Change-Address&#x60; or &#x60;X-Stake-Address&#x60; or &#x60;body&#x60; |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **contracts_sources_contract_source_id_adjacency_get**
> ListObjectContractSourceId contracts_sources_contract_source_id_adjacency_get(contract_source_id)



### Example

```python
import time
import os
import openapi_client
from openapi_client.models.list_object_contract_source_id import ListObjectContractSourceId
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
    contract_source_id = 'contract_source_id_example' # str | 

    try:
        api_response = api_instance.contracts_sources_contract_source_id_adjacency_get(contract_source_id)
        print("The response of DefaultApi->contracts_sources_contract_source_id_adjacency_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->contracts_sources_contract_source_id_adjacency_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_source_id** | **str**|  | 

### Return type

[**ListObjectContractSourceId**](ListObjectContractSourceId.md)

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

# **contracts_sources_contract_source_id_closure_get**
> ListObjectContractSourceId contracts_sources_contract_source_id_closure_get(contract_source_id)



### Example

```python
import time
import os
import openapi_client
from openapi_client.models.list_object_contract_source_id import ListObjectContractSourceId
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
    contract_source_id = 'contract_source_id_example' # str | 

    try:
        api_response = api_instance.contracts_sources_contract_source_id_closure_get(contract_source_id)
        print("The response of DefaultApi->contracts_sources_contract_source_id_closure_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->contracts_sources_contract_source_id_closure_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_source_id** | **str**|  | 

### Return type

[**ListObjectContractSourceId**](ListObjectContractSourceId.md)

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

# **contracts_sources_contract_source_id_get**
> Contract contracts_sources_contract_source_id_get(contract_source_id, expand=expand)



### Example

```python
import time
import os
import openapi_client
from openapi_client.models.contract import Contract
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
    contract_source_id = 'contract_source_id_example' # str | 
    expand = False # bool |  (optional) (default to False)

    try:
        api_response = api_instance.contracts_sources_contract_source_id_get(contract_source_id, expand=expand)
        print("The response of DefaultApi->contracts_sources_contract_source_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->contracts_sources_contract_source_id_get: %s\n" % e)
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

# **contracts_sources_post**
> PostContractSourceResponse contracts_sources_post(main, labelled_object=labelled_object)



### Example

```python
import time
import os
import openapi_client
from openapi_client.models.labelled_object import LabelledObject
from openapi_client.models.post_contract_source_response import PostContractSourceResponse
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
    main = 'main_example' # str | 
    labelled_object = [openapi_client.LabelledObject()] # List[LabelledObject] |  (optional)

    try:
        api_response = api_instance.contracts_sources_post(main, labelled_object=labelled_object)
        print("The response of DefaultApi->contracts_sources_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->contracts_sources_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **main** | **str**|  | 
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

# **healthcheck_get**
> healthcheck_get()



### Example

```python
import time
import os
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

    try:
        api_instance.healthcheck_get()
    except Exception as e:
        print("Exception when calling DefaultApi->healthcheck_get: %s\n" % e)
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

# **payouts_get**
> ListObjectPayoutHeader payouts_get(contract_id=contract_id, role_token=role_token, status=status, range=range)



### Example

```python
import time
import os
import openapi_client
from openapi_client.models.list_object_payout_header import ListObjectPayoutHeader
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
    contract_id = ['contract_id_example'] # List[str] |  (optional)
    role_token = ['role_token_example'] # List[str] |  (optional)
    status = 'status_example' # str |  (optional)
    range = 'range_example' # str |  (optional)

    try:
        api_response = api_instance.payouts_get(contract_id=contract_id, role_token=role_token, status=status, range=range)
        print("The response of DefaultApi->payouts_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->payouts_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | [**List[str]**](str.md)|  | [optional] 
 **role_token** | [**List[str]**](str.md)|  | [optional] 
 **status** | **str**|  | [optional] 
 **range** | **str**|  | [optional] 

### Return type

[**ListObjectPayoutHeader**](ListObjectPayoutHeader.md)

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

# **payouts_payout_id_get**
> PayoutsPayoutIdGet200Response payouts_payout_id_get(payout_id)



### Example

```python
import time
import os
import openapi_client
from openapi_client.models.payouts_payout_id_get200_response import PayoutsPayoutIdGet200Response
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
    payout_id = '98d601c9307dd43307cf68a03aad0086d4e07a789b66919ccf9f7f7676577eb7%231' # str | 

    try:
        api_response = api_instance.payouts_payout_id_get(payout_id)
        print("The response of DefaultApi->payouts_payout_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->payouts_payout_id_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payout_id** | **str**|  | 

### Return type

[**PayoutsPayoutIdGet200Response**](PayoutsPayoutIdGet200Response.md)

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

# **withdrawals_get**
> ListObjectWithdrawalHeader withdrawals_get(role_currency=role_currency, range=range)



### Example

```python
import time
import os
import openapi_client
from openapi_client.models.list_object_withdrawal_header import ListObjectWithdrawalHeader
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
    role_currency = ['role_currency_example'] # List[str] |  (optional)
    range = 'range_example' # str |  (optional)

    try:
        api_response = api_instance.withdrawals_get(role_currency=role_currency, range=range)
        print("The response of DefaultApi->withdrawals_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->withdrawals_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role_currency** | [**List[str]**](str.md)|  | [optional] 
 **range** | **str**|  | [optional] 

### Return type

[**ListObjectWithdrawalHeader**](ListObjectWithdrawalHeader.md)

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

# **withdrawals_post**
> WithdrawalsPost201Response withdrawals_post(x_change_address, x_address=x_address, x_collateral_utx_o=x_collateral_utx_o, post_withdrawals_request=post_withdrawals_request)



### Example

```python
import time
import os
import openapi_client
from openapi_client.models.post_withdrawals_request import PostWithdrawalsRequest
from openapi_client.models.withdrawals_post201_response import WithdrawalsPost201Response
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
    x_change_address = 'addr1w94f8ywk4fg672xasahtk4t9k6w3aql943uxz5rt62d4dvq8evxaf' # str | 
    x_address = 'x_address_example' # str |  (optional)
    x_collateral_utx_o = 'x_collateral_utx_o_example' # str |  (optional)
    post_withdrawals_request = openapi_client.PostWithdrawalsRequest() # PostWithdrawalsRequest |  (optional)

    try:
        api_response = api_instance.withdrawals_post(x_change_address, x_address=x_address, x_collateral_utx_o=x_collateral_utx_o, post_withdrawals_request=post_withdrawals_request)
        print("The response of DefaultApi->withdrawals_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->withdrawals_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_change_address** | **str**|  | 
 **x_address** | **str**|  | [optional] 
 **x_collateral_utx_o** | **str**|  | [optional] 
 **post_withdrawals_request** | [**PostWithdrawalsRequest**](PostWithdrawalsRequest.md)|  | [optional] 

### Return type

[**WithdrawalsPost201Response**](WithdrawalsPost201Response.md)

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

# **withdrawals_withdrawal_id_get**
> Withdrawal withdrawals_withdrawal_id_get(withdrawal_id)



### Example

```python
import time
import os
import openapi_client
from openapi_client.models.withdrawal import Withdrawal
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
    withdrawal_id = 'withdrawal_id_example' # str | 

    try:
        api_response = api_instance.withdrawals_withdrawal_id_get(withdrawal_id)
        print("The response of DefaultApi->withdrawals_withdrawal_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->withdrawals_withdrawal_id_get: %s\n" % e)
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

# **withdrawals_withdrawal_id_put**
> withdrawals_withdrawal_id_put(withdrawal_id, text_envelope=text_envelope)



### Example

```python
import time
import os
import openapi_client
from openapi_client.models.text_envelope import TextEnvelope
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
    withdrawal_id = 'withdrawal_id_example' # str | 
    text_envelope = openapi_client.TextEnvelope() # TextEnvelope |  (optional)

    try:
        api_instance.withdrawals_withdrawal_id_put(withdrawal_id, text_envelope=text_envelope)
    except Exception as e:
        print("Exception when calling DefaultApi->withdrawals_withdrawal_id_put: %s\n" % e)
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

