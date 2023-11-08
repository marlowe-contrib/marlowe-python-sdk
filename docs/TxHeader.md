# TxHeader


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**block** | [**BlockHeader**](BlockHeader.md) |  | [optional] 
**continuations** | **str** |  | [optional] 
**contract_id** | **str** | A reference to a transaction output with a transaction ID and index. | 
**metadata** | **Dict[str, object]** |  | 
**status** | [**TxStatus**](TxStatus.md) |  | 
**tags** | **Dict[str, object]** |  | 
**transaction_id** | **str** | The hex-encoded identifier of a Cardano transaction | 
**utxo** | **str** | A reference to a transaction output with a transaction ID and index. | [optional] 

## Example

```python
from openapi_client.models.tx_header import TxHeader

# TODO update the JSON string below
json = "{}"
# create an instance of TxHeader from a JSON string
tx_header_instance = TxHeader.from_json(json)
# print the JSON string representation of the object
print TxHeader.to_json()

# convert the object into a dict
tx_header_dict = tx_header_instance.to_dict()
# create an instance of TxHeader from a dict
tx_header_form_dict = tx_header.from_dict(tx_header_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


