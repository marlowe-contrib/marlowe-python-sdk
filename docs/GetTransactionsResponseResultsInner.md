# GetTransactionsResponseResultsInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**ApplyInputsResponseLinks**](ApplyInputsResponseLinks.md) |  | 
**resource** | [**TxHeader**](TxHeader.md) |  | 

## Example

```python
from openapi_client.models.get_transactions_response_results_inner import GetTransactionsResponseResultsInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetTransactionsResponseResultsInner from a JSON string
get_transactions_response_results_inner_instance = GetTransactionsResponseResultsInner.from_json(json)
# print the JSON string representation of the object
print GetTransactionsResponseResultsInner.to_json()

# convert the object into a dict
get_transactions_response_results_inner_dict = get_transactions_response_results_inner_instance.to_dict()
# create an instance of GetTransactionsResponseResultsInner from a dict
get_transactions_response_results_inner_form_dict = get_transactions_response_results_inner.from_dict(get_transactions_response_results_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


