# ListObjectPayoutHeader


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[ListObjectPayoutHeaderResultsInner]**](ListObjectPayoutHeaderResultsInner.md) |  | 

## Example

```python
from openapi_client.models.list_object_payout_header import ListObjectPayoutHeader

# TODO update the JSON string below
json = "{}"
# create an instance of ListObjectPayoutHeader from a JSON string
list_object_payout_header_instance = ListObjectPayoutHeader.from_json(json)
# print the JSON string representation of the object
print ListObjectPayoutHeader.to_json()

# convert the object into a dict
list_object_payout_header_dict = list_object_payout_header_instance.to_dict()
# create an instance of ListObjectPayoutHeader from a dict
list_object_payout_header_form_dict = list_object_payout_header.from_dict(list_object_payout_header_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


