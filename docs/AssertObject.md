# AssertObject

Check an observation and produce a warning if it is false.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_assert** | [**ObservationObject**](ObservationObject.md) |  | 
**then** | [**ContractObject**](ContractObject.md) |  | 

## Example

```python
from openapi_client.models.assert_object import AssertObject

# TODO update the JSON string below
json = "{}"
# create an instance of AssertObject from a JSON string
assert_object_instance = AssertObject.from_json(json)
# print the JSON string representation of the object
print AssertObject.to_json()

# convert the object into a dict
assert_object_dict = assert_object_instance.to_dict()
# create an instance of AssertObject from a dict
assert_object_form_dict = assert_object.from_dict(assert_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


