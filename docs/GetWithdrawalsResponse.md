# GetWithdrawalsResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[GetWithdrawalsResponseResultsInner]**](GetWithdrawalsResponseResultsInner.md) |  | 

## Example

```python
from openapi_client.models.get_withdrawals_response import GetWithdrawalsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetWithdrawalsResponse from a JSON string
get_withdrawals_response_instance = GetWithdrawalsResponse.from_json(json)
# print the JSON string representation of the object
print GetWithdrawalsResponse.to_json()

# convert the object into a dict
get_withdrawals_response_dict = get_withdrawals_response_instance.to_dict()
# create an instance of GetWithdrawalsResponse from a dict
get_withdrawals_response_form_dict = get_withdrawals_response.from_dict(get_withdrawals_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


