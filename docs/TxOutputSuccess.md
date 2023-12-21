# TxOutputSuccess

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
from openapi_client.models.tx_output_success import TxOutputSuccess

# TODO update the JSON string below
json = "{}"
# create an instance of TxOutputSuccess from a JSON string
tx_output_success_instance = TxOutputSuccess.from_json(json)
# print the JSON string representation of the object
print TxOutputSuccess.to_json()

# convert the object into a dict
tx_output_success_dict = tx_output_success_instance.to_dict()
# create an instance of TxOutputSuccess from a dict
tx_output_success_form_dict = tx_output_success.from_dict(tx_output_success_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


