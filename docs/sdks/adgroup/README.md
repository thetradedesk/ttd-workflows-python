# AdGroup
(*ad_group*)

## Overview

### Available Operations

* [post_adgroup](#post_adgroup)
* [patch_adgroup](#patch_adgroup)
* [post_adgroup_archive](#post_adgroup_archive) - Archive a list of ad groups

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
        "primary_input": {
            "name": "<value>",
            "is_enabled": True,
            "description": "whose countess instead helplessly honestly unblinking hence opposite",
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
            "programmatic_guaranteed_private_contract_id": "<id>",
        },
        "campaign_id": "<id>",
        "advanced_input": {
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
| models.ProblemDetailsError | 400, 403                   | application/json           |
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

    res = workflows.ad_group.patch_adgroup(request={
        "id": "<id>",
        "primary_input": {
            "name": "<value>",
            "is_enabled": True,
            "description": "insecure geez nor",
            "channel": ttd_workflows.AdGroupChannel.VIDEO,
            "funnel_location": ttd_workflows.AdGroupFunnelLocation.CONSIDERATION,
            "budget": {
                "allocation_type": ttd_workflows.AllocationType.MINIMUM,
                "budget_in_advertiser_currency": 6266.65,
                "budget_in_impressions": 138352,
                "daily_target_in_advertiser_currency": 1751.56,
                "daily_target_in_impressions": 89555,
            },
            "base_bid_cpm_in_advertiser_currency": 1405.86,
            "max_bid_cpm_in_advertiser_currency": 5614.26,
            "audience_targeting": {
                "audience_id": "<id>",
                "audience_accelerator_exclusions_enabled": False,
                "audience_booster_enabled": True,
                "audience_excluder_enabled": True,
                "audience_predictor_enabled": False,
                "cross_device_vendor_list_for_audience": [
                    884208,
                    437227,
                    46344,
                ],
                "recency_exclusion_window_in_minutes": 728415,
                "target_trackable_users_enabled": True,
                "use_mc_id_as_primary": False,
            },
            "roi_goal": {
                "maximize_reach": True,
                "maximize_ltv_incremental_reach": True,
                "cpc_in_advertiser_currency": 6845.97,
                "ctr_in_percent": 2015.13,
                "nielsen_otp_in_percent": 4336.16,
                "cpa_in_advertiser_currency": 6948.4,
                "return_on_ad_spend_percent": 7542.56,
                "vcr_in_percent": 1098.42,
                "viewability_in_percent": 9831.49,
                "vcpm_in_advertiser_currency": 7499.92,
                "cpcv_in_advertiser_currency": 2240.31,
                "miaozhen_otp_in_percent": 2080.35,
            },
            "creative_ids": [
                "<value>",
                "<value>",
            ],
            "associated_bid_lists": [
                {
                    "bid_list_id": "<id>",
                    "is_enabled": True,
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
                    "is_default_for_dimension": False,
                },
            ],
        },
        "advanced_input": {
            "koa_optimization_settings": {
                "are_future_koa_features_enabled": False,
                "predictive_clearing_enabled": True,
            },
            "comscore_settings": {
                "is_enabled": False,
                "population_id": 76485,
                "demographic_member_ids": [
                    793004,
                    525759,
                    730808,
                ],
                "mobile_demographic_member_ids": [
                    178280,
                ],
            },
            "contract_targeting": {
                "allow_open_market_bidding_when_targeting_contracts": False,
            },
            "dimensional_bidding_auto_optimization_settings": [
                [
                    ttd_workflows.DimensionalBiddingDimensions.HAS_FREQUENCY_ADJUSTMENT_ID,
                ],
            ],
            "is_use_clicks_as_conversions_enabled": False,
            "is_use_secondary_conversions_enabled": True,
            "nielsen_tracking_attributes": {
                "enhanced_reporting_option": ttd_workflows.EnhancedNielsenReportingOptions.SITE,
                "gender": ttd_workflows.TargetingGender.BOTH,
                "start_age": ttd_workflows.TargetingStartAge.FORTY,
                "end_age": ttd_workflows.TargetingEndAge.TWENTY,
                "countries": [
                    "<value>",
                ],
            },
            "new_frequency_configs": [
                {
                    "counter_name": "<value>",
                    "frequency_cap": 134682,
                    "frequency_goal": 686039,
                    "reset_interval_in_minutes": 361524,
                },
                {
                    "counter_name": "<value>",
                    "frequency_cap": 608575,
                    "frequency_goal": 188983,
                    "reset_interval_in_minutes": 279270,
                },
                {
                    "counter_name": "<value>",
                    "frequency_cap": 349625,
                    "frequency_goal": 471189,
                    "reset_interval_in_minutes": 543852,
                },
            ],
            "flights": [
                {
                    "allocation_type": ttd_workflows.AllocationType.FIXED,
                    "budget_in_advertiser_currency": 5406.82,
                    "budget_in_impressions": 670564,
                    "daily_target_in_advertiser_currency": 8550.79,
                    "daily_target_in_impressions": 183553,
                    "campaign_flight_id": 76498,
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
| `request`                                                                       | [models.AdGroupUpdateWorkflowInput](../../models/adgroupupdateworkflowinput.md) | :heavy_check_mark:                                                              | The request object to use for the request.                                      |
| `retries`                                                                       | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                | :heavy_minus_sign:                                                              | Configuration to override the default retry behavior of the client.             |

### Response

**[models.AdGroupPayload](../../models/adgrouppayload.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.ProblemDetailsError | 400, 403                   | application/json           |
| models.APIError            | 4XX, 5XX                   | \*/\*                      |

## post_adgroup_archive

Archive a list of ad groups

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
| models.ProblemDetailsError | 400, 403                   | application/json           |
| models.APIError            | 4XX, 5XX                   | \*/\*                      |