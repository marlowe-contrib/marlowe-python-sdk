# ContractObjectOneOf3

Bind a value to a name within the scope of a sub-contract.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**be** | [**ValueObject**](ValueObject.md) |  | 
**let** | **str** |  | 
**then** | [**ContractObject**](ContractObject.md) |  | 

## Example

```python
from openapi_client.models.contract_object_one_of3 import ContractObjectOneOf3

# TODO update the JSON string below
json = "{}"
# create an instance of ContractObjectOneOf3 from a JSON string
contract_object_one_of3_instance = ContractObjectOneOf3.from_json(json)
# print the JSON string representation of the object
print ContractObjectOneOf3.to_json()

# convert the object into a dict
contract_object_one_of3_dict = contract_object_one_of3_instance.to_dict()
# create an instance of ContractObjectOneOf3 from a dict
contract_object_one_of3_form_dict = contract_object_one_of3.from_dict(contract_object_one_of3_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


