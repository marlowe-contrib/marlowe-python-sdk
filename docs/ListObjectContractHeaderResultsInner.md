# ListObjectContractHeaderResultsInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**ListObjectContractHeaderResultsInnerLinks**](ListObjectContractHeaderResultsInnerLinks.md) |  | 
**resource** | [**ContractHeader**](ContractHeader.md) |  | 

## Example

```python
from openapi_client.models.list_object_contract_header_results_inner import ListObjectContractHeaderResultsInner

# TODO update the JSON string below
json = "{}"
# create an instance of ListObjectContractHeaderResultsInner from a JSON string
list_object_contract_header_results_inner_instance = ListObjectContractHeaderResultsInner.from_json(json)
# print the JSON string representation of the object
print ListObjectContractHeaderResultsInner.to_json()

# convert the object into a dict
list_object_contract_header_results_inner_dict = list_object_contract_header_results_inner_instance.to_dict()
# create an instance of ListObjectContractHeaderResultsInner from a dict
list_object_contract_header_results_inner_form_dict = list_object_contract_header_results_inner.from_dict(list_object_contract_header_results_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


