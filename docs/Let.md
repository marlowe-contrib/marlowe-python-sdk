# Let

Bind a value to a name within the scope of a sub-contract.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**be** | [**Value**](Value.md) |  | 
**let** | **str** |  | 
**then** | [**Contract**](Contract.md) |  | 

## Example

```python
from openapi_client.models.let import Let

# TODO update the JSON string below
json = "{}"
# create an instance of Let from a JSON string
let_instance = Let.from_json(json)
# print the JSON string representation of the object
print Let.to_json()

# convert the object into a dict
let_dict = let_instance.to_dict()
# create an instance of Let from a dict
let_form_dict = let.from_dict(let_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


