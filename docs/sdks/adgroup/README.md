# AdGroup
(*ad_group*)

## Overview

### Available Operations

* [post_adgroup](#post_adgroup)
* [patch_adgroup](#patch_adgroup)
* [post_adgroup_archive](#post_adgroup_archive) - Archive a list of AdGroups

## post_adgroup

### Example Usage

```python
import os
import ttd_workflows
from ttd_workflows import Workflows


with Workflows(
    ttd_auth=os.getenv("WORKFLOWS_TTD_AUTH", ""),
) as workflows:

    res = workflows.ad_group.post_adgroup(request={
        "name": "<value>",
        "is_enabled": True,
        "description": "whose countess instead helplessly honestly unblinking hence opposite",
        "programmatic_guaranteed_private_contract_id": "<id>",
        "channel": ttd_workflows.AdGroupChannel.NATIVE,
        "funnel_location": ttd_workflows.AdGroupFunnelLocation.NONE,
        "budget": {
            "allocation_type": ttd_workflows.AllocationType.FIXED,
            "budget_in_advertiser_currency": 1255.27,
            "budget_in_impressions": 469226,
            "daily_target_in_advertiser_currency": 7461.36,
            "daily_target_in_impressions": 790907,
        },
        "base_bid_cpm_in_advertiser_currency": 310.16,
        "max_bid_cpm_in_advertiser_currency": 2360.6,
        "audience_targeting": {
            "audience_id": "<id>",
            "audience_accelerator_exclusions_enabled": False,
            "audience_booster_enabled": False,
            "audience_excluder_enabled": True,
            "audience_predictor_enabled": False,
            "cross_device_vendor_list_for_audience": [
                614673,
                684382,
            ],
            "recency_exclusion_window_in_minutes": 262820,
            "target_trackable_users_enabled": True,
            "use_mc_id_as_primary": True,
        },
        "roi_goal": {
            "maximize_reach": False,
            "maximize_ltv_incremental_reach": False,
            "cpc_in_advertiser_currency": 3537.6,
            "ctr_in_percent": 6333.79,
            "nielsen_otp_in_percent": 8443.6,
            "cpa_in_advertiser_currency": 8183.4,
            "return_on_ad_spend_percent": 9749.47,
            "vcr_in_percent": 5244.57,
            "viewability_in_percent": 1797.09,
            "vcpm_in_advertiser_currency": 9777.89,
            "cpcv_in_advertiser_currency": 4506.52,
            "miaozhen_otp_in_percent": 5639.62,
        },
        "creative_ids": [
            "<value>",
        ],
        "associated_bid_lists": [
            {
                "bid_list_id": "<id>",
                "is_enabled": False,
                "is_default_for_dimension": True,
            },
            {
                "bid_list_id": "<id>",
                "is_enabled": True,
                "is_default_for_dimension": False,
            },
            {
                "bid_list_id": "<id>",
                "is_enabled": False,
                "is_default_for_dimension": True,
            },
        ],
        "campaign_id": "<id>",
        "advanced_settings": {
            "koa_optimization_settings": {
                "are_future_koa_features_enabled": True,
                "predictive_clearing_enabled": True,
            },
            "comscore_settings": {
                "is_enabled": True,
                "population_id": 133150,
                "demographic_member_ids": [
                    199046,
                ],
                "mobile_demographic_member_ids": [
                    964861,
                    667844,
                ],
            },
            "contract_targeting": {
                "allow_open_market_bidding_when_targeting_contracts": True,
            },
            "dimensional_bidding_auto_optimization_settings": [
                [
                    ttd_workflows.DimensionalBiddingDimensions.HAS_VIDEO_COMPLETION_RATE_SCORE_RANGE,
                    ttd_workflows.DimensionalBiddingDimensions.HAS_FULL_REFERRER_URL,
                ],
                [],
                [
                    ttd_workflows.DimensionalBiddingDimensions.HAS_SELLER_ID,
                ],
            ],
            "is_use_clicks_as_conversions_enabled": True,
            "is_use_secondary_conversions_enabled": True,
            "nielsen_tracking_attributes": {
                "enhanced_reporting_option": ttd_workflows.EnhancedNielsenReportingOptions.NONE,
                "gender": ttd_workflows.TargetingGender.FEMALE,
                "start_age": ttd_workflows.TargetingStartAge.SIXTY_FIVE,
                "end_age": ttd_workflows.TargetingEndAge.TWENTY_NINE,
                "countries": [
                    "<value>",
                ],
            },
            "new_frequency_configs": [
                {
                    "counter_name": "<value>",
                    "frequency_cap": 746348,
                    "frequency_goal": 510683,
                    "reset_interval_in_minutes": 129092,
                },
                {
                    "counter_name": "<value>",
                    "frequency_cap": 755997,
                    "frequency_goal": 198769,
                    "reset_interval_in_minutes": 168827,
                },
            ],
            "flights": [
                {
                    "allocation_type": ttd_workflows.AllocationType.FIXED,
                    "budget_in_advertiser_currency": 1595.69,
                    "budget_in_impressions": 474397,
                    "daily_target_in_advertiser_currency": 7814.66,
                    "daily_target_in_impressions": 542673,
                    "campaign_flight_id": 136905,
                },
                {
                    "allocation_type": ttd_workflows.AllocationType.FIXED,
                    "budget_in_advertiser_currency": 3145.56,
                    "budget_in_impressions": 465009,
                    "daily_target_in_advertiser_currency": 8108.2,
                    "daily_target_in_impressions": 109630,
                    "campaign_flight_id": 186465,
                },
                {
                    "allocation_type": ttd_workflows.AllocationType.FIXED,
                    "budget_in_advertiser_currency": 2666.4,
                    "budget_in_impressions": 593663,
                    "daily_target_in_advertiser_currency": 2585.24,
                    "daily_target_in_impressions": 42750,
                    "campaign_flight_id": 597076,
                },
            ],
        },
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                       | Type                                                                            | Required                                                                        | Description                                                                     |
| ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- |
| `request`                                                                       | [models.AdGroupCreateWorkflowInput](../../models/adgroupcreateworkflowinput.md) | :heavy_check_mark:                                                              | The request object to use for the request.                                      |
| `retries`                                                                       | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                | :heavy_minus_sign:                                                              | Configuration to override the default retry behavior of the client.             |

### Response

**[models.AdGroupPayload](../../models/adgrouppayload.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.ProblemDetailsError | 400                        | application/json           |
| models.APIError            | 4XX, 5XX                   | \*/\*                      |

## patch_adgroup

### Example Usage

```python
import os
import ttd_workflows
from ttd_workflows import Workflows


with Workflows(
    ttd_auth=os.getenv("WORKFLOWS_TTD_AUTH", ""),
) as workflows:

    res = workflows.ad_group.patch_adgroup(request=ttd_workflows.AdGroupUpdateWorkflowInput(
        id="<id>",
        name="<value>",
        is_enabled=True,
        description="insecure geez nor",
        channel=ttd_workflows.AdGroupChannel.VIDEO,
        funnel_location=ttd_workflows.AdGroupFunnelLocation.CONSIDERATION,
        budget=ttd_workflows.AdGroupUpdateBudgetInput(
            allocation_type=ttd_workflows.AllocationType.MINIMUM,
            budget_in_advertiser_currency=6266.65,
            budget_in_impressions=ttd_workflows.Int64NullableWorkflowsOptional(
                value=138352,
            ),
            daily_target_in_advertiser_currency=ttd_workflows.DecimalNullableWorkflowsOptional(
                value=1751.56,
            ),
            daily_target_in_impressions=ttd_workflows.Int64NullableWorkflowsOptional(
                value=89555,
            ),
        ),
        base_bid_cpm_in_advertiser_currency=1405.86,
        max_bid_cpm_in_advertiser_currency=5614.26,
        audience_targeting=ttd_workflows.AdGroupUpdateAudienceTargetingInput(
            audience_id=ttd_workflows.StringWorkflowsOptional(
                value="<value>",
            ),
            audience_accelerator_exclusions_enabled=False,
            audience_booster_enabled=True,
            audience_excluder_enabled=True,
            audience_predictor_enabled=False,
            cross_device_vendor_list_for_audience=[
                884208,
                437227,
                46344,
            ],
            recency_exclusion_window_in_minutes=728415,
            target_trackable_users_enabled=True,
        ),
        roi_goal=ttd_workflows.AdGroupRoiGoalInput(
            maximize_reach=False,
            maximize_ltv_incremental_reach=True,
            cpc_in_advertiser_currency=3402.66,
            ctr_in_percent=6845.97,
            nielsen_otp_in_percent=2015.13,
            cpa_in_advertiser_currency=4336.16,
            return_on_ad_spend_percent=6948.4,
            vcr_in_percent=7542.56,
            viewability_in_percent=1098.42,
            vcpm_in_advertiser_currency=9831.49,
            cpcv_in_advertiser_currency=7499.92,
            miaozhen_otp_in_percent=2240.31,
        ),
        creative_ids=[
            "<value>",
        ],
        associated_bid_lists=[
            ttd_workflows.AdGroupAssociateBidListInput(
                bid_list_id="<id>",
                is_enabled=False,
                is_default_for_dimension=True,
            ),
            ttd_workflows.AdGroupAssociateBidListInput(
                bid_list_id="<id>",
                is_enabled=True,
                is_default_for_dimension=True,
            ),
        ],
        advanced_settings=ttd_workflows.AdGroupUpdateAdvancedSettingsInput(
            flights=[
                ttd_workflows.AdGroupUpdateAdGroupFlightInput(
                    allocation_type=ttd_workflows.AllocationType.FIXED,
                    budget_in_advertiser_currency=7599.69,
                    budget_in_impressions=835676,
                    daily_target_in_advertiser_currency=1972.18,
                    daily_target_in_impressions=868300,
                    campaign_flight_id=76485,
                ),
                ttd_workflows.AdGroupUpdateAdGroupFlightInput(
                    allocation_type=ttd_workflows.AllocationType.FIXED,
                    budget_in_advertiser_currency=7930.04,
                    budget_in_impressions=525759,
                    daily_target_in_advertiser_currency=7308.08,
                    daily_target_in_impressions=73098,
                    campaign_flight_id=178280,
                ),
            ],
            koa_optimization_settings=ttd_workflows.AdGroupKoaOptimizationSettingsInput(
                are_future_koa_features_enabled=False,
                predictive_clearing_enabled=True,
            ),
            comscore_settings=ttd_workflows.AdGroupUpdateComscoreSettingsInput(
                is_enabled=True,
                population_id=559618,
                demographic_member_ids=[
                    412741,
                    741043,
                ],
                mobile_demographic_member_ids=[
                    589279,
                    118719,
                    425040,
                ],
            ),
            contract_targeting=ttd_workflows.AdGroupContractTargetingInput(
                allow_open_market_bidding_when_targeting_contracts=False,
            ),
            dimensional_bidding_auto_optimization_settings=[
                [
                    ttd_workflows.DimensionalBiddingDimensions.HAS_PEER39_LANGUAGE_ID,
                    ttd_workflows.DimensionalBiddingDimensions.HAS_AD_BUG_PAGE_QUALITY_CATEGORY_ID,
                ],
            ],
            is_use_clicks_as_conversions_enabled=True,
            is_use_secondary_conversions_enabled=True,
            nielsen_tracking_attributes=ttd_workflows.AdGroupUpdateNielsenTrackingAttributesInputWorkflowsOptional(
                value=ttd_workflows.AdGroupUpdateNielsenTrackingAttributesInput(
                    enhanced_reporting_option=ttd_workflows.EnhancedNielsenReportingOptions.AUDIENCE,
                    gender=ttd_workflows.TargetingGender.FEMALE,
                    start_age=ttd_workflows.TargetingStartAge.THIRTY_FIVE,
                    end_age=ttd_workflows.TargetingEndAge.TWENTY,
                    countries=[
                        "<value>",
                        "<value>",
                        "<value>",
                    ],
                ),
            ),
            new_frequency_configs=[
                ttd_workflows.AdGroupNewFrequencyConfigInput(
                    counter_name="<value>",
                    frequency_cap=670564,
                    frequency_goal=855079,
                    reset_interval_in_minutes=183553,
                ),
                ttd_workflows.AdGroupNewFrequencyConfigInput(
                    counter_name="<value>",
                    frequency_cap=76498,
                    frequency_goal=917722,
                    reset_interval_in_minutes=779095,
                ),
            ],
        ),
    ))

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                       | Type                                                                            | Required                                                                        | Description                                                                     |
| ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- |
| `request`                                                                       | [models.AdGroupUpdateWorkflowInput](../../models/adgroupupdateworkflowinput.md) | :heavy_check_mark:                                                              | The request object to use for the request.                                      |
| `retries`                                                                       | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                | :heavy_minus_sign:                                                              | Configuration to override the default retry behavior of the client.             |

### Response

**[models.AdGroupPayload](../../models/adgrouppayload.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.ProblemDetailsError | 400                        | application/json           |
| models.APIError            | 4XX, 5XX                   | \*/\*                      |

## post_adgroup_archive

Archive a list of AdGroups

### Example Usage

```python
import os
from ttd_workflows import Workflows


with Workflows(
    ttd_auth=os.getenv("WORKFLOWS_TTD_AUTH", ""),
) as workflows:

    res = workflows.ad_group.post_adgroup_archive(request_body=[
        "<value>",
    ])

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `force_archive`                                                     | *Optional[bool]*                                                    | :heavy_minus_sign:                                                  | N/A                                                                 |
| `request_body`                                                      | List[*str*]                                                         | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[List[str]](../../models/.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.ProblemDetailsError | 400                        | application/json           |
| models.APIError            | 4XX, 5XX                   | \*/\*                      |