# MetadataAndRecipients


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadata** | [**TokenMetadata**](TokenMetadata.md) |  | [optional] 
**recipients** | **Dict[str, int]** |  | 

## Example

```python
from openapi_client.models.metadata_and_recipients import MetadataAndRecipients

# TODO update the JSON string below
json = "{}"
# create an instance of MetadataAndRecipients from a JSON string
metadata_and_recipients_instance = MetadataAndRecipients.from_json(json)
# print the JSON string representation of the object
print MetadataAndRecipients.to_json()

# convert the object into a dict
metadata_and_recipients_dict = metadata_and_recipients_instance.to_dict()
# create an instance of MetadataAndRecipients from a dict
metadata_and_recipients_form_dict = metadata_and_recipients.from_dict(metadata_and_recipients_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


