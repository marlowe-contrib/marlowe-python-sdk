# ContractObjectOneOf1

If an observation is true, the first contract applies, otherwise the second contract applies.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_else** | [**ContractObject**](ContractObject.md) |  | 
**var_if** | [**ObservationObject**](ObservationObject.md) |  | 
**then** | [**ContractObject**](ContractObject.md) |  | 

## Example

```python
from openapi_client.models.contract_object_one_of1 import ContractObjectOneOf1

# TODO update the JSON string below
json = "{}"
# create an instance of ContractObjectOneOf1 from a JSON string
contract_object_one_of1_instance = ContractObjectOneOf1.from_json(json)
# print the JSON string representation of the object
print ContractObjectOneOf1.to_json()

# convert the object into a dict
contract_object_one_of1_dict = contract_object_one_of1_instance.to_dict()
# create an instance of ContractObjectOneOf1 from a dict
contract_object_one_of1_form_dict = contract_object_one_of1.from_dict(contract_object_one_of1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


