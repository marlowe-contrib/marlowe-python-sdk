# PayoutHeader


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contract_id** | **str** | A reference to a transaction output with a transaction ID and index. | 
**payout_id** | **str** | A reference to a transaction output with a transaction ID and index. | 
**role** | [**AssetId**](AssetId.md) |  | 
**status** | [**PayoutStatus**](PayoutStatus.md) |  | 
**withdrawal_id** | **str** | The hex-encoded identifier of a Cardano transaction | [optional] 

## Example

```python
from openapi_client.models.payout_header import PayoutHeader

# TODO update the JSON string below
json = "{}"
# create an instance of PayoutHeader from a JSON string
payout_header_instance = PayoutHeader.from_json(json)
# print the JSON string representation of the object
print PayoutHeader.to_json()

# convert the object into a dict
payout_header_dict = payout_header_instance.to_dict()
# create an instance of PayoutHeader from a dict
payout_header_form_dict = payout_header.from_dict(payout_header_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


