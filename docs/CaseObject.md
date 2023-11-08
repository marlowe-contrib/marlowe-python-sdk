# CaseObject

A contract which becomes active when an action occurs.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**case** | [**ActionObject**](ActionObject.md) |  | 
**then** | [**ContractObject**](ContractObject.md) |  | 
**merkleized_then** | **str** |  | 

## Example

```python
from openapi_client.models.case_object import CaseObject

# TODO update the JSON string below
json = "{}"
# create an instance of CaseObject from a JSON string
case_object_instance = CaseObject.from_json(json)
# print the JSON string representation of the object
print CaseObject.to_json()

# convert the object into a dict
case_object_dict = case_object_instance.to_dict()
# create an instance of CaseObject from a dict
case_object_form_dict = case_object.from_dict(case_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


