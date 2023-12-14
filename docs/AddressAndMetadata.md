# AddressAndMetadata


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** | A cardano address, in Bech32 format | 
**metadata** | [**TokenMetadata**](TokenMetadata.md) |  | [optional] 

## Example

```python
from openapi_client.models.address_and_metadata import AddressAndMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of AddressAndMetadata from a JSON string
address_and_metadata_instance = AddressAndMetadata.from_json(json)
# print the JSON string representation of the object
print AddressAndMetadata.to_json()

# convert the object into a dict
address_and_metadata_dict = address_and_metadata_instance.to_dict()
# create an instance of AddressAndMetadata from a dict
address_and_metadata_form_dict = address_and_metadata.from_dict(address_and_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


