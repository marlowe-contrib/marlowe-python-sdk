# ModelIf

If an observation is true, the first contract applies, otherwise the second contract applies.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_else** | [**Contract**](Contract.md) |  | 
**var_if** | [**Observation**](Observation.md) |  | 
**then** | [**Contract**](Contract.md) |  | 

## Example

```python
from openapi_client.models.model_if import ModelIf

# TODO update the JSON string below
json = "{}"
# create an instance of ModelIf from a JSON string
model_if_instance = ModelIf.from_json(json)
# print the JSON string representation of the object
print ModelIf.to_json()

# convert the object into a dict
model_if_dict = model_if_instance.to_dict()
# create an instance of ModelIf from a dict
model_if_form_dict = model_if.from_dict(model_if_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


