# WithdrawalHeader


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**block** | [**BlockHeader**](BlockHeader.md) |  | [optional] 
**status** | [**TxStatus**](TxStatus.md) |  | 
**withdrawal_id** | **str** | The hex-encoded identifier of a Cardano transaction | 

## Example

```python
from openapi_client.models.withdrawal_header import WithdrawalHeader

# TODO update the JSON string below
json = "{}"
# create an instance of WithdrawalHeader from a JSON string
withdrawal_header_instance = WithdrawalHeader.from_json(json)
# print the JSON string representation of the object
print WithdrawalHeader.to_json()

# convert the object into a dict
withdrawal_header_dict = withdrawal_header_instance.to_dict()
# create an instance of WithdrawalHeader from a dict
withdrawal_header_form_dict = withdrawal_header.from_dict(withdrawal_header_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


