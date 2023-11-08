# InputOneOf2

Make a choice in a contract

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**for_choice_id** | [**ChoiceId**](ChoiceId.md) |  | 
**input_that_chooses_num** | **int** |  | 

## Example

```python
from openapi_client.models.input_one_of2 import InputOneOf2

# TODO update the JSON string below
json = "{}"
# create an instance of InputOneOf2 from a JSON string
input_one_of2_instance = InputOneOf2.from_json(json)
# print the JSON string representation of the object
print InputOneOf2.to_json()

# convert the object into a dict
input_one_of2_dict = input_one_of2_instance.to_dict()
# create an instance of InputOneOf2 from a dict
input_one_of2_form_dict = input_one_of2.from_dict(input_one_of2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


