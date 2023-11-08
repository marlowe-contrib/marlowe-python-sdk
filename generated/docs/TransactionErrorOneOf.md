# TransactionErrorOneOf

An invalid time interval.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**context** | [**IntervalError**](IntervalError.md) |  | 
**error** | **str** |  | 

## Example

```python
from openapi_client.models.transaction_error_one_of import TransactionErrorOneOf

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionErrorOneOf from a JSON string
transaction_error_one_of_instance = TransactionErrorOneOf.from_json(json)
# print the JSON string representation of the object
print TransactionErrorOneOf.to_json()

# convert the object into a dict
transaction_error_one_of_dict = transaction_error_one_of_instance.to_dict()
# create an instance of TransactionErrorOneOf from a dict
transaction_error_one_of_form_dict = transaction_error_one_of.from_dict(transaction_error_one_of_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


