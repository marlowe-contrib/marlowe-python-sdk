# PostContractsRequestContract


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**from_account** | [**Party**](Party.md) |  | 
**pay** | [**Value**](Value.md) |  | 
**then** | [**Contract**](Contract.md) |  | 
**to** | [**Payee**](Payee.md) |  | 
**token** | [**Token**](Token.md) |  | 
**var_else** | [**Contract**](Contract.md) |  | 
**var_if** | [**Observation**](Observation.md) |  | 
**timeout** | **int** |  | 
**timeout_continuation** | [**Contract**](Contract.md) |  | 
**when** | [**List[Case]**](Case.md) |  | 
**be** | [**Value**](Value.md) |  | 
**let** | **str** |  | 
**var_assert** | [**Observation**](Observation.md) |  | 

## Example

```python
from openapi_client.models.post_contracts_request_contract import PostContractsRequestContract

# TODO update the JSON string below
json = "{}"
# create an instance of PostContractsRequestContract from a JSON string
post_contracts_request_contract_instance = PostContractsRequestContract.from_json(json)
# print the JSON string representation of the object
print PostContractsRequestContract.to_json()

# convert the object into a dict
post_contracts_request_contract_dict = post_contracts_request_contract_instance.to_dict()
# create an instance of PostContractsRequestContract from a dict
post_contracts_request_contract_form_dict = post_contracts_request_contract.from_dict(post_contracts_request_contract_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


