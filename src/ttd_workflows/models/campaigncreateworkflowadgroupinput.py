"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .adgroupcreateworkflowprimaryinput import (
    AdGroupCreateWorkflowPrimaryInput,
    AdGroupCreateWorkflowPrimaryInputTypedDict,
)
from .campaigncreateworkflowadgroupadvancedinput import (
    CampaignCreateWorkflowAdGroupAdvancedInput,
    CampaignCreateWorkflowAdGroupAdvancedInputTypedDict,
)
import pydantic
from ttd_workflows.types import BaseModel
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class CampaignCreateWorkflowAdGroupInputTypedDict(TypedDict):
    primary_input: AdGroupCreateWorkflowPrimaryInputTypedDict
    advanced_input: NotRequired[CampaignCreateWorkflowAdGroupAdvancedInputTypedDict]


class CampaignCreateWorkflowAdGroupInput(BaseModel):
    primary_input: Annotated[
        AdGroupCreateWorkflowPrimaryInput, pydantic.Field(alias="primaryInput")
    ]

    advanced_input: Annotated[
        Optional[CampaignCreateWorkflowAdGroupAdvancedInput],
        pydantic.Field(alias="advancedInput"),
    ] = None
