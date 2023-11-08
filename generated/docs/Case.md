# Case

A contract which becomes active when an action occurs.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**case** | [**Action**](Action.md) |  | 
**then** | [**Contract**](Contract.md) |  | 
**merkleized_then** | **str** |  | 

## Example

```python
from openapi_client.models.case import Case

# TODO update the JSON string below
json = "{}"
# create an instance of Case from a JSON string
case_instance = Case.from_json(json)
# print the JSON string representation of the object
print Case.to_json()

# convert the object into a dict
case_dict = case_instance.to_dict()
# create an instance of Case from a dict
case_form_dict = case.from_dict(case_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


