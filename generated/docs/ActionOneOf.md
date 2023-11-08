# ActionOneOf


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deposits** | [**Value**](Value.md) |  | 
**into_account** | [**Party**](Party.md) |  | 
**of_token** | [**Token**](Token.md) |  | 
**party** | [**Party**](Party.md) |  | 

## Example

```python
from openapi_client.models.action_one_of import ActionOneOf

# TODO update the JSON string below
json = "{}"
# create an instance of ActionOneOf from a JSON string
action_one_of_instance = ActionOneOf.from_json(json)
# print the JSON string representation of the object
print ActionOneOf.to_json()

# convert the object into a dict
action_one_of_dict = action_one_of_instance.to_dict()
# create an instance of ActionOneOf from a dict
action_one_of_form_dict = action_one_of.from_dict(action_one_of_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


