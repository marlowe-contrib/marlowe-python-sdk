# CanChoose

Choice Inputs that can be applied for a given contract

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**can_choose_between** | [**List[Bound]**](Bound.md) |  | 
**case_index** | **int** | Index of a \&quot;Case Action\&quot; in a \&quot;When\&quot; | 
**for_choice** | [**ChoiceId**](ChoiceId.md) |  | 
**is_merkleized_continuation** | **bool** | Indicates if a given contract continuation is merkleized | 

## Example

```python
from openapi_client.models.can_choose import CanChoose

# TODO update the JSON string below
json = "{}"
# create an instance of CanChoose from a JSON string
can_choose_instance = CanChoose.from_json(json)
# print the JSON string representation of the object
print CanChoose.to_json()

# convert the object into a dict
can_choose_dict = can_choose_instance.to_dict()
# create an instance of CanChoose from a dict
can_choose_form_dict = can_choose.from_dict(can_choose_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


