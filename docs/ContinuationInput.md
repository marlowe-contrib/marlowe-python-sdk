# ContinuationInput

Notify a contract to check a condition and provide the continuation of the contract

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**continuation_hash** | **str** |  | 
**merkleized_continuation** | [**Contract**](Contract.md) |  | 

## Example

```python
from openapi_client.models.continuation_input import ContinuationInput

# TODO update the JSON string below
json = "{}"
# create an instance of ContinuationInput from a JSON string
continuation_input_instance = ContinuationInput.from_json(json)
# print the JSON string representation of the object
print ContinuationInput.to_json()

# convert the object into a dict
continuation_input_dict = continuation_input_instance.to_dict()
# create an instance of ContinuationInput from a dict
continuation_input_form_dict = continuation_input.from_dict(continuation_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


