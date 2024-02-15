# DepositAction


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deposits** | [**Value**](Value.md) |  | 
**into_account** | [**Party**](Party.md) |  | 
**of_token** | [**Token**](Token.md) |  | 
**party** | [**Party**](Party.md) |  | 

## Example

```python
from openapi_client.models.deposit_action import DepositAction

# TODO update the JSON string below
json = "{}"
# create an instance of DepositAction from a JSON string
deposit_action_instance = DepositAction.from_json(json)
# print the JSON string representation of the object
print DepositAction.to_json()

# convert the object into a dict
deposit_action_dict = deposit_action_instance.to_dict()
# create an instance of DepositAction from a dict
deposit_action_form_dict = deposit_action.from_dict(deposit_action_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


