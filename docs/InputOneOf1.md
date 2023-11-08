# InputOneOf1

Make a choice in a contract and provide the continuation of the contract

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**continuation_hash** | **str** |  | 
**for_choice_id** | [**ChoiceId**](ChoiceId.md) |  | 
**input_that_chooses_num** | **int** |  | 
**merkleized_continuation** | [**Contract**](Contract.md) |  | 

## Example

```python
from openapi_client.models.input_one_of1 import InputOneOf1

# TODO update the JSON string below
json = "{}"
# create an instance of InputOneOf1 from a JSON string
input_one_of1_instance = InputOneOf1.from_json(json)
# print the JSON string representation of the object
print InputOneOf1.to_json()

# convert the object into a dict
input_one_of1_dict = input_one_of1_instance.to_dict()
# create an instance of InputOneOf1 from a dict
input_one_of1_form_dict = input_one_of1.from_dict(input_one_of1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


