# TokenInAccountObject


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount_of_token** | [**TokenObject**](TokenObject.md) |  | 
**in_account** | [**PartyObject**](PartyObject.md) |  | 

## Example

```python
from openapi_client.models.token_in_account_object import TokenInAccountObject

# TODO update the JSON string below
json = "{}"
# create an instance of TokenInAccountObject from a JSON string
token_in_account_object_instance = TokenInAccountObject.from_json(json)
# print the JSON string representation of the object
print TokenInAccountObject.to_json()

# convert the object into a dict
token_in_account_object_dict = token_in_account_object_instance.to_dict()
# create an instance of TokenInAccountObject from a dict
token_in_account_object_form_dict = token_in_account_object.from_dict(token_in_account_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


