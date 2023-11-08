# ObservationObject

A time-varying expression that evaluates to an integer

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_and** | [**ObservationObject**](ObservationObject.md) |  | 
**both** | [**ObservationObject**](ObservationObject.md) |  | 
**either** | [**ObservationObject**](ObservationObject.md) |  | 
**var_or** | [**ObservationObject**](ObservationObject.md) |  | 
**var_not** | [**ObservationObject**](ObservationObject.md) |  | 
**chose_something_for** | [**ChoiceIdObject**](ChoiceIdObject.md) |  | 
**ge_than** | [**ValueObject**](ValueObject.md) |  | 
**value** | [**ValueObject**](ValueObject.md) |  | 
**gt** | [**ValueObject**](ValueObject.md) |  | 
**lt** | [**ValueObject**](ValueObject.md) |  | 
**le_than** | [**ValueObject**](ValueObject.md) |  | 
**equal_to** | [**ValueObject**](ValueObject.md) |  | 
**ref** | **str** | An arbitrary text identifier for an object in a Marlowe object bundle. | 

## Example

```python
from openapi_client.models.observation_object import ObservationObject

# TODO update the JSON string below
json = "{}"
# create an instance of ObservationObject from a JSON string
observation_object_instance = ObservationObject.from_json(json)
# print the JSON string representation of the object
print ObservationObject.to_json()

# convert the object into a dict
observation_object_dict = observation_object_instance.to_dict()
# create an instance of ObservationObject from a dict
observation_object_form_dict = observation_object.from_dict(observation_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


