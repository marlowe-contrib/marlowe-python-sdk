# TransactionWarningOneOf

A warning for a non-positive deposit.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**asked_to_deposit** | **int** |  | 
**in_account** | [**Party**](Party.md) |  | 
**of_token** | [**Token**](Token.md) |  | 
**party** | [**Party**](Party.md) |  | 

## Example

```python
from openapi_client.models.transaction_warning_one_of import TransactionWarningOneOf

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionWarningOneOf from a JSON string
transaction_warning_one_of_instance = TransactionWarningOneOf.from_json(json)
# print the JSON string representation of the object
print TransactionWarningOneOf.to_json()

# convert the object into a dict
transaction_warning_one_of_dict = transaction_warning_one_of_instance.to_dict()
# create an instance of TransactionWarningOneOf from a dict
transaction_warning_one_of_form_dict = transaction_warning_one_of.from_dict(transaction_warning_one_of_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


