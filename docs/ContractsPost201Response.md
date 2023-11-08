# ContractsPost201Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**ContractsPost201ResponseLinks**](ContractsPost201ResponseLinks.md) |  | 
**resource** | [**ApplyInputsTxEnvelope**](ApplyInputsTxEnvelope.md) |  | 

## Example

```python
from openapi_client.models.contracts_post201_response import ContractsPost201Response

# TODO update the JSON string below
json = "{}"
# create an instance of ContractsPost201Response from a JSON string
contracts_post201_response_instance = ContractsPost201Response.from_json(json)
# print the JSON string representation of the object
print ContractsPost201Response.to_json()

# convert the object into a dict
contracts_post201_response_dict = contracts_post201_response_instance.to_dict()
# create an instance of ContractsPost201Response from a dict
contracts_post201_response_form_dict = contracts_post201_response.from_dict(contracts_post201_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


