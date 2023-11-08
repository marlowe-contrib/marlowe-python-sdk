# CanDeposit

Deposit Input that can be applied for a given contract

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**can_deposit** | **int** |  | 
**case_index** | **int** | Index of a \&quot;Case Action\&quot; in a \&quot;When\&quot; | 
**into_account** | [**Party**](Party.md) |  | 
**is_merkleized_continuation** | **bool** | Indicates if a given contract continuation is merkleized | 
**of_token** | [**Token**](Token.md) |  | 
**party** | [**Party**](Party.md) |  | 

## Example

```python
from openapi_client.models.can_deposit import CanDeposit

# TODO update the JSON string below
json = "{}"
# create an instance of CanDeposit from a JSON string
can_deposit_instance = CanDeposit.from_json(json)
# print the JSON string representation of the object
print CanDeposit.to_json()

# convert the object into a dict
can_deposit_dict = can_deposit_instance.to_dict()
# create an instance of CanDeposit from a dict
can_deposit_form_dict = can_deposit.from_dict(can_deposit_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


