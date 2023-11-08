# MarloweState

The on-chain state of a Marlowe contract.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accounts** | **List[List[MarloweStateAccountsInnerInner]]** |  | 
**bound_values** | **List[List[MarloweStateBoundValuesInnerInner]]** |  | 
**choices** | **List[List[MarloweStateChoicesInnerInner]]** |  | 
**min_time** | **int** |  | 

## Example

```python
from openapi_client.models.marlowe_state import MarloweState

# TODO update the JSON string below
json = "{}"
# create an instance of MarloweState from a JSON string
marlowe_state_instance = MarloweState.from_json(json)
# print the JSON string representation of the object
print MarloweState.to_json()

# convert the object into a dict
marlowe_state_dict = marlowe_state_instance.to_dict()
# create an instance of MarloweState from a dict
marlowe_state_form_dict = marlowe_state.from_dict(marlowe_state_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


