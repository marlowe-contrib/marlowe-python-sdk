# PostContractSourceResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contract_source_id** | **str** | The hex-encoded identifier of a Marlowe contract source | 
**intermediate_ids** | **Dict[str, str]** |  | 

## Example

```python
from openapi_client.models.post_contract_source_response import PostContractSourceResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PostContractSourceResponse from a JSON string
post_contract_source_response_instance = PostContractSourceResponse.from_json(json)
# print the JSON string representation of the object
print PostContractSourceResponse.to_json()

# convert the object into a dict
post_contract_source_response_dict = post_contract_source_response_instance.to_dict()
# create an instance of PostContractSourceResponse from a dict
post_contract_source_response_form_dict = post_contract_source_response.from_dict(post_contract_source_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


