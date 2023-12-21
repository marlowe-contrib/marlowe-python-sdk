# NonPositivePayment

A warning for a non-positive payment.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account** | [**Party**](Party.md) |  | 
**asked_to_pay** | **int** |  | 
**of_token** | [**Token**](Token.md) |  | 
**to_payee** | [**Payee**](Payee.md) |  | 

## Example

```python
from openapi_client.models.non_positive_payment import NonPositivePayment

# TODO update the JSON string below
json = "{}"
# create an instance of NonPositivePayment from a JSON string
non_positive_payment_instance = NonPositivePayment.from_json(json)
# print the JSON string representation of the object
print NonPositivePayment.to_json()

# convert the object into a dict
non_positive_payment_dict = non_positive_payment_instance.to_dict()
# create an instance of NonPositivePayment from a dict
non_positive_payment_form_dict = non_positive_payment.from_dict(non_positive_payment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


