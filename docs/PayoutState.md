# PayoutState


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**assets** | [**Assets**](Assets.md) |  | 
**contract_id** | **str** | A reference to a transaction output with a transaction ID and index. | 
**payout_id** | **str** | A reference to a transaction output with a transaction ID and index. | 
**payout_validator_address** | **str** | A cardano address | 
**role** | [**AssetId**](AssetId.md) |  | 
**status** | [**PayoutStatus**](PayoutStatus.md) |  | 
**withdrawal_id** | **str** | The hex-encoded identifier of a Cardano transaction | [optional] 

## Example

```python
from openapi_client.models.payout_state import PayoutState

# TODO update the JSON string below
json = "{}"
# create an instance of PayoutState from a JSON string
payout_state_instance = PayoutState.from_json(json)
# print the JSON string representation of the object
print PayoutState.to_json()

# convert the object into a dict
payout_state_dict = payout_state_instance.to_dict()
# create an instance of PayoutState from a dict
payout_state_form_dict = payout_state.from_dict(payout_state_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


