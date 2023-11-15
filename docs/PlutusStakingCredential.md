# PlutusStakingCredential

A Plutus staking credential.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**staking_hash** | **List[int]** |  | 

## Example

```python
from openapi_client.models.plutus_staking_credential import PlutusStakingCredential

# TODO update the JSON string below
json = "{}"
# create an instance of PlutusStakingCredential from a JSON string
plutus_staking_credential_instance = PlutusStakingCredential.from_json(json)
# print the JSON string representation of the object
print PlutusStakingCredential.to_json()

# convert the object into a dict
plutus_staking_credential_dict = plutus_staking_credential_instance.to_dict()
# create an instance of PlutusStakingCredential from a dict
plutus_staking_credential_form_dict = plutus_staking_credential.from_dict(plutus_staking_credential_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


