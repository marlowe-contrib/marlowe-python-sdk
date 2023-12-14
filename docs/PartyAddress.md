# PartyAddress

Refers to a party by Cardano address.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** | A cardano address, in Bech32 format | 

## Example

```python
from openapi_client.models.party_address import PartyAddress

# TODO update the JSON string below
json = "{}"
# create an instance of PartyAddress from a JSON string
party_address_instance = PartyAddress.from_json(json)
# print the JSON string representation of the object
print PartyAddress.to_json()

# convert the object into a dict
party_address_dict = party_address_instance.to_dict()
# create an instance of PartyAddress from a dict
party_address_form_dict = party_address.from_dict(party_address_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


