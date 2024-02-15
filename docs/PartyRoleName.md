# PartyRoleName

Refers to a party by role name.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**role_token** | **str** |  | 

## Example

```python
from openapi_client.models.party_role_name import PartyRoleName

# TODO update the JSON string below
json = "{}"
# create an instance of PartyRoleName from a JSON string
party_role_name_instance = PartyRoleName.from_json(json)
# print the JSON string representation of the object
print PartyRoleName.to_json()

# convert the object into a dict
party_role_name_dict = party_role_name_instance.to_dict()
# create an instance of PartyRoleName from a dict
party_role_name_form_dict = party_role_name.from_dict(party_role_name_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


