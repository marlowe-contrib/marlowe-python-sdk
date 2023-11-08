# GetTransactionResponseLinks


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.get_transaction_response_links import GetTransactionResponseLinks

# TODO update the JSON string below
json = "{}"
# create an instance of GetTransactionResponseLinks from a JSON string
get_transaction_response_links_instance = GetTransactionResponseLinks.from_json(json)
# print the JSON string representation of the object
print GetTransactionResponseLinks.to_json()

# convert the object into a dict
get_transaction_response_links_dict = get_transaction_response_links_instance.to_dict()
# create an instance of GetTransactionResponseLinks from a dict
get_transaction_response_links_form_dict = get_transaction_response_links.from_dict(get_transaction_response_links_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


