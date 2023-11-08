# ApplyInputsTxEnvelope


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tx** | [**TextEnvelope**](TextEnvelope.md) |  | 
**withdrawal_id** | **str** | The hex-encoded identifier of a Cardano transaction | 

## Example

```python
from openapi_client.models.apply_inputs_tx_envelope import ApplyInputsTxEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of ApplyInputsTxEnvelope from a JSON string
apply_inputs_tx_envelope_instance = ApplyInputsTxEnvelope.from_json(json)
# print the JSON string representation of the object
print ApplyInputsTxEnvelope.to_json()

# convert the object into a dict
apply_inputs_tx_envelope_dict = apply_inputs_tx_envelope_instance.to_dict()
# create an instance of ApplyInputsTxEnvelope from a dict
apply_inputs_tx_envelope_form_dict = apply_inputs_tx_envelope.from_dict(apply_inputs_tx_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


