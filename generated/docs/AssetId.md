# AssetId


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**asset_name** | **str** |  | 
**policy_id** | **str** | The hex-encoded minting policy ID for a native Cardano token | 

## Example

```python
from openapi_client.models.asset_id import AssetId

# TODO update the JSON string below
json = "{}"
# create an instance of AssetId from a JSON string
asset_id_instance = AssetId.from_json(json)
# print the JSON string representation of the object
print AssetId.to_json()

# convert the object into a dict
asset_id_dict = asset_id_instance.to_dict()
# create an instance of AssetId from a dict
asset_id_form_dict = asset_id.from_dict(asset_id_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


