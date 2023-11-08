# InputOneOf

Notify a contract to check a condition and provide the continuation of the contract

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**continuation_hash** | **str** |  | 
**merkleized_continuation** | [**Contract**](Contract.md) |  | 

## Example

```python
from openapi_client.models.input_one_of import InputOneOf

# TODO update the JSON string below
json = "{}"
# create an instance of InputOneOf from a JSON string
input_one_of_instance = InputOneOf.from_json(json)
# print the JSON string representation of the object
print InputOneOf.to_json()

# convert the object into a dict
input_one_of_dict = input_one_of_instance.to_dict()
# create an instance of InputOneOf from a dict
input_one_of_form_dict = input_one_of.from_dict(input_one_of_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


