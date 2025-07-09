# Campaign
(*campaign*)

## Overview

### Available Operations

* [create](#create) - Create a new campaign with required fields
* [create_campaigns_job](#create_campaigns_job) - Create multiple new campaigns with required fields
* [update_campaigns_job](#update_campaigns_job) - Update multiple campaigns with specified fields
* [get_version](#get_version) - Get a campaign's version

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
            "description": "woot furthermore mentor",
            "time_zone": "Europe/Ulyanovsk",
            "custom_cpa_click_weight": 2561.01,
            "custom_cpa_viewthrough_weight": 5604.35,
            "custom_cpa_type": ttd_workflows.CustomCPAType.CLICK_VIEWTHROUGH_WEIGHTING,
            "impressions_only_budgeting_cpm": 1502.33,
            "budget": {
                "pacing_mode": ttd_workflows.CampaignPacingMode.PACE_AS_SOON_AS_POSSIBLE,
                "budget_in_advertiser_currency": 6363.35,
                "budget_in_impressions": 836518,
                "daily_target_in_advertiser_currency": 7814.79,
                "daily_target_in_impressions": 784985,
            },
            "end_date_in_utc": None,
            "seed_id": None,
            "campaign_conversion_reporting_columns": [
                {
                    "tracking_tag_id": "<id>",
                    "include_in_custom_cpa": False,
                    "reporting_column_id": 888649,
                    "roas_config": {
                        "include_in_custom_roas": False,
                        "custom_roas_weight": 4766.9,
                        "custom_roas_click_weight": 3310.24,
                        "custom_roas_viewthrough_weight": 2919.37,
                    },
                    "weight": 5369.43,
                    "cross_device_attribution_model_id": "<id>",
                },
            ],
            "advertiser_id": "<id>",
            "name": "<value>",
            "primary_channel": ttd_workflows.CampaignChannelType.DOOH,
            "primary_goal": {
                "maximize_reach": False,
                "maximize_ltv_incremental_reach": None,
                "cpc_in_advertiser_currency": 6678.34,
                "ctr_in_percent": 5357.4,
                "nielsen_otp_in_percent": 2741.6,
                "cpa_in_advertiser_currency": 4220.63,
                "return_on_ad_spend_percent": 8572.83,
                "vcr_in_percent": 8294.92,
                "viewability_in_percent": 8592.21,
                "vcpm_in_advertiser_currency": 8388.8,
                "cpcv_in_advertiser_currency": None,
                "miaozhen_otp_in_percent": 3033.14,
            },
            "start_date_in_utc": None,
        },
        "advanced_input": {
            "flights": [
                {
                    "start_date_inclusive_utc": parse_datetime("2024-07-08T10:52:56.944Z"),
                    "end_date_exclusive_utc": parse_datetime("2023-05-12T16:41:56.386Z"),
                    "budget_in_advertiser_currency": 5904.11,
                    "budget_in_impressions": None,
                    "daily_target_in_advertiser_currency": 6112.24,
                    "daily_target_in_impressions": 333131,
                },
            ],
            "purchase_order_number": None,
        },
        "ad_groups": [
            {
                "primary_input": {
                    "is_enabled": False,
                    "description": "quash lightly rot bashfully slope",
                    "budget": {
                        "allocation_type": ttd_workflows.AllocationType.MINIMUM,
                        "budget_in_advertiser_currency": 4043.98,
                        "budget_in_impressions": 907414,
                        "daily_target_in_advertiser_currency": 49.95,
                        "daily_target_in_impressions": 62363,
                    },
                    "base_bid_cpm_in_advertiser_currency": 1136.89,
                    "max_bid_cpm_in_advertiser_currency": 6950.27,
                    "audience_targeting": {
                        "audience_id": "<id>",
                        "audience_accelerator_exclusions_enabled": False,
                        "audience_booster_enabled": True,
                        "audience_excluder_enabled": False,
                        "audience_predictor_enabled": True,
                        "cross_device_vendor_list_for_audience": [
                            458524,
                            284141,
                        ],
                        "recency_exclusion_window_in_minutes": 982426,
                        "target_trackable_users_enabled": False,
                        "use_mc_id_as_primary": True,
                    },
                    "roi_goal": {
                        "maximize_reach": None,
                        "maximize_ltv_incremental_reach": True,
                        "cpc_in_advertiser_currency": 8782.74,
                        "ctr_in_percent": None,
                        "nielsen_otp_in_percent": 7930.85,
                        "cpa_in_advertiser_currency": 4606.89,
                        "return_on_ad_spend_percent": 2522.83,
                        "vcr_in_percent": 5828.49,
                        "viewability_in_percent": 6824.44,
                        "vcpm_in_advertiser_currency": 7123.95,
                        "cpcv_in_advertiser_currency": 6233.72,
                        "miaozhen_otp_in_percent": 8437.22,
                    },
                    "creative_ids": [
                        "<value 1>",
                    ],
                    "associated_bid_lists": [
                        {
                            "bid_list_id": "<id>",
                            "is_enabled": True,
                            "is_default_for_dimension": False,
                        },
                    ],
                    "name": "<value>",
                    "channel": ttd_workflows.AdGroupChannel.NATIVE_VIDEO,
                    "funnel_location": ttd_workflows.AdGroupFunnelLocation.NONE,
                    "programmatic_guaranteed_private_contract_id": "<id>",
                },
                "advanced_input": {
                    "koa_optimization_settings": {
                        "are_future_koa_features_enabled": True,
                        "predictive_clearing_enabled": True,
                    },
                    "comscore_settings": {
                        "is_enabled": False,
                        "population_id": 523753,
                        "demographic_member_ids": None,
                        "mobile_demographic_member_ids": None,
                    },
                    "contract_targeting": {
                        "allow_open_market_bidding_when_targeting_contracts": True,
                    },
                    "dimensional_bidding_auto_optimization_settings": [
                        [
                            ttd_workflows.DimensionalBiddingDimensions.HAS_FULL_REFERRER_URL,
                        ],
                        [
                            ttd_workflows.DimensionalBiddingDimensions.HAS_PUBLISHER_ID,
                        ],
                    ],
                    "is_use_clicks_as_conversions_enabled": None,
                    "is_use_secondary_conversions_enabled": True,
                    "nielsen_tracking_attributes": {
                        "enhanced_reporting_option": ttd_workflows.EnhancedNielsenReportingOptions.SITE,
                        "gender": ttd_workflows.TargetingGender.FEMALE,
                        "start_age": ttd_workflows.TargetingStartAge.THIRTY_FIVE,
                        "end_age": ttd_workflows.TargetingEndAge.FORTY_NINE,
                        "countries": [],
                    },
                    "new_frequency_configs": [
                        {
                            "counter_name": "<value>",
                            "frequency_cap": 391231,
                            "frequency_goal": 499235,
                            "reset_interval_in_minutes": 587736,
                        },
                    ],
                    "flights": [
                        {
                            "allocation_type": ttd_workflows.AllocationType.FIXED,
                            "budget_in_advertiser_currency": 5340.32,
                            "budget_in_impressions": 492382,
                            "daily_target_in_advertiser_currency": 5622.5,
                            "daily_target_in_impressions": 398919,
                        },
                    ],
                },
            },
        ],
        "validate_input_only": False,
    })

    assert res.campaign_payload is not None

    # Handle response
    print(res.campaign_payload)

```

### Parameters

| Parameter                                                                                                     | Type                                                                                                          | Required                                                                                                      | Description                                                                                                   |
| ------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                     | [models.CampaignCreateWorkflowInputWithValidation](../../models/campaigncreateworkflowinputwithvalidation.md) | :heavy_check_mark:                                                                                            | The request object to use for the request.                                                                    |
| `retries`                                                                                                     | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                              | :heavy_minus_sign:                                                                                            | Configuration to override the default retry behavior of the client.                                           |

### Response

**[models.CreateCampaignResponse](../../models/createcampaignresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.ProblemDetailsError | 400, 403                   | application/json           |
| models.APIError            | 4XX, 5XX                   | \*/\*                      |

## create_campaigns_job

Create multiple new campaigns with required fields

### Example Usage

```python
import os
import ttd_workflows
from ttd_workflows import Workflows
from ttd_workflows.utils import parse_datetime


with Workflows(
    ttd_auth=os.getenv("WORKFLOWS_TTD_AUTH", ""),
) as workflows:

    res = workflows.campaign.create_campaigns_job(request={
        "input": [
            {
                "primary_input": {
                    "description": None,
                    "time_zone": "America/North_Dakota/Center",
                    "custom_cpa_click_weight": 9662.9,
                    "custom_cpa_viewthrough_weight": 3558.78,
                    "custom_cpa_type": ttd_workflows.CustomCPAType.CLICK_VIEWTHROUGH_WEIGHTING,
                    "impressions_only_budgeting_cpm": 4427.56,
                    "budget": {
                        "pacing_mode": ttd_workflows.CampaignPacingMode.PACE_AHEAD,
                        "budget_in_advertiser_currency": 5501.96,
                        "budget_in_impressions": 629784,
                        "daily_target_in_advertiser_currency": 2524.41,
                        "daily_target_in_impressions": 726807,
                    },
                    "end_date_in_utc": parse_datetime("2023-12-21T01:12:20.772Z"),
                    "seed_id": "<id>",
                    "campaign_conversion_reporting_columns": [
                        {
                            "tracking_tag_id": "<id>",
                            "include_in_custom_cpa": False,
                            "reporting_column_id": 356532,
                            "roas_config": {
                                "include_in_custom_roas": False,
                                "custom_roas_weight": 1483.03,
                                "custom_roas_click_weight": 5286.76,
                                "custom_roas_viewthrough_weight": 8906.82,
                            },
                            "weight": None,
                            "cross_device_attribution_model_id": "<id>",
                        },
                    ],
                    "advertiser_id": "<id>",
                    "name": "<value>",
                    "primary_channel": ttd_workflows.CampaignChannelType.NATIVE_VIDEO,
                    "primary_goal": {
                        "maximize_reach": False,
                        "maximize_ltv_incremental_reach": False,
                        "cpc_in_advertiser_currency": 25.32,
                        "ctr_in_percent": 4889.32,
                        "nielsen_otp_in_percent": 5258.8,
                        "cpa_in_advertiser_currency": 2553.01,
                        "return_on_ad_spend_percent": 1142.91,
                        "vcr_in_percent": 1152.77,
                        "viewability_in_percent": 6711.38,
                        "vcpm_in_advertiser_currency": 4528.37,
                        "cpcv_in_advertiser_currency": 9833.69,
                        "miaozhen_otp_in_percent": 1951.58,
                    },
                    "start_date_in_utc": parse_datetime("2025-09-26T21:06:42.946Z"),
                },
                "advanced_input": {
                    "flights": [
                        {
                            "start_date_inclusive_utc": parse_datetime("2024-09-20T06:04:19.345Z"),
                            "end_date_exclusive_utc": parse_datetime("2024-01-18T07:43:56.299Z"),
                            "budget_in_advertiser_currency": 8219.9,
                            "budget_in_impressions": 76925,
                            "daily_target_in_advertiser_currency": 9309.03,
                            "daily_target_in_impressions": 152838,
                        },
                    ],
                    "purchase_order_number": "<value>",
                },
                "ad_groups": [
                    {
                        "primary_input": {
                            "is_enabled": True,
                            "description": "scenario dish gracefully through tame yahoo pension husband as atop",
                            "budget": {
                                "allocation_type": ttd_workflows.AllocationType.MAXIMUM,
                                "budget_in_advertiser_currency": 2283.06,
                                "budget_in_impressions": 301691,
                                "daily_target_in_advertiser_currency": 9268.18,
                                "daily_target_in_impressions": 851470,
                            },
                            "base_bid_cpm_in_advertiser_currency": 694.78,
                            "max_bid_cpm_in_advertiser_currency": 6084.4,
                            "audience_targeting": {
                                "audience_id": "<id>",
                                "audience_accelerator_exclusions_enabled": True,
                                "audience_booster_enabled": False,
                                "audience_excluder_enabled": True,
                                "audience_predictor_enabled": False,
                                "cross_device_vendor_list_for_audience": [
                                    497890,
                                    566253,
                                ],
                                "recency_exclusion_window_in_minutes": 742665,
                                "target_trackable_users_enabled": True,
                                "use_mc_id_as_primary": True,
                            },
                            "roi_goal": {
                                "maximize_reach": False,
                                "maximize_ltv_incremental_reach": True,
                                "cpc_in_advertiser_currency": 9062.02,
                                "ctr_in_percent": 7192.99,
                                "nielsen_otp_in_percent": 2823.22,
                                "cpa_in_advertiser_currency": 3140.25,
                                "return_on_ad_spend_percent": 6857.21,
                                "vcr_in_percent": 2704.73,
                                "viewability_in_percent": 2247.4,
                                "vcpm_in_advertiser_currency": 8383.69,
                                "cpcv_in_advertiser_currency": 4755.8,
                                "miaozhen_otp_in_percent": 4575.86,
                            },
                            "creative_ids": [
                                "<value 1>",
                                "<value 2>",
                            ],
                            "associated_bid_lists": [
                                {
                                    "bid_list_id": "<id>",
                                    "is_enabled": True,
                                    "is_default_for_dimension": False,
                                },
                            ],
                            "name": "<value>",
                            "channel": ttd_workflows.AdGroupChannel.DISPLAY,
                            "funnel_location": ttd_workflows.AdGroupFunnelLocation.AWARENESS,
                            "programmatic_guaranteed_private_contract_id": "<id>",
                        },
                        "advanced_input": {
                            "koa_optimization_settings": {
                                "are_future_koa_features_enabled": True,
                                "predictive_clearing_enabled": False,
                            },
                            "comscore_settings": {
                                "is_enabled": False,
                                "population_id": 559587,
                                "demographic_member_ids": [
                                    139340,
                                    129935,
                                ],
                                "mobile_demographic_member_ids": None,
                            },
                            "contract_targeting": {
                                "allow_open_market_bidding_when_targeting_contracts": True,
                            },
                            "dimensional_bidding_auto_optimization_settings": [
                                [
                                    ttd_workflows.DimensionalBiddingDimensions.HAS_AUDIENCE_REACH_PERCENTAGE_TIER_ID,
                                ],
                                [],
                            ],
                            "is_use_clicks_as_conversions_enabled": False,
                            "is_use_secondary_conversions_enabled": True,
                            "nielsen_tracking_attributes": {
                                "enhanced_reporting_option": ttd_workflows.EnhancedNielsenReportingOptions.NONE,
                                "gender": ttd_workflows.TargetingGender.FEMALE,
                                "start_age": ttd_workflows.TargetingStartAge.THIRTY_FIVE,
                                "end_age": ttd_workflows.TargetingEndAge.TWENTY_FOUR,
                                "countries": [
                                    "<value 1>",
                                    "<value 2>",
                                ],
                            },
                            "new_frequency_configs": None,
                            "flights": [
                                {
                                    "allocation_type": ttd_workflows.AllocationType.MAXIMUM,
                                    "budget_in_advertiser_currency": 4838.47,
                                    "budget_in_impressions": 420224,
                                    "daily_target_in_advertiser_currency": 1513.78,
                                    "daily_target_in_impressions": 735500,
                                },
                            ],
                        },
                    },
                ],
            },
        ],
        "validate_input_only": True,
        "callback_input": {
            "callback_url": "https://impeccable-pick.com/",
            "callback_headers": {
                "key": "<value>",
            },
        },
    })

    assert res.standard_job_submit_response is not None

    # Handle response
    print(res.standard_job_submit_response)

```

### Parameters

| Parameter                                                                                                             | Type                                                                                                                  | Required                                                                                                              | Description                                                                                                           |
| --------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                             | [models.CampaignBulkCreateWorkflowInputWithValidation](../../models/campaignbulkcreateworkflowinputwithvalidation.md) | :heavy_check_mark:                                                                                                    | The request object to use for the request.                                                                            |
| `retries`                                                                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                      | :heavy_minus_sign:                                                                                                    | Configuration to override the default retry behavior of the client.                                                   |

### Response

**[models.CreateCampaignsJobResponse](../../models/createcampaignsjobresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.ProblemDetailsError | 400, 403                   | application/json           |
| models.APIError            | 4XX, 5XX                   | \*/\*                      |

## update_campaigns_job

Only the fields provided in the request payload for each specific campaign will be updated.

### Example Usage

```python
import os
import ttd_workflows
from ttd_workflows import Workflows
from ttd_workflows.utils import parse_datetime


with Workflows(
    ttd_auth=os.getenv("WORKFLOWS_TTD_AUTH", ""),
) as workflows:

    res = workflows.campaign.update_campaigns_job(request={
        "input": [
            {
                "id": "<id>",
                "primary_input": {
                    "description": "hmph energetically yet surprisingly swift knight swear multicolored absent",
                    "time_zone": "America/Argentina/San_Juan",
                    "custom_cpa_click_weight": None,
                    "custom_cpa_viewthrough_weight": 8361.84,
                    "custom_cpa_type": ttd_workflows.CustomCPAType.PIXEL_WEIGHTING,
                    "impressions_only_budgeting_cpm": 2706.4,
                    "budget": {
                        "pacing_mode": ttd_workflows.CampaignPacingMode.PACE_AS_SOON_AS_POSSIBLE,
                        "budget_in_advertiser_currency": 2564.89,
                        "budget_in_impressions": 659726,
                        "daily_target_in_advertiser_currency": 6514.48,
                        "daily_target_in_impressions": 892097,
                    },
                    "end_date_in_utc": parse_datetime("2023-11-11T21:39:56.025Z"),
                    "seed_id": "<id>",
                    "campaign_conversion_reporting_columns": [
                        {
                            "tracking_tag_id": "<id>",
                            "include_in_custom_cpa": True,
                            "reporting_column_id": 809247,
                            "roas_config": {
                                "include_in_custom_roas": False,
                                "custom_roas_weight": None,
                                "custom_roas_click_weight": None,
                                "custom_roas_viewthrough_weight": 6784.9,
                            },
                            "weight": 2260.69,
                            "cross_device_attribution_model_id": "<id>",
                        },
                    ],
                    "name": "<value>",
                    "primary_channel": ttd_workflows.CampaignChannelType.NONE,
                    "primary_goal": {
                        "maximize_reach": True,
                        "maximize_ltv_incremental_reach": False,
                        "cpc_in_advertiser_currency": 3354.68,
                        "ctr_in_percent": 7716.49,
                        "nielsen_otp_in_percent": None,
                        "cpa_in_advertiser_currency": 381.7,
                        "return_on_ad_spend_percent": 8461.44,
                        "vcr_in_percent": 4170.61,
                        "viewability_in_percent": 5364.85,
                        "vcpm_in_advertiser_currency": 1107.08,
                        "cpcv_in_advertiser_currency": None,
                        "miaozhen_otp_in_percent": 4584.96,
                    },
                    "start_date_in_utc": parse_datetime("2023-01-13T23:06:05.083Z"),
                },
                "advanced_input": {
                    "flights": [
                        {
                            "start_date_inclusive_utc": parse_datetime("2023-08-14T13:47:31.198Z"),
                            "end_date_exclusive_utc": parse_datetime("2024-07-07T14:46:57.378Z"),
                            "budget_in_advertiser_currency": 1874.95,
                            "budget_in_impressions": 207094,
                            "daily_target_in_advertiser_currency": 7255.71,
                            "daily_target_in_impressions": 760981,
                        },
                    ],
                    "purchase_order_number": "<value>",
                },
            },
        ],
        "validate_input_only": True,
        "callback_input": {
            "callback_url": "https://soggy-apparatus.org/",
            "callback_headers": {
                "key": "<value>",
                "key1": "<value>",
                "key2": "<value>",
            },
        },
    })

    assert res.standard_job_submit_response is not None

    # Handle response
    print(res.standard_job_submit_response)

```

### Parameters

| Parameter                                                                                                             | Type                                                                                                                  | Required                                                                                                              | Description                                                                                                           |
| --------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                             | [models.CampaignBulkUpdateWorkflowInputWithValidation](../../models/campaignbulkupdateworkflowinputwithvalidation.md) | :heavy_check_mark:                                                                                                    | The request object to use for the request.                                                                            |
| `retries`                                                                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                      | :heavy_minus_sign:                                                                                                    | Configuration to override the default retry behavior of the client.                                                   |

### Response

**[models.UpdateCampaignsJobResponse](../../models/updatecampaignsjobresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.ProblemDetailsError | 400, 403                   | application/json           |
| models.APIError            | 4XX, 5XX                   | \*/\*                      |

## get_version

Get a campaign's version

### Example Usage

```python
import os
from ttd_workflows import Workflows


with Workflows(
    ttd_auth=os.getenv("WORKFLOWS_TTD_AUTH", ""),
) as workflows:

    res = workflows.campaign.get_version(id="<id>")

    assert res.campaign_version_workflow is not None

    # Handle response
    print(res.campaign_version_workflow)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GetCampaignVersionResponse](../../models/getcampaignversionresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.ProblemDetailsError | 400, 401, 403, 404         | application/json           |
| models.APIError            | 4XX, 5XX                   | \*/\*                      |