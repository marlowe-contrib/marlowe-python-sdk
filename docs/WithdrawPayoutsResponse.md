# WithdrawPayoutsResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**GetWithdrawalsResponseResultsInnerLinks**](GetWithdrawalsResponseResultsInnerLinks.md) |  | 
**resource** | [**WithdrawTxEnvelope**](WithdrawTxEnvelope.md) |  | 

## Example

```python
from openapi_client.models.withdraw_payouts_response import WithdrawPayoutsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of WithdrawPayoutsResponse from a JSON string
withdraw_payouts_response_instance = WithdrawPayoutsResponse.from_json(json)
# print the JSON string representation of the object
print WithdrawPayoutsResponse.to_json()

# convert the object into a dict
withdraw_payouts_response_dict = withdraw_payouts_response_instance.to_dict()
# create an instance of WithdrawPayoutsResponse from a dict
withdraw_payouts_response_form_dict = withdraw_payouts_response.from_dict(withdraw_payouts_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


