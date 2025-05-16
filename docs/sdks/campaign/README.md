# Campaign
(*campaign*)

## Overview

### Available Operations

* [create](#create) - Create a new campaign with required fields
* [patch_campaign](#patch_campaign) - Update an existing campaign with specified fields
* [post_campaign_bulk](#post_campaign_bulk) - Create a list of campaigns with required fields. `ValidationOnly` value should be the same for all campaigns.
* [post_campaign_archive](#post_campaign_archive) - Archive a list of campaigns
* [get_version](#get_version) - GET a campaign's version

## create

Create a new campaign with required fields

### Example Usage

```python
import os
import ttd_workflows
from ttd_workflows import Workflows
from ttd_workflows.utils import parse_datetime


with Workflows(
    ttd_auth=os.getenv("WORKFLOWS_TTD_AUTH", ""),
) as workflows:

    res = workflows.campaign.create(request={
        "primary_input": {
            "description": "yuck vice between gee ugh ha",
            "time_zone": "Pacific/Chuuk",
            "custom_cpa_click_weight": 7804.86,
            "custom_cpa_viewthrough_weight": 7602.59,
            "custom_cpa_type": ttd_workflows.CustomCPAType.DISABLED,
            "impressions_only_budgeting_cpm": 4492.21,
            "budget": {
                "pacing_mode": ttd_workflows.CampaignPacingMode.PACE_EVENLY,
                "budget_in_advertiser_currency": 5884.97,
                "budget_in_impressions": 93470,
                "daily_target_in_advertiser_currency": 4914.27,
                "daily_target_in_impressions": 490420,
            },
            "end_date_in_utc": parse_datetime("2023-12-23T16:58:53.860Z"),
            "seed_id": "<id>",
            "campaign_conversion_reporting_columns": [
                {
                    "tracking_tag_id": "<id>",
                    "include_in_custom_cpa": True,
                    "reporting_column_id": 129663,
                    "roas_config": {
                        "include_in_custom_roas": True,
                        "custom_roas_weight": 5833.53,
                        "custom_roas_click_weight": 5193.59,
                        "custom_roas_viewthrough_weight": 3259.9,
                    },
                    "weight": 4078.33,
                    "cross_device_attribution_model_id": "<id>",
                },
                {
                    "tracking_tag_id": "<id>",
                    "include_in_custom_cpa": True,
                    "reporting_column_id": 188435,
                    "roas_config": {
                        "include_in_custom_roas": False,
                        "custom_roas_weight": 8891.64,
                        "custom_roas_click_weight": 54.36,
                        "custom_roas_viewthrough_weight": 9117.42,
                    },
                    "weight": 8988.41,
                    "cross_device_attribution_model_id": "<id>",
                },
                {
                    "tracking_tag_id": "<id>",
                    "include_in_custom_cpa": False,
                    "reporting_column_id": 17207,
                    "roas_config": {
                        "include_in_custom_roas": True,
                        "custom_roas_weight": 8441.62,
                        "custom_roas_click_weight": 3535.31,
                        "custom_roas_viewthrough_weight": 4287.45,
                    },
                    "weight": 6798.85,
                    "cross_device_attribution_model_id": "<id>",
                },
            ],
            "advertiser_id": "<id>",
            "name": "<value>",
            "primary_channel": ttd_workflows.CampaignChannelType.NONE,
            "primary_goal": {
                "maximize_reach": False,
                "maximize_ltv_incremental_reach": False,
                "cpc_in_advertiser_currency": 5665.12,
                "ctr_in_percent": 2955.58,
                "nielsen_otp_in_percent": 2032.57,
                "cpa_in_advertiser_currency": 4332.24,
                "return_on_ad_spend_percent": 7122.14,
                "vcr_in_percent": 9958.52,
                "viewability_in_percent": 8236.83,
                "vcpm_in_advertiser_currency": 2127.75,
                "cpcv_in_advertiser_currency": 6207.47,
                "miaozhen_otp_in_percent": 2841.2,
            },
            "start_date_in_utc": parse_datetime("2024-10-28T18:55:39.709Z"),
        },
        "advanced_input": {
            "flights": [
                {
                    "start_date_inclusive_utc": parse_datetime("2024-06-28T18:56:13.043Z"),
                    "end_date_exclusive_utc": parse_datetime("2024-10-30T06:59:44.964Z"),
                    "budget_in_advertiser_currency": 5200.49,
                    "budget_in_impressions": 728836,
                    "daily_target_in_advertiser_currency": 8007.59,
                    "daily_target_in_impressions": 117747,
                },
            ],
            "purchase_order_number": "<value>",
        },
        "ad_groups": [
            {
                "primary_input": {
                    "name": "<value>",
                    "is_enabled": False,
                    "description": "yippee where until waver colorless beyond victoriously consequently apud",
                    "channel": ttd_workflows.AdGroupChannel.VIDEO,
                    "funnel_location": ttd_workflows.AdGroupFunnelLocation.CONVERSION,
                    "budget": {
                        "allocation_type": ttd_workflows.AllocationType.FIXED,
                        "budget_in_advertiser_currency": 5906.34,
                        "budget_in_impressions": 223877,
                        "daily_target_in_advertiser_currency": 7543.1,
                        "daily_target_in_impressions": 850693,
                    },
                    "base_bid_cpm_in_advertiser_currency": 8664.87,
                    "max_bid_cpm_in_advertiser_currency": 2000.77,
                    "audience_targeting": {
                        "audience_id": "<id>",
                        "audience_accelerator_exclusions_enabled": True,
                        "audience_booster_enabled": False,
                        "audience_excluder_enabled": False,
                        "audience_predictor_enabled": True,
                        "cross_device_vendor_list_for_audience": [
                            883321,
                            892770,
                            199311,
                        ],
                        "recency_exclusion_window_in_minutes": 564854,
                        "target_trackable_users_enabled": False,
                        "use_mc_id_as_primary": False,
                    },
                    "roi_goal": {
                        "maximize_reach": True,
                        "maximize_ltv_incremental_reach": True,
                        "cpc_in_advertiser_currency": 5474.83,
                        "ctr_in_percent": 9609.09,
                        "nielsen_otp_in_percent": 9138.67,
                        "cpa_in_advertiser_currency": 4757.86,
                        "return_on_ad_spend_percent": 6954.13,
                        "vcr_in_percent": 3246.89,
                        "viewability_in_percent": 2617.57,
                        "vcpm_in_advertiser_currency": 6084.35,
                        "cpcv_in_advertiser_currency": 4004.22,
                        "miaozhen_otp_in_percent": 2574.33,
                    },
                    "creative_ids": [
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
                            "is_enabled": False,
                            "is_default_for_dimension": False,
                        },
                    ],
                    "programmatic_guaranteed_private_contract_id": "<id>",
                },
                "advanced_input": {
                    "koa_optimization_settings": {
                        "are_future_koa_features_enabled": True,
                        "predictive_clearing_enabled": False,
                    },
                    "comscore_settings": {
                        "is_enabled": False,
                        "population_id": 339267,
                        "demographic_member_ids": [
                            885411,
                        ],
                        "mobile_demographic_member_ids": [
                            557925,
                            643654,
                            700013,
                        ],
                    },
                    "contract_targeting": {
                        "allow_open_market_bidding_when_targeting_contracts": False,
                    },
                    "dimensional_bidding_auto_optimization_settings": [
                        [
                            ttd_workflows.DimensionalBiddingDimensions.HAS_AD_BUG_VIDEO_PAGE_QUALITY_CATEGORY_ID,
                            ttd_workflows.DimensionalBiddingDimensions.HAS_DOUBLE_VERIFY_VIDEO_VIEWABILITY_CATEGORY_ID,
                        ],
                        [
                            ttd_workflows.DimensionalBiddingDimensions.HAS_RENDERING_CONTEXT_ID,
                            ttd_workflows.DimensionalBiddingDimensions.HAS_CONTEXTUAL_APP_CATEGORY_ID,
                        ],
                    ],
                    "is_use_clicks_as_conversions_enabled": True,
                    "is_use_secondary_conversions_enabled": True,
                    "nielsen_tracking_attributes": {
                        "enhanced_reporting_option": ttd_workflows.EnhancedNielsenReportingOptions.AUDIENCE,
                        "gender": ttd_workflows.TargetingGender.MALE,
                        "start_age": ttd_workflows.TargetingStartAge.FIFTY_FIVE,
                        "end_age": ttd_workflows.TargetingEndAge.FIFTY_FOUR,
                        "countries": [
                            "<value>",
                            "<value>",
                            "<value>",
                        ],
                    },
                    "new_frequency_configs": [
                        {
                            "counter_name": "<value>",
                            "frequency_cap": 661881,
                            "frequency_goal": 79826,
                            "reset_interval_in_minutes": 564782,
                        },
                        {
                            "counter_name": "<value>",
                            "frequency_cap": 496696,
                            "frequency_goal": 622836,
                            "reset_interval_in_minutes": 542231,
                        },
                        {
                            "counter_name": "<value>",
                            "frequency_cap": 339193,
                            "frequency_goal": 320521,
                            "reset_interval_in_minutes": 708684,
                        },
                    ],
                    "flights": [
                        {
                            "allocation_type": ttd_workflows.AllocationType.FIXED,
                            "budget_in_advertiser_currency": 2460.82,
                            "budget_in_impressions": 689435,
                            "daily_target_in_advertiser_currency": 5733.26,
                            "daily_target_in_impressions": 522908,
                        },
                        {
                            "allocation_type": ttd_workflows.AllocationType.MINIMUM,
                            "budget_in_advertiser_currency": 3302.92,
                            "budget_in_impressions": 257617,
                            "daily_target_in_advertiser_currency": 9488.67,
                            "daily_target_in_impressions": 286214,
                        },
                    ],
                },
            },
            {
                "primary_input": {
                    "name": "<value>",
                    "is_enabled": True,
                    "description": "browse colorfully blank",
                    "channel": ttd_workflows.AdGroupChannel.VIDEO,
                    "funnel_location": ttd_workflows.AdGroupFunnelLocation.CONVERSION,
                    "budget": {
                        "allocation_type": ttd_workflows.AllocationType.FIXED,
                        "budget_in_advertiser_currency": 5085.11,
                        "budget_in_impressions": 12544,
                        "daily_target_in_advertiser_currency": 4263.75,
                        "daily_target_in_impressions": 306126,
                    },
                    "base_bid_cpm_in_advertiser_currency": 6393.88,
                    "max_bid_cpm_in_advertiser_currency": 7806.19,
                    "audience_targeting": {
                        "audience_id": "<id>",
                        "audience_accelerator_exclusions_enabled": False,
                        "audience_booster_enabled": True,
                        "audience_excluder_enabled": True,
                        "audience_predictor_enabled": False,
                        "cross_device_vendor_list_for_audience": [
                            515066,
                            724887,
                        ],
                        "recency_exclusion_window_in_minutes": 997242,
                        "target_trackable_users_enabled": False,
                        "use_mc_id_as_primary": False,
                    },
                    "roi_goal": {
                        "maximize_reach": False,
                        "maximize_ltv_incremental_reach": False,
                        "cpc_in_advertiser_currency": 1285.82,
                        "ctr_in_percent": 2880.02,
                        "nielsen_otp_in_percent": 6752.2,
                        "cpa_in_advertiser_currency": 4797.25,
                        "return_on_ad_spend_percent": 6967.11,
                        "vcr_in_percent": 8422.44,
                        "viewability_in_percent": 87.86,
                        "vcpm_in_advertiser_currency": 9921.62,
                        "cpcv_in_advertiser_currency": 6912.82,
                        "miaozhen_otp_in_percent": 8566.65,
                    },
                    "creative_ids": [
                        "<value>",
                        "<value>",
                    ],
                    "associated_bid_lists": [
                        {
                            "bid_list_id": "<id>",
                            "is_enabled": False,
                            "is_default_for_dimension": False,
                        },
                    ],
                    "programmatic_guaranteed_private_contract_id": "<id>",
                },
                "advanced_input": {
                    "koa_optimization_settings": {
                        "are_future_koa_features_enabled": False,
                        "predictive_clearing_enabled": True,
                    },
                    "comscore_settings": {
                        "is_enabled": False,
                        "population_id": 511670,
                        "demographic_member_ids": [
                            275977,
                            930307,
                        ],
                        "mobile_demographic_member_ids": [
                            29308,
                        ],
                    },
                    "contract_targeting": {
                        "allow_open_market_bidding_when_targeting_contracts": False,
                    },
                    "dimensional_bidding_auto_optimization_settings": [
                        [
                            ttd_workflows.DimensionalBiddingDimensions.HAS_SUPPLY_VENDOR_ID,
                            ttd_workflows.DimensionalBiddingDimensions.HAS_WEATHER_CONDITION_ID,
                            ttd_workflows.DimensionalBiddingDimensions.HAS_CONTEXTUAL_APP_CATEGORY_ID,
                        ],
                        [
                            ttd_workflows.DimensionalBiddingDimensions.HAS_PEER39_PAGE_QUALITY_CATEGORY_ID,
                            ttd_workflows.DimensionalBiddingDimensions.HAS_FACTUAL_PROXIMITY_DATA_ID,
                            ttd_workflows.DimensionalBiddingDimensions.HAS_PLACEMENT_POSITION_RELATIVE_TO_FOLD_ID,
                        ],
                    ],
                    "is_use_clicks_as_conversions_enabled": True,
                    "is_use_secondary_conversions_enabled": True,
                    "nielsen_tracking_attributes": {
                        "enhanced_reporting_option": ttd_workflows.EnhancedNielsenReportingOptions.AUDIENCE,
                        "gender": ttd_workflows.TargetingGender.MALE,
                        "start_age": ttd_workflows.TargetingStartAge.FORTY_FIVE,
                        "end_age": ttd_workflows.TargetingEndAge.TWENTY_NINE,
                        "countries": [],
                    },
                    "new_frequency_configs": [
                        {
                            "counter_name": "<value>",
                            "frequency_cap": 293620,
                            "frequency_goal": 333281,
                            "reset_interval_in_minutes": 637441,
                        },
                        {
                            "counter_name": "<value>",
                            "frequency_cap": 855423,
                            "frequency_goal": 967917,
                            "reset_interval_in_minutes": 649685,
                        },
                    ],
                    "flights": [
                        {
                            "allocation_type": ttd_workflows.AllocationType.MAXIMUM,
                            "budget_in_advertiser_currency": 286.08,
                            "budget_in_impressions": 316907,
                            "daily_target_in_advertiser_currency": 485.54,
                            "daily_target_in_impressions": 257790,
                        },
                        {
                            "allocation_type": ttd_workflows.AllocationType.FIXED,
                            "budget_in_advertiser_currency": 4780.27,
                            "budget_in_impressions": 913385,
                            "daily_target_in_advertiser_currency": 650.97,
                            "daily_target_in_impressions": 624357,
                        },
                    ],
                },
            },
        ],
        "validation_only": False,
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                         | Type                                                                              | Required                                                                          | Description                                                                       |
| --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- |
| `request`                                                                         | [models.CampaignCreateWorkflowInput](../../models/campaigncreateworkflowinput.md) | :heavy_check_mark:                                                                | The request object to use for the request.                                        |
| `retries`                                                                         | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                  | :heavy_minus_sign:                                                                | Configuration to override the default retry behavior of the client.               |

### Response

**[models.CampaignPayload](../../models/campaignpayload.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.ProblemDetailsError | 400, 403                   | application/json           |
| models.APIError            | 4XX, 5XX                   | \*/\*                      |

## patch_campaign

Update an existing campaign with specified fields

### Example Usage

```python
import os
import ttd_workflows
from ttd_workflows import Workflows
from ttd_workflows.utils import parse_datetime


with Workflows(
    ttd_auth=os.getenv("WORKFLOWS_TTD_AUTH", ""),
) as workflows:

    res = workflows.campaign.patch_campaign(request={
        "primary_input": {
            "description": "onto frail incline watery besmirch wallaby ew",
            "time_zone": "Europe/Tirane",
            "custom_cpa_click_weight": 2654.86,
            "custom_cpa_viewthrough_weight": 2212.44,
            "custom_cpa_type": ttd_workflows.CustomCPAType.CLICK_VIEWTHROUGH_WEIGHTING,
            "impressions_only_budgeting_cpm": 4161.04,
            "budget": {
                "pacing_mode": ttd_workflows.CampaignPacingMode.PACE_AS_SOON_AS_POSSIBLE,
                "budget_in_advertiser_currency": 9734.67,
                "budget_in_impressions": 144079,
                "daily_target_in_advertiser_currency": 796.2,
                "daily_target_in_impressions": 927058,
            },
            "end_date_in_utc": parse_datetime("2023-10-30T21:03:42.194Z"),
            "seed_id": "<id>",
            "campaign_conversion_reporting_columns": [
                {
                    "tracking_tag_id": "<id>",
                    "include_in_custom_cpa": True,
                    "reporting_column_id": 612696,
                    "roas_config": {
                        "include_in_custom_roas": True,
                        "custom_roas_weight": 8227.87,
                        "custom_roas_click_weight": 948.27,
                        "custom_roas_viewthrough_weight": 260.92,
                    },
                    "weight": 7435.48,
                    "cross_device_attribution_model_id": "<id>",
                },
                {
                    "tracking_tag_id": "<id>",
                    "include_in_custom_cpa": False,
                    "reporting_column_id": 224688,
                    "roas_config": {
                        "include_in_custom_roas": True,
                        "custom_roas_weight": 4746.2,
                        "custom_roas_click_weight": 9836.19,
                        "custom_roas_viewthrough_weight": 1435.91,
                    },
                    "weight": 7084.86,
                    "cross_device_attribution_model_id": "<id>",
                },
            ],
            "id": "<id>",
            "name": "<value>",
            "primary_channel": ttd_workflows.CampaignChannelType.NATIVE_VIDEO,
            "primary_goal": {
                "maximize_reach": False,
                "maximize_ltv_incremental_reach": True,
                "cpc_in_advertiser_currency": 212.16,
                "ctr_in_percent": 6382.42,
                "nielsen_otp_in_percent": 9528.23,
                "cpa_in_advertiser_currency": 3018.04,
                "return_on_ad_spend_percent": 8304.12,
                "vcr_in_percent": 4110.43,
                "viewability_in_percent": 8517.26,
                "vcpm_in_advertiser_currency": 5362.46,
                "cpcv_in_advertiser_currency": 2648.21,
                "miaozhen_otp_in_percent": 2901.77,
            },
            "start_date_in_utc": parse_datetime("2024-03-11T02:18:44.439Z"),
        },
        "advanced_input": {
            "flights": [
                {
                    "start_date_inclusive_utc": parse_datetime("2024-01-25T23:11:41.832Z"),
                    "end_date_exclusive_utc": parse_datetime("2024-08-28T04:40:52.034Z"),
                    "budget_in_advertiser_currency": 333.49,
                    "budget_in_impressions": 475492,
                    "daily_target_in_advertiser_currency": 4540.7,
                    "daily_target_in_impressions": 777398,
                },
            ],
            "purchase_order_number": "<value>",
        },
        "validation_only": False,
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                         | Type                                                                              | Required                                                                          | Description                                                                       |
| --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- |
| `request`                                                                         | [models.CampaignUpdateWorkflowInput](../../models/campaignupdateworkflowinput.md) | :heavy_check_mark:                                                                | The request object to use for the request.                                        |
| `retries`                                                                         | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                  | :heavy_minus_sign:                                                                | Configuration to override the default retry behavior of the client.               |

### Response

**[models.CampaignPayload](../../models/campaignpayload.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.ProblemDetailsError | 400                        | application/json           |
| models.APIError            | 4XX, 5XX                   | \*/\*                      |

## post_campaign_bulk

Create a list of campaigns with required fields. `ValidationOnly` value should be the same for all campaigns.

### Example Usage

```python
import os
import ttd_workflows
from ttd_workflows import Workflows
from ttd_workflows.utils import parse_datetime


with Workflows(
    ttd_auth=os.getenv("WORKFLOWS_TTD_AUTH", ""),
) as workflows:

    res = workflows.campaign.post_campaign_bulk(request=[
        {
            "primary_input": {
                "description": "smart worldly onto woot",
                "time_zone": "America/Kralendijk",
                "custom_cpa_click_weight": 2762.27,
                "custom_cpa_viewthrough_weight": 5943.3,
                "custom_cpa_type": ttd_workflows.CustomCPAType.DISABLED,
                "impressions_only_budgeting_cpm": 2758.05,
                "budget": {
                    "pacing_mode": ttd_workflows.CampaignPacingMode.PACE_TO_DAILY_CAP,
                    "budget_in_advertiser_currency": 5417.34,
                    "budget_in_impressions": 821964,
                    "daily_target_in_advertiser_currency": 1697.17,
                    "daily_target_in_impressions": 398351,
                },
                "end_date_in_utc": parse_datetime("2023-08-24T08:55:11.132Z"),
                "seed_id": "<id>",
                "campaign_conversion_reporting_columns": [
                    {
                        "tracking_tag_id": "<id>",
                        "include_in_custom_cpa": True,
                        "reporting_column_id": 703028,
                        "roas_config": {
                            "include_in_custom_roas": True,
                            "custom_roas_weight": 1814.65,
                            "custom_roas_click_weight": 4282.39,
                            "custom_roas_viewthrough_weight": 4447.49,
                        },
                        "weight": 3151.21,
                        "cross_device_attribution_model_id": "<id>",
                    },
                    {
                        "tracking_tag_id": "<id>",
                        "include_in_custom_cpa": True,
                        "reporting_column_id": 331553,
                        "roas_config": {
                            "include_in_custom_roas": False,
                            "custom_roas_weight": 4761.15,
                            "custom_roas_click_weight": 2378.41,
                            "custom_roas_viewthrough_weight": 9085.58,
                        },
                        "weight": 3057.19,
                        "cross_device_attribution_model_id": "<id>",
                    },
                    {
                        "tracking_tag_id": "<id>",
                        "include_in_custom_cpa": True,
                        "reporting_column_id": 443742,
                        "roas_config": {
                            "include_in_custom_roas": False,
                            "custom_roas_weight": 2014.11,
                            "custom_roas_click_weight": 1962.45,
                            "custom_roas_viewthrough_weight": 3162.7,
                        },
                        "weight": 4033.15,
                        "cross_device_attribution_model_id": "<id>",
                    },
                ],
                "advertiser_id": "<id>",
                "name": "<value>",
                "primary_channel": ttd_workflows.CampaignChannelType.NONE,
                "primary_goal": {
                    "maximize_reach": False,
                    "maximize_ltv_incremental_reach": True,
                    "cpc_in_advertiser_currency": 1087.92,
                    "ctr_in_percent": 7857.51,
                    "nielsen_otp_in_percent": 4590.03,
                    "cpa_in_advertiser_currency": 3159.27,
                    "return_on_ad_spend_percent": 6083.48,
                    "vcr_in_percent": 3419.3,
                    "viewability_in_percent": 9282.66,
                    "vcpm_in_advertiser_currency": 8871.73,
                    "cpcv_in_advertiser_currency": 3132.81,
                    "miaozhen_otp_in_percent": 8003.45,
                },
                "start_date_in_utc": parse_datetime("2023-05-11T19:43:54.351Z"),
            },
            "advanced_input": {
                "flights": [
                    {
                        "start_date_inclusive_utc": parse_datetime("2024-04-25T15:59:05.641Z"),
                        "end_date_exclusive_utc": parse_datetime("2025-05-17T08:50:28.237Z"),
                        "budget_in_advertiser_currency": 5539.65,
                        "budget_in_impressions": 422521,
                        "daily_target_in_advertiser_currency": 2874.97,
                        "daily_target_in_impressions": 868493,
                    },
                    {
                        "start_date_inclusive_utc": parse_datetime("2023-10-06T22:04:36.901Z"),
                        "end_date_exclusive_utc": parse_datetime("2024-04-18T20:10:37.392Z"),
                        "budget_in_advertiser_currency": 6454.67,
                        "budget_in_impressions": 549393,
                        "daily_target_in_advertiser_currency": 8083.81,
                        "daily_target_in_impressions": 291618,
                    },
                ],
                "purchase_order_number": "<value>",
            },
            "ad_groups": [
                {
                    "primary_input": {
                        "name": "<value>",
                        "is_enabled": True,
                        "description": "sediment nerve duh equally lend blah aha reluctantly",
                        "channel": ttd_workflows.AdGroupChannel.AUDIO,
                        "funnel_location": ttd_workflows.AdGroupFunnelLocation.CONVERSION,
                        "budget": {
                            "allocation_type": ttd_workflows.AllocationType.MAXIMUM,
                            "budget_in_advertiser_currency": 3707.15,
                            "budget_in_impressions": 664735,
                            "daily_target_in_advertiser_currency": 1717.08,
                            "daily_target_in_impressions": 251940,
                        },
                        "base_bid_cpm_in_advertiser_currency": 7775.47,
                        "max_bid_cpm_in_advertiser_currency": 4502.74,
                        "audience_targeting": {
                            "audience_id": "<id>",
                            "audience_accelerator_exclusions_enabled": False,
                            "audience_booster_enabled": False,
                            "audience_excluder_enabled": True,
                            "audience_predictor_enabled": True,
                            "cross_device_vendor_list_for_audience": [
                                261292,
                                89377,
                            ],
                            "recency_exclusion_window_in_minutes": 23536,
                            "target_trackable_users_enabled": True,
                            "use_mc_id_as_primary": True,
                        },
                        "roi_goal": {
                            "maximize_reach": False,
                            "maximize_ltv_incremental_reach": False,
                            "cpc_in_advertiser_currency": 9399.82,
                            "ctr_in_percent": 3118.69,
                            "nielsen_otp_in_percent": 9358.84,
                            "cpa_in_advertiser_currency": 8483.78,
                            "return_on_ad_spend_percent": 8626.31,
                            "vcr_in_percent": 8829.21,
                            "viewability_in_percent": 571.67,
                            "vcpm_in_advertiser_currency": 1675.48,
                            "cpcv_in_advertiser_currency": 9423.3,
                            "miaozhen_otp_in_percent": 4806.49,
                        },
                        "creative_ids": [
                            "<value>",
                            "<value>",
                            "<value>",
                        ],
                        "associated_bid_lists": [
                            {
                                "bid_list_id": "<id>",
                                "is_enabled": True,
                                "is_default_for_dimension": False,
                            },
                        ],
                        "programmatic_guaranteed_private_contract_id": "<id>",
                    },
                    "advanced_input": {
                        "koa_optimization_settings": {
                            "are_future_koa_features_enabled": False,
                            "predictive_clearing_enabled": True,
                        },
                        "comscore_settings": {
                            "is_enabled": True,
                            "population_id": 549853,
                            "demographic_member_ids": [
                                75953,
                            ],
                            "mobile_demographic_member_ids": [
                                869836,
                                192225,
                                899573,
                            ],
                        },
                        "contract_targeting": {
                            "allow_open_market_bidding_when_targeting_contracts": False,
                        },
                        "dimensional_bidding_auto_optimization_settings": [
                            [],
                            [
                                ttd_workflows.DimensionalBiddingDimensions.HAS_VIDEO_MUTED_STATE_ID,
                            ],
                            [
                                ttd_workflows.DimensionalBiddingDimensions.HAS_AUDIENCE_REACH_PERCENTAGE_TIER_ID,
                                ttd_workflows.DimensionalBiddingDimensions.HAS_AD_LOAD_CATEGORY,
                                ttd_workflows.DimensionalBiddingDimensions.HAS_THIRD_PARTY_DATA,
                            ],
                        ],
                        "is_use_clicks_as_conversions_enabled": True,
                        "is_use_secondary_conversions_enabled": False,
                        "nielsen_tracking_attributes": {
                            "enhanced_reporting_option": ttd_workflows.EnhancedNielsenReportingOptions.NONE,
                            "gender": ttd_workflows.TargetingGender.FEMALE,
                            "start_age": ttd_workflows.TargetingStartAge.THIRTY_FIVE,
                            "end_age": ttd_workflows.TargetingEndAge.FORTY_FOUR,
                            "countries": [
                                "<value>",
                                "<value>",
                            ],
                        },
                        "new_frequency_configs": [
                            {
                                "counter_name": "<value>",
                                "frequency_cap": 360043,
                                "frequency_goal": 965696,
                                "reset_interval_in_minutes": 860037,
                            },
                            {
                                "counter_name": "<value>",
                                "frequency_cap": 344075,
                                "frequency_goal": 136066,
                                "reset_interval_in_minutes": 373611,
                            },
                            {
                                "counter_name": "<value>",
                                "frequency_cap": 258101,
                                "frequency_goal": 118163,
                                "reset_interval_in_minutes": 721137,
                            },
                        ],
                        "flights": [
                            {
                                "allocation_type": ttd_workflows.AllocationType.MINIMUM,
                                "budget_in_advertiser_currency": 2624.72,
                                "budget_in_impressions": 976218,
                                "daily_target_in_advertiser_currency": 7465.95,
                                "daily_target_in_impressions": 995275,
                            },
                            {
                                "allocation_type": ttd_workflows.AllocationType.MINIMUM,
                                "budget_in_advertiser_currency": 7520.92,
                                "budget_in_impressions": 901010,
                                "daily_target_in_advertiser_currency": 1232.28,
                                "daily_target_in_impressions": 740317,
                            },
                            {
                                "allocation_type": ttd_workflows.AllocationType.MAXIMUM,
                                "budget_in_advertiser_currency": 8257.73,
                                "budget_in_impressions": 85457,
                                "daily_target_in_advertiser_currency": 7173.67,
                                "daily_target_in_impressions": 81726,
                            },
                        ],
                    },
                },
                {
                    "primary_input": {
                        "name": "<value>",
                        "is_enabled": True,
                        "description": "absent valuable gruesome shyly where till subsidy",
                        "channel": ttd_workflows.AdGroupChannel.TV,
                        "funnel_location": ttd_workflows.AdGroupFunnelLocation.AWARENESS,
                        "budget": {
                            "allocation_type": ttd_workflows.AllocationType.FIXED,
                            "budget_in_advertiser_currency": 1639.17,
                            "budget_in_impressions": 428972,
                            "daily_target_in_advertiser_currency": 1190.66,
                            "daily_target_in_impressions": 732688,
                        },
                        "base_bid_cpm_in_advertiser_currency": 5613.5,
                        "max_bid_cpm_in_advertiser_currency": 9770.39,
                        "audience_targeting": {
                            "audience_id": "<id>",
                            "audience_accelerator_exclusions_enabled": True,
                            "audience_booster_enabled": False,
                            "audience_excluder_enabled": True,
                            "audience_predictor_enabled": True,
                            "cross_device_vendor_list_for_audience": [
                                606453,
                                44469,
                                455948,
                            ],
                            "recency_exclusion_window_in_minutes": 949741,
                            "target_trackable_users_enabled": False,
                            "use_mc_id_as_primary": False,
                        },
                        "roi_goal": {
                            "maximize_reach": True,
                            "maximize_ltv_incremental_reach": False,
                            "cpc_in_advertiser_currency": 7839.82,
                            "ctr_in_percent": 3117.69,
                            "nielsen_otp_in_percent": 7799.56,
                            "cpa_in_advertiser_currency": 3711.12,
                            "return_on_ad_spend_percent": 5368.14,
                            "vcr_in_percent": 1599.94,
                            "viewability_in_percent": 4701.02,
                            "vcpm_in_advertiser_currency": 5819.43,
                            "cpcv_in_advertiser_currency": 5672.37,
                            "miaozhen_otp_in_percent": 9104.31,
                        },
                        "creative_ids": [
                            "<value>",
                        ],
                        "associated_bid_lists": [
                            {
                                "bid_list_id": "<id>",
                                "is_enabled": False,
                                "is_default_for_dimension": False,
                            },
                            {
                                "bid_list_id": "<id>",
                                "is_enabled": False,
                                "is_default_for_dimension": False,
                            },
                        ],
                        "programmatic_guaranteed_private_contract_id": "<id>",
                    },
                    "advanced_input": {
                        "koa_optimization_settings": {
                            "are_future_koa_features_enabled": False,
                            "predictive_clearing_enabled": True,
                        },
                        "comscore_settings": {
                            "is_enabled": False,
                            "population_id": 353367,
                            "demographic_member_ids": [
                                615697,
                                643154,
                            ],
                            "mobile_demographic_member_ids": [
                                297484,
                                444326,
                                466904,
                            ],
                        },
                        "contract_targeting": {
                            "allow_open_market_bidding_when_targeting_contracts": True,
                        },
                        "dimensional_bidding_auto_optimization_settings": [
                            [
                                ttd_workflows.DimensionalBiddingDimensions.HAS_FREQUENCY_ADJUSTMENT_ID,
                            ],
                            [
                                ttd_workflows.DimensionalBiddingDimensions.HAS_CONTENT_LIVESTREAM,
                                ttd_workflows.DimensionalBiddingDimensions.HAS_RENDERING_CONTEXT_ID,
                                ttd_workflows.DimensionalBiddingDimensions.HAS_DOMAIN_CLASS_ID,
                            ],
                        ],
                        "is_use_clicks_as_conversions_enabled": True,
                        "is_use_secondary_conversions_enabled": False,
                        "nielsen_tracking_attributes": {
                            "enhanced_reporting_option": ttd_workflows.EnhancedNielsenReportingOptions.NONE,
                            "gender": ttd_workflows.TargetingGender.MALE,
                            "start_age": ttd_workflows.TargetingStartAge.TWENTY_FIVE,
                            "end_age": ttd_workflows.TargetingEndAge.SIXTY_FOUR,
                            "countries": [
                                "<value>",
                                "<value>",
                            ],
                        },
                        "new_frequency_configs": [
                            {
                                "counter_name": "<value>",
                                "frequency_cap": 582809,
                                "frequency_goal": 714168,
                                "reset_interval_in_minutes": 788864,
                            },
                        ],
                        "flights": [
                            {
                                "allocation_type": ttd_workflows.AllocationType.MAXIMUM,
                                "budget_in_advertiser_currency": 2670.46,
                                "budget_in_impressions": 464053,
                                "daily_target_in_advertiser_currency": 2346.64,
                                "daily_target_in_impressions": 168258,
                            },
                            {
                                "allocation_type": ttd_workflows.AllocationType.MINIMUM,
                                "budget_in_advertiser_currency": 8824.72,
                                "budget_in_impressions": 517318,
                                "daily_target_in_advertiser_currency": 3976.56,
                                "daily_target_in_impressions": 85485,
                            },
                            {
                                "allocation_type": ttd_workflows.AllocationType.MINIMUM,
                                "budget_in_advertiser_currency": 3119.46,
                                "budget_in_impressions": 425344,
                                "daily_target_in_advertiser_currency": 3450.15,
                                "daily_target_in_impressions": 280049,
                            },
                        ],
                    },
                },
                {
                    "primary_input": {
                        "name": "<value>",
                        "is_enabled": False,
                        "description": "archive amid typewriter careless",
                        "channel": ttd_workflows.AdGroupChannel.NATIVE_VIDEO,
                        "funnel_location": ttd_workflows.AdGroupFunnelLocation.NONE,
                        "budget": {
                            "allocation_type": ttd_workflows.AllocationType.MINIMUM,
                            "budget_in_advertiser_currency": 7501.99,
                            "budget_in_impressions": 614609,
                            "daily_target_in_advertiser_currency": 2906.22,
                            "daily_target_in_impressions": 801561,
                        },
                        "base_bid_cpm_in_advertiser_currency": 3102.42,
                        "max_bid_cpm_in_advertiser_currency": 1452.26,
                        "audience_targeting": {
                            "audience_id": "<id>",
                            "audience_accelerator_exclusions_enabled": True,
                            "audience_booster_enabled": False,
                            "audience_excluder_enabled": True,
                            "audience_predictor_enabled": True,
                            "cross_device_vendor_list_for_audience": [
                                909931,
                            ],
                            "recency_exclusion_window_in_minutes": 91561,
                            "target_trackable_users_enabled": False,
                            "use_mc_id_as_primary": False,
                        },
                        "roi_goal": {
                            "maximize_reach": False,
                            "maximize_ltv_incremental_reach": False,
                            "cpc_in_advertiser_currency": 3839.86,
                            "ctr_in_percent": 2480.51,
                            "nielsen_otp_in_percent": 5257.21,
                            "cpa_in_advertiser_currency": 7546.84,
                            "return_on_ad_spend_percent": 737.38,
                            "vcr_in_percent": 9027.15,
                            "viewability_in_percent": 606.63,
                            "vcpm_in_advertiser_currency": 7254.65,
                            "cpcv_in_advertiser_currency": 4470.71,
                            "miaozhen_otp_in_percent": 9684.09,
                        },
                        "creative_ids": [
                            "<value>",
                            "<value>",
                        ],
                        "associated_bid_lists": [
                            {
                                "bid_list_id": "<id>",
                                "is_enabled": True,
                                "is_default_for_dimension": False,
                            },
                            {
                                "bid_list_id": "<id>",
                                "is_enabled": True,
                                "is_default_for_dimension": True,
                            },
                            {
                                "bid_list_id": "<id>",
                                "is_enabled": False,
                                "is_default_for_dimension": False,
                            },
                        ],
                        "programmatic_guaranteed_private_contract_id": "<id>",
                    },
                    "advanced_input": {
                        "koa_optimization_settings": {
                            "are_future_koa_features_enabled": True,
                            "predictive_clearing_enabled": True,
                        },
                        "comscore_settings": {
                            "is_enabled": True,
                            "population_id": 478825,
                            "demographic_member_ids": [
                                811346,
                                376746,
                            ],
                            "mobile_demographic_member_ids": [
                                430775,
                            ],
                        },
                        "contract_targeting": {
                            "allow_open_market_bidding_when_targeting_contracts": True,
                        },
                        "dimensional_bidding_auto_optimization_settings": [
                            [],
                        ],
                        "is_use_clicks_as_conversions_enabled": False,
                        "is_use_secondary_conversions_enabled": True,
                        "nielsen_tracking_attributes": {
                            "enhanced_reporting_option": ttd_workflows.EnhancedNielsenReportingOptions.AUDIENCE,
                            "gender": ttd_workflows.TargetingGender.BOTH,
                            "start_age": ttd_workflows.TargetingStartAge.TWENTY_FIVE,
                            "end_age": ttd_workflows.TargetingEndAge.FORTY_FOUR,
                            "countries": [],
                        },
                        "new_frequency_configs": [
                            {
                                "counter_name": "<value>",
                                "frequency_cap": 178224,
                                "frequency_goal": 365705,
                                "reset_interval_in_minutes": 509377,
                            },
                            {
                                "counter_name": "<value>",
                                "frequency_cap": 933396,
                                "frequency_goal": 270385,
                                "reset_interval_in_minutes": 991790,
                            },
                        ],
                        "flights": [
                            {
                                "allocation_type": ttd_workflows.AllocationType.MINIMUM,
                                "budget_in_advertiser_currency": 1291.85,
                                "budget_in_impressions": 732169,
                                "daily_target_in_advertiser_currency": 6182.19,
                                "daily_target_in_impressions": 584980,
                            },
                        ],
                    },
                },
            ],
            "validation_only": True,
        },
    ])

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [List[models.CampaignCreateWorkflowInput]](../../models/.md)        | :heavy_check_mark:                                                  | The request object to use for the request.                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.BulkJobSubmitResponse](../../models/bulkjobsubmitresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.ProblemDetailsError | 400, 403                   | application/json           |
| models.APIError            | 4XX, 5XX                   | \*/\*                      |

## post_campaign_archive

Archive a list of campaigns

### Example Usage

```python
import os
from ttd_workflows import Workflows


with Workflows(
    ttd_auth=os.getenv("WORKFLOWS_TTD_AUTH", ""),
) as workflows:

    res = workflows.campaign.post_campaign_archive(request_body=[
        "<value>",
        "<value>",
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

## get_version

GET a campaign's version

### Example Usage

```python
import os
from ttd_workflows import Workflows


with Workflows(
    ttd_auth=os.getenv("WORKFLOWS_TTD_AUTH", ""),
) as workflows:

    res = workflows.campaign.get_version(id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.CampaignVersionWorkflow](../../models/campaignversionworkflow.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.ProblemDetailsError | 400, 401, 403, 404         | application/json           |
| models.APIError            | 4XX, 5XX                   | \*/\*                      |