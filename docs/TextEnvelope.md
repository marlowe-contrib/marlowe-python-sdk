# TextEnvelope


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cbor_hex** | **str** |  | 
**description** | **str** |  | 
**type** | **str** | What type of data is encoded in the CBOR Hex. Valid values include \&quot;Tx &lt;era&gt;\&quot;, \&quot;TxBody &lt;era&gt;\&quot;, and \&quot;ShelleyTxWitness &lt;era&gt;\&quot; where &lt;era&gt; is one of \&quot;BabbageEra\&quot;, \&quot;ConwayEra\&quot;. | 

## Example

```python
from openapi_client.models.text_envelope import TextEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of TextEnvelope from a JSON string
text_envelope_instance = TextEnvelope.from_json(json)
# print the JSON string representation of the object
print TextEnvelope.to_json()

# convert the object into a dict
text_envelope_dict = text_envelope_instance.to_dict()
# create an instance of TextEnvelope from a dict
text_envelope_form_dict = text_envelope.from_dict(text_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


