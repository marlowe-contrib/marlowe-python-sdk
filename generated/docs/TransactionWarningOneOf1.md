# TransactionWarningOneOf1

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
from openapi_client.models.transaction_warning_one_of1 import TransactionWarningOneOf1

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionWarningOneOf1 from a JSON string
transaction_warning_one_of1_instance = TransactionWarningOneOf1.from_json(json)
# print the JSON string representation of the object
print TransactionWarningOneOf1.to_json()

# convert the object into a dict
transaction_warning_one_of1_dict = transaction_warning_one_of1_instance.to_dict()
# create an instance of TransactionWarningOneOf1 from a dict
transaction_warning_one_of1_form_dict = transaction_warning_one_of1.from_dict(transaction_warning_one_of1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


