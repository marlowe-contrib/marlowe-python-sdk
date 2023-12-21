# NonPositiveDeposit

A warning for a non-positive deposit.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**asked_to_deposit** | **int** |  | 
**in_account** | [**Party**](Party.md) |  | 
**of_token** | [**Token**](Token.md) |  | 
**party** | [**Party**](Party.md) |  | 

## Example

```python
from openapi_client.models.non_positive_deposit import NonPositiveDeposit

# TODO update the JSON string below
json = "{}"
# create an instance of NonPositiveDeposit from a JSON string
non_positive_deposit_instance = NonPositiveDeposit.from_json(json)
# print the JSON string representation of the object
print NonPositiveDeposit.to_json()

# convert the object into a dict
non_positive_deposit_dict = non_positive_deposit_instance.to_dict()
# create an instance of NonPositiveDeposit from a dict
non_positive_deposit_form_dict = non_positive_deposit.from_dict(non_positive_deposit_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


