# ListObjectPayoutHeaderResultsInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**ListObjectPayoutHeaderResultsInnerLinks**](ListObjectPayoutHeaderResultsInnerLinks.md) |  | 
**resource** | [**PayoutHeader**](PayoutHeader.md) |  | 

## Example

```python
from openapi_client.models.list_object_payout_header_results_inner import ListObjectPayoutHeaderResultsInner

# TODO update the JSON string below
json = "{}"
# create an instance of ListObjectPayoutHeaderResultsInner from a JSON string
list_object_payout_header_results_inner_instance = ListObjectPayoutHeaderResultsInner.from_json(json)
# print the JSON string representation of the object
print ListObjectPayoutHeaderResultsInner.to_json()

# convert the object into a dict
list_object_payout_header_results_inner_dict = list_object_payout_header_results_inner_instance.to_dict()
# create an instance of ListObjectPayoutHeaderResultsInner from a dict
list_object_payout_header_results_inner_form_dict = list_object_payout_header_results_inner.from_dict(list_object_payout_header_results_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


