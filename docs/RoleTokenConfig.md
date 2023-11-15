# RoleTokenConfig


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** | A cardano address, in Bech32 format | 
**metadata** | [**TokenMetadata**](TokenMetadata.md) |  | 
**script** | **str** | The type of script receiving the role token. | 

## Example

```python
from openapi_client.models.role_token_config import RoleTokenConfig

# TODO update the JSON string below
json = "{}"
# create an instance of RoleTokenConfig from a JSON string
role_token_config_instance = RoleTokenConfig.from_json(json)
# print the JSON string representation of the object
print RoleTokenConfig.to_json()

# convert the object into a dict
role_token_config_dict = role_token_config_instance.to_dict()
# create an instance of RoleTokenConfig from a dict
role_token_config_form_dict = role_token_config.from_dict(role_token_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


