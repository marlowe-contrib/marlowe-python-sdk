# Contract

Contract terms specified in Marlowe

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
from openapi_client.models.contract import Contract

# TODO update the JSON string below
json = "{}"
# create an instance of Contract from a JSON string
contract_instance = Contract.from_json(json)
# print the JSON string representation of the object
print Contract.to_json()

# convert the object into a dict
contract_dict = contract_instance.to_dict()
# create an instance of Contract from a dict
contract_form_dict = contract.from_dict(contract_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


