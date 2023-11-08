# LabelledObjectValue


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount_of_token** | [**TokenObject**](TokenObject.md) |  | 
**in_account** | [**PartyObject**](PartyObject.md) |  | 
**negate** | [**ValueObject**](ValueObject.md) |  | 
**add** | [**ValueObject**](ValueObject.md) |  | 
**var_and** | [**ObservationObject**](ObservationObject.md) |  | 
**minus** | [**ValueObject**](ValueObject.md) |  | 
**value** | [**ValueObject**](ValueObject.md) |  | 
**multiply** | [**ValueObject**](ValueObject.md) |  | 
**times** | [**ValueObject**](ValueObject.md) |  | 
**by** | [**ValueObject**](ValueObject.md) |  | 
**divide** | [**ValueObject**](ValueObject.md) |  | 
**value_of_choice** | [**ChoiceIdObject**](ChoiceIdObject.md) |  | 
**use_value** | **str** |  | 
**var_else** | [**ContractObject**](ContractObject.md) |  | 
**var_if** | [**ObservationObject**](ObservationObject.md) |  | 
**then** | [**ContractObject**](ContractObject.md) |  | 
**ref** | **str** | An arbitrary text identifier for an object in a Marlowe object bundle. | 
**both** | [**ObservationObject**](ObservationObject.md) |  | 
**either** | [**ObservationObject**](ObservationObject.md) |  | 
**var_or** | [**ObservationObject**](ObservationObject.md) |  | 
**var_not** | [**ObservationObject**](ObservationObject.md) |  | 
**chose_something_for** | [**ChoiceIdObject**](ChoiceIdObject.md) |  | 
**ge_than** | [**ValueObject**](ValueObject.md) |  | 
**gt** | [**ValueObject**](ValueObject.md) |  | 
**lt** | [**ValueObject**](ValueObject.md) |  | 
**le_than** | [**ValueObject**](ValueObject.md) |  | 
**equal_to** | [**ValueObject**](ValueObject.md) |  | 
**from_account** | [**PartyObject**](PartyObject.md) |  | 
**pay** | [**ValueObject**](ValueObject.md) |  | 
**to** | [**PayeeObject**](PayeeObject.md) |  | 
**token** | [**TokenObject**](TokenObject.md) |  | 
**timeout** | **int** |  | 
**timeout_continuation** | [**ContractObject**](ContractObject.md) |  | 
**when** | [**List[CaseObject]**](CaseObject.md) |  | 
**be** | [**ValueObject**](ValueObject.md) |  | 
**let** | **str** |  | 
**var_assert** | [**ObservationObject**](ObservationObject.md) |  | 
**role_token** | **str** |  | 
**address** | **str** | A cardano address | 
**currency_symbol** | **str** |  | 
**token_name** | **str** |  | 
**deposits** | [**Value**](Value.md) |  | 
**into_account** | [**Party**](Party.md) |  | 
**of_token** | [**Token**](Token.md) |  | 
**party** | [**Party**](Party.md) |  | 
**choose_between** | [**List[Bound]**](Bound.md) |  | 
**for_choice** | [**ChoiceId**](ChoiceId.md) |  | 
**notify_if** | [**Observation**](Observation.md) |  | 

## Example

```python
from openapi_client.models.labelled_object_value import LabelledObjectValue

# TODO update the JSON string below
json = "{}"
# create an instance of LabelledObjectValue from a JSON string
labelled_object_value_instance = LabelledObjectValue.from_json(json)
# print the JSON string representation of the object
print LabelledObjectValue.to_json()

# convert the object into a dict
labelled_object_value_dict = labelled_object_value_instance.to_dict()
# create an instance of LabelledObjectValue from a dict
labelled_object_value_form_dict = labelled_object_value.from_dict(labelled_object_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


