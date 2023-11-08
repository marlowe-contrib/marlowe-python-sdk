# PayeeObject

A recipient of a payment

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account** | [**PartyObject**](PartyObject.md) |  | 
**party** | [**PartyObject**](PartyObject.md) |  | 

## Example

```python
from openapi_client.models.payee_object import PayeeObject

# TODO update the JSON string below
json = "{}"
# create an instance of PayeeObject from a JSON string
payee_object_instance = PayeeObject.from_json(json)
# print the JSON string representation of the object
print PayeeObject.to_json()

# convert the object into a dict
payee_object_dict = payee_object_instance.to_dict()
# create an instance of PayeeObject from a dict
payee_object_form_dict = payee_object.from_dict(payee_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


