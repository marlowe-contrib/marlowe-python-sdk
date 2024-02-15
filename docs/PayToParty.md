# PayToParty

Pays funds to a party.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**party** | [**Party**](Party.md) |  | 

## Example

```python
from openapi_client.models.pay_to_party import PayToParty

# TODO update the JSON string below
json = "{}"
# create an instance of PayToParty from a JSON string
pay_to_party_instance = PayToParty.from_json(json)
# print the JSON string representation of the object
print PayToParty.to_json()

# convert the object into a dict
pay_to_party_dict = pay_to_party_instance.to_dict()
# create an instance of PayToParty from a dict
pay_to_party_form_dict = pay_to_party.from_dict(pay_to_party_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


