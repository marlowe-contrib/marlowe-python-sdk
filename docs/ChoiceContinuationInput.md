# ChoiceContinuationInput

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
from openapi_client.models.choice_continuation_input import ChoiceContinuationInput

# TODO update the JSON string below
json = "{}"
# create an instance of ChoiceContinuationInput from a JSON string
choice_continuation_input_instance = ChoiceContinuationInput.from_json(json)
# print the JSON string representation of the object
print ChoiceContinuationInput.to_json()

# convert the object into a dict
choice_continuation_input_dict = choice_continuation_input_instance.to_dict()
# create an instance of ChoiceContinuationInput from a dict
choice_continuation_input_form_dict = choice_continuation_input.from_dict(choice_continuation_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


