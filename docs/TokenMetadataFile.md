# TokenMetadataFile


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**media_type** | **str** |  | 
**name** | **str** |  | 
**src** | **str** |  | 

## Example

```python
from openapi_client.models.token_metadata_file import TokenMetadataFile

# TODO update the JSON string below
json = "{}"
# create an instance of TokenMetadataFile from a JSON string
token_metadata_file_instance = TokenMetadataFile.from_json(json)
# print the JSON string representation of the object
print TokenMetadataFile.to_json()

# convert the object into a dict
token_metadata_file_dict = token_metadata_file_instance.to_dict()
# create an instance of TokenMetadataFile from a dict
token_metadata_file_form_dict = token_metadata_file.from_dict(token_metadata_file_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


