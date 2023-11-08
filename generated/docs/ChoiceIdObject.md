# ChoiceIdObject

Refers to a party by role name.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**choice_name** | **str** |  | 
**choice_owner** | [**PartyObject**](PartyObject.md) |  | 

## Example

```python
from openapi_client.models.choice_id_object import ChoiceIdObject

# TODO update the JSON string below
json = "{}"
# create an instance of ChoiceIdObject from a JSON string
choice_id_object_instance = ChoiceIdObject.from_json(json)
# print the JSON string representation of the object
print ChoiceIdObject.to_json()

# convert the object into a dict
choice_id_object_dict = choice_id_object_instance.to_dict()
# create an instance of ChoiceIdObject from a dict
choice_id_object_form_dict = choice_id_object.from_dict(choice_id_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


