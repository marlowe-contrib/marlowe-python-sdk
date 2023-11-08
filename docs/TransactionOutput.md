# TransactionOutput

Marlowe transaction output.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contract** | [**Contract**](Contract.md) |  | 
**payments** | [**List[Payment]**](Payment.md) |  | 
**state** | [**MarloweState**](MarloweState.md) |  | 
**warnings** | [**List[TransactionWarning]**](TransactionWarning.md) |  | 
**transaction_error** | [**TransactionError**](TransactionError.md) |  | 

## Example

```python
from openapi_client.models.transaction_output import TransactionOutput

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionOutput from a JSON string
transaction_output_instance = TransactionOutput.from_json(json)
# print the JSON string representation of the object
print TransactionOutput.to_json()

# convert the object into a dict
transaction_output_dict = transaction_output_instance.to_dict()
# create an instance of TransactionOutput from a dict
transaction_output_form_dict = transaction_output.from_dict(transaction_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


