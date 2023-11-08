# Tx


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**assets** | [**Assets**](Assets.md) |  | 
**block** | [**BlockHeader**](BlockHeader.md) |  | [optional] 
**consuming_tx** | **str** | The hex-encoded identifier of a Cardano transaction | [optional] 
**continuations** | **str** |  | [optional] 
**contract_id** | **str** | A reference to a transaction output with a transaction ID and index. | 
**input_utxo** | **str** | A reference to a transaction output with a transaction ID and index. | 
**inputs** | [**List[Input]**](Input.md) |  | 
**invalid_before** | **str** |  | 
**invalid_hereafter** | **str** |  | 
**metadata** | **Dict[str, object]** |  | 
**output_contract** | [**Contract**](Contract.md) |  | [optional] 
**output_state** | [**MarloweState**](MarloweState.md) |  | [optional] 
**output_utxo** | **str** | A reference to a transaction output with a transaction ID and index. | [optional] 
**payouts** | [**List[Payout]**](Payout.md) |  | 
**status** | [**TxStatus**](TxStatus.md) |  | 
**tags** | **Dict[str, object]** |  | 
**transaction_id** | **str** | The hex-encoded identifier of a Cardano transaction | 
**tx_body** | [**TextEnvelope**](TextEnvelope.md) |  | [optional] 

## Example

```python
from openapi_client.models.tx import Tx

# TODO update the JSON string below
json = "{}"
# create an instance of Tx from a JSON string
tx_instance = Tx.from_json(json)
# print the JSON string representation of the object
print Tx.to_json()

# convert the object into a dict
tx_dict = tx_instance.to_dict()
# create an instance of Tx from a dict
tx_form_dict = tx.from_dict(tx_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


