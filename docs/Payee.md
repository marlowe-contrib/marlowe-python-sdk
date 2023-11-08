# Payee

A recipient of a payment

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account** | [**Party**](Party.md) |  | 
**party** | [**Party**](Party.md) |  | 

## Example

```python
from openapi_client.models.payee import Payee

# TODO update the JSON string below
json = "{}"
# create an instance of Payee from a JSON string
payee_instance = Payee.from_json(json)
# print the JSON string representation of the object
print Payee.to_json()

# convert the object into a dict
payee_dict = payee_instance.to_dict()
# create an instance of Payee from a dict
payee_form_dict = payee.from_dict(payee_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


