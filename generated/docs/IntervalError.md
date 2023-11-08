# IntervalError

A Marlowe transaction interval error.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**invalid_interval** | [**IntervalErrorOneOfInvalidInterval**](IntervalErrorOneOfInvalidInterval.md) |  | 
**interval_in_past_error** | [**IntervalErrorOneOf1IntervalInPastError**](IntervalErrorOneOf1IntervalInPastError.md) |  | 

## Example

```python
from openapi_client.models.interval_error import IntervalError

# TODO update the JSON string below
json = "{}"
# create an instance of IntervalError from a JSON string
interval_error_instance = IntervalError.from_json(json)
# print the JSON string representation of the object
print IntervalError.to_json()

# convert the object into a dict
interval_error_dict = interval_error_instance.to_dict()
# create an instance of IntervalError from a dict
interval_error_form_dict = interval_error.from_dict(interval_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


