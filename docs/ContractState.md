# ContractState


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**assets** | [**Assets**](Assets.md) |  | 
**block** | [**BlockHeader**](BlockHeader.md) |  | [optional] 
**continuations** | **str** |  | [optional] 
**contract_id** | **str** | A reference to a transaction output with a transaction ID and index. | 
**current_contract** | [**Contract**](Contract.md) |  | [optional] 
**initial_contract** | [**Contract**](Contract.md) |  | 
**metadata** | **Dict[str, object]** |  | 
**role_token_minting_policy_id** | **str** | The hex-encoded minting policy ID for a native Cardano token | 
**state** | [**MarloweState**](MarloweState.md) |  | [optional] 
**status** | [**TxStatus**](TxStatus.md) |  | 
**tags** | **Dict[str, object]** |  | 
**tx_body** | [**TextEnvelope**](TextEnvelope.md) |  | [optional] 
**unclaimed_payouts** | [**List[Payout]**](Payout.md) |  | 
**utxo** | **str** | A reference to a transaction output with a transaction ID and index. | [optional] 
**version** | [**MarloweVersion**](MarloweVersion.md) |  | 

## Example

```python
from openapi_client.models.contract_state import ContractState

# TODO update the JSON string below
json = "{}"
# create an instance of ContractState from a JSON string
contract_state_instance = ContractState.from_json(json)
# print the JSON string representation of the object
print ContractState.to_json()

# convert the object into a dict
contract_state_dict = contract_state_instance.to_dict()
# create an instance of ContractState from a dict
contract_state_form_dict = contract_state.from_dict(contract_state_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


