# ValueObjectOneOf


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount_of_token** | [**TokenObject**](TokenObject.md) |  | 
**in_account** | [**PartyObject**](PartyObject.md) |  | 

## Example

```python
from openapi_client.models.value_object_one_of import ValueObjectOneOf

# TODO update the JSON string below
json = "{}"
# create an instance of ValueObjectOneOf from a JSON string
value_object_one_of_instance = ValueObjectOneOf.from_json(json)
# print the JSON string representation of the object
print ValueObjectOneOf.to_json()

# convert the object into a dict
value_object_one_of_dict = value_object_one_of_instance.to_dict()
# create an instance of ValueObjectOneOf from a dict
value_object_one_of_form_dict = value_object_one_of.from_dict(value_object_one_of_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


