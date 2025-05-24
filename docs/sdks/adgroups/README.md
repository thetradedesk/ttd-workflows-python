# AdGroups
(*ad_groups*)

## Overview

### Available Operations

* [create](#create)
* [update](#update)
* [archive](#archive) - Archive a list of ad groups
* [bulk_create](#bulk_create) - Create a list of ad groups with required fields. `ValidateInputOnly` value should be the same for all ad groups.

## create

### Example Usage

```python
import os
import ttd_workflows
from ttd_workflows import Workflows


with Workflows(
    ttd_auth=os.getenv("WORKFLOWS_TTD_AUTH", ""),
) as workflows:

    res = workflows.ad_groups.create(request={
        "primary_input": {
            "is_enabled": True,
            "description": "into save rosy forsaken well",
            "budget": {
                "allocation_type": ttd_workflows.AllocationType.MINIMUM,
                "budget_in_advertiser_currency": 6554.77,
                "budget_in_impressions": 675757,
                "daily_target_in_advertiser_currency": 7451.45,
                "daily_target_in_impressions": 589518,
            },
            "base_bid_cpm_in_advertiser_currency": 1274.31,
            "max_bid_cpm_in_advertiser_currency": 9584.2,
            "audience_targeting": {
                "audience_id": "<id>",
                "audience_accelerator_exclusions_enabled": None,
                "audience_booster_enabled": False,
                "audience_excluder_enabled": True,
                "audience_predictor_enabled": False,
                "cross_device_vendor_list_for_audience": [
                    506873,
                ],
                "recency_exclusion_window_in_minutes": None,
                "target_trackable_users_enabled": True,
                "use_mc_id_as_primary": True,
            },
            "roi_goal": {
                "maximize_reach": False,
                "maximize_ltv_incremental_reach": False,
                "cpc_in_advertiser_currency": 259.31,
                "ctr_in_percent": 9665.19,
                "nielsen_otp_in_percent": 2917.69,
                "cpa_in_advertiser_currency": 9415.05,
                "return_on_ad_spend_percent": 5100.12,
                "vcr_in_percent": None,
                "viewability_in_percent": 5088.49,
                "vcpm_in_advertiser_currency": 1723.03,
                "cpcv_in_advertiser_currency": 9723.52,
                "miaozhen_otp_in_percent": 7814.66,
            },
            "creative_ids": [
                "<value 1>",
                "<value 2>",
            ],
            "associated_bid_lists": [
                {
                    "bid_list_id": "<id>",
                    "is_enabled": False,
                    "is_default_for_dimension": None,
                },
                {
                    "bid_list_id": "<id>",
                    "is_enabled": False,
                    "is_default_for_dimension": None,
                },
                {
                    "bid_list_id": "<id>",
                    "is_enabled": False,
                    "is_default_for_dimension": None,
                },
            ],
            "name": "<value>",
            "channel": ttd_workflows.AdGroupChannel.NATIVE_DISPLAY,
            "funnel_location": ttd_workflows.AdGroupFunnelLocation.CONSIDERATION,
            "programmatic_guaranteed_private_contract_id": None,
        },
        "campaign_id": "<id>",
        "advanced_input": {
            "koa_optimization_settings": {
                "are_future_koa_features_enabled": False,
                "predictive_clearing_enabled": None,
            },
            "comscore_settings": {
                "is_enabled": False,
                "population_id": 948705,
                "demographic_member_ids": [
                    229256,
                    508459,
                ],
                "mobile_demographic_member_ids": [
                    655581,
                ],
            },
            "contract_targeting": {
                "allow_open_market_bidding_when_targeting_contracts": False,
            },
            "dimensional_bidding_auto_optimization_settings": [
                [
                    ttd_workflows.DimensionalBiddingDimensions.HAS_CARRIER_ID,
                ],
                [],
                [
                    ttd_workflows.DimensionalBiddingDimensions.HAS_DISPLAY_VIEWABILITY_SCORE_RANGE,
                    ttd_workflows.DimensionalBiddingDimensions.HAS_MARKETPLACE_ID,
                ],
            ],
            "is_use_clicks_as_conversions_enabled": True,
            "is_use_secondary_conversions_enabled": True,
            "nielsen_tracking_attributes": {
                "enhanced_reporting_option": ttd_workflows.EnhancedNielsenReportingOptions.SITE,
                "gender": ttd_workflows.TargetingGender.FEMALE,
                "start_age": ttd_workflows.TargetingStartAge.TWENTY_ONE,
                "end_age": ttd_workflows.TargetingEndAge.THIRTY_NINE,
                "countries": [],
            },
            "new_frequency_configs": [
                {
                    "counter_name": "<value>",
                    "frequency_cap": 30631,
                    "frequency_goal": 746586,
                    "reset_interval_in_minutes": 170903,
                },
            ],
            "flights": None,
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

## update

### Example Usage

```python
import os
import ttd_workflows
from ttd_workflows import Workflows


with Workflows(
    ttd_auth=os.getenv("WORKFLOWS_TTD_AUTH", ""),
) as workflows:

    res = workflows.ad_groups.update(request={
        "id": "<id>",
        "primary_input": {
            "is_enabled": False,
            "description": "dimly hovercraft psst",
            "budget": {
                "allocation_type": ttd_workflows.AllocationType.MINIMUM,
                "budget_in_advertiser_currency": 6528.75,
                "budget_in_impressions": 826462,
                "daily_target_in_advertiser_currency": 7095.3,
                "daily_target_in_impressions": 456549,
            },
            "base_bid_cpm_in_advertiser_currency": 8869.73,
            "max_bid_cpm_in_advertiser_currency": 2014.55,
            "audience_targeting": {
                "audience_id": None,
                "audience_accelerator_exclusions_enabled": None,
                "audience_booster_enabled": False,
                "audience_excluder_enabled": True,
                "audience_predictor_enabled": True,
                "cross_device_vendor_list_for_audience": [
                    954278,
                    92417,
                    823921,
                ],
                "recency_exclusion_window_in_minutes": 977199,
                "target_trackable_users_enabled": False,
                "use_mc_id_as_primary": True,
            },
            "roi_goal": {
                "maximize_reach": False,
                "maximize_ltv_incremental_reach": True,
                "cpc_in_advertiser_currency": 7875.88,
                "ctr_in_percent": 2676.34,
                "nielsen_otp_in_percent": 7661.57,
                "cpa_in_advertiser_currency": 2230.31,
                "return_on_ad_spend_percent": 7618.53,
                "vcr_in_percent": 896.12,
                "viewability_in_percent": 4096.16,
                "vcpm_in_advertiser_currency": None,
                "cpcv_in_advertiser_currency": 2158.47,
                "miaozhen_otp_in_percent": 9383.83,
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
            "channel": ttd_workflows.AdGroupChannel.NATIVE_DISPLAY,
            "funnel_location": ttd_workflows.AdGroupFunnelLocation.NONE,
        },
        "advanced_input": {
            "koa_optimization_settings": {
                "are_future_koa_features_enabled": None,
                "predictive_clearing_enabled": True,
            },
            "comscore_settings": {
                "is_enabled": False,
                "population_id": 842024,
                "demographic_member_ids": [
                    987840,
                ],
                "mobile_demographic_member_ids": None,
            },
            "contract_targeting": {
                "allow_open_market_bidding_when_targeting_contracts": True,
            },
            "dimensional_bidding_auto_optimization_settings": [
                [
                    ttd_workflows.DimensionalBiddingDimensions.HAS_TTD_NATIVE_CONTEXT_TYPE_ID,
                ],
            ],
            "is_use_clicks_as_conversions_enabled": False,
            "is_use_secondary_conversions_enabled": False,
            "nielsen_tracking_attributes": {
                "enhanced_reporting_option": ttd_workflows.EnhancedNielsenReportingOptions.SITE,
                "gender": ttd_workflows.TargetingGender.BOTH,
                "start_age": ttd_workflows.TargetingStartAge.EIGHTEEN,
                "end_age": ttd_workflows.TargetingEndAge.SEVENTEEN,
                "countries": [],
            },
            "new_frequency_configs": [
                {
                    "counter_name": "<value>",
                    "frequency_cap": 914501,
                    "frequency_goal": None,
                    "reset_interval_in_minutes": 479592,
                },
            ],
            "flights": [
                {
                    "allocation_type": ttd_workflows.AllocationType.MAXIMUM,
                    "budget_in_advertiser_currency": 8445.33,
                    "budget_in_impressions": 752263,
                    "daily_target_in_advertiser_currency": 6432.51,
                    "daily_target_in_impressions": 660094,
                    "campaign_flight_id": 657893,
                },
                {
                    "allocation_type": ttd_workflows.AllocationType.MAXIMUM,
                    "budget_in_advertiser_currency": 8445.33,
                    "budget_in_impressions": 752263,
                    "daily_target_in_advertiser_currency": 6432.51,
                    "daily_target_in_impressions": 660094,
                    "campaign_flight_id": 657893,
                },
                {
                    "allocation_type": ttd_workflows.AllocationType.MAXIMUM,
                    "budget_in_advertiser_currency": 8445.33,
                    "budget_in_impressions": 752263,
                    "daily_target_in_advertiser_currency": 6432.51,
                    "daily_target_in_impressions": 660094,
                    "campaign_flight_id": 657893,
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

## archive

Archive a list of ad groups

### Example Usage

```python
import os
from ttd_workflows import Workflows


with Workflows(
    ttd_auth=os.getenv("WORKFLOWS_TTD_AUTH", ""),
) as workflows:

    res = workflows.ad_groups.archive(request_body=[
        "<value 1>",
        "<value 2>",
        "<value 3>",
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

## bulk_create

Create a list of ad groups with required fields. `ValidateInputOnly` value should be the same for all ad groups.

### Example Usage

```python
import os
import ttd_workflows
from ttd_workflows import Workflows


with Workflows(
    ttd_auth=os.getenv("WORKFLOWS_TTD_AUTH", ""),
) as workflows:

    res = workflows.ad_groups.bulk_create(request=[
        {
            "primary_input": {
                "is_enabled": False,
                "description": "shrill toward fully sniveling gah after",
                "budget": {
                    "allocation_type": ttd_workflows.AllocationType.FIXED,
                    "budget_in_advertiser_currency": 1220.65,
                    "budget_in_impressions": None,
                    "daily_target_in_advertiser_currency": 575.45,
                    "daily_target_in_impressions": None,
                },
                "base_bid_cpm_in_advertiser_currency": 2152.93,
                "max_bid_cpm_in_advertiser_currency": 1303.66,
                "audience_targeting": {
                    "audience_id": "<id>",
                    "audience_accelerator_exclusions_enabled": None,
                    "audience_booster_enabled": False,
                    "audience_excluder_enabled": False,
                    "audience_predictor_enabled": False,
                    "cross_device_vendor_list_for_audience": [
                        804001,
                        437853,
                    ],
                    "recency_exclusion_window_in_minutes": 11169,
                    "target_trackable_users_enabled": False,
                    "use_mc_id_as_primary": True,
                },
                "roi_goal": {
                    "maximize_reach": False,
                    "maximize_ltv_incremental_reach": None,
                    "cpc_in_advertiser_currency": 9818.14,
                    "ctr_in_percent": 5994.66,
                    "nielsen_otp_in_percent": 9542.27,
                    "cpa_in_advertiser_currency": 6940.2,
                    "return_on_ad_spend_percent": 738.42,
                    "vcr_in_percent": 2183.12,
                    "viewability_in_percent": None,
                    "vcpm_in_advertiser_currency": 6424.17,
                    "cpcv_in_advertiser_currency": 3444,
                    "miaozhen_otp_in_percent": 7849.59,
                },
                "creative_ids": [
                    "<value 1>",
                    "<value 2>",
                    "<value 3>",
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
                        "is_default_for_dimension": True,
                    },
                    {
                        "bid_list_id": "<id>",
                        "is_enabled": True,
                        "is_default_for_dimension": True,
                    },
                ],
                "name": "<value>",
                "channel": ttd_workflows.AdGroupChannel.VIDEO,
                "funnel_location": ttd_workflows.AdGroupFunnelLocation.AWARENESS,
                "programmatic_guaranteed_private_contract_id": "<id>",
            },
            "campaign_id": "<id>",
            "advanced_input": {
                "koa_optimization_settings": {
                    "are_future_koa_features_enabled": True,
                    "predictive_clearing_enabled": False,
                },
                "comscore_settings": {
                    "is_enabled": False,
                    "population_id": 604624,
                    "demographic_member_ids": [
                        780904,
                        83143,
                    ],
                    "mobile_demographic_member_ids": [
                        922102,
                    ],
                },
                "contract_targeting": {
                    "allow_open_market_bidding_when_targeting_contracts": False,
                },
                "dimensional_bidding_auto_optimization_settings": [
                    [
                        ttd_workflows.DimensionalBiddingDimensions.HAS_UNIVERSAL_CATEGORY_TAXONOMY_ID,
                        ttd_workflows.DimensionalBiddingDimensions.HAS_VIDEO_QUALITY_ID,
                    ],
                    [
                        ttd_workflows.DimensionalBiddingDimensions.HAS_PRIVATE_CONTRACT_ID,
                        ttd_workflows.DimensionalBiddingDimensions.HAS_INTEGRAL_PAGE_QUALITY_CATEGORY_ID,
                        ttd_workflows.DimensionalBiddingDimensions.HAS_MARKETPLACE_ID,
                    ],
                ],
                "is_use_clicks_as_conversions_enabled": False,
                "is_use_secondary_conversions_enabled": True,
                "nielsen_tracking_attributes": {
                    "enhanced_reporting_option": ttd_workflows.EnhancedNielsenReportingOptions.SITE,
                    "gender": ttd_workflows.TargetingGender.FEMALE,
                    "start_age": ttd_workflows.TargetingStartAge.TWO,
                    "end_age": ttd_workflows.TargetingEndAge.FORTY_NINE,
                    "countries": None,
                },
                "new_frequency_configs": [
                    {
                        "counter_name": None,
                        "frequency_cap": 22628,
                        "frequency_goal": None,
                        "reset_interval_in_minutes": 999065,
                    },
                    {
                        "counter_name": None,
                        "frequency_cap": 22628,
                        "frequency_goal": None,
                        "reset_interval_in_minutes": 999065,
                    },
                    {
                        "counter_name": None,
                        "frequency_cap": 22628,
                        "frequency_goal": None,
                        "reset_interval_in_minutes": 999065,
                    },
                ],
                "flights": [
                    {
                        "allocation_type": ttd_workflows.AllocationType.MAXIMUM,
                        "budget_in_advertiser_currency": 2901.68,
                        "budget_in_impressions": None,
                        "daily_target_in_advertiser_currency": 3735.15,
                        "daily_target_in_impressions": 609234,
                        "campaign_flight_id": 563931,
                    },
                    {
                        "allocation_type": ttd_workflows.AllocationType.MAXIMUM,
                        "budget_in_advertiser_currency": 2901.68,
                        "budget_in_impressions": None,
                        "daily_target_in_advertiser_currency": 3735.15,
                        "daily_target_in_impressions": 609234,
                        "campaign_flight_id": 563931,
                    },
                ],
            },
        },
        {
            "primary_input": {
                "is_enabled": False,
                "description": "shrill toward fully sniveling gah after",
                "budget": {
                    "allocation_type": ttd_workflows.AllocationType.FIXED,
                    "budget_in_advertiser_currency": 1220.65,
                    "budget_in_impressions": None,
                    "daily_target_in_advertiser_currency": 575.45,
                    "daily_target_in_impressions": None,
                },
                "base_bid_cpm_in_advertiser_currency": 2152.93,
                "max_bid_cpm_in_advertiser_currency": 1303.66,
                "audience_targeting": {
                    "audience_id": "<id>",
                    "audience_accelerator_exclusions_enabled": None,
                    "audience_booster_enabled": False,
                    "audience_excluder_enabled": False,
                    "audience_predictor_enabled": False,
                    "cross_device_vendor_list_for_audience": [
                        804001,
                        437853,
                    ],
                    "recency_exclusion_window_in_minutes": 11169,
                    "target_trackable_users_enabled": False,
                    "use_mc_id_as_primary": True,
                },
                "roi_goal": {
                    "maximize_reach": False,
                    "maximize_ltv_incremental_reach": None,
                    "cpc_in_advertiser_currency": 9818.14,
                    "ctr_in_percent": 5994.66,
                    "nielsen_otp_in_percent": 9542.27,
                    "cpa_in_advertiser_currency": 6940.2,
                    "return_on_ad_spend_percent": 738.42,
                    "vcr_in_percent": 2183.12,
                    "viewability_in_percent": None,
                    "vcpm_in_advertiser_currency": 6424.17,
                    "cpcv_in_advertiser_currency": 3444,
                    "miaozhen_otp_in_percent": 7849.59,
                },
                "creative_ids": [
                    "<value 1>",
                    "<value 2>",
                    "<value 3>",
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
                        "is_default_for_dimension": True,
                    },
                    {
                        "bid_list_id": "<id>",
                        "is_enabled": True,
                        "is_default_for_dimension": True,
                    },
                ],
                "name": "<value>",
                "channel": ttd_workflows.AdGroupChannel.VIDEO,
                "funnel_location": ttd_workflows.AdGroupFunnelLocation.AWARENESS,
                "programmatic_guaranteed_private_contract_id": "<id>",
            },
            "campaign_id": "<id>",
            "advanced_input": {
                "koa_optimization_settings": {
                    "are_future_koa_features_enabled": True,
                    "predictive_clearing_enabled": False,
                },
                "comscore_settings": {
                    "is_enabled": False,
                    "population_id": 604624,
                    "demographic_member_ids": [
                        780904,
                        83143,
                    ],
                    "mobile_demographic_member_ids": [
                        922102,
                    ],
                },
                "contract_targeting": {
                    "allow_open_market_bidding_when_targeting_contracts": False,
                },
                "dimensional_bidding_auto_optimization_settings": [
                    [
                        ttd_workflows.DimensionalBiddingDimensions.HAS_UNIVERSAL_CATEGORY_TAXONOMY_ID,
                        ttd_workflows.DimensionalBiddingDimensions.HAS_VIDEO_QUALITY_ID,
                    ],
                    [
                        ttd_workflows.DimensionalBiddingDimensions.HAS_PRIVATE_CONTRACT_ID,
                        ttd_workflows.DimensionalBiddingDimensions.HAS_INTEGRAL_PAGE_QUALITY_CATEGORY_ID,
                        ttd_workflows.DimensionalBiddingDimensions.HAS_MARKETPLACE_ID,
                    ],
                ],
                "is_use_clicks_as_conversions_enabled": False,
                "is_use_secondary_conversions_enabled": True,
                "nielsen_tracking_attributes": {
                    "enhanced_reporting_option": ttd_workflows.EnhancedNielsenReportingOptions.SITE,
                    "gender": ttd_workflows.TargetingGender.FEMALE,
                    "start_age": ttd_workflows.TargetingStartAge.TWO,
                    "end_age": ttd_workflows.TargetingEndAge.FORTY_NINE,
                    "countries": None,
                },
                "new_frequency_configs": [
                    {
                        "counter_name": None,
                        "frequency_cap": 22628,
                        "frequency_goal": None,
                        "reset_interval_in_minutes": 999065,
                    },
                    {
                        "counter_name": None,
                        "frequency_cap": 22628,
                        "frequency_goal": None,
                        "reset_interval_in_minutes": 999065,
                    },
                    {
                        "counter_name": None,
                        "frequency_cap": 22628,
                        "frequency_goal": None,
                        "reset_interval_in_minutes": 999065,
                    },
                ],
                "flights": [
                    {
                        "allocation_type": ttd_workflows.AllocationType.MAXIMUM,
                        "budget_in_advertiser_currency": 2901.68,
                        "budget_in_impressions": None,
                        "daily_target_in_advertiser_currency": 3735.15,
                        "daily_target_in_impressions": 609234,
                        "campaign_flight_id": 563931,
                    },
                    {
                        "allocation_type": ttd_workflows.AllocationType.MAXIMUM,
                        "budget_in_advertiser_currency": 2901.68,
                        "budget_in_impressions": None,
                        "daily_target_in_advertiser_currency": 3735.15,
                        "daily_target_in_impressions": 609234,
                        "campaign_flight_id": 563931,
                    },
                ],
            },
        },
        {
            "primary_input": {
                "is_enabled": False,
                "description": "shrill toward fully sniveling gah after",
                "budget": {
                    "allocation_type": ttd_workflows.AllocationType.FIXED,
                    "budget_in_advertiser_currency": 1220.65,
                    "budget_in_impressions": None,
                    "daily_target_in_advertiser_currency": 575.45,
                    "daily_target_in_impressions": None,
                },
                "base_bid_cpm_in_advertiser_currency": 2152.93,
                "max_bid_cpm_in_advertiser_currency": 1303.66,
                "audience_targeting": {
                    "audience_id": "<id>",
                    "audience_accelerator_exclusions_enabled": None,
                    "audience_booster_enabled": False,
                    "audience_excluder_enabled": False,
                    "audience_predictor_enabled": False,
                    "cross_device_vendor_list_for_audience": [
                        804001,
                        437853,
                    ],
                    "recency_exclusion_window_in_minutes": 11169,
                    "target_trackable_users_enabled": False,
                    "use_mc_id_as_primary": True,
                },
                "roi_goal": {
                    "maximize_reach": False,
                    "maximize_ltv_incremental_reach": None,
                    "cpc_in_advertiser_currency": 9818.14,
                    "ctr_in_percent": 5994.66,
                    "nielsen_otp_in_percent": 9542.27,
                    "cpa_in_advertiser_currency": 6940.2,
                    "return_on_ad_spend_percent": 738.42,
                    "vcr_in_percent": 2183.12,
                    "viewability_in_percent": None,
                    "vcpm_in_advertiser_currency": 6424.17,
                    "cpcv_in_advertiser_currency": 3444,
                    "miaozhen_otp_in_percent": 7849.59,
                },
                "creative_ids": [
                    "<value 1>",
                    "<value 2>",
                    "<value 3>",
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
                        "is_default_for_dimension": True,
                    },
                    {
                        "bid_list_id": "<id>",
                        "is_enabled": True,
                        "is_default_for_dimension": True,
                    },
                ],
                "name": "<value>",
                "channel": ttd_workflows.AdGroupChannel.VIDEO,
                "funnel_location": ttd_workflows.AdGroupFunnelLocation.AWARENESS,
                "programmatic_guaranteed_private_contract_id": "<id>",
            },
            "campaign_id": "<id>",
            "advanced_input": {
                "koa_optimization_settings": {
                    "are_future_koa_features_enabled": True,
                    "predictive_clearing_enabled": False,
                },
                "comscore_settings": {
                    "is_enabled": False,
                    "population_id": 604624,
                    "demographic_member_ids": [
                        780904,
                        83143,
                    ],
                    "mobile_demographic_member_ids": [
                        922102,
                    ],
                },
                "contract_targeting": {
                    "allow_open_market_bidding_when_targeting_contracts": False,
                },
                "dimensional_bidding_auto_optimization_settings": [
                    [
                        ttd_workflows.DimensionalBiddingDimensions.HAS_UNIVERSAL_CATEGORY_TAXONOMY_ID,
                        ttd_workflows.DimensionalBiddingDimensions.HAS_VIDEO_QUALITY_ID,
                    ],
                    [
                        ttd_workflows.DimensionalBiddingDimensions.HAS_PRIVATE_CONTRACT_ID,
                        ttd_workflows.DimensionalBiddingDimensions.HAS_INTEGRAL_PAGE_QUALITY_CATEGORY_ID,
                        ttd_workflows.DimensionalBiddingDimensions.HAS_MARKETPLACE_ID,
                    ],
                ],
                "is_use_clicks_as_conversions_enabled": False,
                "is_use_secondary_conversions_enabled": True,
                "nielsen_tracking_attributes": {
                    "enhanced_reporting_option": ttd_workflows.EnhancedNielsenReportingOptions.SITE,
                    "gender": ttd_workflows.TargetingGender.FEMALE,
                    "start_age": ttd_workflows.TargetingStartAge.TWO,
                    "end_age": ttd_workflows.TargetingEndAge.FORTY_NINE,
                    "countries": None,
                },
                "new_frequency_configs": [
                    {
                        "counter_name": None,
                        "frequency_cap": 22628,
                        "frequency_goal": None,
                        "reset_interval_in_minutes": 999065,
                    },
                    {
                        "counter_name": None,
                        "frequency_cap": 22628,
                        "frequency_goal": None,
                        "reset_interval_in_minutes": 999065,
                    },
                    {
                        "counter_name": None,
                        "frequency_cap": 22628,
                        "frequency_goal": None,
                        "reset_interval_in_minutes": 999065,
                    },
                ],
                "flights": [
                    {
                        "allocation_type": ttd_workflows.AllocationType.MAXIMUM,
                        "budget_in_advertiser_currency": 2901.68,
                        "budget_in_impressions": None,
                        "daily_target_in_advertiser_currency": 3735.15,
                        "daily_target_in_impressions": 609234,
                        "campaign_flight_id": 563931,
                    },
                    {
                        "allocation_type": ttd_workflows.AllocationType.MAXIMUM,
                        "budget_in_advertiser_currency": 2901.68,
                        "budget_in_impressions": None,
                        "daily_target_in_advertiser_currency": 3735.15,
                        "daily_target_in_impressions": 609234,
                        "campaign_flight_id": 563931,
                    },
                ],
            },
        },
    ])

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [List[models.AdGroupCreateWorkflowInput]](../../models/.md)         | :heavy_check_mark:                                                  | The request object to use for the request.                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.BulkJobSubmitResponse](../../models/bulkjobsubmitresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.ProblemDetailsError | 400, 403                   | application/json           |
| models.APIError            | 4XX, 5XX                   | \*/\*                      |