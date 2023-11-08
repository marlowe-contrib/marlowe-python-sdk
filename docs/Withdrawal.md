# Withdrawal


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**block** | [**BlockHeader**](BlockHeader.md) |  | [optional] 
**payouts** | [**List[PayoutHeader]**](PayoutHeader.md) |  | 
**status** | [**TxStatus**](TxStatus.md) |  | 
**withdrawal_id** | **str** | The hex-encoded identifier of a Cardano transaction | 

## Example

```python
from openapi_client.models.withdrawal import Withdrawal

# TODO update the JSON string below
json = "{}"
# create an instance of Withdrawal from a JSON string
withdrawal_instance = Withdrawal.from_json(json)
# print the JSON string representation of the object
print Withdrawal.to_json()

# convert the object into a dict
withdrawal_dict = withdrawal_instance.to_dict()
# create an instance of Withdrawal from a dict
withdrawal_form_dict = withdrawal.from_dict(withdrawal_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


