# Pay

A payment will be sent from an account to a payee.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**from_account** | [**Party**](Party.md) |  | 
**pay** | [**Value**](Value.md) |  | 
**then** | [**Contract**](Contract.md) |  | 
**to** | [**Payee**](Payee.md) |  | 
**token** | [**Token**](Token.md) |  | 

## Example

```python
from openapi_client.models.pay import Pay

# TODO update the JSON string below
json = "{}"
# create an instance of Pay from a JSON string
pay_instance = Pay.from_json(json)
# print the JSON string representation of the object
print Pay.to_json()

# convert the object into a dict
pay_dict = pay_instance.to_dict()
# create an instance of Pay from a dict
pay_form_dict = pay.from_dict(pay_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


