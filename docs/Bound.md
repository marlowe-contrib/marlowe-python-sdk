# Bound

An inclusive range of values for a choice.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_from** | **int** |  | 
**to** | **int** |  | 

## Example

```python
from openapi_client.models.bound import Bound

# TODO update the JSON string below
json = "{}"
# create an instance of Bound from a JSON string
bound_instance = Bound.from_json(json)
# print the JSON string representation of the object
print Bound.to_json()

# convert the object into a dict
bound_dict = bound_instance.to_dict()
# create an instance of Bound from a dict
bound_form_dict = bound.from_dict(bound_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


