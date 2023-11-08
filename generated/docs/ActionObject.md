# ActionObject

A contract which becomes active when an action occurs.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deposits** | [**Value**](Value.md) |  | 
**into_account** | [**Party**](Party.md) |  | 
**of_token** | [**Token**](Token.md) |  | 
**party** | [**Party**](Party.md) |  | 
**choose_between** | [**List[Bound]**](Bound.md) |  | 
**for_choice** | [**ChoiceId**](ChoiceId.md) |  | 
**notify_if** | [**Observation**](Observation.md) |  | 
**ref** | **str** | An arbitrary text identifier for an object in a Marlowe object bundle. | 

## Example

```python
from openapi_client.models.action_object import ActionObject

# TODO update the JSON string below
json = "{}"
# create an instance of ActionObject from a JSON string
action_object_instance = ActionObject.from_json(json)
# print the JSON string representation of the object
print ActionObject.to_json()

# convert the object into a dict
action_object_dict = action_object_instance.to_dict()
# create an instance of ActionObject from a dict
action_object_form_dict = action_object.from_dict(action_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


