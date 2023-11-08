# PartyObject

A participant in a contract

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**role_token** | **str** |  | 
**address** | **str** | A cardano address, in Bech32 format | 
**ref** | **str** | An arbitrary text identifier for an object in a Marlowe object bundle. | 

## Example

```python
from openapi_client.models.party_object import PartyObject

# TODO update the JSON string below
json = "{}"
# create an instance of PartyObject from a JSON string
party_object_instance = PartyObject.from_json(json)
# print the JSON string representation of the object
print PartyObject.to_json()

# convert the object into a dict
party_object_dict = party_object_instance.to_dict()
# create an instance of PartyObject from a dict
party_object_form_dict = party_object.from_dict(party_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


