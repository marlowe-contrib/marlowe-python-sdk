# PlutusAddress

A Plutus address.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address_credential** | [**PlutusCredential**](PlutusCredential.md) |  | 
**address_staking_credential** | [**PlutusStakingCredential**](PlutusStakingCredential.md) |  | [optional] 

## Example

```python
from openapi_client.models.plutus_address import PlutusAddress

# TODO update the JSON string below
json = "{}"
# create an instance of PlutusAddress from a JSON string
plutus_address_instance = PlutusAddress.from_json(json)
# print the JSON string representation of the object
print PlutusAddress.to_json()

# convert the object into a dict
plutus_address_dict = plutus_address_instance.to_dict()
# create an instance of PlutusAddress from a dict
plutus_address_form_dict = plutus_address.from_dict(plutus_address_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


