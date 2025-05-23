# Campaign
(*campaign*)

## Overview

### Available Operations

* [create](#create) - Create a new campaign with required fields
* [patch_campaign](#patch_campaign) - Update an existing campaign with specified fields
* [post_campaign_bulk](#post_campaign_bulk) - Create a list of campaigns with required fields. `ValidateInputOnly` value should be the same for all campaigns.
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
            "description": "brightly once incidentally biodegrade waterlogged geez quaff coolly remark",
            "time_zone": "America/Martinique",
            "custom_cpa_click_weight": 8565.86,
            "custom_cpa_viewthrough_weight": 4944.28,
            "custom_cpa_type": ttd_workflows.CustomCPAType.DISABLED,
            "impressions_only_budgeting_cpm": 3563.37,
            "budget": {
                "pacing_mode": ttd_workflows.CampaignPacingMode.PACE_AS_SOON_AS_POSSIBLE,
                "budget_in_advertiser_currency": 3004.71,
                "budget_in_impressions": 470604,
                "daily_target_in_advertiser_currency": 6178.77,
                "daily_target_in_impressions": 229960,
            },
            "end_date_in_utc": parse_datetime("2023-10-12T00:18:24.941Z"),
            "seed_id": "<id>",
            "campaign_conversion_reporting_columns": [
                {
                    "tracking_tag_id": "<id>",
                    "include_in_custom_cpa": False,
                    "reporting_column_id": 637398,
                    "roas_config": {
                        "include_in_custom_roas": False,
                        "custom_roas_weight": 6976.5,
                        "custom_roas_click_weight": 3551.1,
                        "custom_roas_viewthrough_weight": 4100.93,
                    },
                    "weight": 2092.05,
                    "cross_device_attribution_model_id": "<id>",
                },
                {
                    "tracking_tag_id": "<id>",
                    "include_in_custom_cpa": False,
                    "reporting_column_id": 637398,
                    "roas_config": {
                        "include_in_custom_roas": False,
                        "custom_roas_weight": 6976.5,
                        "custom_roas_click_weight": 3551.1,
                        "custom_roas_viewthrough_weight": 4100.93,
                    },
                    "weight": 2092.05,
                    "cross_device_attribution_model_id": "<id>",
                },
                {
                    "tracking_tag_id": "<id>",
                    "include_in_custom_cpa": False,
                    "reporting_column_id": 637398,
                    "roas_config": {
                        "include_in_custom_roas": False,
                        "custom_roas_weight": 6976.5,
                        "custom_roas_click_weight": 3551.1,
                        "custom_roas_viewthrough_weight": 4100.93,
                    },
                    "weight": 2092.05,
                    "cross_device_attribution_model_id": "<id>",
                },
            ],
            "advertiser_id": "<id>",
            "name": "<value>",
            "primary_channel": ttd_workflows.CampaignChannelType.NATIVE_VIDEO,
            "primary_goal": {
                "maximize_reach": True,
                "maximize_ltv_incremental_reach": True,
                "cpc_in_advertiser_currency": 8043.58,
                "ctr_in_percent": 5969.41,
                "nielsen_otp_in_percent": 2053.15,
                "cpa_in_advertiser_currency": 1984.87,
                "return_on_ad_spend_percent": None,
                "vcr_in_percent": 8220.61,
                "viewability_in_percent": 3757.54,
                "vcpm_in_advertiser_currency": 5996.9,
                "cpcv_in_advertiser_currency": None,
                "miaozhen_otp_in_percent": 9595.06,
            },
            "start_date_in_utc": parse_datetime("2025-11-14T15:34:57.905Z"),
        },
        "advanced_input": {
            "flights": [
                {
                    "start_date_inclusive_utc": parse_datetime("2025-03-12T15:05:09.942Z"),
                    "end_date_exclusive_utc": parse_datetime("2023-09-04T20:53:09.531Z"),
                    "budget_in_advertiser_currency": 4180.14,
                    "budget_in_impressions": 222439,
                    "daily_target_in_advertiser_currency": 7167.72,
                    "daily_target_in_impressions": 948610,
                },
                {
                    "start_date_inclusive_utc": parse_datetime("2025-03-12T15:05:09.942Z"),
                    "end_date_exclusive_utc": parse_datetime("2023-09-04T20:53:09.531Z"),
                    "budget_in_advertiser_currency": 4180.14,
                    "budget_in_impressions": 222439,
                    "daily_target_in_advertiser_currency": 7167.72,
                    "daily_target_in_impressions": 948610,
                },
            ],
            "purchase_order_number": "<value>",
        },
        "ad_groups": None,
        "validate_input_only": False,
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
            "description": "until notwithstanding bump",
            "time_zone": None,
            "custom_cpa_click_weight": 6995,
            "custom_cpa_viewthrough_weight": 8563.38,
            "custom_cpa_type": ttd_workflows.CustomCPAType.DISABLED,
            "impressions_only_budgeting_cpm": 8246.96,
            "budget": {
                "pacing_mode": ttd_workflows.CampaignPacingMode.PACE_EVENLY,
                "budget_in_advertiser_currency": 8712.02,
                "budget_in_impressions": None,
                "daily_target_in_advertiser_currency": 8897.46,
                "daily_target_in_impressions": 665232,
            },
            "end_date_in_utc": None,
            "seed_id": "<id>",
            "campaign_conversion_reporting_columns": [
                {
                    "tracking_tag_id": "<id>",
                    "include_in_custom_cpa": True,
                    "reporting_column_id": 97349,
                    "roas_config": {
                        "include_in_custom_roas": False,
                        "custom_roas_weight": 4101.84,
                        "custom_roas_click_weight": None,
                        "custom_roas_viewthrough_weight": 4368.63,
                    },
                    "weight": 7340.95,
                    "cross_device_attribution_model_id": "<id>",
                },
                {
                    "tracking_tag_id": "<id>",
                    "include_in_custom_cpa": True,
                    "reporting_column_id": 97349,
                    "roas_config": {
                        "include_in_custom_roas": False,
                        "custom_roas_weight": 4101.84,
                        "custom_roas_click_weight": None,
                        "custom_roas_viewthrough_weight": 4368.63,
                    },
                    "weight": 7340.95,
                    "cross_device_attribution_model_id": "<id>",
                },
                {
                    "tracking_tag_id": "<id>",
                    "include_in_custom_cpa": True,
                    "reporting_column_id": 97349,
                    "roas_config": {
                        "include_in_custom_roas": False,
                        "custom_roas_weight": 4101.84,
                        "custom_roas_click_weight": None,
                        "custom_roas_viewthrough_weight": 4368.63,
                    },
                    "weight": 7340.95,
                    "cross_device_attribution_model_id": "<id>",
                },
            ],
            "id": "<id>",
            "name": "<value>",
            "primary_channel": ttd_workflows.CampaignChannelType.NONE,
            "primary_goal": {
                "maximize_reach": False,
                "maximize_ltv_incremental_reach": True,
                "cpc_in_advertiser_currency": 8699.49,
                "ctr_in_percent": 8949.6,
                "nielsen_otp_in_percent": 37.27,
                "cpa_in_advertiser_currency": 3521.28,
                "return_on_ad_spend_percent": 7256.13,
                "vcr_in_percent": 5452.85,
                "viewability_in_percent": 737.27,
                "vcpm_in_advertiser_currency": 1743.53,
                "cpcv_in_advertiser_currency": None,
                "miaozhen_otp_in_percent": 5666.12,
            },
            "start_date_in_utc": parse_datetime("2023-03-15T19:37:35.952Z"),
        },
        "advanced_input": {
            "flights": [
                {
                    "start_date_inclusive_utc": parse_datetime("2023-06-20T19:40:02.162Z"),
                    "end_date_exclusive_utc": parse_datetime("2025-01-24T04:52:37.846Z"),
                    "budget_in_advertiser_currency": 8764.81,
                    "budget_in_impressions": 472441,
                    "daily_target_in_advertiser_currency": 5399.55,
                    "daily_target_in_impressions": 808445,
                },
                {
                    "start_date_inclusive_utc": parse_datetime("2023-06-20T19:40:02.162Z"),
                    "end_date_exclusive_utc": parse_datetime("2025-01-24T04:52:37.846Z"),
                    "budget_in_advertiser_currency": 8764.81,
                    "budget_in_impressions": 472441,
                    "daily_target_in_advertiser_currency": 5399.55,
                    "daily_target_in_impressions": 808445,
                },
            ],
            "purchase_order_number": "<value>",
        },
        "validate_input_only": None,
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

Create a list of campaigns with required fields. `ValidateInputOnly` value should be the same for all campaigns.

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
                "description": "indeed ick ah warming unnecessarily",
                "time_zone": "Asia/Pontianak",
                "custom_cpa_click_weight": 1382.14,
                "custom_cpa_viewthrough_weight": 2161.08,
                "custom_cpa_type": ttd_workflows.CustomCPAType.CLICK_VIEWTHROUGH_WEIGHTING,
                "impressions_only_budgeting_cpm": 1414.35,
                "budget": {
                    "pacing_mode": ttd_workflows.CampaignPacingMode.PACE_EVENLY,
                    "budget_in_advertiser_currency": 6165.83,
                    "budget_in_impressions": 161063,
                    "daily_target_in_advertiser_currency": 2249.56,
                    "daily_target_in_impressions": 571430,
                },
                "end_date_in_utc": parse_datetime("2025-12-08T11:15:36.327Z"),
                "seed_id": "<id>",
                "campaign_conversion_reporting_columns": [
                    {
                        "tracking_tag_id": "<id>",
                        "include_in_custom_cpa": True,
                        "reporting_column_id": 160127,
                        "roas_config": {
                            "include_in_custom_roas": True,
                            "custom_roas_weight": 2304.44,
                            "custom_roas_click_weight": 5699.49,
                            "custom_roas_viewthrough_weight": 3622.69,
                        },
                        "weight": 3775.79,
                        "cross_device_attribution_model_id": "<id>",
                    },
                    {
                        "tracking_tag_id": "<id>",
                        "include_in_custom_cpa": True,
                        "reporting_column_id": 160127,
                        "roas_config": {
                            "include_in_custom_roas": True,
                            "custom_roas_weight": 2304.44,
                            "custom_roas_click_weight": 5699.49,
                            "custom_roas_viewthrough_weight": 3622.69,
                        },
                        "weight": 3775.79,
                        "cross_device_attribution_model_id": "<id>",
                    },
                    {
                        "tracking_tag_id": "<id>",
                        "include_in_custom_cpa": True,
                        "reporting_column_id": 160127,
                        "roas_config": {
                            "include_in_custom_roas": True,
                            "custom_roas_weight": 2304.44,
                            "custom_roas_click_weight": 5699.49,
                            "custom_roas_viewthrough_weight": 3622.69,
                        },
                        "weight": 3775.79,
                        "cross_device_attribution_model_id": "<id>",
                    },
                ],
                "advertiser_id": "<id>",
                "name": "<value>",
                "primary_channel": ttd_workflows.CampaignChannelType.TV,
                "primary_goal": {
                    "maximize_reach": True,
                    "maximize_ltv_incremental_reach": True,
                    "cpc_in_advertiser_currency": 6343.77,
                    "ctr_in_percent": 8167.4,
                    "nielsen_otp_in_percent": 8037.31,
                    "cpa_in_advertiser_currency": 9530.19,
                    "return_on_ad_spend_percent": 8552.34,
                    "vcr_in_percent": 9248.22,
                    "viewability_in_percent": 4354.75,
                    "vcpm_in_advertiser_currency": 319.18,
                    "cpcv_in_advertiser_currency": 1655.1,
                    "miaozhen_otp_in_percent": 2861.62,
                },
                "start_date_in_utc": None,
            },
            "advanced_input": {
                "flights": [
                    {
                        "start_date_inclusive_utc": parse_datetime("2025-10-15T07:00:15.844Z"),
                        "end_date_exclusive_utc": parse_datetime("2024-06-02T19:40:28.199Z"),
                        "budget_in_advertiser_currency": 5457.78,
                        "budget_in_impressions": 430971,
                        "daily_target_in_advertiser_currency": 3071.93,
                        "daily_target_in_impressions": 300915,
                    },
                    {
                        "start_date_inclusive_utc": parse_datetime("2025-10-15T07:00:15.844Z"),
                        "end_date_exclusive_utc": parse_datetime("2024-06-02T19:40:28.199Z"),
                        "budget_in_advertiser_currency": 5457.78,
                        "budget_in_impressions": 430971,
                        "daily_target_in_advertiser_currency": 3071.93,
                        "daily_target_in_impressions": 300915,
                    },
                    {
                        "start_date_inclusive_utc": parse_datetime("2025-10-15T07:00:15.844Z"),
                        "end_date_exclusive_utc": parse_datetime("2024-06-02T19:40:28.199Z"),
                        "budget_in_advertiser_currency": 5457.78,
                        "budget_in_impressions": 430971,
                        "daily_target_in_advertiser_currency": 3071.93,
                        "daily_target_in_impressions": 300915,
                    },
                ],
                "purchase_order_number": "<value>",
            },
            "ad_groups": [
                {
                    "primary_input": {
                        "name": "<value>",
                        "is_enabled": True,
                        "description": "coop ugh freely",
                        "channel": ttd_workflows.AdGroupChannel.NATIVE_VIDEO,
                        "funnel_location": ttd_workflows.AdGroupFunnelLocation.CONSIDERATION,
                        "budget": {
                            "allocation_type": ttd_workflows.AllocationType.FIXED,
                            "budget_in_advertiser_currency": 8559.9,
                            "budget_in_impressions": 879228,
                            "daily_target_in_advertiser_currency": 4378.96,
                            "daily_target_in_impressions": 247265,
                        },
                        "base_bid_cpm_in_advertiser_currency": 8271.76,
                        "max_bid_cpm_in_advertiser_currency": 1899.52,
                        "audience_targeting": {
                            "audience_id": "<id>",
                            "audience_accelerator_exclusions_enabled": False,
                            "audience_booster_enabled": True,
                            "audience_excluder_enabled": True,
                            "audience_predictor_enabled": True,
                            "cross_device_vendor_list_for_audience": [
                                645562,
                                527150,
                                574307,
                            ],
                            "recency_exclusion_window_in_minutes": 112177,
                            "target_trackable_users_enabled": False,
                            "use_mc_id_as_primary": False,
                        },
                        "roi_goal": {
                            "maximize_reach": False,
                            "maximize_ltv_incremental_reach": True,
                            "cpc_in_advertiser_currency": 1919.2,
                            "ctr_in_percent": 4140.95,
                            "nielsen_otp_in_percent": 3353.63,
                            "cpa_in_advertiser_currency": 7971.19,
                            "return_on_ad_spend_percent": 8859.59,
                            "vcr_in_percent": 9706.24,
                            "viewability_in_percent": None,
                            "vcpm_in_advertiser_currency": 3015.37,
                            "cpcv_in_advertiser_currency": 8797.74,
                            "miaozhen_otp_in_percent": None,
                        },
                        "creative_ids": [
                            "<value 1>",
                            "<value 2>",
                            "<value 3>",
                        ],
                        "associated_bid_lists": [
                            {
                                "bid_list_id": "<id>",
                                "is_enabled": False,
                                "is_default_for_dimension": None,
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
                            "population_id": 738685,
                            "demographic_member_ids": [
                                328311,
                                129775,
                            ],
                            "mobile_demographic_member_ids": [
                                857904,
                                221530,
                                841146,
                            ],
                        },
                        "contract_targeting": {
                            "allow_open_market_bidding_when_targeting_contracts": False,
                        },
                        "dimensional_bidding_auto_optimization_settings": [
                            [
                                ttd_workflows.DimensionalBiddingDimensions.HAS_CONTEXTUAL_SUPPLY_VENDOR_CATEGORY_ID,
                                ttd_workflows.DimensionalBiddingDimensions.HAS_VIDEO_PLAYER_SIZE_ID,
                            ],
                            [
                                ttd_workflows.DimensionalBiddingDimensions.HAS_INTEGRAL_VIDEO_VIEWABILITY_CATEGORY_ID,
                                ttd_workflows.DimensionalBiddingDimensions.HAS_DOUBLE_VERIFY_VIEWABILITY_CATEGORY_ID,
                                ttd_workflows.DimensionalBiddingDimensions.HAS_AD_LOAD_CATEGORY,
                            ],
                            [
                                ttd_workflows.DimensionalBiddingDimensions.HAS_SUPPLY_PATH_OPTIMIZATION_LIST_ID,
                            ],
                        ],
                        "is_use_clicks_as_conversions_enabled": True,
                        "is_use_secondary_conversions_enabled": True,
                        "nielsen_tracking_attributes": {
                            "enhanced_reporting_option": ttd_workflows.EnhancedNielsenReportingOptions.AUDIENCE,
                            "gender": ttd_workflows.TargetingGender.BOTH,
                            "start_age": ttd_workflows.TargetingStartAge.TWENTY_ONE,
                            "end_age": ttd_workflows.TargetingEndAge.TWENTY,
                            "countries": None,
                        },
                        "new_frequency_configs": [
                            {
                                "counter_name": "<value>",
                                "frequency_cap": 350226,
                                "frequency_goal": 904723,
                                "reset_interval_in_minutes": 167805,
                            },
                            {
                                "counter_name": "<value>",
                                "frequency_cap": 350226,
                                "frequency_goal": 904723,
                                "reset_interval_in_minutes": 167805,
                            },
                        ],
                        "flights": [
                            {
                                "allocation_type": ttd_workflows.AllocationType.FIXED,
                                "budget_in_advertiser_currency": 7149.15,
                                "budget_in_impressions": 562606,
                                "daily_target_in_advertiser_currency": 8257.64,
                                "daily_target_in_impressions": 122483,
                            },
                            {
                                "allocation_type": ttd_workflows.AllocationType.FIXED,
                                "budget_in_advertiser_currency": 7149.15,
                                "budget_in_impressions": 562606,
                                "daily_target_in_advertiser_currency": 8257.64,
                                "daily_target_in_impressions": 122483,
                            },
                        ],
                    },
                },
                {
                    "primary_input": {
                        "name": "<value>",
                        "is_enabled": True,
                        "description": "coop ugh freely",
                        "channel": ttd_workflows.AdGroupChannel.NATIVE_VIDEO,
                        "funnel_location": ttd_workflows.AdGroupFunnelLocation.CONSIDERATION,
                        "budget": {
                            "allocation_type": ttd_workflows.AllocationType.FIXED,
                            "budget_in_advertiser_currency": 8559.9,
                            "budget_in_impressions": 879228,
                            "daily_target_in_advertiser_currency": 4378.96,
                            "daily_target_in_impressions": 247265,
                        },
                        "base_bid_cpm_in_advertiser_currency": 8271.76,
                        "max_bid_cpm_in_advertiser_currency": 1899.52,
                        "audience_targeting": {
                            "audience_id": "<id>",
                            "audience_accelerator_exclusions_enabled": False,
                            "audience_booster_enabled": True,
                            "audience_excluder_enabled": True,
                            "audience_predictor_enabled": True,
                            "cross_device_vendor_list_for_audience": [
                                645562,
                                527150,
                                574307,
                            ],
                            "recency_exclusion_window_in_minutes": 112177,
                            "target_trackable_users_enabled": False,
                            "use_mc_id_as_primary": False,
                        },
                        "roi_goal": {
                            "maximize_reach": False,
                            "maximize_ltv_incremental_reach": True,
                            "cpc_in_advertiser_currency": 1919.2,
                            "ctr_in_percent": 4140.95,
                            "nielsen_otp_in_percent": 3353.63,
                            "cpa_in_advertiser_currency": 7971.19,
                            "return_on_ad_spend_percent": 8859.59,
                            "vcr_in_percent": 9706.24,
                            "viewability_in_percent": None,
                            "vcpm_in_advertiser_currency": 3015.37,
                            "cpcv_in_advertiser_currency": 8797.74,
                            "miaozhen_otp_in_percent": None,
                        },
                        "creative_ids": [
                            "<value 1>",
                            "<value 2>",
                            "<value 3>",
                        ],
                        "associated_bid_lists": [
                            {
                                "bid_list_id": "<id>",
                                "is_enabled": False,
                                "is_default_for_dimension": None,
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
                            "population_id": 738685,
                            "demographic_member_ids": [
                                328311,
                                129775,
                            ],
                            "mobile_demographic_member_ids": [
                                857904,
                                221530,
                                841146,
                            ],
                        },
                        "contract_targeting": {
                            "allow_open_market_bidding_when_targeting_contracts": False,
                        },
                        "dimensional_bidding_auto_optimization_settings": [
                            [
                                ttd_workflows.DimensionalBiddingDimensions.HAS_CONTEXTUAL_SUPPLY_VENDOR_CATEGORY_ID,
                                ttd_workflows.DimensionalBiddingDimensions.HAS_VIDEO_PLAYER_SIZE_ID,
                            ],
                            [
                                ttd_workflows.DimensionalBiddingDimensions.HAS_INTEGRAL_VIDEO_VIEWABILITY_CATEGORY_ID,
                                ttd_workflows.DimensionalBiddingDimensions.HAS_DOUBLE_VERIFY_VIEWABILITY_CATEGORY_ID,
                                ttd_workflows.DimensionalBiddingDimensions.HAS_AD_LOAD_CATEGORY,
                            ],
                            [
                                ttd_workflows.DimensionalBiddingDimensions.HAS_SUPPLY_PATH_OPTIMIZATION_LIST_ID,
                            ],
                        ],
                        "is_use_clicks_as_conversions_enabled": True,
                        "is_use_secondary_conversions_enabled": True,
                        "nielsen_tracking_attributes": {
                            "enhanced_reporting_option": ttd_workflows.EnhancedNielsenReportingOptions.AUDIENCE,
                            "gender": ttd_workflows.TargetingGender.BOTH,
                            "start_age": ttd_workflows.TargetingStartAge.TWENTY_ONE,
                            "end_age": ttd_workflows.TargetingEndAge.TWENTY,
                            "countries": None,
                        },
                        "new_frequency_configs": [
                            {
                                "counter_name": "<value>",
                                "frequency_cap": 350226,
                                "frequency_goal": 904723,
                                "reset_interval_in_minutes": 167805,
                            },
                            {
                                "counter_name": "<value>",
                                "frequency_cap": 350226,
                                "frequency_goal": 904723,
                                "reset_interval_in_minutes": 167805,
                            },
                        ],
                        "flights": [
                            {
                                "allocation_type": ttd_workflows.AllocationType.FIXED,
                                "budget_in_advertiser_currency": 7149.15,
                                "budget_in_impressions": 562606,
                                "daily_target_in_advertiser_currency": 8257.64,
                                "daily_target_in_impressions": 122483,
                            },
                            {
                                "allocation_type": ttd_workflows.AllocationType.FIXED,
                                "budget_in_advertiser_currency": 7149.15,
                                "budget_in_impressions": 562606,
                                "daily_target_in_advertiser_currency": 8257.64,
                                "daily_target_in_impressions": 122483,
                            },
                        ],
                    },
                },
            ],
            "validate_input_only": True,
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
        "<value 1>",
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