# ContractOneOf3

Bind a value to a name within the scope of a sub-contract.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**be** | [**Value**](Value.md) |  | 
**let** | **str** |  | 
**then** | [**Contract**](Contract.md) |  | 

## Example

```python
from openapi_client.models.contract_one_of3 import ContractOneOf3

# TODO update the JSON string below
json = "{}"
# create an instance of ContractOneOf3 from a JSON string
contract_one_of3_instance = ContractOneOf3.from_json(json)
# print the JSON string representation of the object
print ContractOneOf3.to_json()

# convert the object into a dict
contract_one_of3_dict = contract_one_of3_instance.to_dict()
# create an instance of ContractOneOf3 from a dict
contract_one_of3_form_dict = contract_one_of3.from_dict(contract_one_of3_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


