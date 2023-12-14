# PayToAccount

Pays funds into a party's account in the contract.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account** | [**Party**](Party.md) |  | 

## Example

```python
from openapi_client.models.pay_to_account import PayToAccount

# TODO update the JSON string below
json = "{}"
# create an instance of PayToAccount from a JSON string
pay_to_account_instance = PayToAccount.from_json(json)
# print the JSON string representation of the object
print PayToAccount.to_json()

# convert the object into a dict
pay_to_account_dict = pay_to_account_instance.to_dict()
# create an instance of PayToAccount from a dict
pay_to_account_form_dict = pay_to_account.from_dict(pay_to_account_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


