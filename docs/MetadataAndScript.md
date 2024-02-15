# MetadataAndScript


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadata** | [**TokenMetadata**](TokenMetadata.md) |  | [optional] 
**script** | **str** | The type of script receiving the role token. | 

## Example

```python
from openapi_client.models.metadata_and_script import MetadataAndScript

# TODO update the JSON string below
json = "{}"
# create an instance of MetadataAndScript from a JSON string
metadata_and_script_instance = MetadataAndScript.from_json(json)
# print the JSON string representation of the object
print MetadataAndScript.to_json()

# convert the object into a dict
metadata_and_script_dict = metadata_and_script_instance.to_dict()
# create an instance of MetadataAndScript from a dict
metadata_and_script_form_dict = metadata_and_script.from_dict(metadata_and_script_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


