# CreateTxBodyEnvelope

The \"type\" property of \"txBody\" must be \"TxBody BabbageEra\" or \"TxBody ConwayEra\"

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contract_id** | **str** | A reference to a transaction output with a transaction ID and index. | 
**safety_errors** | [**List[SafetyError]**](SafetyError.md) |  | [optional] 
**tx_body** | [**TextEnvelope**](TextEnvelope.md) |  | 

## Example

```python
from openapi_client.models.create_tx_body_envelope import CreateTxBodyEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of CreateTxBodyEnvelope from a JSON string
create_tx_body_envelope_instance = CreateTxBodyEnvelope.from_json(json)
# print the JSON string representation of the object
print CreateTxBodyEnvelope.to_json()

# convert the object into a dict
create_tx_body_envelope_dict = create_tx_body_envelope_instance.to_dict()
# create an instance of CreateTxBodyEnvelope from a dict
create_tx_body_envelope_form_dict = create_tx_body_envelope.from_dict(create_tx_body_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


