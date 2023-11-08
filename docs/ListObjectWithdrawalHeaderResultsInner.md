# ListObjectWithdrawalHeaderResultsInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**WithdrawalsPost201ResponseLinks**](WithdrawalsPost201ResponseLinks.md) |  | 
**resource** | [**WithdrawalHeader**](WithdrawalHeader.md) |  | 

## Example

```python
from openapi_client.models.list_object_withdrawal_header_results_inner import ListObjectWithdrawalHeaderResultsInner

# TODO update the JSON string below
json = "{}"
# create an instance of ListObjectWithdrawalHeaderResultsInner from a JSON string
list_object_withdrawal_header_results_inner_instance = ListObjectWithdrawalHeaderResultsInner.from_json(json)
# print the JSON string representation of the object
print ListObjectWithdrawalHeaderResultsInner.to_json()

# convert the object into a dict
list_object_withdrawal_header_results_inner_dict = list_object_withdrawal_header_results_inner_instance.to_dict()
# create an instance of ListObjectWithdrawalHeaderResultsInner from a dict
list_object_withdrawal_header_results_inner_form_dict = list_object_withdrawal_header_results_inner.from_dict(list_object_withdrawal_header_results_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


