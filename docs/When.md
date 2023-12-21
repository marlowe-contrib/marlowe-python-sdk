# When

Wait for an action to be performed and apply the matching contract when it does. Apply the timeout contract if no actions have been performed in the timeout period.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**timeout** | **int** |  | 
**timeout_continuation** | [**Contract**](Contract.md) |  | 
**when** | [**List[Case]**](Case.md) |  | 

## Example

```python
from openapi_client.models.when import When

# TODO update the JSON string below
json = "{}"
# create an instance of When from a JSON string
when_instance = When.from_json(json)
# print the JSON string representation of the object
print When.to_json()

# convert the object into a dict
when_dict = when_instance.to_dict()
# create an instance of When from a dict
when_form_dict = when.from_dict(when_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


