# PubKeyCredential

A Plutus public key credential.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pub_key_credential** | **str** |  | 

## Example

```python
from openapi_client.models.pub_key_credential import PubKeyCredential

# TODO update the JSON string below
json = "{}"
# create an instance of PubKeyCredential from a JSON string
pub_key_credential_instance = PubKeyCredential.from_json(json)
# print the JSON string representation of the object
print PubKeyCredential.to_json()

# convert the object into a dict
pub_key_credential_dict = pub_key_credential_instance.to_dict()
# create an instance of PubKeyCredential from a dict
pub_key_credential_form_dict = pub_key_credential.from_dict(pub_key_credential_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


