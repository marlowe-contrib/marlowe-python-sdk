# GetPayoutsResponseResultsInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**GetPayoutsResponseResultsInnerLinks**](GetPayoutsResponseResultsInnerLinks.md) |  | 
**resource** | [**PayoutHeader**](PayoutHeader.md) |  | 

## Example

```python
from openapi_client.models.get_payouts_response_results_inner import GetPayoutsResponseResultsInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetPayoutsResponseResultsInner from a JSON string
get_payouts_response_results_inner_instance = GetPayoutsResponseResultsInner.from_json(json)
# print the JSON string representation of the object
print GetPayoutsResponseResultsInner.to_json()

# convert the object into a dict
get_payouts_response_results_inner_dict = get_payouts_response_results_inner_instance.to_dict()
# create an instance of GetPayoutsResponseResultsInner from a dict
get_payouts_response_results_inner_form_dict = get_payouts_response_results_inner.from_dict(get_payouts_response_results_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


