# ContractHeader


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**block** | [**BlockHeader**](BlockHeader.md) |  | [optional] 
**continuations** | **str** |  | [optional] 
**contract_id** | **str** | A reference to a transaction output with a transaction ID and index. | 
**metadata** | [**Dict[str, Metadata]**](Metadata.md) |  | 
**role_token_minting_policy_id** | **str** | The hex-encoded minting policy ID for a native Cardano token | 
**status** | [**TxStatus**](TxStatus.md) |  | 
**tags** | [**Dict[str, Metadata]**](Metadata.md) |  | 
**version** | [**MarloweVersion**](MarloweVersion.md) |  | 

## Example

```python
from openapi_client.models.contract_header import ContractHeader

# TODO update the JSON string below
json = "{}"
# create an instance of ContractHeader from a JSON string
contract_header_instance = ContractHeader.from_json(json)
# print the JSON string representation of the object
print ContractHeader.to_json()

# convert the object into a dict
contract_header_dict = contract_header_instance.to_dict()
# create an instance of ContractHeader from a dict
contract_header_form_dict = contract_header.from_dict(contract_header_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


