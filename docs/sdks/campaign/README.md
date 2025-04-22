# Campaign
(*campaign*)

## Overview

### Available Operations

* [create](#create) - Create a new campaign with required fields
* [post_campaign_bulk](#post_campaign_bulk) - Create a new campaign with required fields
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
        "campaign_create_workflow_primary_input": {
            "advertiser_id": "<id>",
            "name": "<value>",
            "description": "yuck vice between gee ugh ha",
            "time_zone": "Pacific/Chuuk",
            "custom_cpa_click_weight": 7804.86,
            "custom_cpa_viewthrough_weight": 7602.59,
            "custom_cpa_type": ttd_workflows.CustomCPAType.DISABLED,
            "impressions_only_budgeting_cpm": 4492.21,
            "primary_channel": ttd_workflows.CampaignChannelType.AUDIO,
            "budget": {
                "pacing_mode": ttd_workflows.CampaignPacingMode.PACE_TO_DAILY_CAP,
                "budget_in_advertiser_currency": 934.7,
                "budget_in_impressions": 491427,
                "daily_target_in_advertiser_currency": 4904.2,
                "daily_target_in_impressions": 325463,
            },
            "primary_goal": {
                "maximize_reach": False,
                "maximize_ltv_incremental_reach": True,
                "cpc_in_advertiser_currency": 1296.63,
                "ctr_in_percent": 2881.04,
                "nielsen_otp_in_percent": 5833.53,
                "cpa_in_advertiser_currency": 5193.59,
                "return_on_ad_spend_percent": 3259.9,
                "vcr_in_percent": 4078.33,
                "viewability_in_percent": 1012.51,
                "vcpm_in_advertiser_currency": 1884.35,
                "cpcv_in_advertiser_currency": 8133.97,
                "miaozhen_otp_in_percent": 8891.64,
            },
            "start_date_in_utc": parse_datetime("2023-01-06T22:59:38.009Z"),
            "end_date_in_utc": parse_datetime("2025-09-26T06:26:29.839Z"),
            "seed_id": "<id>",
            "campaign_conversion_reporting_columns": [
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
                {
                    "tracking_tag_id": "<id>",
                    "include_in_custom_cpa": True,
                    "reporting_column_id": 860420,
                    "roas_config": {
                        "include_in_custom_roas": False,
                        "custom_roas_weight": 5665.12,
                        "custom_roas_click_weight": 2955.58,
                        "custom_roas_viewthrough_weight": 2032.57,
                    },
                    "weight": 4332.24,
                    "cross_device_attribution_model_id": "<id>",
                },
                {
                    "tracking_tag_id": "<id>",
                    "include_in_custom_cpa": False,
                    "reporting_column_id": 995852,
                    "roas_config": {
                        "include_in_custom_roas": False,
                        "custom_roas_weight": 2127.75,
                        "custom_roas_click_weight": 6207.47,
                        "custom_roas_viewthrough_weight": 2841.2,
                    },
                    "weight": 6083.84,
                    "cross_device_attribution_model_id": "<id>",
                },
            ],
        },
        "campaign_create_advanced_input": {
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
                "name": "<value>",
                "is_enabled": False,
                "description": "simple ouch when pfft ah",
                "programmatic_guaranteed_private_contract_id": "<id>",
                "channel": ttd_workflows.AdGroupChannel.NATIVE_VIDEO,
                "funnel_location": ttd_workflows.AdGroupFunnelLocation.NONE,
                "budget": {
                    "allocation_type": ttd_workflows.AllocationType.MAXIMUM,
                    "budget_in_advertiser_currency": 6290.63,
                    "budget_in_impressions": 784768,
                    "daily_target_in_advertiser_currency": 3385.24,
                    "daily_target_in_impressions": 913221,
                },
                "base_bid_cpm_in_advertiser_currency": 1541.5,
                "max_bid_cpm_in_advertiser_currency": 7218.8,
                "audience_targeting": {
                    "audience_id": "<id>",
                    "audience_accelerator_exclusions_enabled": False,
                    "audience_booster_enabled": False,
                    "audience_excluder_enabled": True,
                    "audience_predictor_enabled": False,
                    "cross_device_vendor_list_for_audience": [
                        257762,
                    ],
                    "recency_exclusion_window_in_minutes": 982866,
                    "target_trackable_users_enabled": True,
                    "use_mc_id_as_primary": True,
                },
                "roi_goal": {
                    "maximize_reach": False,
                    "maximize_ltv_incremental_reach": True,
                    "cpc_in_advertiser_currency": 3831.56,
                    "ctr_in_percent": 5720.12,
                    "nielsen_otp_in_percent": 9789.08,
                    "cpa_in_advertiser_currency": 1850.76,
                    "return_on_ad_spend_percent": 6168.92,
                    "vcr_in_percent": 9775.91,
                    "viewability_in_percent": 1909.73,
                    "vcpm_in_advertiser_currency": 3141.79,
                    "cpcv_in_advertiser_currency": 8272.61,
                    "miaozhen_otp_in_percent": 7609.47,
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
                "advanced_settings": {
                    "flights": [
                        {
                            "allocation_type": ttd_workflows.AllocationType.MINIMUM,
                            "budget_in_advertiser_currency": 4285.01,
                            "budget_in_impressions": 838181,
                            "daily_target_in_advertiser_currency": 9525.44,
                            "daily_target_in_impressions": 188907,
                        },
                        {
                            "allocation_type": ttd_workflows.AllocationType.FIXED,
                            "budget_in_advertiser_currency": 8833.21,
                            "budget_in_impressions": 892770,
                            "daily_target_in_advertiser_currency": 1993.11,
                            "daily_target_in_impressions": 564854,
                        },
                        {
                            "allocation_type": ttd_workflows.AllocationType.MAXIMUM,
                            "budget_in_advertiser_currency": 7458.53,
                            "budget_in_impressions": 290123,
                            "daily_target_in_advertiser_currency": 700.72,
                            "daily_target_in_impressions": 547483,
                        },
                    ],
                    "koa_optimization_settings": {
                        "are_future_koa_features_enabled": False,
                        "predictive_clearing_enabled": False,
                    },
                    "comscore_settings": {
                        "is_enabled": True,
                        "population_id": 695413,
                        "demographic_member_ids": [
                            261757,
                        ],
                        "mobile_demographic_member_ids": [
                            400422,
                            257433,
                        ],
                    },
                    "contract_targeting": {
                        "allow_open_market_bidding_when_targeting_contracts": True,
                    },
                    "dimensional_bidding_auto_optimization_settings": [
                        [],
                        [
                            ttd_workflows.DimensionalBiddingDimensions.HAS_VIDEO_COMPLETION_RATE_SCORE_RANGE,
                        ],
                    ],
                    "is_use_clicks_as_conversions_enabled": False,
                    "is_use_secondary_conversions_enabled": True,
                    "nielsen_tracking_attributes": {
                        "enhanced_reporting_option": ttd_workflows.EnhancedNielsenReportingOptions.AUDIENCE,
                        "gender": ttd_workflows.TargetingGender.BOTH,
                        "start_age": ttd_workflows.TargetingStartAge.TWENTY_FIVE,
                        "end_age": ttd_workflows.TargetingEndAge.TWENTY_NINE,
                        "countries": [
                            "<value>",
                            "<value>",
                            "<value>",
                        ],
                    },
                    "new_frequency_configs": [
                        {
                            "counter_name": "<value>",
                            "frequency_cap": 557925,
                            "frequency_goal": 643654,
                            "reset_interval_in_minutes": 700013,
                        },
                        {
                            "counter_name": "<value>",
                            "frequency_cap": 770948,
                            "frequency_goal": 347880,
                            "reset_interval_in_minutes": 698997,
                        },
                        {
                            "counter_name": "<value>",
                            "frequency_cap": 620608,
                            "frequency_goal": 546216,
                            "reset_interval_in_minutes": 500290,
                        },
                    ],
                },
            },
            {
                "name": "<value>",
                "is_enabled": True,
                "description": "satisfy majority pace however crocodile yowza",
                "programmatic_guaranteed_private_contract_id": "<id>",
                "channel": ttd_workflows.AdGroupChannel.VIDEO,
                "funnel_location": ttd_workflows.AdGroupFunnelLocation.NONE,
                "budget": {
                    "allocation_type": ttd_workflows.AllocationType.FIXED,
                    "budget_in_advertiser_currency": 2032.81,
                    "budget_in_impressions": 778234,
                    "daily_target_in_advertiser_currency": 4040.62,
                    "daily_target_in_impressions": 421607,
                },
                "base_bid_cpm_in_advertiser_currency": 9476.87,
                "max_bid_cpm_in_advertiser_currency": 703.96,
                "audience_targeting": {
                    "audience_id": "<id>",
                    "audience_accelerator_exclusions_enabled": True,
                    "audience_booster_enabled": False,
                    "audience_excluder_enabled": False,
                    "audience_predictor_enabled": False,
                    "cross_device_vendor_list_for_audience": [
                        426375,
                    ],
                    "recency_exclusion_window_in_minutes": 306126,
                    "target_trackable_users_enabled": False,
                    "use_mc_id_as_primary": False,
                },
                "roi_goal": {
                    "maximize_reach": False,
                    "maximize_ltv_incremental_reach": True,
                    "cpc_in_advertiser_currency": 4735.88,
                    "ctr_in_percent": 9915.94,
                    "nielsen_otp_in_percent": 4475.13,
                    "cpa_in_advertiser_currency": 5150.66,
                    "return_on_ad_spend_percent": 7248.87,
                    "vcr_in_percent": 9972.42,
                    "viewability_in_percent": 6545.2,
                    "vcpm_in_advertiser_currency": 7746.63,
                    "cpcv_in_advertiser_currency": 6813.67,
                    "miaozhen_otp_in_percent": 9625.35,
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
                ],
                "advanced_settings": {
                    "flights": [
                        {
                            "allocation_type": ttd_workflows.AllocationType.FIXED,
                            "budget_in_advertiser_currency": 87.86,
                            "budget_in_impressions": 992162,
                            "daily_target_in_advertiser_currency": 6912.82,
                            "daily_target_in_impressions": 856665,
                        },
                        {
                            "allocation_type": ttd_workflows.AllocationType.MAXIMUM,
                            "budget_in_advertiser_currency": 2102.57,
                            "budget_in_impressions": 784309,
                            "daily_target_in_advertiser_currency": 9390.93,
                            "daily_target_in_impressions": 704061,
                        },
                        {
                            "allocation_type": ttd_workflows.AllocationType.MAXIMUM,
                            "budget_in_advertiser_currency": 6477.52,
                            "budget_in_impressions": 511670,
                            "daily_target_in_advertiser_currency": 4530.79,
                            "daily_target_in_impressions": 275977,
                        },
                    ],
                    "koa_optimization_settings": {
                        "are_future_koa_features_enabled": False,
                        "predictive_clearing_enabled": True,
                    },
                    "comscore_settings": {
                        "is_enabled": True,
                        "population_id": 610092,
                        "demographic_member_ids": [
                            909366,
                            209538,
                        ],
                        "mobile_demographic_member_ids": [
                            493315,
                            778851,
                            468734,
                        ],
                    },
                    "contract_targeting": {
                        "allow_open_market_bidding_when_targeting_contracts": True,
                    },
                    "dimensional_bidding_auto_optimization_settings": [
                        [
                            ttd_workflows.DimensionalBiddingDimensions.HAS_INTEGRAL_VIDEO_BRAND_SAFETY_CATEGORY_ID,
                        ],
                    ],
                    "is_use_clicks_as_conversions_enabled": True,
                    "is_use_secondary_conversions_enabled": True,
                    "nielsen_tracking_attributes": {
                        "enhanced_reporting_option": ttd_workflows.EnhancedNielsenReportingOptions.SITE,
                        "gender": ttd_workflows.TargetingGender.MALE,
                        "start_age": ttd_workflows.TargetingStartAge.EIGHTEEN,
                        "end_age": ttd_workflows.TargetingEndAge.FORTY_FOUR,
                        "countries": [
                            "<value>",
                        ],
                    },
                    "new_frequency_configs": [
                        {
                            "counter_name": "<value>",
                            "frequency_cap": 637441,
                            "frequency_goal": 855423,
                            "reset_interval_in_minutes": 967917,
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
| models.ProblemDetailsError | 400                        | application/json           |
| models.APIError            | 4XX, 5XX                   | \*/\*                      |

## post_campaign_bulk

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

    res = workflows.campaign.post_campaign_bulk(request=[
        {
            "campaign_create_workflow_primary_input": {
                "advertiser_id": "<id>",
                "name": "<value>",
                "description": "quarrelsome nimble fuss greedily slime dramatic",
                "time_zone": "America/Belize",
                "custom_cpa_click_weight": 4282.39,
                "custom_cpa_viewthrough_weight": 4447.49,
                "custom_cpa_type": ttd_workflows.CustomCPAType.DISABLED,
                "impressions_only_budgeting_cpm": 223.53,
                "primary_channel": ttd_workflows.CampaignChannelType.VIDEO,
                "budget": {
                    "pacing_mode": ttd_workflows.CampaignPacingMode.PACE_TO_DAILY_CAP,
                    "budget_in_advertiser_currency": 4761.15,
                    "budget_in_impressions": 237841,
                    "daily_target_in_advertiser_currency": 9085.58,
                    "daily_target_in_impressions": 305719,
                },
                "primary_goal": {
                    "maximize_reach": True,
                    "maximize_ltv_incremental_reach": True,
                    "cpc_in_advertiser_currency": 5100.58,
                    "ctr_in_percent": 2014.11,
                    "nielsen_otp_in_percent": 1962.45,
                    "cpa_in_advertiser_currency": 3162.7,
                    "return_on_ad_spend_percent": 4033.15,
                    "vcr_in_percent": 576.36,
                    "viewability_in_percent": 6937.09,
                    "vcpm_in_advertiser_currency": 4907.71,
                    "cpcv_in_advertiser_currency": 1087.92,
                    "miaozhen_otp_in_percent": 7857.51,
                },
                "start_date_in_utc": parse_datetime("2024-05-18T01:36:37.822Z"),
                "end_date_in_utc": parse_datetime("2023-12-13T06:09:37.218Z"),
                "seed_id": "<id>",
                "campaign_conversion_reporting_columns": [
                    {
                        "tracking_tag_id": "<id>",
                        "include_in_custom_cpa": True,
                        "reporting_column_id": 928266,
                        "roas_config": {
                            "include_in_custom_roas": False,
                            "custom_roas_weight": 3132.81,
                            "custom_roas_click_weight": 8003.45,
                            "custom_roas_viewthrough_weight": 1193.63,
                        },
                        "weight": 4966.24,
                        "cross_device_attribution_model_id": "<id>",
                    },
                    {
                        "tracking_tag_id": "<id>",
                        "include_in_custom_cpa": True,
                        "reporting_column_id": 791395,
                        "roas_config": {
                            "include_in_custom_roas": False,
                            "custom_roas_weight": 4225.21,
                            "custom_roas_click_weight": 2874.97,
                            "custom_roas_viewthrough_weight": 8684.93,
                        },
                        "weight": 2544.89,
                        "cross_device_attribution_model_id": "<id>",
                    },
                ],
            },
            "campaign_create_advanced_input": {
                "flights": [
                    {
                        "start_date_inclusive_utc": parse_datetime("2024-12-08T10:20:56.542Z"),
                        "end_date_exclusive_utc": parse_datetime("2024-08-25T03:13:30.407Z"),
                        "budget_in_advertiser_currency": 8083.81,
                        "budget_in_impressions": 291618,
                        "daily_target_in_advertiser_currency": 4734.03,
                        "daily_target_in_impressions": 661092,
                    },
                    {
                        "start_date_inclusive_utc": parse_datetime("2023-08-15T10:26:52.566Z"),
                        "end_date_exclusive_utc": parse_datetime("2024-09-05T22:25:31.049Z"),
                        "budget_in_advertiser_currency": 407.04,
                        "budget_in_impressions": 995084,
                        "daily_target_in_advertiser_currency": 7866.35,
                        "daily_target_in_impressions": 714765,
                    },
                ],
                "purchase_order_number": "<value>",
            },
            "ad_groups": [
                {
                    "name": "<value>",
                    "is_enabled": False,
                    "description": "mmm validity times pro",
                    "programmatic_guaranteed_private_contract_id": "<id>",
                    "channel": ttd_workflows.AdGroupChannel.VIDEO,
                    "funnel_location": ttd_workflows.AdGroupFunnelLocation.AWARENESS,
                    "budget": {
                        "allocation_type": ttd_workflows.AllocationType.MINIMUM,
                        "budget_in_advertiser_currency": 1349.27,
                        "budget_in_impressions": 76524,
                        "daily_target_in_advertiser_currency": 6197.34,
                        "daily_target_in_impressions": 40746,
                    },
                    "base_bid_cpm_in_advertiser_currency": 5534.59,
                    "max_bid_cpm_in_advertiser_currency": 6326.42,
                    "audience_targeting": {
                        "audience_id": "<id>",
                        "audience_accelerator_exclusions_enabled": True,
                        "audience_booster_enabled": False,
                        "audience_excluder_enabled": True,
                        "audience_predictor_enabled": True,
                        "cross_device_vendor_list_for_audience": [
                            465521,
                            178176,
                            260829,
                        ],
                        "recency_exclusion_window_in_minutes": 409655,
                        "target_trackable_users_enabled": False,
                        "use_mc_id_as_primary": True,
                    },
                    "roi_goal": {
                        "maximize_reach": False,
                        "maximize_ltv_incremental_reach": False,
                        "cpc_in_advertiser_currency": 3707.15,
                        "ctr_in_percent": 6647.35,
                        "nielsen_otp_in_percent": 1717.08,
                        "cpa_in_advertiser_currency": 2519.4,
                        "return_on_ad_spend_percent": 7775.47,
                        "vcr_in_percent": 4502.74,
                        "viewability_in_percent": 5060.79,
                        "vcpm_in_advertiser_currency": 5526.97,
                        "cpcv_in_advertiser_currency": 4219.33,
                        "miaozhen_otp_in_percent": 1381.33,
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
                    ],
                    "advanced_settings": {
                        "flights": [
                            {
                                "allocation_type": ttd_workflows.AllocationType.MINIMUM,
                                "budget_in_advertiser_currency": 5017.64,
                                "budget_in_impressions": 635802,
                                "daily_target_in_advertiser_currency": 9399.82,
                                "daily_target_in_impressions": 311869,
                            },
                        ],
                        "koa_optimization_settings": {
                            "are_future_koa_features_enabled": False,
                            "predictive_clearing_enabled": False,
                        },
                        "comscore_settings": {
                            "is_enabled": False,
                            "population_id": 882921,
                            "demographic_member_ids": [
                                167548,
                            ],
                            "mobile_demographic_member_ids": [
                                480649,
                                677457,
                                25637,
                            ],
                        },
                        "contract_targeting": {
                            "allow_open_market_bidding_when_targeting_contracts": True,
                        },
                        "dimensional_bidding_auto_optimization_settings": [
                            [
                                ttd_workflows.DimensionalBiddingDimensions.HAS_DOMAIN_FRAGMENT_ID,
                                ttd_workflows.DimensionalBiddingDimensions.HAS_INTEGRAL_VIDEO_PAGE_QUALITY_CATEGORY_ID,
                                ttd_workflows.DimensionalBiddingDimensions.HAS_DOUBLE_VERIFY_VIDEO_VIEWABILITY_CATEGORY_ID,
                            ],
                            [],
                        ],
                        "is_use_clicks_as_conversions_enabled": True,
                        "is_use_secondary_conversions_enabled": False,
                        "nielsen_tracking_attributes": {
                            "enhanced_reporting_option": ttd_workflows.EnhancedNielsenReportingOptions.SITE,
                            "gender": ttd_workflows.TargetingGender.MALE,
                            "start_age": ttd_workflows.TargetingStartAge.FIFTY_FIVE,
                            "end_age": ttd_workflows.TargetingEndAge.FIFTY_FOUR,
                            "countries": [
                                "<value>",
                                "<value>",
                            ],
                        },
                        "new_frequency_configs": [
                            {
                                "counter_name": "<value>",
                                "frequency_cap": 475654,
                                "frequency_goal": 245053,
                                "reset_interval_in_minutes": 883515,
                            },
                        ],
                    },
                },
                {
                    "name": "<value>",
                    "is_enabled": False,
                    "description": "masterpiece among barring whoa mockingly thump pike woeful but geez",
                    "programmatic_guaranteed_private_contract_id": "<id>",
                    "channel": ttd_workflows.AdGroupChannel.TV,
                    "funnel_location": ttd_workflows.AdGroupFunnelLocation.CONVERSION,
                    "budget": {
                        "allocation_type": ttd_workflows.AllocationType.MAXIMUM,
                        "budget_in_advertiser_currency": 9478.31,
                        "budget_in_impressions": 874088,
                        "daily_target_in_advertiser_currency": 3116.56,
                        "daily_target_in_impressions": 768111,
                    },
                    "base_bid_cpm_in_advertiser_currency": 6687.67,
                    "max_bid_cpm_in_advertiser_currency": 4386.78,
                    "audience_targeting": {
                        "audience_id": "<id>",
                        "audience_accelerator_exclusions_enabled": True,
                        "audience_booster_enabled": True,
                        "audience_excluder_enabled": True,
                        "audience_predictor_enabled": True,
                        "cross_device_vendor_list_for_audience": [
                            865156,
                            785484,
                        ],
                        "recency_exclusion_window_in_minutes": 494534,
                        "target_trackable_users_enabled": False,
                        "use_mc_id_as_primary": True,
                    },
                    "roi_goal": {
                        "maximize_reach": True,
                        "maximize_ltv_incremental_reach": True,
                        "cpc_in_advertiser_currency": 7326.88,
                        "ctr_in_percent": 5613.5,
                        "nielsen_otp_in_percent": 9770.39,
                        "cpa_in_advertiser_currency": 1158.44,
                        "return_on_ad_spend_percent": 7855.77,
                        "vcr_in_percent": 4875.53,
                        "viewability_in_percent": 3237.65,
                        "vcpm_in_advertiser_currency": 7772.03,
                        "cpcv_in_advertiser_currency": 6064.53,
                        "miaozhen_otp_in_percent": 444.69,
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
                    "advanced_settings": {
                        "flights": [
                            {
                                "allocation_type": ttd_workflows.AllocationType.MAXIMUM,
                                "budget_in_advertiser_currency": 5368.14,
                                "budget_in_impressions": 159994,
                                "daily_target_in_advertiser_currency": 4701.02,
                                "daily_target_in_impressions": 581943,
                            },
                            {
                                "allocation_type": ttd_workflows.AllocationType.MAXIMUM,
                                "budget_in_advertiser_currency": 9104.31,
                                "budget_in_impressions": 153893,
                                "daily_target_in_advertiser_currency": 4231.63,
                                "daily_target_in_impressions": 772933,
                            },
                            {
                                "allocation_type": ttd_workflows.AllocationType.FIXED,
                                "budget_in_advertiser_currency": 6064.88,
                                "budget_in_impressions": 542744,
                                "daily_target_in_advertiser_currency": 7557.84,
                                "daily_target_in_impressions": 267592,
                            },
                        ],
                        "koa_optimization_settings": {
                            "are_future_koa_features_enabled": False,
                            "predictive_clearing_enabled": True,
                        },
                        "comscore_settings": {
                            "is_enabled": False,
                            "population_id": 615697,
                            "demographic_member_ids": [
                                798868,
                                297484,
                            ],
                            "mobile_demographic_member_ids": [
                                466904,
                                214928,
                            ],
                        },
                        "contract_targeting": {
                            "allow_open_market_bidding_when_targeting_contracts": False,
                        },
                        "dimensional_bidding_auto_optimization_settings": [
                            [
                                ttd_workflows.DimensionalBiddingDimensions.HAS_CONTENT_TRANSPARENCY,
                                ttd_workflows.DimensionalBiddingDimensions.HAS_CONTENT_LIVESTREAM,
                            ],
                            [],
                        ],
                        "is_use_clicks_as_conversions_enabled": False,
                        "is_use_secondary_conversions_enabled": True,
                        "nielsen_tracking_attributes": {
                            "enhanced_reporting_option": ttd_workflows.EnhancedNielsenReportingOptions.AUDIENCE,
                            "gender": ttd_workflows.TargetingGender.MALE,
                            "start_age": ttd_workflows.TargetingStartAge.EIGHTEEN,
                            "end_age": ttd_workflows.TargetingEndAge.THIRTY_FOUR,
                            "countries": [
                                "<value>",
                                "<value>",
                                "<value>",
                            ],
                        },
                        "new_frequency_configs": [
                            {
                                "counter_name": "<value>",
                                "frequency_cap": 57684,
                                "frequency_goal": 582809,
                                "reset_interval_in_minutes": 714168,
                            },
                            {
                                "counter_name": "<value>",
                                "frequency_cap": 788864,
                                "frequency_goal": 919011,
                                "reset_interval_in_minutes": 423321,
                            },
                        ],
                    },
                },
                {
                    "name": "<value>",
                    "is_enabled": True,
                    "description": "because daughter archive amid typewriter careless",
                    "programmatic_guaranteed_private_contract_id": "<id>",
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
                    "advanced_settings": {
                        "flights": [
                            {
                                "allocation_type": ttd_workflows.AllocationType.MINIMUM,
                                "budget_in_advertiser_currency": 3736.14,
                                "budget_in_impressions": 478825,
                                "daily_target_in_advertiser_currency": 3340.68,
                                "daily_target_in_impressions": 811346,
                            },
                        ],
                        "koa_optimization_settings": {
                            "are_future_koa_features_enabled": True,
                            "predictive_clearing_enabled": True,
                        },
                        "comscore_settings": {
                            "is_enabled": True,
                            "population_id": 353963,
                            "demographic_member_ids": [
                                184508,
                            ],
                            "mobile_demographic_member_ids": [
                                94825,
                                374794,
                                867963,
                            ],
                        },
                        "contract_targeting": {
                            "allow_open_market_bidding_when_targeting_contracts": True,
                        },
                        "dimensional_bidding_auto_optimization_settings": [
                            [],
                            [
                                ttd_workflows.DimensionalBiddingDimensions.HAS_RENDERING_CONTEXT_ID,
                                ttd_workflows.DimensionalBiddingDimensions.HAS_PEER39_LANGUAGE_ID,
                            ],
                        ],
                        "is_use_clicks_as_conversions_enabled": False,
                        "is_use_secondary_conversions_enabled": False,
                        "nielsen_tracking_attributes": {
                            "enhanced_reporting_option": ttd_workflows.EnhancedNielsenReportingOptions.NONE,
                            "gender": ttd_workflows.TargetingGender.BOTH,
                            "start_age": ttd_workflows.TargetingStartAge.THIRTEEN,
                            "end_age": ttd_workflows.TargetingEndAge.TWENTY_NINE,
                            "countries": [],
                        },
                        "new_frequency_configs": [
                            {
                                "counter_name": "<value>",
                                "frequency_cap": 618219,
                                "frequency_goal": 584980,
                                "reset_interval_in_minutes": 188756,
                            },
                            {
                                "counter_name": "<value>",
                                "frequency_cap": 356009,
                                "frequency_goal": 559681,
                                "reset_interval_in_minutes": 786602,
                            },
                            {
                                "counter_name": "<value>",
                                "frequency_cap": 161840,
                                "frequency_goal": 959863,
                                "reset_interval_in_minutes": 656522,
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

**[List[models.CampaignBulkPayload]](../../models/.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.ProblemDetailsError | 400                        | application/json           |
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