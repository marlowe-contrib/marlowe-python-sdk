# GetContractsResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[GetContractsResponseResultsInner]**](GetContractsResponseResultsInner.md) |  | 

## Example

```python
from openapi_client.models.get_contracts_response import GetContractsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetContractsResponse from a JSON string
get_contracts_response_instance = GetContractsResponse.from_json(json)
# print the JSON string representation of the object
print GetContractsResponse.to_json()

# convert the object into a dict
get_contracts_response_dict = get_contracts_response_instance.to_dict()
# create an instance of GetContractsResponse from a dict
get_contracts_response_form_dict = get_contracts_response.from_dict(get_contracts_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


