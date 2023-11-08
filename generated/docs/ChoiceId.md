# ChoiceId

Refers to a party by role name.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**choice_name** | **str** |  | 
**choice_owner** | [**Party**](Party.md) |  | 

## Example

```python
from openapi_client.models.choice_id import ChoiceId

# TODO update the JSON string below
json = "{}"
# create an instance of ChoiceId from a JSON string
choice_id_instance = ChoiceId.from_json(json)
# print the JSON string representation of the object
print ChoiceId.to_json()

# convert the object into a dict
choice_id_dict = choice_id_instance.to_dict()
# create an instance of ChoiceId from a dict
choice_id_form_dict = choice_id.from_dict(choice_id_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


