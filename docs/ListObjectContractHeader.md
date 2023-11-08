# ListObjectContractHeader


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[ListObjectContractHeaderResultsInner]**](ListObjectContractHeaderResultsInner.md) |  | 

## Example

```python
from openapi_client.models.list_object_contract_header import ListObjectContractHeader

# TODO update the JSON string below
json = "{}"
# create an instance of ListObjectContractHeader from a JSON string
list_object_contract_header_instance = ListObjectContractHeader.from_json(json)
# print the JSON string representation of the object
print ListObjectContractHeader.to_json()

# convert the object into a dict
list_object_contract_header_dict = list_object_contract_header_instance.to_dict()
# create an instance of ListObjectContractHeader from a dict
list_object_contract_header_form_dict = list_object_contract_header.from_dict(list_object_contract_header_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


