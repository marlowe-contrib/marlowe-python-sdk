# TransactionInput

Marlowe transaction input.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tx_inputs** | [**List[Input]**](Input.md) |  | 
**tx_interval** | [**TransactionInputTxInterval**](TransactionInputTxInterval.md) |  | 

## Example

```python
from openapi_client.models.transaction_input import TransactionInput

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionInput from a JSON string
transaction_input_instance = TransactionInput.from_json(json)
# print the JSON string representation of the object
print TransactionInput.to_json()

# convert the object into a dict
transaction_input_dict = transaction_input_instance.to_dict()
# create an instance of TransactionInput from a dict
transaction_input_form_dict = transaction_input.from_dict(transaction_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


