# AdGroup
(*ad_group*)

## Overview

### Available Operations

* [post_typebasedjob_adgroup_bulk](#post_typebasedjob_adgroup_bulk) - Create multiple new ad groups with required fields
* [patch_typebasedjob_adgroup_bulk](#patch_typebasedjob_adgroup_bulk) - Update multiple ad groups with specified fields

## post_typebasedjob_adgroup_bulk

Create multiple new ad groups with required fields

### Example Usage

```python
import os
from ttd_workflows import Workflows


with Workflows(
    ttd_auth=os.getenv("WORKFLOWS_TTD_AUTH", ""),
) as workflows:

    res = workflows.ad_group.post_typebasedjob_adgroup_bulk(request={
        "input": [],
        "validate_input_only": True,
        "callback_input": {
            "callback_url": "https://unhealthy-toothbrush.biz/",
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

| Parameter                                                                                                           | Type                                                                                                                | Required                                                                                                            | Description                                                                                                         |
| ------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                           | [models.AdGroupBulkCreateWorkflowInputWithValidation](../../models/adgroupbulkcreateworkflowinputwithvalidation.md) | :heavy_check_mark:                                                                                                  | The request object to use for the request.                                                                          |
| `retries`                                                                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                    | :heavy_minus_sign:                                                                                                  | Configuration to override the default retry behavior of the client.                                                 |

### Response

**[models.TypeBasedJobSubmitResponse](../../models/typebasedjobsubmitresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.ProblemDetailsError | 400, 403                   | application/json           |
| models.APIError            | 4XX, 5XX                   | \*/\*                      |

## patch_typebasedjob_adgroup_bulk

Only the fields provided in the request payload for each specific ad group will be updated.

### Example Usage

```python
import os
import ttd_workflows
from ttd_workflows import Workflows


with Workflows(
    ttd_auth=os.getenv("WORKFLOWS_TTD_AUTH", ""),
) as workflows:

    res = workflows.ad_group.patch_typebasedjob_adgroup_bulk(request={
        "input": [
            {
                "id": "<id>",
                "primary_input": {
                    "is_enabled": True,
                    "description": None,
                    "budget": {
                        "allocation_type": ttd_workflows.AllocationType.MINIMUM,
                        "budget_in_advertiser_currency": 4365.6,
                        "budget_in_impressions": 797262,
                        "daily_target_in_advertiser_currency": 2847.63,
                        "daily_target_in_impressions": None,
                    },
                    "base_bid_cpm_in_advertiser_currency": 1985.29,
                    "max_bid_cpm_in_advertiser_currency": 4757.87,
                    "audience_targeting": {
                        "audience_id": "<id>",
                        "audience_accelerator_exclusions_enabled": False,
                        "audience_booster_enabled": False,
                        "audience_excluder_enabled": False,
                        "audience_predictor_enabled": False,
                        "cross_device_vendor_list_for_audience": [
                            66244,
                            540186,
                            225330,
                        ],
                        "recency_exclusion_window_in_minutes": 524436,
                        "target_trackable_users_enabled": False,
                        "use_mc_id_as_primary": False,
                    },
                    "roi_goal": {
                        "maximize_reach": True,
                        "maximize_ltv_incremental_reach": True,
                        "cpc_in_advertiser_currency": 4773.66,
                        "ctr_in_percent": 8842.31,
                        "nielsen_otp_in_percent": None,
                        "cpa_in_advertiser_currency": 1316.63,
                        "return_on_ad_spend_percent": 3656.49,
                        "vcr_in_percent": 8557.42,
                        "viewability_in_percent": 7299.96,
                        "vcpm_in_advertiser_currency": 7239.85,
                        "cpcv_in_advertiser_currency": None,
                        "miaozhen_otp_in_percent": 2809.53,
                    },
                    "creative_ids": None,
                    "associated_bid_lists": [
                        {
                            "bid_list_id": "<id>",
                            "is_enabled": True,
                            "is_default_for_dimension": True,
                        },
                    ],
                    "name": "<value>",
                    "channel": ttd_workflows.AdGroupChannel.NATIVE_DISPLAY,
                    "funnel_location": ttd_workflows.AdGroupFunnelLocation.NONE,
                },
                "advanced_input": {
                    "koa_optimization_settings": {
                        "are_future_koa_features_enabled": True,
                        "predictive_clearing_enabled": True,
                    },
                    "comscore_settings": {
                        "is_enabled": False,
                        "population_id": 809148,
                        "demographic_member_ids": [
                            532747,
                            484388,
                        ],
                        "mobile_demographic_member_ids": [
                            529979,
                            812676,
                        ],
                    },
                    "contract_targeting": {
                        "allow_open_market_bidding_when_targeting_contracts": True,
                    },
                    "dimensional_bidding_auto_optimization_settings": [
                        [
                            ttd_workflows.DimensionalBiddingDimensions.HAS_VIDEO_MUTED_STATE_ID,
                        ],
                        [],
                    ],
                    "is_use_clicks_as_conversions_enabled": True,
                    "is_use_secondary_conversions_enabled": False,
                    "nielsen_tracking_attributes": {
                        "enhanced_reporting_option": ttd_workflows.EnhancedNielsenReportingOptions.NONE,
                        "gender": ttd_workflows.TargetingGender.BOTH,
                        "start_age": ttd_workflows.TargetingStartAge.SIXTY_FIVE,
                        "end_age": ttd_workflows.TargetingEndAge.TWENTY,
                        "countries": [
                            "<value 1>",
                        ],
                    },
                    "new_frequency_configs": None,
                    "flights": [
                        {
                            "allocation_type": ttd_workflows.AllocationType.MINIMUM,
                            "budget_in_advertiser_currency": 3571.65,
                            "budget_in_impressions": None,
                            "daily_target_in_advertiser_currency": 9076.57,
                            "daily_target_in_impressions": 864528,
                            "campaign_flight_id": 284595,
                        },
                    ],
                },
            },
        ],
        "validate_input_only": False,
        "callback_input": {
            "callback_url": "https://funny-prohibition.org/",
            "callback_headers": {
                "key": "<value>",
            },
        },
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                           | Type                                                                                                                | Required                                                                                                            | Description                                                                                                         |
| ------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                           | [models.AdGroupBulkUpdateWorkflowInputWithValidation](../../models/adgroupbulkupdateworkflowinputwithvalidation.md) | :heavy_check_mark:                                                                                                  | The request object to use for the request.                                                                          |
| `retries`                                                                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                    | :heavy_minus_sign:                                                                                                  | Configuration to override the default retry behavior of the client.                                                 |

### Response

**[models.TypeBasedJobSubmitResponse](../../models/typebasedjobsubmitresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.ProblemDetailsError | 400, 403                   | application/json           |
| models.APIError            | 4XX, 5XX                   | \*/\*                      |