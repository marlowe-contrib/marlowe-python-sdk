# CanNotify

Notify Input tha can be applied for a given contract

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**case_index** | **int** | Index of a \&quot;Case Action\&quot; in a \&quot;When\&quot; | 
**is_merkleized_continuation** | **bool** | Indicates if a given contract continuation is merkleized | 

## Example

```python
from openapi_client.models.can_notify import CanNotify

# TODO update the JSON string below
json = "{}"
# create an instance of CanNotify from a JSON string
can_notify_instance = CanNotify.from_json(json)
# print the JSON string representation of the object
print CanNotify.to_json()

# convert the object into a dict
can_notify_dict = can_notify_instance.to_dict()
# create an instance of CanNotify from a dict
can_notify_form_dict = can_notify.from_dict(can_notify_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


