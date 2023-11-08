# PayoutsPayoutIdGet200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**PayoutsPayoutIdGet200ResponseLinks**](PayoutsPayoutIdGet200ResponseLinks.md) |  | 
**resource** | [**PayoutState**](PayoutState.md) |  | 

## Example

```python
from openapi_client.models.payouts_payout_id_get200_response import PayoutsPayoutIdGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of PayoutsPayoutIdGet200Response from a JSON string
payouts_payout_id_get200_response_instance = PayoutsPayoutIdGet200Response.from_json(json)
# print the JSON string representation of the object
print PayoutsPayoutIdGet200Response.to_json()

# convert the object into a dict
payouts_payout_id_get200_response_dict = payouts_payout_id_get200_response_instance.to_dict()
# create an instance of PayoutsPayoutIdGet200Response from a dict
payouts_payout_id_get200_response_form_dict = payouts_payout_id_get200_response.from_dict(payouts_payout_id_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


