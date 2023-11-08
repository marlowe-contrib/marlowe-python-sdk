# BlockHeader


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**block_header_hash** | **str** |  | 
**block_no** | **int** |  | 
**slot_no** | **int** |  | 

## Example

```python
from openapi_client.models.block_header import BlockHeader

# TODO update the JSON string below
json = "{}"
# create an instance of BlockHeader from a JSON string
block_header_instance = BlockHeader.from_json(json)
# print the JSON string representation of the object
print BlockHeader.to_json()

# convert the object into a dict
block_header_dict = block_header_instance.to_dict()
# create an instance of BlockHeader from a dict
block_header_form_dict = block_header.from_dict(block_header_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


