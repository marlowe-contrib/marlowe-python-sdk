# ContractOneOf

A payment will be sent from an account to a payee.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**from_account** | [**Party**](Party.md) |  | 
**pay** | [**Value**](Value.md) |  | 
**then** | [**Contract**](Contract.md) |  | 
**to** | [**Payee**](Payee.md) |  | 
**token** | [**Token**](Token.md) |  | 

## Example

```python
from openapi_client.models.contract_one_of import ContractOneOf

# TODO update the JSON string below
json = "{}"
# create an instance of ContractOneOf from a JSON string
contract_one_of_instance = ContractOneOf.from_json(json)
# print the JSON string representation of the object
print ContractOneOf.to_json()

# convert the object into a dict
contract_one_of_dict = contract_one_of_instance.to_dict()
# create an instance of ContractOneOf from a dict
contract_one_of_form_dict = contract_one_of.from_dict(contract_one_of_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


