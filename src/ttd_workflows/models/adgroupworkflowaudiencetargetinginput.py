"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import pydantic
from pydantic import model_serializer
from ttd_workflows.types import (
    BaseModel,
    Nullable,
    OptionalNullable,
    UNSET,
    UNSET_SENTINEL,
)
from typing import List
from typing_extensions import Annotated, NotRequired, TypedDict


class AdGroupWorkflowAudienceTargetingInputTypedDict(TypedDict):
    audience_id: NotRequired[Nullable[str]]
    audience_accelerator_exclusions_enabled: NotRequired[Nullable[bool]]
    audience_booster_enabled: NotRequired[Nullable[bool]]
    audience_excluder_enabled: NotRequired[Nullable[bool]]
    audience_predictor_enabled: NotRequired[Nullable[bool]]
    cross_device_vendor_list_for_audience: NotRequired[Nullable[List[int]]]
    recency_exclusion_window_in_minutes: NotRequired[Nullable[int]]
    target_trackable_users_enabled: NotRequired[Nullable[bool]]
    use_mc_id_as_primary: NotRequired[Nullable[bool]]


class AdGroupWorkflowAudienceTargetingInput(BaseModel):
    audience_id: Annotated[
        OptionalNullable[str], pydantic.Field(alias="audienceId")
    ] = UNSET

    audience_accelerator_exclusions_enabled: Annotated[
        OptionalNullable[bool],
        pydantic.Field(alias="audienceAcceleratorExclusionsEnabled"),
    ] = UNSET

    audience_booster_enabled: Annotated[
        OptionalNullable[bool], pydantic.Field(alias="audienceBoosterEnabled")
    ] = UNSET

    audience_excluder_enabled: Annotated[
        OptionalNullable[bool], pydantic.Field(alias="audienceExcluderEnabled")
    ] = UNSET

    audience_predictor_enabled: Annotated[
        OptionalNullable[bool], pydantic.Field(alias="audiencePredictorEnabled")
    ] = UNSET

    cross_device_vendor_list_for_audience: Annotated[
        OptionalNullable[List[int]],
        pydantic.Field(alias="crossDeviceVendorListForAudience"),
    ] = UNSET

    recency_exclusion_window_in_minutes: Annotated[
        OptionalNullable[int], pydantic.Field(alias="recencyExclusionWindowInMinutes")
    ] = UNSET

    target_trackable_users_enabled: Annotated[
        OptionalNullable[bool], pydantic.Field(alias="targetTrackableUsersEnabled")
    ] = UNSET

    use_mc_id_as_primary: Annotated[
        OptionalNullable[bool], pydantic.Field(alias="useMcIdAsPrimary")
    ] = UNSET

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = [
            "audienceId",
            "audienceAcceleratorExclusionsEnabled",
            "audienceBoosterEnabled",
            "audienceExcluderEnabled",
            "audiencePredictorEnabled",
            "crossDeviceVendorListForAudience",
            "recencyExclusionWindowInMinutes",
            "targetTrackableUsersEnabled",
            "useMcIdAsPrimary",
        ]
        nullable_fields = [
            "audienceId",
            "audienceAcceleratorExclusionsEnabled",
            "audienceBoosterEnabled",
            "audienceExcluderEnabled",
            "audiencePredictorEnabled",
            "crossDeviceVendorListForAudience",
            "recencyExclusionWindowInMinutes",
            "targetTrackableUsersEnabled",
            "useMcIdAsPrimary",
        ]
        null_default_fields = []

        serialized = handler(self)

        m = {}

        for n, f in type(self).model_fields.items():
            k = f.alias or n
            val = serialized.get(k)
            serialized.pop(k, None)

            optional_nullable = k in optional_fields and k in nullable_fields
            is_set = (
                self.__pydantic_fields_set__.intersection({n})
                or k in null_default_fields
            )  # pylint: disable=no-member

            if val is not None and val != UNSET_SENTINEL:
                m[k] = val
            elif val != UNSET_SENTINEL and (
                not k in optional_fields or (optional_nullable and is_set)
            ):
                m[k] = val

        return m
