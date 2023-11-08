# ValueOneOf


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount_of_token** | [**Token**](Token.md) |  | 
**in_account** | [**Party**](Party.md) |  | 

## Example

```python
from openapi_client.models.value_one_of import ValueOneOf

# TODO update the JSON string below
json = "{}"
# create an instance of ValueOneOf from a JSON string
value_one_of_instance = ValueOneOf.from_json(json)
# print the JSON string representation of the object
print ValueOneOf.to_json()

# convert the object into a dict
value_one_of_dict = value_one_of_instance.to_dict()
# create an instance of ValueOneOf from a dict
value_one_of_form_dict = value_one_of.from_dict(value_one_of_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


