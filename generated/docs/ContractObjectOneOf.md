# ContractObjectOneOf

A payment will be sent from an account to a payee.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**from_account** | [**PartyObject**](PartyObject.md) |  | 
**pay** | [**ValueObject**](ValueObject.md) |  | 
**then** | [**ContractObject**](ContractObject.md) |  | 
**to** | [**PayeeObject**](PayeeObject.md) |  | 
**token** | [**TokenObject**](TokenObject.md) |  | 

## Example

```python
from openapi_client.models.contract_object_one_of import ContractObjectOneOf

# TODO update the JSON string below
json = "{}"
# create an instance of ContractObjectOneOf from a JSON string
contract_object_one_of_instance = ContractObjectOneOf.from_json(json)
# print the JSON string representation of the object
print ContractObjectOneOf.to_json()

# convert the object into a dict
contract_object_one_of_dict = contract_object_one_of_instance.to_dict()
# create an instance of ContractObjectOneOf from a dict
contract_object_one_of_form_dict = contract_object_one_of.from_dict(contract_object_one_of_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


