# DepositContinuationInput

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
from openapi_client.models.deposit_continuation_input import DepositContinuationInput

# TODO update the JSON string below
json = "{}"
# create an instance of DepositContinuationInput from a JSON string
deposit_continuation_input_instance = DepositContinuationInput.from_json(json)
# print the JSON string representation of the object
print DepositContinuationInput.to_json()

# convert the object into a dict
deposit_continuation_input_dict = deposit_continuation_input_instance.to_dict()
# create an instance of DepositContinuationInput from a dict
deposit_continuation_input_form_dict = deposit_continuation_input.from_dict(deposit_continuation_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


