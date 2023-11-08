# GetContractResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**GetContractResponseLinks**](GetContractResponseLinks.md) |  | 
**resource** | [**ContractState**](ContractState.md) |  | 

## Example

```python
from openapi_client.models.get_contract_response import GetContractResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetContractResponse from a JSON string
get_contract_response_instance = GetContractResponse.from_json(json)
# print the JSON string representation of the object
print GetContractResponse.to_json()

# convert the object into a dict
get_contract_response_dict = get_contract_response_instance.to_dict()
# create an instance of GetContractResponse from a dict
get_contract_response_form_dict = get_contract_response.from_dict(get_contract_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


