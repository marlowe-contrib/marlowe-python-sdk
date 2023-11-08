# TokenMetadata

Metadata for an NFT, as described by https://cips.cardano.org/cips/cip25/

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | [optional] 
**files** | [**List[TokenMetadataFile]**](TokenMetadataFile.md) |  | [optional] 
**image** | **str** |  | 
**media_type** | **str** |  | [optional] 
**name** | **str** |  | 

## Example

```python
from openapi_client.models.token_metadata import TokenMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of TokenMetadata from a JSON string
token_metadata_instance = TokenMetadata.from_json(json)
# print the JSON string representation of the object
print TokenMetadata.to_json()

# convert the object into a dict
token_metadata_dict = token_metadata_instance.to_dict()
# create an instance of TokenMetadata from a dict
token_metadata_form_dict = token_metadata.from_dict(token_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


