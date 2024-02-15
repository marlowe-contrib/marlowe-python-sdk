# WhenObject

Wait for an action to be performed and apply the matching contract when it does. Apply the timeout contract if no actions have been performed in the timeout period.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**timeout** | **int** |  | 
**timeout_continuation** | [**ContractObject**](ContractObject.md) |  | 
**when** | [**List[CaseObject]**](CaseObject.md) |  | 

## Example

```python
from openapi_client.models.when_object import WhenObject

# TODO update the JSON string below
json = "{}"
# create an instance of WhenObject from a JSON string
when_object_instance = WhenObject.from_json(json)
# print the JSON string representation of the object
print WhenObject.to_json()

# convert the object into a dict
when_object_dict = when_object_instance.to_dict()
# create an instance of WhenObject from a dict
when_object_form_dict = when_object.from_dict(when_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


