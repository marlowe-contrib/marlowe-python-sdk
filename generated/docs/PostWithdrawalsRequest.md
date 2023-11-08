# PostWithdrawalsRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payouts** | **List[str]** |  | 

## Example

```python
from openapi_client.models.post_withdrawals_request import PostWithdrawalsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostWithdrawalsRequest from a JSON string
post_withdrawals_request_instance = PostWithdrawalsRequest.from_json(json)
# print the JSON string representation of the object
print PostWithdrawalsRequest.to_json()

# convert the object into a dict
post_withdrawals_request_dict = post_withdrawals_request_instance.to_dict()
# create an instance of PostWithdrawalsRequest from a dict
post_withdrawals_request_form_dict = post_withdrawals_request.from_dict(post_withdrawals_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


