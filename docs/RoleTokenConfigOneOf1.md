# RoleTokenConfigOneOf1


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadata** | [**TokenMetadata**](TokenMetadata.md) |  | [optional] 
**script** | **str** | The type of script receiving the role token. | 

## Example

```python
from openapi_client.models.role_token_config_one_of1 import RoleTokenConfigOneOf1

# TODO update the JSON string below
json = "{}"
# create an instance of RoleTokenConfigOneOf1 from a JSON string
role_token_config_one_of1_instance = RoleTokenConfigOneOf1.from_json(json)
# print the JSON string representation of the object
print RoleTokenConfigOneOf1.to_json()

# convert the object into a dict
role_token_config_one_of1_dict = role_token_config_one_of1_instance.to_dict()
# create an instance of RoleTokenConfigOneOf1 from a dict
role_token_config_one_of1_form_dict = role_token_config_one_of1.from_dict(role_token_config_one_of1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


