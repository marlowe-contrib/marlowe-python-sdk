# coding: utf-8

"""
    

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json



from pydantic import BaseModel, Field
from openapi_client.models.apply_inputs_tx_envelope import ApplyInputsTxEnvelope
from openapi_client.models.contracts_contract_id_transactions_post201_response_links import ContractsContractIdTransactionsPost201ResponseLinks

class ContractsContractIdTransactionsPost201Response(BaseModel):
    """
    ContractsContractIdTransactionsPost201Response
    """
    links: ContractsContractIdTransactionsPost201ResponseLinks = Field(...)
    resource: ApplyInputsTxEnvelope = Field(...)
    __properties = ["links", "resource"]

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> ContractsContractIdTransactionsPost201Response:
        """Create an instance of ContractsContractIdTransactionsPost201Response from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of links
        if self.links:
            _dict['links'] = self.links.to_dict()
        # override the default output from pydantic by calling `to_dict()` of resource
        if self.resource:
            _dict['resource'] = self.resource.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ContractsContractIdTransactionsPost201Response:
        """Create an instance of ContractsContractIdTransactionsPost201Response from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ContractsContractIdTransactionsPost201Response.parse_obj(obj)

        _obj = ContractsContractIdTransactionsPost201Response.parse_obj({
            "links": ContractsContractIdTransactionsPost201ResponseLinks.from_dict(obj.get("links")) if obj.get("links") is not None else None,
            "resource": ApplyInputsTxEnvelope.from_dict(obj.get("resource")) if obj.get("resource") is not None else None
        })
        return _obj


