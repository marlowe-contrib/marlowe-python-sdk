# TokenInAccount


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount_of_token** | [**Token**](Token.md) |  | 
**in_account** | [**Party**](Party.md) |  | 

## Example

```python
from openapi_client.models.token_in_account import TokenInAccount

# TODO update the JSON string below
json = "{}"
# create an instance of TokenInAccount from a JSON string
token_in_account_instance = TokenInAccount.from_json(json)
# print the JSON string representation of the object
print TokenInAccount.to_json()

# convert the object into a dict
token_in_account_dict = token_in_account_instance.to_dict()
# create an instance of TokenInAccount from a dict
token_in_account_form_dict = token_in_account.from_dict(token_in_account_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


