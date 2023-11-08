# Action

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

## Example

```python
from openapi_client.models.action import Action

# TODO update the JSON string below
json = "{}"
# create an instance of Action from a JSON string
action_instance = Action.from_json(json)
# print the JSON string representation of the object
print Action.to_json()

# convert the object into a dict
action_dict = action_instance.to_dict()
# create an instance of Action from a dict
action_form_dict = action.from_dict(action_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


