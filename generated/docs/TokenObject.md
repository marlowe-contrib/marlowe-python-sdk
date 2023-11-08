# TokenObject

A token with a currency symbol (minting policy ID) and token name.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**currency_symbol** | **str** |  | 
**token_name** | **str** |  | 
**ref** | **str** | An arbitrary text identifier for an object in a Marlowe object bundle. | 

## Example

```python
from openapi_client.models.token_object import TokenObject

# TODO update the JSON string below
json = "{}"
# create an instance of TokenObject from a JSON string
token_object_instance = TokenObject.from_json(json)
# print the JSON string representation of the object
print TokenObject.to_json()

# convert the object into a dict
token_object_dict = token_object_instance.to_dict()
# create an instance of TokenObject from a dict
token_object_form_dict = token_object.from_dict(token_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


