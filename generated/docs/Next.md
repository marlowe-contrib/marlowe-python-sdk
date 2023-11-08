# Next

Describe the reducibility (Can be Reduced ?) and the applicability (Can Inputs be Applied ?) for a given contract.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**applicable_inputs** | [**ApplicableInputs**](ApplicableInputs.md) |  | 
**can_reduce** | **bool** | Indicates if a given contract can be reduced (apply []) or not. | 

## Example

```python
from openapi_client.models.next import Next

# TODO update the JSON string below
json = "{}"
# create an instance of Next from a JSON string
next_instance = Next.from_json(json)
# print the JSON string representation of the object
print Next.to_json()

# convert the object into a dict
next_dict = next_instance.to_dict()
# create an instance of Next from a dict
next_form_dict = next.from_dict(next_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


