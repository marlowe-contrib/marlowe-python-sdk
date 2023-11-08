# InputOneOf3

Deposit funds into an account in a contract and provide the continuation of the contract

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**continuation_hash** | **str** |  | 
**input_from_party** | [**Party**](Party.md) |  | 
**into_account** | [**Party**](Party.md) |  | 
**merkleized_continuation** | [**Contract**](Contract.md) |  | 
**of_token** | [**Token**](Token.md) |  | 
**that_deposits** | **int** |  | 

## Example

```python
from openapi_client.models.input_one_of3 import InputOneOf3

# TODO update the JSON string below
json = "{}"
# create an instance of InputOneOf3 from a JSON string
input_one_of3_instance = InputOneOf3.from_json(json)
# print the JSON string representation of the object
print InputOneOf3.to_json()

# convert the object into a dict
input_one_of3_dict = input_one_of3_instance.to_dict()
# create an instance of InputOneOf3 from a dict
input_one_of3_form_dict = input_one_of3.from_dict(input_one_of3_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


