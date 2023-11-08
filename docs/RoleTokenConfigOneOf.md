# RoleTokenConfigOneOf


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** | A cardano address | 
**metadata** | [**TokenMetadata**](TokenMetadata.md) |  | 

## Example

```python
from openapi_client.models.role_token_config_one_of import RoleTokenConfigOneOf

# TODO update the JSON string below
json = "{}"
# create an instance of RoleTokenConfigOneOf from a JSON string
role_token_config_one_of_instance = RoleTokenConfigOneOf.from_json(json)
# print the JSON string representation of the object
print RoleTokenConfigOneOf.to_json()

# convert the object into a dict
role_token_config_one_of_dict = role_token_config_one_of_instance.to_dict()
# create an instance of RoleTokenConfigOneOf from a dict
role_token_config_one_of_form_dict = role_token_config_one_of.from_dict(role_token_config_one_of_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


