# GetWithdrawalsResponseResultsInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**GetWithdrawalsResponseResultsInnerLinks**](GetWithdrawalsResponseResultsInnerLinks.md) |  | 
**resource** | [**WithdrawalHeader**](WithdrawalHeader.md) |  | 

## Example

```python
from openapi_client.models.get_withdrawals_response_results_inner import GetWithdrawalsResponseResultsInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetWithdrawalsResponseResultsInner from a JSON string
get_withdrawals_response_results_inner_instance = GetWithdrawalsResponseResultsInner.from_json(json)
# print the JSON string representation of the object
print GetWithdrawalsResponseResultsInner.to_json()

# convert the object into a dict
get_withdrawals_response_results_inner_dict = get_withdrawals_response_results_inner_instance.to_dict()
# create an instance of GetWithdrawalsResponseResultsInner from a dict
get_withdrawals_response_results_inner_form_dict = get_withdrawals_response_results_inner.from_dict(get_withdrawals_response_results_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


