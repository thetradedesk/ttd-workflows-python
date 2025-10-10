# AdGroups
(*ad_groups*)

## Overview

### Available Operations

* [create](#create) - Create a new ad group with required fields
* [update](#update) - Update an ad group with specified fields
* [archive](#archive) - Archive multiple ad groups

## create

Create a new ad group with required fields

### Example Usage

<!-- UsageSnippet language="python" operationID="createAdGroup" method="post" path="/adgroup" -->
```python
import os
import ttd_workflows
from ttd_workflows import Workflows


with Workflows(
    ttd_auth=os.getenv("WORKFLOWS_TTD_AUTH", ""),
) as workflows:

    res = workflows.ad_groups.create(request={
        "primary_input": {
            "is_enabled": False,
            "description": "twine from gosh poor safely editor astride vice lost and",
            "budget": {
                "allocation_type": ttd_workflows.AllocationType.MAXIMUM,
                "budget_in_advertiser_currency": 3786.02,
                "budget_in_impressions": 783190,
                "daily_target_in_advertiser_currency": 9747.02,
                "daily_target_in_impressions": 985999,
            },
            "base_bid_cpm_in_advertiser_currency": 3785.04,
            "max_bid_cpm_in_advertiser_currency": 7447.3,
            "audience_targeting": {
                "audience_id": "<id>",
                "audience_accelerator_exclusions_enabled": True,
                "audience_booster_enabled": True,
                "audience_excluder_enabled": True,
                "audience_predictor_enabled": False,
                "cross_device_vendor_list_for_audience": [
                    107263,
                ],
                "recency_exclusion_window_in_minutes": 90062,
                "target_trackable_users_enabled": True,
                "use_mc_id_as_primary": True,
            },
            "roi_goal": {
                "maximize_reach": True,
                "maximize_ltv_incremental_reach": False,
                "cpc_in_advertiser_currency": 2280.31,
                "ctr_in_percent": None,
                "nielsen_otp_in_percent": 5175.21,
                "cpa_in_advertiser_currency": 2544.37,
                "return_on_ad_spend_percent": 8201.47,
                "vcr_in_percent": 4846.08,
                "viewability_in_percent": None,
                "vcpm_in_advertiser_currency": 4649.53,
                "cpcv_in_advertiser_currency": 313.95,
                "miaozhen_otp_in_percent": 4704.1,
            },
            "creative_ids": None,
            "associated_bid_lists": [
                {
                    "bid_list_id": "<id>",
                    "is_enabled": False,
                    "is_default_for_dimension": True,
                },
            ],
            "name": "<value>",
            "channel": ttd_workflows.AdGroupChannel.DISPLAY,
            "funnel_location": ttd_workflows.AdGroupFunnelLocation.CONSIDERATION,
            "programmatic_guaranteed_private_contract_id": "<id>",
        },
        "campaign_id": "<id>",
        "advanced_input": {
            "koa_optimization_settings": {
                "are_future_koa_features_enabled": False,
                "predictive_clearing_enabled": False,
            },
            "comscore_settings": {
                "is_enabled": False,
                "population_id": None,
                "demographic_member_ids": [
                    959580,
                    236376,
                ],
                "mobile_demographic_member_ids": [
                    664689,
                    827980,
                    21321,
                ],
            },
            "contract_targeting": {
                "allow_open_market_bidding_when_targeting_contracts": True,
            },
            "dimensional_bidding_auto_optimization_settings": [
                [],
                [],
            ],
            "is_use_clicks_as_conversions_enabled": False,
            "is_use_secondary_conversions_enabled": False,
            "nielsen_tracking_attributes": {
                "enhanced_reporting_option": ttd_workflows.EnhancedNielsenReportingOptionsInput.SITE,
                "gender": ttd_workflows.TargetingGenderInput.MALE,
                "start_age": ttd_workflows.TargetingStartAgeInput.TWENTY_FIVE,
                "end_age": ttd_workflows.TargetingEndAgeInput.SEVENTEEN,
                "countries": [
                    "<value 1>",
                    "<value 2>",
                    "<value 3>",
                ],
            },
            "new_frequency_configs": [
                {
                    "counter_name": None,
                    "frequency_cap": 375286,
                    "frequency_goal": 534735,
                    "reset_interval_in_minutes": 788122,
                },
            ],
            "flights": [
                {
                    "allocation_type": ttd_workflows.AllocationType.MAXIMUM,
                    "budget_in_advertiser_currency": 4070.96,
                    "budget_in_impressions": 901477,
                    "daily_target_in_advertiser_currency": 5847.35,
                    "daily_target_in_impressions": 257517,
                    "campaign_flight_id": 874887,
                },
            ],
        },
        "validate_input_only": True,
    })

    assert res.ad_group_payload is not None

    # Handle response
    print(res.ad_group_payload)

```

### Parameters

| Parameter                                                                                                   | Type                                                                                                        | Required                                                                                                    | Description                                                                                                 |
| ----------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                   | [models.AdGroupCreateWorkflowInputWithValidation](../../models/adgroupcreateworkflowinputwithvalidation.md) | :heavy_check_mark:                                                                                          | The request object to use for the request.                                                                  |
| `retries`                                                                                                   | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                            | :heavy_minus_sign:                                                                                          | Configuration to override the default retry behavior of the client.                                         |

### Response

**[models.CreateAdGroupResponse](../../models/createadgroupresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.ProblemDetailsError | 400, 403                   | application/json           |
| models.APIError            | 4XX, 5XX                   | \*/\*                      |

## update

Only the fields provided in the request payload will be updated.

### Example Usage

<!-- UsageSnippet language="python" operationID="updateAdGroup" method="patch" path="/adgroup" -->
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
            "is_enabled": None,
            "description": "likely upliftingly league that finally after owlishly when furthermore brush",
            "budget": {
                "allocation_type": ttd_workflows.AllocationType.MAXIMUM,
                "budget_in_advertiser_currency": 2166.43,
                "budget_in_impressions": 508947,
                "daily_target_in_advertiser_currency": 5830.53,
                "daily_target_in_impressions": 377823,
            },
            "base_bid_cpm_in_advertiser_currency": 1710.9,
            "max_bid_cpm_in_advertiser_currency": 1926.83,
            "audience_targeting": {
                "audience_id": "<id>",
                "audience_accelerator_exclusions_enabled": False,
                "audience_booster_enabled": True,
                "audience_excluder_enabled": True,
                "audience_predictor_enabled": True,
                "cross_device_vendor_list_for_audience": [
                    774064,
                    165155,
                    542528,
                ],
                "recency_exclusion_window_in_minutes": 740341,
                "target_trackable_users_enabled": False,
                "use_mc_id_as_primary": True,
            },
            "roi_goal": {
                "maximize_reach": False,
                "maximize_ltv_incremental_reach": False,
                "cpc_in_advertiser_currency": 1146.61,
                "ctr_in_percent": 3063.1,
                "nielsen_otp_in_percent": 411.57,
                "cpa_in_advertiser_currency": None,
                "return_on_ad_spend_percent": 7161.01,
                "vcr_in_percent": 5983.85,
                "viewability_in_percent": 9094.92,
                "vcpm_in_advertiser_currency": 1135.94,
                "cpcv_in_advertiser_currency": 6372.45,
                "miaozhen_otp_in_percent": 8405.28,
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
            ],
            "name": "<value>",
            "channel": ttd_workflows.AdGroupChannel.NATIVE,
            "funnel_location": ttd_workflows.AdGroupFunnelLocation.CONVERSION,
        },
        "advanced_input": {
            "koa_optimization_settings": {
                "are_future_koa_features_enabled": False,
                "predictive_clearing_enabled": True,
            },
            "comscore_settings": {
                "is_enabled": False,
                "population_id": 935670,
                "demographic_member_ids": [
                    873274,
                    940674,
                    350994,
                ],
                "mobile_demographic_member_ids": [
                    572403,
                    872508,
                    141651,
                ],
            },
            "contract_targeting": {
                "allow_open_market_bidding_when_targeting_contracts": True,
            },
            "dimensional_bidding_auto_optimization_settings": [
                [
                    ttd_workflows.DimensionalBiddingDimensions.HAS_CONTENT_LIVESTREAM,
                ],
            ],
            "is_use_clicks_as_conversions_enabled": False,
            "is_use_secondary_conversions_enabled": False,
            "nielsen_tracking_attributes": {
                "enhanced_reporting_option": ttd_workflows.EnhancedNielsenReportingOptionsInput.NONE,
                "gender": ttd_workflows.TargetingGenderInput.FEMALE,
                "start_age": ttd_workflows.TargetingStartAgeInput.FIFTY_FIVE,
                "end_age": ttd_workflows.TargetingEndAgeInput.SIXTY_FOUR_PLUS,
                "countries": [
                    "<value 1>",
                    "<value 2>",
                ],
            },
            "new_frequency_configs": [
                {
                    "counter_name": "<value>",
                    "frequency_cap": 685969,
                    "frequency_goal": 448470,
                    "reset_interval_in_minutes": 577492,
                },
            ],
            "flights": [
                {
                    "allocation_type": ttd_workflows.AllocationType.MINIMUM,
                    "budget_in_advertiser_currency": 5325.23,
                    "budget_in_impressions": 876101,
                    "daily_target_in_advertiser_currency": 44.58,
                    "daily_target_in_impressions": 815686,
                    "campaign_flight_id": 528311,
                },
            ],
        },
        "validate_input_only": False,
    })

    assert res.ad_group_payload is not None

    # Handle response
    print(res.ad_group_payload)

```

### Parameters

| Parameter                                                                                                   | Type                                                                                                        | Required                                                                                                    | Description                                                                                                 |
| ----------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                   | [models.AdGroupUpdateWorkflowInputWithValidation](../../models/adgroupupdateworkflowinputwithvalidation.md) | :heavy_check_mark:                                                                                          | The request object to use for the request.                                                                  |
| `retries`                                                                                                   | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                            | :heavy_minus_sign:                                                                                          | Configuration to override the default retry behavior of the client.                                         |

### Response

**[models.UpdateAdGroupResponse](../../models/updateadgroupresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.ProblemDetailsError | 400, 403                   | application/json           |
| models.APIError            | 4XX, 5XX                   | \*/\*                      |

## archive

**NOTE**: Once archived, ad groups cannot be un-archived.

### Example Usage

<!-- UsageSnippet language="python" operationID="archiveAdGroups" method="post" path="/adgroup/archive" -->
```python
import os
from ttd_workflows import Workflows


with Workflows(
    ttd_auth=os.getenv("WORKFLOWS_TTD_AUTH", ""),
) as workflows:

    res = workflows.ad_groups.archive(force_archive=False, request_body=[
        "<value 1>",
        "<value 2>",
    ])

    assert res.strings is not None

    # Handle response
    print(res.strings)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `force_archive`                                                     | *Optional[bool]*                                                    | :heavy_minus_sign:                                                  | N/A                                                                 |
| `request_body`                                                      | List[*str*]                                                         | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.ArchiveAdGroupsResponse](../../models/archiveadgroupsresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.ProblemDetailsError | 400, 403                   | application/json           |
| models.APIError            | 4XX, 5XX                   | \*/\*                      |