# IntervalErrorOneOf

Invalid Marlowe transaction interval.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**invalid_interval** | [**IntervalErrorOneOfInvalidInterval**](IntervalErrorOneOfInvalidInterval.md) |  | 

## Example

```python
from openapi_client.models.interval_error_one_of import IntervalErrorOneOf

# TODO update the JSON string below
json = "{}"
# create an instance of IntervalErrorOneOf from a JSON string
interval_error_one_of_instance = IntervalErrorOneOf.from_json(json)
# print the JSON string representation of the object
print IntervalErrorOneOf.to_json()

# convert the object into a dict
interval_error_one_of_dict = interval_error_one_of_instance.to_dict()
# create an instance of IntervalErrorOneOf from a dict
interval_error_one_of_form_dict = interval_error_one_of.from_dict(interval_error_one_of_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


