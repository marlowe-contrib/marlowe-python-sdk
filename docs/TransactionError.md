# TransactionError

A Marlowe transaction error.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**context** | [**IntervalError**](IntervalError.md) |  | 
**error** | **str** |  | 

## Example

```python
from openapi_client.models.transaction_error import TransactionError

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionError from a JSON string
transaction_error_instance = TransactionError.from_json(json)
# print the JSON string representation of the object
print TransactionError.to_json()

# convert the object into a dict
transaction_error_dict = transaction_error_instance.to_dict()
# create an instance of TransactionError from a dict
transaction_error_form_dict = transaction_error.from_dict(transaction_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


