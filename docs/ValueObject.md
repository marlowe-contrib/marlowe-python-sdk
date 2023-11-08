# ValueObject

A time-varying expression that evaluates to a boolean

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount_of_token** | [**TokenObject**](TokenObject.md) |  | 
**in_account** | [**PartyObject**](PartyObject.md) |  | 
**negate** | [**ValueObject**](ValueObject.md) |  | 
**add** | [**ValueObject**](ValueObject.md) |  | 
**var_and** | [**ValueObject**](ValueObject.md) |  | 
**minus** | [**ValueObject**](ValueObject.md) |  | 
**value** | [**ValueObject**](ValueObject.md) |  | 
**multiply** | [**ValueObject**](ValueObject.md) |  | 
**times** | [**ValueObject**](ValueObject.md) |  | 
**by** | [**ValueObject**](ValueObject.md) |  | 
**divide** | [**ValueObject**](ValueObject.md) |  | 
**value_of_choice** | [**ChoiceIdObject**](ChoiceIdObject.md) |  | 
**use_value** | **str** |  | 
**var_else** | [**ValueObject**](ValueObject.md) |  | 
**var_if** | [**ObservationObject**](ObservationObject.md) |  | 
**then** | [**ValueObject**](ValueObject.md) |  | 
**ref** | **str** | An arbitrary text identifier for an object in a Marlowe object bundle. | 

## Example

```python
from openapi_client.models.value_object import ValueObject

# TODO update the JSON string below
json = "{}"
# create an instance of ValueObject from a JSON string
value_object_instance = ValueObject.from_json(json)
# print the JSON string representation of the object
print ValueObject.to_json()

# convert the object into a dict
value_object_dict = value_object_instance.to_dict()
# create an instance of ValueObject from a dict
value_object_form_dict = value_object.from_dict(value_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


