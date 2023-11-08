# ContractObject

Contract terms specified in Marlowe

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**from_account** | [**PartyObject**](PartyObject.md) |  | 
**pay** | [**ValueObject**](ValueObject.md) |  | 
**then** | [**ContractObject**](ContractObject.md) |  | 
**to** | [**PayeeObject**](PayeeObject.md) |  | 
**token** | [**TokenObject**](TokenObject.md) |  | 
**var_else** | [**ContractObject**](ContractObject.md) |  | 
**var_if** | [**ObservationObject**](ObservationObject.md) |  | 
**timeout** | **int** |  | 
**timeout_continuation** | [**ContractObject**](ContractObject.md) |  | 
**when** | [**List[CaseObject]**](CaseObject.md) |  | 
**be** | [**ValueObject**](ValueObject.md) |  | 
**let** | **str** |  | 
**var_assert** | [**ObservationObject**](ObservationObject.md) |  | 
**ref** | **str** | An arbitrary text identifier for an object in a Marlowe object bundle. | 

## Example

```python
from openapi_client.models.contract_object import ContractObject

# TODO update the JSON string below
json = "{}"
# create an instance of ContractObject from a JSON string
contract_object_instance = ContractObject.from_json(json)
# print the JSON string representation of the object
print ContractObject.to_json()

# convert the object into a dict
contract_object_dict = contract_object_instance.to_dict()
# create an instance of ContractObject from a dict
contract_object_form_dict = contract_object.from_dict(contract_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


