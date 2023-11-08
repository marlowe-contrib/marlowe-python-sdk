# GetPayoutResponseLinks


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contract** | **str** |  | [optional] 
**transaction** | **str** |  | [optional] 
**withdrawal** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.get_payout_response_links import GetPayoutResponseLinks

# TODO update the JSON string below
json = "{}"
# create an instance of GetPayoutResponseLinks from a JSON string
get_payout_response_links_instance = GetPayoutResponseLinks.from_json(json)
# print the JSON string representation of the object
print GetPayoutResponseLinks.to_json()

# convert the object into a dict
get_payout_response_links_dict = get_payout_response_links_instance.to_dict()
# create an instance of GetPayoutResponseLinks from a dict
get_payout_response_links_form_dict = get_payout_response_links.from_dict(get_payout_response_links_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


