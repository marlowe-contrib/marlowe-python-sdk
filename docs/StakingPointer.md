# StakingPointer

A Plutus staking pointer.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**staking_hash** | **List[int]** |  | 

## Example

```python
from openapi_client.models.staking_pointer import StakingPointer

# TODO update the JSON string below
json = "{}"
# create an instance of StakingPointer from a JSON string
staking_pointer_instance = StakingPointer.from_json(json)
# print the JSON string representation of the object
print StakingPointer.to_json()

# convert the object into a dict
staking_pointer_dict = staking_pointer_instance.to_dict()
# create an instance of StakingPointer from a dict
staking_pointer_form_dict = staking_pointer.from_dict(staking_pointer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


