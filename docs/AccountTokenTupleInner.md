# AccountTokenTupleInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**role_token** | **str** |  | 
**address** | **str** | A cardano address, in Bech32 format | 
**currency_symbol** | **str** |  | 
**token_name** | **str** |  | 

## Example

```python
from openapi_client.models.account_token_tuple_inner import AccountTokenTupleInner

# TODO update the JSON string below
json = "{}"
# create an instance of AccountTokenTupleInner from a JSON string
account_token_tuple_inner_instance = AccountTokenTupleInner.from_json(json)
# print the JSON string representation of the object
print AccountTokenTupleInner.to_json()

# convert the object into a dict
account_token_tuple_inner_dict = account_token_tuple_inner_instance.to_dict()
# create an instance of AccountTokenTupleInner from a dict
account_token_tuple_inner_form_dict = account_token_tuple_inner.from_dict(account_token_tuple_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


