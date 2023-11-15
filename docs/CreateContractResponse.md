# CreateContractResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**CreateContractResponseLinks**](CreateContractResponseLinks.md) |  | 
**resource** | [**CreateTxEnvelope**](CreateTxEnvelope.md) |  | 

## Example

```python
from openapi_client.models.create_contract_response import CreateContractResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreateContractResponse from a JSON string
create_contract_response_instance = CreateContractResponse.from_json(json)
# print the JSON string representation of the object
print CreateContractResponse.to_json()

# convert the object into a dict
create_contract_response_dict = create_contract_response_instance.to_dict()
# create an instance of CreateContractResponse from a dict
create_contract_response_form_dict = create_contract_response.from_dict(create_contract_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


