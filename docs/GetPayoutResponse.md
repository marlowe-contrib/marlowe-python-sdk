# GetPayoutResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**GetPayoutResponseLinks**](GetPayoutResponseLinks.md) |  | 
**resource** | [**PayoutState**](PayoutState.md) |  | 

## Example

```python
from openapi_client.models.get_payout_response import GetPayoutResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetPayoutResponse from a JSON string
get_payout_response_instance = GetPayoutResponse.from_json(json)
# print the JSON string representation of the object
print GetPayoutResponse.to_json()

# convert the object into a dict
get_payout_response_dict = get_payout_response_instance.to_dict()
# create an instance of GetPayoutResponse from a dict
get_payout_response_form_dict = get_payout_response.from_dict(get_payout_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


