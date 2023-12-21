# PayToAccountObject

Pays funds into a party's account in the contract.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account** | [**PartyObject**](PartyObject.md) |  | 

## Example

```python
from openapi_client.models.pay_to_account_object import PayToAccountObject

# TODO update the JSON string below
json = "{}"
# create an instance of PayToAccountObject from a JSON string
pay_to_account_object_instance = PayToAccountObject.from_json(json)
# print the JSON string representation of the object
print PayToAccountObject.to_json()

# convert the object into a dict
pay_to_account_object_dict = pay_to_account_object_instance.to_dict()
# create an instance of PayToAccountObject from a dict
pay_to_account_object_form_dict = pay_to_account_object.from_dict(pay_to_account_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


