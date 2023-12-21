# ChoiceInput

Make a choice in a contract

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**for_choice_id** | [**ChoiceId**](ChoiceId.md) |  | 
**input_that_chooses_num** | **int** |  | 

## Example

```python
from openapi_client.models.choice_input import ChoiceInput

# TODO update the JSON string below
json = "{}"
# create an instance of ChoiceInput from a JSON string
choice_input_instance = ChoiceInput.from_json(json)
# print the JSON string representation of the object
print ChoiceInput.to_json()

# convert the object into a dict
choice_input_dict = choice_input_instance.to_dict()
# create an instance of ChoiceInput from a dict
choice_input_form_dict = choice_input.from_dict(choice_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


