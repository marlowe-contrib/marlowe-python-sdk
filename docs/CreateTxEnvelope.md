# CreateTxEnvelope

The \"type\" property of \"tx\" must be \"Tx BabbageEra\" or \"Tx ConwayEra\"

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contract_id** | **str** | A reference to a transaction output with a transaction ID and index. | 
**safety_errors** | [**List[SafetyError]**](SafetyError.md) |  | [optional] 
**tx** | [**TextEnvelope**](TextEnvelope.md) |  | 

## Example

```python
from openapi_client.models.create_tx_envelope import CreateTxEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of CreateTxEnvelope from a JSON string
create_tx_envelope_instance = CreateTxEnvelope.from_json(json)
# print the JSON string representation of the object
print CreateTxEnvelope.to_json()

# convert the object into a dict
create_tx_envelope_dict = create_tx_envelope_instance.to_dict()
# create an instance of CreateTxEnvelope from a dict
create_tx_envelope_form_dict = create_tx_envelope.from_dict(create_tx_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


