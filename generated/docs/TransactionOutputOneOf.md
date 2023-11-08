# TransactionOutputOneOf

Marlowe transaction output information.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contract** | [**Contract**](Contract.md) |  | 
**payments** | [**List[Payment]**](Payment.md) |  | 
**state** | [**MarloweState**](MarloweState.md) |  | 
**warnings** | [**List[TransactionWarning]**](TransactionWarning.md) |  | 

## Example

```python
from openapi_client.models.transaction_output_one_of import TransactionOutputOneOf

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionOutputOneOf from a JSON string
transaction_output_one_of_instance = TransactionOutputOneOf.from_json(json)
# print the JSON string representation of the object
print TransactionOutputOneOf.to_json()

# convert the object into a dict
transaction_output_one_of_dict = transaction_output_one_of_instance.to_dict()
# create an instance of TransactionOutputOneOf from a dict
transaction_output_one_of_form_dict = transaction_output_one_of.from_dict(transaction_output_one_of_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


