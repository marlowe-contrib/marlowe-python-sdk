# PostTransactionsRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**inputs** | [**List[Input]**](Input.md) |  | 
**invalid_before** | **str** |  | [optional] 
**invalid_hereafter** | **str** |  | [optional] 
**metadata** | [**Dict[str, Metadata]**](Metadata.md) |  | 
**tags** | [**Dict[str, Metadata]**](Metadata.md) |  | 
**version** | [**MarloweVersion**](MarloweVersion.md) |  | 

## Example

```python
from openapi_client.models.post_transactions_request import PostTransactionsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostTransactionsRequest from a JSON string
post_transactions_request_instance = PostTransactionsRequest.from_json(json)
# print the JSON string representation of the object
print PostTransactionsRequest.to_json()

# convert the object into a dict
post_transactions_request_dict = post_transactions_request_instance.to_dict()
# create an instance of PostTransactionsRequest from a dict
post_transactions_request_form_dict = post_transactions_request.from_dict(post_transactions_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


