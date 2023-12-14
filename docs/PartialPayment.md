# PartialPayment

A warning for partial payment.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account** | [**Party**](Party.md) |  | 
**asked_to_pay** | **int** |  | 
**but_only_paid** | **int** |  | 
**of_token** | [**Token**](Token.md) |  | 
**to_payee** | [**Payee**](Payee.md) |  | 

## Example

```python
from openapi_client.models.partial_payment import PartialPayment

# TODO update the JSON string below
json = "{}"
# create an instance of PartialPayment from a JSON string
partial_payment_instance = PartialPayment.from_json(json)
# print the JSON string representation of the object
print PartialPayment.to_json()

# convert the object into a dict
partial_payment_dict = partial_payment_instance.to_dict()
# create an instance of PartialPayment from a dict
partial_payment_form_dict = partial_payment.from_dict(partial_payment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


