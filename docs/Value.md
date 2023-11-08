# Value

A time-varying expression that evaluates to a boolean

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount_of_token** | [**Token**](Token.md) |  | 
**in_account** | [**Party**](Party.md) |  | 
**negate** | [**Value**](Value.md) |  | 
**add** | [**Value**](Value.md) |  | 
**var_and** | [**Value**](Value.md) |  | 
**minus** | [**Value**](Value.md) |  | 
**value** | [**Value**](Value.md) |  | 
**multiply** | [**Value**](Value.md) |  | 
**times** | [**Value**](Value.md) |  | 
**by** | [**Value**](Value.md) |  | 
**divide** | [**Value**](Value.md) |  | 
**value_of_choice** | [**ChoiceId**](ChoiceId.md) |  | 
**use_value** | **str** |  | 
**var_else** | [**Value**](Value.md) |  | 
**var_if** | [**Observation**](Observation.md) |  | 
**then** | [**Value**](Value.md) |  | 

## Example

```python
from openapi_client.models.value import Value

# TODO update the JSON string below
json = "{}"
# create an instance of Value from a JSON string
value_instance = Value.from_json(json)
# print the JSON string representation of the object
print Value.to_json()

# convert the object into a dict
value_dict = value_instance.to_dict()
# create an instance of Value from a dict
value_form_dict = value.from_dict(value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


