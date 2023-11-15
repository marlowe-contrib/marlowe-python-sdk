# WithdrawTxBodyEnvelope

The \"type\" property of \"txBody\" must be \"TxBody BabbageEra\" or \"TxBody ConwayEra\"

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tx_body** | [**TextEnvelope**](TextEnvelope.md) |  | 
**withdrawal_id** | **str** | The hex-encoded identifier of a Cardano transaction | 

## Example

```python
from openapi_client.models.withdraw_tx_body_envelope import WithdrawTxBodyEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of WithdrawTxBodyEnvelope from a JSON string
withdraw_tx_body_envelope_instance = WithdrawTxBodyEnvelope.from_json(json)
# print the JSON string representation of the object
print WithdrawTxBodyEnvelope.to_json()

# convert the object into a dict
withdraw_tx_body_envelope_dict = withdraw_tx_body_envelope_instance.to_dict()
# create an instance of WithdrawTxBodyEnvelope from a dict
withdraw_tx_body_envelope_form_dict = withdraw_tx_body_envelope.from_dict(withdraw_tx_body_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


