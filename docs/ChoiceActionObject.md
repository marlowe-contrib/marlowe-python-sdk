# ChoiceActionObject


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**choose_between** | [**List[Bound]**](Bound.md) |  | 
**for_choice** | [**ChoiceId**](ChoiceId.md) |  | 

## Example

```python
from openapi_client.models.choice_action_object import ChoiceActionObject

# TODO update the JSON string below
json = "{}"
# create an instance of ChoiceActionObject from a JSON string
choice_action_object_instance = ChoiceActionObject.from_json(json)
# print the JSON string representation of the object
print ChoiceActionObject.to_json()

# convert the object into a dict
choice_action_object_dict = choice_action_object_instance.to_dict()
# create an instance of ChoiceActionObject from a dict
choice_action_object_form_dict = choice_action_object.from_dict(choice_action_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


