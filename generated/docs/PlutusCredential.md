# PlutusCredential

A Plutus credential.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pub_key_credential** | **str** |  | 
**script_credential** | **str** |  | 

## Example

```python
from openapi_client.models.plutus_credential import PlutusCredential

# TODO update the JSON string below
json = "{}"
# create an instance of PlutusCredential from a JSON string
plutus_credential_instance = PlutusCredential.from_json(json)
# print the JSON string representation of the object
print PlutusCredential.to_json()

# convert the object into a dict
plutus_credential_dict = plutus_credential_instance.to_dict()
# create an instance of PlutusCredential from a dict
plutus_credential_form_dict = plutus_credential.from_dict(plutus_credential_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


