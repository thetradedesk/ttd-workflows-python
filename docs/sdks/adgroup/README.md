# AdGroup
(*ad_group*)

## Overview

### Available Operations

* [patch_adgroup_bulk](#patch_adgroup_bulk) - Create a list of ad groups with required fields. `ValidateInputOnly` value should be the same for all ad groups.

## patch_adgroup_bulk

Create a list of ad groups with required fields. `ValidateInputOnly` value should be the same for all ad groups.

### Example Usage

```python
import os
import ttd_workflows
from ttd_workflows import Workflows


with Workflows(
    ttd_auth=os.getenv("WORKFLOWS_TTD_AUTH", ""),
) as workflows:

    res = workflows.ad_group.patch_adgroup_bulk(request={
        "input": [
            {
                "id": "<id>",
                "primary_input": {
                    "is_enabled": True,
                    "description": "hence disbar within weatherize bah amused",
                    "budget": {
                        "allocation_type": ttd_workflows.AllocationType.MAXIMUM,
                        "budget_in_advertiser_currency": 3268.79,
                        "budget_in_impressions": 185004,
                        "daily_target_in_advertiser_currency": 304.35,
                        "daily_target_in_impressions": 547566,
                    },
                    "base_bid_cpm_in_advertiser_currency": 9092.47,
                    "max_bid_cpm_in_advertiser_currency": 3654.86,
                    "audience_targeting": {
                        "audience_id": "<id>",
                        "audience_accelerator_exclusions_enabled": True,
                        "audience_booster_enabled": True,
                        "audience_excluder_enabled": False,
                        "audience_predictor_enabled": True,
                        "cross_device_vendor_list_for_audience": [
                            218209,
                            103038,
                        ],
                        "recency_exclusion_window_in_minutes": 917898,
                        "target_trackable_users_enabled": None,
                        "use_mc_id_as_primary": True,
                    },
                    "roi_goal": {
                        "maximize_reach": None,
                        "maximize_ltv_incremental_reach": False,
                        "cpc_in_advertiser_currency": None,
                        "ctr_in_percent": 806.78,
                        "nielsen_otp_in_percent": 6345.56,
                        "cpa_in_advertiser_currency": 920.88,
                        "return_on_ad_spend_percent": 7121.59,
                        "vcr_in_percent": 986.04,
                        "viewability_in_percent": 8457.51,
                        "vcpm_in_advertiser_currency": None,
                        "cpcv_in_advertiser_currency": 5308.5,
                        "miaozhen_otp_in_percent": 7264.42,
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
                        {
                            "bid_list_id": "<id>",
                            "is_enabled": True,
                            "is_default_for_dimension": False,
                        },
                        {
                            "bid_list_id": "<id>",
                            "is_enabled": True,
                            "is_default_for_dimension": False,
                        },
                    ],
                    "name": "<value>",
                    "channel": ttd_workflows.AdGroupChannel.AUDIO,
                    "funnel_location": ttd_workflows.AdGroupFunnelLocation.CONVERSION,
                },
                "advanced_input": {
                    "koa_optimization_settings": {
                        "are_future_koa_features_enabled": True,
                        "predictive_clearing_enabled": None,
                    },
                    "comscore_settings": {
                        "is_enabled": False,
                        "population_id": 456020,
                        "demographic_member_ids": [
                            278818,
                            634558,
                            707304,
                        ],
                        "mobile_demographic_member_ids": [
                            548034,
                            335760,
                        ],
                    },
                    "contract_targeting": {
                        "allow_open_market_bidding_when_targeting_contracts": False,
                    },
                    "dimensional_bidding_auto_optimization_settings": [
                        [],
                    ],
                    "is_use_clicks_as_conversions_enabled": True,
                    "is_use_secondary_conversions_enabled": False,
                    "nielsen_tracking_attributes": {
                        "enhanced_reporting_option": ttd_workflows.EnhancedNielsenReportingOptions.SITE,
                        "gender": ttd_workflows.TargetingGender.FEMALE,
                        "start_age": ttd_workflows.TargetingStartAge.FIFTY,
                        "end_age": ttd_workflows.TargetingEndAge.THIRTY_NINE,
                        "countries": [],
                    },
                    "new_frequency_configs": [
                        {
                            "counter_name": "<value>",
                            "frequency_cap": 568469,
                            "frequency_goal": 860019,
                            "reset_interval_in_minutes": 280265,
                        },
                    ],
                    "flights": [
                        {
                            "allocation_type": ttd_workflows.AllocationType.FIXED,
                            "budget_in_advertiser_currency": 4586.15,
                            "budget_in_impressions": 381675,
                            "daily_target_in_advertiser_currency": 5045.51,
                            "daily_target_in_impressions": None,
                            "campaign_flight_id": 382445,
                        },
                    ],
                },
            },
            {
                "id": "<id>",
                "primary_input": {
                    "is_enabled": True,
                    "description": "hence disbar within weatherize bah amused",
                    "budget": {
                        "allocation_type": ttd_workflows.AllocationType.MAXIMUM,
                        "budget_in_advertiser_currency": 3268.79,
                        "budget_in_impressions": 185004,
                        "daily_target_in_advertiser_currency": 304.35,
                        "daily_target_in_impressions": 547566,
                    },
                    "base_bid_cpm_in_advertiser_currency": 9092.47,
                    "max_bid_cpm_in_advertiser_currency": 3654.86,
                    "audience_targeting": {
                        "audience_id": "<id>",
                        "audience_accelerator_exclusions_enabled": True,
                        "audience_booster_enabled": True,
                        "audience_excluder_enabled": False,
                        "audience_predictor_enabled": True,
                        "cross_device_vendor_list_for_audience": [
                            218209,
                            103038,
                        ],
                        "recency_exclusion_window_in_minutes": 917898,
                        "target_trackable_users_enabled": None,
                        "use_mc_id_as_primary": True,
                    },
                    "roi_goal": {
                        "maximize_reach": None,
                        "maximize_ltv_incremental_reach": False,
                        "cpc_in_advertiser_currency": None,
                        "ctr_in_percent": 806.78,
                        "nielsen_otp_in_percent": 6345.56,
                        "cpa_in_advertiser_currency": 920.88,
                        "return_on_ad_spend_percent": 7121.59,
                        "vcr_in_percent": 986.04,
                        "viewability_in_percent": 8457.51,
                        "vcpm_in_advertiser_currency": None,
                        "cpcv_in_advertiser_currency": 5308.5,
                        "miaozhen_otp_in_percent": 7264.42,
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
                        {
                            "bid_list_id": "<id>",
                            "is_enabled": True,
                            "is_default_for_dimension": False,
                        },
                        {
                            "bid_list_id": "<id>",
                            "is_enabled": True,
                            "is_default_for_dimension": False,
                        },
                    ],
                    "name": "<value>",
                    "channel": ttd_workflows.AdGroupChannel.AUDIO,
                    "funnel_location": ttd_workflows.AdGroupFunnelLocation.CONVERSION,
                },
                "advanced_input": {
                    "koa_optimization_settings": {
                        "are_future_koa_features_enabled": True,
                        "predictive_clearing_enabled": None,
                    },
                    "comscore_settings": {
                        "is_enabled": False,
                        "population_id": 456020,
                        "demographic_member_ids": [
                            278818,
                            634558,
                            707304,
                        ],
                        "mobile_demographic_member_ids": [
                            548034,
                            335760,
                        ],
                    },
                    "contract_targeting": {
                        "allow_open_market_bidding_when_targeting_contracts": False,
                    },
                    "dimensional_bidding_auto_optimization_settings": [
                        [],
                    ],
                    "is_use_clicks_as_conversions_enabled": True,
                    "is_use_secondary_conversions_enabled": False,
                    "nielsen_tracking_attributes": {
                        "enhanced_reporting_option": ttd_workflows.EnhancedNielsenReportingOptions.SITE,
                        "gender": ttd_workflows.TargetingGender.FEMALE,
                        "start_age": ttd_workflows.TargetingStartAge.FIFTY,
                        "end_age": ttd_workflows.TargetingEndAge.THIRTY_NINE,
                        "countries": [],
                    },
                    "new_frequency_configs": [
                        {
                            "counter_name": "<value>",
                            "frequency_cap": 568469,
                            "frequency_goal": 860019,
                            "reset_interval_in_minutes": 280265,
                        },
                    ],
                    "flights": [
                        {
                            "allocation_type": ttd_workflows.AllocationType.FIXED,
                            "budget_in_advertiser_currency": 4586.15,
                            "budget_in_impressions": 381675,
                            "daily_target_in_advertiser_currency": 5045.51,
                            "daily_target_in_impressions": None,
                            "campaign_flight_id": 382445,
                        },
                    ],
                },
            },
        ],
        "validate_input_only": True,
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

**[models.BulkJobSubmitResponse](../../models/bulkjobsubmitresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.ProblemDetailsError | 400, 403                   | application/json           |
| models.APIError            | 4XX, 5XX                   | \*/\*                      |