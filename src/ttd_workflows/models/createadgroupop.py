"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .adgrouppayload import AdGroupPayload, AdGroupPayloadTypedDict
from .httpmetadata import HTTPMetadata, HTTPMetadataTypedDict
import pydantic
from ttd_workflows.types import BaseModel
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class CreateAdGroupResponseTypedDict(TypedDict):
    http_meta: HTTPMetadataTypedDict
    ad_group_payload: NotRequired[AdGroupPayloadTypedDict]
    r"""Created"""


class CreateAdGroupResponse(BaseModel):
    http_meta: Annotated[Optional[HTTPMetadata], pydantic.Field(exclude=True)] = None

    ad_group_payload: Optional[AdGroupPayload] = None
    r"""Created"""
