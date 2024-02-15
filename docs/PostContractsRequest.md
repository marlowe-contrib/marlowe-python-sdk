# PostContractsRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contract** | [**PostContractsRequestContract**](PostContractsRequestContract.md) |  | 
**metadata** | [**Dict[str, Metadata]**](Metadata.md) |  | 
**min_utx_o_deposit** | **int** |  | [optional] 
**roles** | [**RolesConfig**](RolesConfig.md) |  | [optional] 
**tags** | [**Dict[str, Metadata]**](Metadata.md) |  | 
**thread_token_name** | **str** |  | [optional] 
**version** | [**MarloweVersion**](MarloweVersion.md) |  | 

## Example

```python
from openapi_client.models.post_contracts_request import PostContractsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostContractsRequest from a JSON string
post_contracts_request_instance = PostContractsRequest.from_json(json)
# print the JSON string representation of the object
print PostContractsRequest.to_json()

# convert the object into a dict
post_contracts_request_dict = post_contracts_request_instance.to_dict()
# create an instance of PostContractsRequest from a dict
post_contracts_request_form_dict = post_contracts_request.from_dict(post_contracts_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


