# PayeeObjectOneOf

Pays funds into a party's account in the contract.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account** | [**PartyObject**](PartyObject.md) |  | 

## Example

```python
from openapi_client.models.payee_object_one_of import PayeeObjectOneOf

# TODO update the JSON string below
json = "{}"
# create an instance of PayeeObjectOneOf from a JSON string
payee_object_one_of_instance = PayeeObjectOneOf.from_json(json)
# print the JSON string representation of the object
print PayeeObjectOneOf.to_json()

# convert the object into a dict
payee_object_one_of_dict = payee_object_one_of_instance.to_dict()
# create an instance of PayeeObjectOneOf from a dict
payee_object_one_of_form_dict = payee_object_one_of.from_dict(payee_object_one_of_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


