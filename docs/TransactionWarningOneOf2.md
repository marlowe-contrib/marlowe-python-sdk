# TransactionWarningOneOf2

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
from openapi_client.models.transaction_warning_one_of2 import TransactionWarningOneOf2

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionWarningOneOf2 from a JSON string
transaction_warning_one_of2_instance = TransactionWarningOneOf2.from_json(json)
# print the JSON string representation of the object
print TransactionWarningOneOf2.to_json()

# convert the object into a dict
transaction_warning_one_of2_dict = transaction_warning_one_of2_instance.to_dict()
# create an instance of TransactionWarningOneOf2 from a dict
transaction_warning_one_of2_form_dict = transaction_warning_one_of2.from_dict(transaction_warning_one_of2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


