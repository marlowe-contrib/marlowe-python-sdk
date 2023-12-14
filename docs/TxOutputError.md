# TxOutputError

Marlowe transaction error.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transaction_error** | [**TransactionError**](TransactionError.md) |  | 

## Example

```python
from openapi_client.models.tx_output_error import TxOutputError

# TODO update the JSON string below
json = "{}"
# create an instance of TxOutputError from a JSON string
tx_output_error_instance = TxOutputError.from_json(json)
# print the JSON string representation of the object
print TxOutputError.to_json()

# convert the object into a dict
tx_output_error_dict = tx_output_error_instance.to_dict()
# create an instance of TxOutputError from a dict
tx_output_error_form_dict = tx_output_error.from_dict(tx_output_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


