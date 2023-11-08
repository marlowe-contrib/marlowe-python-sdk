# SafetyError

Information about the safety of a Marlowe contract and its state.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | [**Party**](Party.md) |  | [optional] 
**address** | [**PlutusAddress**](PlutusAddress.md) |  | [optional] 
**bytes** | **int** |  | [optional] 
**choice_id** | [**ChoiceId**](ChoiceId.md) |  | [optional] 
**cost** | [**ExBudget**](ExBudget.md) |  | [optional] 
**currency_symbol** | **str** |  | [optional] 
**detail** | **str** |  | 
**error** | **str** |  | 
**fatal** | **bool** |  | 
**hash** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**role_name** | **str** |  | [optional] 
**token** | [**Token**](Token.md) |  | [optional] 
**token_name** | **str** |  | [optional] 
**transaction** | [**Transaction**](Transaction.md) |  | [optional] 
**value_id** | **str** |  | [optional] 
**warning** | [**TransactionWarning**](TransactionWarning.md) |  | [optional] 

## Example

```python
from openapi_client.models.safety_error import SafetyError

# TODO update the JSON string below
json = "{}"
# create an instance of SafetyError from a JSON string
safety_error_instance = SafetyError.from_json(json)
# print the JSON string representation of the object
print SafetyError.to_json()

# convert the object into a dict
safety_error_dict = safety_error_instance.to_dict()
# create an instance of SafetyError from a dict
safety_error_form_dict = safety_error.from_dict(safety_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


