# ContractsContractIdGet200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**ContractsContractIdGet200ResponseLinks**](ContractsContractIdGet200ResponseLinks.md) |  | 
**resource** | [**ContractState**](ContractState.md) |  | 

## Example

```python
from openapi_client.models.contracts_contract_id_get200_response import ContractsContractIdGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ContractsContractIdGet200Response from a JSON string
contracts_contract_id_get200_response_instance = ContractsContractIdGet200Response.from_json(json)
# print the JSON string representation of the object
print ContractsContractIdGet200Response.to_json()

# convert the object into a dict
contracts_contract_id_get200_response_dict = contracts_contract_id_get200_response_instance.to_dict()
# create an instance of ContractsContractIdGet200Response from a dict
contracts_contract_id_get200_response_form_dict = contracts_contract_id_get200_response.from_dict(contracts_contract_id_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


