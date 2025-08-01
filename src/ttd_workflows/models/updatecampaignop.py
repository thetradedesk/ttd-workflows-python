"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .campaignpayload import CampaignPayload, CampaignPayloadTypedDict
from .httpmetadata import HTTPMetadata, HTTPMetadataTypedDict
import pydantic
from ttd_workflows.types import BaseModel
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class UpdateCampaignResponseTypedDict(TypedDict):
    http_meta: HTTPMetadataTypedDict
    campaign_payload: NotRequired[CampaignPayloadTypedDict]
    r"""OK"""


class UpdateCampaignResponse(BaseModel):
    http_meta: Annotated[Optional[HTTPMetadata], pydantic.Field(exclude=True)] = None

    campaign_payload: Optional[CampaignPayload] = None
    r"""OK"""
