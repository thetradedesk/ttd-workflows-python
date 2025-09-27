# AdGroup
(*ad_group*)

## Overview

### Available Operations

* [create_ad_groups_job](#create_ad_groups_job) - Create multiple new ad groups with required fields
* [update_ad_groups_job](#update_ad_groups_job) - Update multiple ad groups with specified fields

## create_ad_groups_job

Create multiple new ad groups with required fields

### Example Usage

<!-- UsageSnippet language="python" operationID="createAdGroupsJob" method="post" path="/standardjob/adgroup/bulk" -->
```python
import os
from ttd_workflows import Workflows


with Workflows(
    ttd_auth=os.getenv("WORKFLOWS_TTD_AUTH", ""),
) as workflows:

    res = workflows.ad_group.create_ad_groups_job(request={
        "input": [],
        "validate_input_only": False,
        "callback_input": {
            "callback_url": "https://fantastic-daughter.biz/",
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

| Parameter                                                                                                           | Type                                                                                                                | Required                                                                                                            | Description                                                                                                         |
| ------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                           | [models.AdGroupBulkCreateWorkflowInputWithValidation](../../models/adgroupbulkcreateworkflowinputwithvalidation.md) | :heavy_check_mark:                                                                                                  | The request object to use for the request.                                                                          |
| `retries`                                                                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                    | :heavy_minus_sign:                                                                                                  | Configuration to override the default retry behavior of the client.                                                 |

### Response

**[models.CreateAdGroupsJobResponse](../../models/createadgroupsjobresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.ProblemDetailsError | 400, 403                   | application/json           |
| models.APIError            | 4XX, 5XX                   | \*/\*                      |

## update_ad_groups_job

Only the fields provided in the request payload for each specific ad group will be updated.

### Example Usage

<!-- UsageSnippet language="python" operationID="updateAdGroupsJob" method="patch" path="/standardjob/adgroup/bulk" -->
```python
import os
import ttd_workflows
from ttd_workflows import Workflows


with Workflows(
    ttd_auth=os.getenv("WORKFLOWS_TTD_AUTH", ""),
) as workflows:

    res = workflows.ad_group.update_ad_groups_job(request={
        "input": [
            {
                "id": "<id>",
                "primary_input": {
                    "is_enabled": False,
                    "description": "stealthily miserable imaginary er since athwart er blah marten",
                    "budget": {
                        "allocation_type": ttd_workflows.AllocationType.MINIMUM,
                        "budget_in_advertiser_currency": 5440.47,
                        "budget_in_impressions": None,
                        "daily_target_in_advertiser_currency": 6251.13,
                        "daily_target_in_impressions": 931411,
                    },
                    "base_bid_cpm_in_advertiser_currency": 188.02,
                    "max_bid_cpm_in_advertiser_currency": 6077.98,
                    "audience_targeting": {
                        "audience_id": "<id>",
                        "audience_accelerator_exclusions_enabled": True,
                        "audience_booster_enabled": True,
                        "audience_excluder_enabled": False,
                        "audience_predictor_enabled": False,
                        "cross_device_vendor_list_for_audience": [
                            27262,
                        ],
                        "recency_exclusion_window_in_minutes": 676417,
                        "target_trackable_users_enabled": True,
                        "use_mc_id_as_primary": True,
                    },
                    "roi_goal": {
                        "maximize_reach": False,
                        "maximize_ltv_incremental_reach": True,
                        "cpc_in_advertiser_currency": None,
                        "ctr_in_percent": 2972.79,
                        "nielsen_otp_in_percent": 4206.38,
                        "cpa_in_advertiser_currency": None,
                        "return_on_ad_spend_percent": 842.94,
                        "vcr_in_percent": 6307.13,
                        "viewability_in_percent": 9286.78,
                        "vcpm_in_advertiser_currency": 8251.2,
                        "cpcv_in_advertiser_currency": 4502.77,
                        "miaozhen_otp_in_percent": 2362.43,
                    },
                    "creative_ids": [
                        "<value 1>",
                    ],
                    "associated_bid_lists": [
                        {
                            "bid_list_id": "<id>",
                            "is_enabled": True,
                            "is_default_for_dimension": True,
                        },
                    ],
                    "name": "<value>",
                    "channel": ttd_workflows.AdGroupChannel.TV,
                    "funnel_location": ttd_workflows.AdGroupFunnelLocation.NONE,
                },
                "advanced_input": {
                    "koa_optimization_settings": {
                        "are_future_koa_features_enabled": True,
                        "predictive_clearing_enabled": False,
                    },
                    "comscore_settings": {
                        "is_enabled": True,
                        "population_id": 907569,
                        "demographic_member_ids": None,
                        "mobile_demographic_member_ids": [
                            169306,
                            568551,
                        ],
                    },
                    "contract_targeting": {
                        "allow_open_market_bidding_when_targeting_contracts": True,
                    },
                    "dimensional_bidding_auto_optimization_settings": [
                        [
                            ttd_workflows.DimensionalBiddingDimensions.HAS_FREQUENCY_ADJUSTMENT_ID,
                        ],
                    ],
                    "is_use_clicks_as_conversions_enabled": True,
                    "is_use_secondary_conversions_enabled": True,
                    "nielsen_tracking_attributes": {
                        "enhanced_reporting_option": ttd_workflows.EnhancedNielsenReportingOptionsInput.AUDIENCE,
                        "gender": ttd_workflows.TargetingGenderInput.FEMALE,
                        "start_age": ttd_workflows.TargetingStartAgeInput.FORTY_FIVE,
                        "end_age": ttd_workflows.TargetingEndAgeInput.THIRTY_FOUR,
                        "countries": [
                            "<value 1>",
                            "<value 2>",
                        ],
                    },
                    "new_frequency_configs": [
                        {
                            "counter_name": "<value>",
                            "frequency_cap": 25438,
                            "frequency_goal": 637221,
                            "reset_interval_in_minutes": 375296,
                        },
                    ],
                    "flights": None,
                },
            },
        ],
        "validate_input_only": True,
        "callback_input": {
            "callback_url": "https://winged-bathhouse.net",
            "callback_headers": None,
        },
    })

    assert res.standard_job_submit_response is not None

    # Handle response
    print(res.standard_job_submit_response)

```

### Parameters

| Parameter                                                                                                           | Type                                                                                                                | Required                                                                                                            | Description                                                                                                         |
| ------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                           | [models.AdGroupBulkUpdateWorkflowInputWithValidation](../../models/adgroupbulkupdateworkflowinputwithvalidation.md) | :heavy_check_mark:                                                                                                  | The request object to use for the request.                                                                          |
| `retries`                                                                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                    | :heavy_minus_sign:                                                                                                  | Configuration to override the default retry behavior of the client.                                                 |

### Response

**[models.UpdateAdGroupsJobResponse](../../models/updateadgroupsjobresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.ProblemDetailsError | 400, 403                   | application/json           |
| models.APIError            | 4XX, 5XX                   | \*/\*                      |