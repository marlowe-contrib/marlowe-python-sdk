# PayeeOneOf

Pays funds into a party's account in the contract.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account** | [**Party**](Party.md) |  | 

## Example

```python
from openapi_client.models.payee_one_of import PayeeOneOf

# TODO update the JSON string below
json = "{}"
# create an instance of PayeeOneOf from a JSON string
payee_one_of_instance = PayeeOneOf.from_json(json)
# print the JSON string representation of the object
print PayeeOneOf.to_json()

# convert the object into a dict
payee_one_of_dict = payee_one_of_instance.to_dict()
# create an instance of PayeeOneOf from a dict
payee_one_of_form_dict = payee_one_of.from_dict(payee_one_of_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


