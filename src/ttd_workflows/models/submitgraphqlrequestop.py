"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .httpmetadata import HTTPMetadata, HTTPMetadataTypedDict
import pydantic
from ttd_workflows.types import BaseModel
from typing import Any, Dict, Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class SubmitGraphQlRequestResponseTypedDict(TypedDict):
    http_meta: HTTPMetadataTypedDict
    object: NotRequired[Dict[str, Any]]
    r"""OK"""


class SubmitGraphQlRequestResponse(BaseModel):
    http_meta: Annotated[Optional[HTTPMetadata], pydantic.Field(exclude=True)] = None

    object: Optional[Dict[str, Any]] = None
    r"""OK"""
