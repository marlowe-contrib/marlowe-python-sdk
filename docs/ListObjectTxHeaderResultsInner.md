# ListObjectTxHeaderResultsInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**ContractsContractIdTransactionsPost201ResponseLinks**](ContractsContractIdTransactionsPost201ResponseLinks.md) |  | 
**resource** | [**TxHeader**](TxHeader.md) |  | 

## Example

```python
from openapi_client.models.list_object_tx_header_results_inner import ListObjectTxHeaderResultsInner

# TODO update the JSON string below
json = "{}"
# create an instance of ListObjectTxHeaderResultsInner from a JSON string
list_object_tx_header_results_inner_instance = ListObjectTxHeaderResultsInner.from_json(json)
# print the JSON string representation of the object
print ListObjectTxHeaderResultsInner.to_json()

# convert the object into a dict
list_object_tx_header_results_inner_dict = list_object_tx_header_results_inner_instance.to_dict()
# create an instance of ListObjectTxHeaderResultsInner from a dict
list_object_tx_header_results_inner_form_dict = list_object_tx_header_results_inner.from_dict(list_object_tx_header_results_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


