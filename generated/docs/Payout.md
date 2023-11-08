# Payout


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**assets** | [**Assets**](Assets.md) |  | 
**payout_id** | **str** | A reference to a transaction output with a transaction ID and index. | 
**role** | **str** |  | 

## Example

```python
from openapi_client.models.payout import Payout

# TODO update the JSON string below
json = "{}"
# create an instance of Payout from a JSON string
payout_instance = Payout.from_json(json)
# print the JSON string representation of the object
print Payout.to_json()

# convert the object into a dict
payout_dict = payout_instance.to_dict()
# create an instance of Payout from a dict
payout_form_dict = payout.from_dict(payout_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


