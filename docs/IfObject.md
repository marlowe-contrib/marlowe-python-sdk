# IfObject

If an observation is true, the first contract applies, otherwise the second contract applies.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_else** | [**ContractObject**](ContractObject.md) |  | 
**var_if** | [**ObservationObject**](ObservationObject.md) |  | 
**then** | [**ContractObject**](ContractObject.md) |  | 

## Example

```python
from openapi_client.models.if_object import IfObject

# TODO update the JSON string below
json = "{}"
# create an instance of IfObject from a JSON string
if_object_instance = IfObject.from_json(json)
# print the JSON string representation of the object
print IfObject.to_json()

# convert the object into a dict
if_object_dict = if_object_instance.to_dict()
# create an instance of IfObject from a dict
if_object_form_dict = if_object.from_dict(if_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


