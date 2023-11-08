# ApplicableInputs

Applicable Inputs for a given contract

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**choices** | [**List[CanChoose]**](CanChoose.md) |  | 
**deposits** | [**List[CanDeposit]**](CanDeposit.md) |  | 
**notify** | [**CanNotify**](CanNotify.md) |  | [optional] 

## Example

```python
from openapi_client.models.applicable_inputs import ApplicableInputs

# TODO update the JSON string below
json = "{}"
# create an instance of ApplicableInputs from a JSON string
applicable_inputs_instance = ApplicableInputs.from_json(json)
# print the JSON string representation of the object
print ApplicableInputs.to_json()

# convert the object into a dict
applicable_inputs_dict = applicable_inputs_instance.to_dict()
# create an instance of ApplicableInputs from a dict
applicable_inputs_form_dict = applicable_inputs.from_dict(applicable_inputs_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


