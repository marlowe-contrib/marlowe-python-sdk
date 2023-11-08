# ContractOneOf2

Wait for an action to be performed and apply the matching contract when it does. Apply the timeout contract if no actions have been performed in the timeout period.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**timeout** | **int** |  | 
**timeout_continuation** | [**Contract**](Contract.md) |  | 
**when** | [**List[Case]**](Case.md) |  | 

## Example

```python
from openapi_client.models.contract_one_of2 import ContractOneOf2

# TODO update the JSON string below
json = "{}"
# create an instance of ContractOneOf2 from a JSON string
contract_one_of2_instance = ContractOneOf2.from_json(json)
# print the JSON string representation of the object
print ContractOneOf2.to_json()

# convert the object into a dict
contract_one_of2_dict = contract_one_of2_instance.to_dict()
# create an instance of ContractOneOf2 from a dict
contract_one_of2_form_dict = contract_one_of2.from_dict(contract_one_of2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


