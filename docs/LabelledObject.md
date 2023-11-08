# LabelledObject

A bundle of labelled Marlowe objects in define-before-use order.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**label** | **str** | An arbitrary text identifier for an object in a Marlowe object bundle. | 
**type** | **str** |  | 
**value** | [**LabelledObjectValue**](LabelledObjectValue.md) |  | 

## Example

```python
from openapi_client.models.labelled_object import LabelledObject

# TODO update the JSON string below
json = "{}"
# create an instance of LabelledObject from a JSON string
labelled_object_instance = LabelledObject.from_json(json)
# print the JSON string representation of the object
print LabelledObject.to_json()

# convert the object into a dict
labelled_object_dict = labelled_object_instance.to_dict()
# create an instance of LabelledObject from a dict
labelled_object_form_dict = labelled_object.from_dict(labelled_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


