# PayToPartyObject

Pays funds to a party.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**party** | [**PartyObject**](PartyObject.md) |  | 

## Example

```python
from openapi_client.models.pay_to_party_object import PayToPartyObject

# TODO update the JSON string below
json = "{}"
# create an instance of PayToPartyObject from a JSON string
pay_to_party_object_instance = PayToPartyObject.from_json(json)
# print the JSON string representation of the object
print PayToPartyObject.to_json()

# convert the object into a dict
pay_to_party_object_dict = pay_to_party_object_instance.to_dict()
# create an instance of PayToPartyObject from a dict
pay_to_party_object_form_dict = pay_to_party_object.from_dict(pay_to_party_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


