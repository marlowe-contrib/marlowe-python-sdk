# TransactionWarning

A transaction semantics warning.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**asked_to_deposit** | **int** |  | 
**in_account** | [**Party**](Party.md) |  | 
**of_token** | [**Token**](Token.md) |  | 
**party** | [**Party**](Party.md) |  | 
**account** | [**Party**](Party.md) |  | 
**asked_to_pay** | **int** |  | 
**to_payee** | [**Payee**](Payee.md) |  | 
**but_only_paid** | **int** |  | 
**had_value** | **int** |  | 
**is_now_assigned** | **int** |  | 
**value_id** | **str** |  | 

## Example

```python
from openapi_client.models.transaction_warning import TransactionWarning

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionWarning from a JSON string
transaction_warning_instance = TransactionWarning.from_json(json)
# print the JSON string representation of the object
print TransactionWarning.to_json()

# convert the object into a dict
transaction_warning_dict = transaction_warning_instance.to_dict()
# create an instance of TransactionWarning from a dict
transaction_warning_form_dict = transaction_warning.from_dict(transaction_warning_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


