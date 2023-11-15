# WithdrawTxEnvelope

The \"type\" property of \"tx\" must be \"Tx BabbageEra\" or \"Tx ConwayEra\"

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tx** | [**TextEnvelope**](TextEnvelope.md) |  | 
**withdrawal_id** | **str** | The hex-encoded identifier of a Cardano transaction | 

## Example

```python
from openapi_client.models.withdraw_tx_envelope import WithdrawTxEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of WithdrawTxEnvelope from a JSON string
withdraw_tx_envelope_instance = WithdrawTxEnvelope.from_json(json)
# print the JSON string representation of the object
print WithdrawTxEnvelope.to_json()

# convert the object into a dict
withdraw_tx_envelope_dict = withdraw_tx_envelope_instance.to_dict()
# create an instance of WithdrawTxEnvelope from a dict
withdraw_tx_envelope_form_dict = withdraw_tx_envelope.from_dict(withdraw_tx_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


