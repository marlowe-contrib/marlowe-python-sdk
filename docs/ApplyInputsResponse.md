# ApplyInputsResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**ApplyInputsResponseLinks**](ApplyInputsResponseLinks.md) |  | 
**resource** | [**ApplyInputsTxEnvelope**](ApplyInputsTxEnvelope.md) |  | 

## Example

```python
from openapi_client.models.apply_inputs_response import ApplyInputsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ApplyInputsResponse from a JSON string
apply_inputs_response_instance = ApplyInputsResponse.from_json(json)
# print the JSON string representation of the object
print ApplyInputsResponse.to_json()

# convert the object into a dict
apply_inputs_response_dict = apply_inputs_response_instance.to_dict()
# create an instance of ApplyInputsResponse from a dict
apply_inputs_response_form_dict = apply_inputs_response.from_dict(apply_inputs_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


