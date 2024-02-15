# VariableShadowing

A variable-name shadowing warning.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**had_value** | **int** |  | 
**is_now_assigned** | **int** |  | 
**value_id** | **str** |  | 

## Example

```python
from openapi_client.models.variable_shadowing import VariableShadowing

# TODO update the JSON string below
json = "{}"
# create an instance of VariableShadowing from a JSON string
variable_shadowing_instance = VariableShadowing.from_json(json)
# print the JSON string representation of the object
print VariableShadowing.to_json()

# convert the object into a dict
variable_shadowing_dict = variable_shadowing_instance.to_dict()
# create an instance of VariableShadowing from a dict
variable_shadowing_form_dict = variable_shadowing.from_dict(variable_shadowing_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


