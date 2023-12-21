# PayObject

A payment will be sent from an account to a payee.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**from_account** | [**PartyObject**](PartyObject.md) |  | 
**pay** | [**ValueObject**](ValueObject.md) |  | 
**then** | [**ContractObject**](ContractObject.md) |  | 
**to** | [**PayeeObject**](PayeeObject.md) |  | 
**token** | [**TokenObject**](TokenObject.md) |  | 

## Example

```python
from openapi_client.models.pay_object import PayObject

# TODO update the JSON string below
json = "{}"
# create an instance of PayObject from a JSON string
pay_object_instance = PayObject.from_json(json)
# print the JSON string representation of the object
print PayObject.to_json()

# convert the object into a dict
pay_object_dict = pay_object_instance.to_dict()
# create an instance of PayObject from a dict
pay_object_form_dict = pay_object.from_dict(pay_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


