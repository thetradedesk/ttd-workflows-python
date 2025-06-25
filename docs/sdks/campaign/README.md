# Campaign
(*campaign*)

## Overview

### Available Operations

* [create](#create) - Create a new campaign with required fields
* [post_typebasedjob_campaign_bulk](#post_typebasedjob_campaign_bulk) - Create multiple new campaigns with required fields
* [patch_typebasedjob_campaign_bulk](#patch_typebasedjob_campaign_bulk) - Update multiple campaigns with specified fields
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

| Parameter                                                                                                     | Type                                                                                                          | Required                                                                                                      | Description                                                                                                   |
| ------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                     | [models.CampaignCreateWorkflowInputWithValidation](../../models/campaigncreateworkflowinputwithvalidation.md) | :heavy_check_mark:                                                                                            | The request object to use for the request.                                                                    |
| `retries`                                                                                                     | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                              | :heavy_minus_sign:                                                                                            | Configuration to override the default retry behavior of the client.                                           |

### Response

**[models.CampaignPayload](../../models/campaignpayload.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.ProblemDetailsError | 400, 403                   | application/json           |
| models.APIError            | 4XX, 5XX                   | \*/\*                      |

## post_typebasedjob_campaign_bulk

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

    res = workflows.campaign.post_typebasedjob_campaign_bulk(request={
        "input": [
            {
                "primary_input": {
                    "description": "terribly someplace deflect",
                    "time_zone": "America/Miquelon",
                    "custom_cpa_click_weight": 779.21,
                    "custom_cpa_viewthrough_weight": 1198.23,
                    "custom_cpa_type": ttd_workflows.CustomCPAType.PIXEL_WEIGHTING,
                    "impressions_only_budgeting_cpm": 5375.63,
                    "budget": {
                        "pacing_mode": ttd_workflows.CampaignPacingMode.PACE_AHEAD,
                        "budget_in_advertiser_currency": 4629.97,
                        "budget_in_impressions": 808130,
                        "daily_target_in_advertiser_currency": 4067.56,
                        "daily_target_in_impressions": 243576,
                    },
                    "end_date_in_utc": parse_datetime("2025-12-15T08:27:00.961Z"),
                    "seed_id": None,
                    "campaign_conversion_reporting_columns": [
                        {
                            "tracking_tag_id": "<id>",
                            "include_in_custom_cpa": True,
                            "reporting_column_id": 265596,
                            "roas_config": {
                                "include_in_custom_roas": False,
                                "custom_roas_weight": 1659.76,
                                "custom_roas_click_weight": 7838.93,
                                "custom_roas_viewthrough_weight": 7814.81,
                            },
                            "weight": 9286.55,
                            "cross_device_attribution_model_id": "<id>",
                        },
                    ],
                    "advertiser_id": "<id>",
                    "name": "<value>",
                    "primary_channel": ttd_workflows.CampaignChannelType.NONE,
                    "primary_goal": {
                        "maximize_reach": None,
                        "maximize_ltv_incremental_reach": True,
                        "cpc_in_advertiser_currency": 7342.9,
                        "ctr_in_percent": 4157.33,
                        "nielsen_otp_in_percent": 1508.37,
                        "cpa_in_advertiser_currency": 5200.65,
                        "return_on_ad_spend_percent": 2714.64,
                        "vcr_in_percent": 4408.66,
                        "viewability_in_percent": 4646.22,
                        "vcpm_in_advertiser_currency": 5303.62,
                        "cpcv_in_advertiser_currency": 7628.07,
                        "miaozhen_otp_in_percent": 2965.51,
                    },
                    "start_date_in_utc": None,
                },
                "advanced_input": {
                    "flights": [
                        {
                            "start_date_inclusive_utc": parse_datetime("2023-05-29T15:44:07.749Z"),
                            "end_date_exclusive_utc": parse_datetime("2024-01-24T07:42:34.281Z"),
                            "budget_in_advertiser_currency": 9558.91,
                            "budget_in_impressions": 73147,
                            "daily_target_in_advertiser_currency": 4332.71,
                            "daily_target_in_impressions": 768928,
                        },
                    ],
                    "purchase_order_number": "<value>",
                },
                "ad_groups": [
                    {
                        "primary_input": {
                            "is_enabled": True,
                            "description": None,
                            "budget": {
                                "allocation_type": ttd_workflows.AllocationType.MAXIMUM,
                                "budget_in_advertiser_currency": 6785.04,
                                "budget_in_impressions": 835320,
                                "daily_target_in_advertiser_currency": 4763.51,
                                "daily_target_in_impressions": 267343,
                            },
                            "base_bid_cpm_in_advertiser_currency": 2929.53,
                            "max_bid_cpm_in_advertiser_currency": 3306.27,
                            "audience_targeting": {
                                "audience_id": "<id>",
                                "audience_accelerator_exclusions_enabled": True,
                                "audience_booster_enabled": True,
                                "audience_excluder_enabled": False,
                                "audience_predictor_enabled": False,
                                "cross_device_vendor_list_for_audience": [
                                    745991,
                                    421485,
                                    187325,
                                ],
                                "recency_exclusion_window_in_minutes": 651644,
                                "target_trackable_users_enabled": None,
                                "use_mc_id_as_primary": True,
                            },
                            "roi_goal": {
                                "maximize_reach": False,
                                "maximize_ltv_incremental_reach": False,
                                "cpc_in_advertiser_currency": 3342.73,
                                "ctr_in_percent": 8498.13,
                                "nielsen_otp_in_percent": None,
                                "cpa_in_advertiser_currency": 4541.91,
                                "return_on_ad_spend_percent": 1951.31,
                                "vcr_in_percent": 4890.16,
                                "viewability_in_percent": 7796.33,
                                "vcpm_in_advertiser_currency": 9686.38,
                                "cpcv_in_advertiser_currency": 5397.14,
                                "miaozhen_otp_in_percent": 6837.51,
                            },
                            "creative_ids": None,
                            "associated_bid_lists": [
                                {
                                    "bid_list_id": "<id>",
                                    "is_enabled": False,
                                    "is_default_for_dimension": None,
                                },
                            ],
                            "name": "<value>",
                            "channel": ttd_workflows.AdGroupChannel.AUDIO,
                            "funnel_location": ttd_workflows.AdGroupFunnelLocation.AWARENESS,
                            "programmatic_guaranteed_private_contract_id": "<id>",
                        },
                        "advanced_input": {
                            "koa_optimization_settings": {
                                "are_future_koa_features_enabled": None,
                                "predictive_clearing_enabled": True,
                            },
                            "comscore_settings": {
                                "is_enabled": False,
                                "population_id": 392396,
                                "demographic_member_ids": [
                                    815546,
                                    208096,
                                    412653,
                                ],
                                "mobile_demographic_member_ids": None,
                            },
                            "contract_targeting": {
                                "allow_open_market_bidding_when_targeting_contracts": True,
                            },
                            "dimensional_bidding_auto_optimization_settings": [
                                [
                                    ttd_workflows.DimensionalBiddingDimensions.HAS_FREQUENCY_V2_ADJUSTMENT_ID,
                                ],
                            ],
                            "is_use_clicks_as_conversions_enabled": False,
                            "is_use_secondary_conversions_enabled": True,
                            "nielsen_tracking_attributes": {
                                "enhanced_reporting_option": ttd_workflows.EnhancedNielsenReportingOptions.SITE,
                                "gender": ttd_workflows.TargetingGender.MALE,
                                "start_age": ttd_workflows.TargetingStartAge.THIRTY,
                                "end_age": ttd_workflows.TargetingEndAge.TWENTY_NINE,
                                "countries": [
                                    "<value 1>",
                                    "<value 2>",
                                ],
                            },
                            "new_frequency_configs": [
                                {
                                    "counter_name": "<value>",
                                    "frequency_cap": 26304,
                                    "frequency_goal": 197135,
                                    "reset_interval_in_minutes": 993919,
                                },
                            ],
                            "flights": [
                                {
                                    "allocation_type": ttd_workflows.AllocationType.FIXED,
                                    "budget_in_advertiser_currency": 1254.25,
                                    "budget_in_impressions": 426962,
                                    "daily_target_in_advertiser_currency": 3971.88,
                                    "daily_target_in_impressions": 746686,
                                },
                            ],
                        },
                    },
                ],
            },
        ],
        "validate_input_only": False,
        "callback_input": {
            "callback_url": "https://neat-inspection.biz/",
            "callback_headers": {
                "key": "<value>",
                "key1": "<value>",
            },
        },
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                             | Type                                                                                                                  | Required                                                                                                              | Description                                                                                                           |
| --------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                             | [models.CampaignBulkCreateWorkflowInputWithValidation](../../models/campaignbulkcreateworkflowinputwithvalidation.md) | :heavy_check_mark:                                                                                                    | The request object to use for the request.                                                                            |
| `retries`                                                                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                      | :heavy_minus_sign:                                                                                                    | Configuration to override the default retry behavior of the client.                                                   |

### Response

**[models.TypeBasedJobSubmitResponse](../../models/typebasedjobsubmitresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.ProblemDetailsError | 400, 403                   | application/json           |
| models.APIError            | 4XX, 5XX                   | \*/\*                      |

## patch_typebasedjob_campaign_bulk

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

    res = workflows.campaign.patch_typebasedjob_campaign_bulk(request={
        "input": [
            {
                "id": "<id>",
                "primary_input": {
                    "description": "dreamily oxygenate swine instead cannon indeed concerning clamp queasily",
                    "time_zone": "America/North_Dakota/New_Salem",
                    "custom_cpa_click_weight": 2069.39,
                    "custom_cpa_viewthrough_weight": 6500.84,
                    "custom_cpa_type": ttd_workflows.CustomCPAType.CLICK_VIEWTHROUGH_WEIGHTING,
                    "impressions_only_budgeting_cpm": 6512.22,
                    "budget": {
                        "pacing_mode": ttd_workflows.CampaignPacingMode.PACE_EVENLY,
                        "budget_in_advertiser_currency": 4239.6,
                        "budget_in_impressions": 22149,
                        "daily_target_in_advertiser_currency": 2521.81,
                        "daily_target_in_impressions": 843774,
                    },
                    "end_date_in_utc": parse_datetime("2024-08-25T01:07:39.538Z"),
                    "seed_id": "<id>",
                    "campaign_conversion_reporting_columns": None,
                    "name": None,
                    "primary_channel": ttd_workflows.CampaignChannelType.NATIVE_DISPLAY,
                    "primary_goal": {
                        "maximize_reach": False,
                        "maximize_ltv_incremental_reach": False,
                        "cpc_in_advertiser_currency": 7023.26,
                        "ctr_in_percent": None,
                        "nielsen_otp_in_percent": 7851.49,
                        "cpa_in_advertiser_currency": None,
                        "return_on_ad_spend_percent": 8228.66,
                        "vcr_in_percent": 1734.42,
                        "viewability_in_percent": 9398.46,
                        "vcpm_in_advertiser_currency": 3476.53,
                        "cpcv_in_advertiser_currency": 6537.87,
                        "miaozhen_otp_in_percent": 4667.23,
                    },
                    "start_date_in_utc": None,
                },
                "advanced_input": {
                    "flights": [
                        {
                            "start_date_inclusive_utc": parse_datetime("2025-05-03T18:31:10.973Z"),
                            "end_date_exclusive_utc": parse_datetime("2023-02-05T18:37:52.192Z"),
                            "budget_in_advertiser_currency": 1936.69,
                            "budget_in_impressions": 216227,
                            "daily_target_in_advertiser_currency": 3384.57,
                            "daily_target_in_impressions": 677379,
                        },
                    ],
                    "purchase_order_number": "<value>",
                },
            },
        ],
        "validate_input_only": False,
        "callback_input": {
            "callback_url": "https://hollow-rosemary.biz/",
            "callback_headers": {
                "key": "<value>",
                "key1": "<value>",
                "key2": "<value>",
            },
        },
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                             | Type                                                                                                                  | Required                                                                                                              | Description                                                                                                           |
| --------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                             | [models.CampaignBulkUpdateWorkflowInputWithValidation](../../models/campaignbulkupdateworkflowinputwithvalidation.md) | :heavy_check_mark:                                                                                                    | The request object to use for the request.                                                                            |
| `retries`                                                                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                      | :heavy_minus_sign:                                                                                                    | Configuration to override the default retry behavior of the client.                                                   |

### Response

**[models.TypeBasedJobSubmitResponse](../../models/typebasedjobsubmitresponse.md)**

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