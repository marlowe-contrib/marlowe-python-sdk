# IfValue


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_else** | [**Value**](Value.md) |  | 
**var_if** | [**Observation**](Observation.md) |  | 
**then** | [**Value**](Value.md) |  | 

## Example

```python
from openapi_client.models.if_value import IfValue

# TODO update the JSON string below
json = "{}"
# create an instance of IfValue from a JSON string
if_value_instance = IfValue.from_json(json)
# print the JSON string representation of the object
print IfValue.to_json()

# convert the object into a dict
if_value_dict = if_value_instance.to_dict()
# create an instance of IfValue from a dict
if_value_form_dict = if_value.from_dict(if_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


