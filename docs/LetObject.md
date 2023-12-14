# LetObject

Bind a value to a name within the scope of a sub-contract.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**be** | [**ValueObject**](ValueObject.md) |  | 
**let** | **str** |  | 
**then** | [**ContractObject**](ContractObject.md) |  | 

## Example

```python
from openapi_client.models.let_object import LetObject

# TODO update the JSON string below
json = "{}"
# create an instance of LetObject from a JSON string
let_object_instance = LetObject.from_json(json)
# print the JSON string representation of the object
print LetObject.to_json()

# convert the object into a dict
let_object_dict = let_object_instance.to_dict()
# create an instance of LetObject from a dict
let_object_form_dict = let_object.from_dict(let_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


