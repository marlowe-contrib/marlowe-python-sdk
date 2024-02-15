# ModelAssert

Check an observation and produce a warning if it is false.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_assert** | [**Observation**](Observation.md) |  | 
**then** | [**Contract**](Contract.md) |  | 

## Example

```python
from openapi_client.models.model_assert import ModelAssert

# TODO update the JSON string below
json = "{}"
# create an instance of ModelAssert from a JSON string
model_assert_instance = ModelAssert.from_json(json)
# print the JSON string representation of the object
print ModelAssert.to_json()

# convert the object into a dict
model_assert_dict = model_assert_instance.to_dict()
# create an instance of ModelAssert from a dict
model_assert_form_dict = model_assert.from_dict(model_assert_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


