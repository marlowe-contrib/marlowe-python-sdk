# ContractObjectOneOf2

Wait for an action to be performed and apply the matching contract when it does. Apply the timeout contract if no actions have been performed in the timeout period.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**timeout** | **int** |  | 
**timeout_continuation** | [**ContractObject**](ContractObject.md) |  | 
**when** | [**List[CaseObject]**](CaseObject.md) |  | 

## Example

```python
from openapi_client.models.contract_object_one_of2 import ContractObjectOneOf2

# TODO update the JSON string below
json = "{}"
# create an instance of ContractObjectOneOf2 from a JSON string
contract_object_one_of2_instance = ContractObjectOneOf2.from_json(json)
# print the JSON string representation of the object
print ContractObjectOneOf2.to_json()

# convert the object into a dict
contract_object_one_of2_dict = contract_object_one_of2_instance.to_dict()
# create an instance of ContractObjectOneOf2 from a dict
contract_object_one_of2_form_dict = contract_object_one_of2.from_dict(contract_object_one_of2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


