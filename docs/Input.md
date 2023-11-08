# Input

An input to a Marlowe transaction

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**continuation_hash** | **str** |  | 
**merkleized_continuation** | [**Contract**](Contract.md) |  | 
**for_choice_id** | [**ChoiceId**](ChoiceId.md) |  | 
**input_that_chooses_num** | **int** |  | 
**input_from_party** | [**Party**](Party.md) |  | 
**into_account** | [**Party**](Party.md) |  | 
**of_token** | [**Token**](Token.md) |  | 
**that_deposits** | **int** |  | 

## Example

```python
from openapi_client.models.input import Input

# TODO update the JSON string below
json = "{}"
# create an instance of Input from a JSON string
input_instance = Input.from_json(json)
# print the JSON string representation of the object
print Input.to_json()

# convert the object into a dict
input_dict = input_instance.to_dict()
# create an instance of Input from a dict
input_form_dict = input.from_dict(input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


