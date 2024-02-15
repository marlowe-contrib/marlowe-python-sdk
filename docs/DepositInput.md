# DepositInput

Deposit funds into an account in a contract

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**input_from_party** | [**Party**](Party.md) |  | 
**into_account** | [**Party**](Party.md) |  | 
**of_token** | [**Token**](Token.md) |  | 
**that_deposits** | **int** |  | 

## Example

```python
from openapi_client.models.deposit_input import DepositInput

# TODO update the JSON string below
json = "{}"
# create an instance of DepositInput from a JSON string
deposit_input_instance = DepositInput.from_json(json)
# print the JSON string representation of the object
print DepositInput.to_json()

# convert the object into a dict
deposit_input_dict = deposit_input_instance.to_dict()
# create an instance of DepositInput from a dict
deposit_input_form_dict = deposit_input.from_dict(deposit_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


