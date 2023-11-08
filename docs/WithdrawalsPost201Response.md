# WithdrawalsPost201Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**WithdrawalsPost201ResponseLinks**](WithdrawalsPost201ResponseLinks.md) |  | 
**resource** | [**ApplyInputsTxEnvelope**](ApplyInputsTxEnvelope.md) |  | 

## Example

```python
from openapi_client.models.withdrawals_post201_response import WithdrawalsPost201Response

# TODO update the JSON string below
json = "{}"
# create an instance of WithdrawalsPost201Response from a JSON string
withdrawals_post201_response_instance = WithdrawalsPost201Response.from_json(json)
# print the JSON string representation of the object
print WithdrawalsPost201Response.to_json()

# convert the object into a dict
withdrawals_post201_response_dict = withdrawals_post201_response_instance.to_dict()
# create an instance of WithdrawalsPost201Response from a dict
withdrawals_post201_response_form_dict = withdrawals_post201_response.from_dict(withdrawals_post201_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


