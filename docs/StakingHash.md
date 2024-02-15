# StakingHash

A Plutus staking hash.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**staking_hash** | [**PlutusCredential**](PlutusCredential.md) |  | 

## Example

```python
from openapi_client.models.staking_hash import StakingHash

# TODO update the JSON string below
json = "{}"
# create an instance of StakingHash from a JSON string
staking_hash_instance = StakingHash.from_json(json)
# print the JSON string representation of the object
print StakingHash.to_json()

# convert the object into a dict
staking_hash_dict = staking_hash_instance.to_dict()
# create an instance of StakingHash from a dict
staking_hash_form_dict = staking_hash.from_dict(staking_hash_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


