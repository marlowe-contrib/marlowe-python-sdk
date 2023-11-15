# Party

A participant in a contract

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**role_token** | **str** |  | 
**address** | **str** | A cardano address, in Bech32 format | 

## Example

```python
from openapi_client.models.party import Party

# TODO update the JSON string below
json = "{}"
# create an instance of Party from a JSON string
party_instance = Party.from_json(json)
# print the JSON string representation of the object
print Party.to_json()

# convert the object into a dict
party_dict = party_instance.to_dict()
# create an instance of Party from a dict
party_form_dict = party.from_dict(party_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


