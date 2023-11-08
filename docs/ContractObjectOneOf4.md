# ContractObjectOneOf4

Check an observation and produce a warning if it is false.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_assert** | [**ObservationObject**](ObservationObject.md) |  | 
**then** | [**ContractObject**](ContractObject.md) |  | 

## Example

```python
from openapi_client.models.contract_object_one_of4 import ContractObjectOneOf4

# TODO update the JSON string below
json = "{}"
# create an instance of ContractObjectOneOf4 from a JSON string
contract_object_one_of4_instance = ContractObjectOneOf4.from_json(json)
# print the JSON string representation of the object
print ContractObjectOneOf4.to_json()

# convert the object into a dict
contract_object_one_of4_dict = contract_object_one_of4_instance.to_dict()
# create an instance of ContractObjectOneOf4 from a dict
contract_object_one_of4_form_dict = contract_object_one_of4.from_dict(contract_object_one_of4_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


