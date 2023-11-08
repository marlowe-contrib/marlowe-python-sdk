# GetContractsResponseResultsInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**GetContractsResponseResultsInnerLinks**](GetContractsResponseResultsInnerLinks.md) |  | 
**resource** | [**PayoutHeader**](PayoutHeader.md) |  | 

## Example

```python
from openapi_client.models.get_contracts_response_results_inner import GetContractsResponseResultsInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetContractsResponseResultsInner from a JSON string
get_contracts_response_results_inner_instance = GetContractsResponseResultsInner.from_json(json)
# print the JSON string representation of the object
print GetContractsResponseResultsInner.to_json()

# convert the object into a dict
get_contracts_response_results_inner_dict = get_contracts_response_results_inner_instance.to_dict()
# create an instance of GetContractsResponseResultsInner from a dict
get_contracts_response_results_inner_form_dict = get_contracts_response_results_inner.from_dict(get_contracts_response_results_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


