# ttd-workflows-python

<!-- Start Summary [summary] -->
## Summary

Workflows API: A RESTful service for commonly used workflows.
<!-- End Summary [summary] -->

<!-- Start Table of Contents [toc] -->
## Table of Contents
<!-- $toc-max-depth=2 -->
* [ttd-workflows-python](https://github.com/thetradedesk/ttd-workflows-python/blob/master/#ttd-workflows-python)
  * [SDK Installation](https://github.com/thetradedesk/ttd-workflows-python/blob/master/#sdk-installation)
  * [IDE Support](https://github.com/thetradedesk/ttd-workflows-python/blob/master/#ide-support)
  * [SDK Example Usage](https://github.com/thetradedesk/ttd-workflows-python/blob/master/#sdk-example-usage)
  * [Authentication](https://github.com/thetradedesk/ttd-workflows-python/blob/master/#authentication)
  * [Available Resources and Operations](https://github.com/thetradedesk/ttd-workflows-python/blob/master/#available-resources-and-operations)
  * [Retries](https://github.com/thetradedesk/ttd-workflows-python/blob/master/#retries)
  * [Error Handling](https://github.com/thetradedesk/ttd-workflows-python/blob/master/#error-handling)
  * [Server Selection](https://github.com/thetradedesk/ttd-workflows-python/blob/master/#server-selection)
  * [Custom HTTP Client](https://github.com/thetradedesk/ttd-workflows-python/blob/master/#custom-http-client)
  * [Resource Management](https://github.com/thetradedesk/ttd-workflows-python/blob/master/#resource-management)
  * [Debugging](https://github.com/thetradedesk/ttd-workflows-python/blob/master/#debugging)

<!-- End Table of Contents [toc] -->

<!-- Start SDK Installation [installation] -->
## SDK Installation

> [!NOTE]
> **Python version upgrade policy**
>
> Once a Python version reaches its [official end of life date](https://devguide.python.org/versions/), a 3-month grace period is provided for users to upgrade. Following this grace period, the minimum python version supported in the SDK will be updated.

The SDK can be installed with either *pip* or *poetry* package managers.

### PIP

*PIP* is the default package installer for Python, enabling easy installation and management of packages from PyPI via the command line.

```bash
pip install ttd-workflows
```

### Poetry

*Poetry* is a modern tool that simplifies dependency management and package publishing by using a single `pyproject.toml` file to handle project metadata and dependencies.

```bash
poetry add ttd-workflows
```

### Shell and script usage with `uv`

You can use this SDK in a Python shell with [uv](https://docs.astral.sh/uv/) and the `uvx` command that comes with it like so:

```shell
uvx --from ttd-workflows python
```

It's also possible to write a standalone Python script without needing to set up a whole project like so:

```python
#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.9"
# dependencies = [
#     "ttd-workflows",
# ]
# ///

from ttd_workflows import Workflows

sdk = Workflows(
  # SDK arguments
)

# Rest of script here...
```

Once that is saved to a file, you can run it with `uv run script.py` where
`script.py` can be replaced with the actual file name.
<!-- End SDK Installation [installation] -->

<!-- Start IDE Support [idesupport] -->
## IDE Support

### PyCharm

Generally, the SDK will work well with most IDEs out of the box. However, when using PyCharm, you can enjoy much better integration with Pydantic by installing an additional plugin.

- [PyCharm Pydantic Plugin](https://docs.pydantic.dev/latest/integrations/pycharm/)
<!-- End IDE Support [idesupport] -->

<!-- Start SDK Example Usage [usage] -->
## SDK Example Usage

### Example

```python
# Synchronous Example
import os
import ttd_workflows
from ttd_workflows import Workflows


with Workflows(
    ttd_auth=os.getenv("WORKFLOWS_TTD_AUTH", ""),
) as workflows:

    res = workflows.ad_group.post_adgroup(request={
        "name": "<value>",
        "is_enabled": True,
        "description": "whose countess instead helplessly honestly unblinking hence opposite",
        "programmatic_guaranteed_private_contract_id": "<id>",
        "channel": ttd_workflows.AdGroupChannel.NATIVE,
        "funnel_location": ttd_workflows.AdGroupFunnelLocation.NONE,
        "budget": {
            "allocation_type": ttd_workflows.AllocationType.FIXED,
            "budget_in_advertiser_currency": 1255.27,
            "budget_in_impressions": 469226,
            "daily_target_in_advertiser_currency": 7461.36,
            "daily_target_in_impressions": 790907,
        },
        "base_bid_cpm_in_advertiser_currency": 310.16,
        "max_bid_cpm_in_advertiser_currency": 2360.6,
        "audience_targeting": {
            "audience_id": "<id>",
            "audience_accelerator_exclusions_enabled": False,
            "audience_booster_enabled": False,
            "audience_excluder_enabled": True,
            "audience_predictor_enabled": False,
            "cross_device_vendor_list_for_audience": [
                614673,
                684382,
            ],
            "recency_exclusion_window_in_minutes": 262820,
            "target_trackable_users_enabled": True,
            "use_mc_id_as_primary": True,
        },
        "roi_goal": {
            "maximize_reach": False,
            "maximize_ltv_incremental_reach": False,
            "cpc_in_advertiser_currency": 3537.6,
            "ctr_in_percent": 6333.79,
            "nielsen_otp_in_percent": 8443.6,
            "cpa_in_advertiser_currency": 8183.4,
            "return_on_ad_spend_percent": 9749.47,
            "vcr_in_percent": 5244.57,
            "viewability_in_percent": 1797.09,
            "vcpm_in_advertiser_currency": 9777.89,
            "cpcv_in_advertiser_currency": 4506.52,
            "miaozhen_otp_in_percent": 5639.62,
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
        "campaign_id": "<id>",
        "advanced_settings": {
            "koa_optimization_settings": {
                "are_future_koa_features_enabled": True,
                "predictive_clearing_enabled": True,
            },
            "comscore_settings": {
                "is_enabled": True,
                "population_id": 133150,
                "demographic_member_ids": [
                    199046,
                ],
                "mobile_demographic_member_ids": [
                    964861,
                    667844,
                ],
            },
            "contract_targeting": {
                "allow_open_market_bidding_when_targeting_contracts": True,
            },
            "dimensional_bidding_auto_optimization_settings": [
                [
                    ttd_workflows.DimensionalBiddingDimensions.HAS_VIDEO_COMPLETION_RATE_SCORE_RANGE,
                    ttd_workflows.DimensionalBiddingDimensions.HAS_FULL_REFERRER_URL,
                ],
                [],
                [
                    ttd_workflows.DimensionalBiddingDimensions.HAS_SELLER_ID,
                ],
            ],
            "is_use_clicks_as_conversions_enabled": True,
            "is_use_secondary_conversions_enabled": True,
            "nielsen_tracking_attributes": {
                "enhanced_reporting_option": ttd_workflows.EnhancedNielsenReportingOptions.NONE,
                "gender": ttd_workflows.TargetingGender.FEMALE,
                "start_age": ttd_workflows.TargetingStartAge.SIXTY_FIVE,
                "end_age": ttd_workflows.TargetingEndAge.TWENTY_NINE,
                "countries": [
                    "<value>",
                ],
            },
            "new_frequency_configs": [
                {
                    "counter_name": "<value>",
                    "frequency_cap": 746348,
                    "frequency_goal": 510683,
                    "reset_interval_in_minutes": 129092,
                },
                {
                    "counter_name": "<value>",
                    "frequency_cap": 755997,
                    "frequency_goal": 198769,
                    "reset_interval_in_minutes": 168827,
                },
            ],
            "flights": [
                {
                    "allocation_type": ttd_workflows.AllocationType.FIXED,
                    "budget_in_advertiser_currency": 1595.69,
                    "budget_in_impressions": 474397,
                    "daily_target_in_advertiser_currency": 7814.66,
                    "daily_target_in_impressions": 542673,
                    "campaign_flight_id": 136905,
                },
                {
                    "allocation_type": ttd_workflows.AllocationType.FIXED,
                    "budget_in_advertiser_currency": 3145.56,
                    "budget_in_impressions": 465009,
                    "daily_target_in_advertiser_currency": 8108.2,
                    "daily_target_in_impressions": 109630,
                    "campaign_flight_id": 186465,
                },
                {
                    "allocation_type": ttd_workflows.AllocationType.FIXED,
                    "budget_in_advertiser_currency": 2666.4,
                    "budget_in_impressions": 593663,
                    "daily_target_in_advertiser_currency": 2585.24,
                    "daily_target_in_impressions": 42750,
                    "campaign_flight_id": 597076,
                },
            ],
        },
    })

    # Handle response
    print(res)
```

</br>

The same SDK client can also be used to make asychronous requests by importing asyncio.
```python
# Asynchronous Example
import asyncio
import os
import ttd_workflows
from ttd_workflows import Workflows

async def main():

    async with Workflows(
        ttd_auth=os.getenv("WORKFLOWS_TTD_AUTH", ""),
    ) as workflows:

        res = await workflows.ad_group.post_adgroup_async(request={
            "name": "<value>",
            "is_enabled": True,
            "description": "whose countess instead helplessly honestly unblinking hence opposite",
            "programmatic_guaranteed_private_contract_id": "<id>",
            "channel": ttd_workflows.AdGroupChannel.NATIVE,
            "funnel_location": ttd_workflows.AdGroupFunnelLocation.NONE,
            "budget": {
                "allocation_type": ttd_workflows.AllocationType.FIXED,
                "budget_in_advertiser_currency": 1255.27,
                "budget_in_impressions": 469226,
                "daily_target_in_advertiser_currency": 7461.36,
                "daily_target_in_impressions": 790907,
            },
            "base_bid_cpm_in_advertiser_currency": 310.16,
            "max_bid_cpm_in_advertiser_currency": 2360.6,
            "audience_targeting": {
                "audience_id": "<id>",
                "audience_accelerator_exclusions_enabled": False,
                "audience_booster_enabled": False,
                "audience_excluder_enabled": True,
                "audience_predictor_enabled": False,
                "cross_device_vendor_list_for_audience": [
                    614673,
                    684382,
                ],
                "recency_exclusion_window_in_minutes": 262820,
                "target_trackable_users_enabled": True,
                "use_mc_id_as_primary": True,
            },
            "roi_goal": {
                "maximize_reach": False,
                "maximize_ltv_incremental_reach": False,
                "cpc_in_advertiser_currency": 3537.6,
                "ctr_in_percent": 6333.79,
                "nielsen_otp_in_percent": 8443.6,
                "cpa_in_advertiser_currency": 8183.4,
                "return_on_ad_spend_percent": 9749.47,
                "vcr_in_percent": 5244.57,
                "viewability_in_percent": 1797.09,
                "vcpm_in_advertiser_currency": 9777.89,
                "cpcv_in_advertiser_currency": 4506.52,
                "miaozhen_otp_in_percent": 5639.62,
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
            "campaign_id": "<id>",
            "advanced_settings": {
                "koa_optimization_settings": {
                    "are_future_koa_features_enabled": True,
                    "predictive_clearing_enabled": True,
                },
                "comscore_settings": {
                    "is_enabled": True,
                    "population_id": 133150,
                    "demographic_member_ids": [
                        199046,
                    ],
                    "mobile_demographic_member_ids": [
                        964861,
                        667844,
                    ],
                },
                "contract_targeting": {
                    "allow_open_market_bidding_when_targeting_contracts": True,
                },
                "dimensional_bidding_auto_optimization_settings": [
                    [
                        ttd_workflows.DimensionalBiddingDimensions.HAS_VIDEO_COMPLETION_RATE_SCORE_RANGE,
                        ttd_workflows.DimensionalBiddingDimensions.HAS_FULL_REFERRER_URL,
                    ],
                    [],
                    [
                        ttd_workflows.DimensionalBiddingDimensions.HAS_SELLER_ID,
                    ],
                ],
                "is_use_clicks_as_conversions_enabled": True,
                "is_use_secondary_conversions_enabled": True,
                "nielsen_tracking_attributes": {
                    "enhanced_reporting_option": ttd_workflows.EnhancedNielsenReportingOptions.NONE,
                    "gender": ttd_workflows.TargetingGender.FEMALE,
                    "start_age": ttd_workflows.TargetingStartAge.SIXTY_FIVE,
                    "end_age": ttd_workflows.TargetingEndAge.TWENTY_NINE,
                    "countries": [
                        "<value>",
                    ],
                },
                "new_frequency_configs": [
                    {
                        "counter_name": "<value>",
                        "frequency_cap": 746348,
                        "frequency_goal": 510683,
                        "reset_interval_in_minutes": 129092,
                    },
                    {
                        "counter_name": "<value>",
                        "frequency_cap": 755997,
                        "frequency_goal": 198769,
                        "reset_interval_in_minutes": 168827,
                    },
                ],
                "flights": [
                    {
                        "allocation_type": ttd_workflows.AllocationType.FIXED,
                        "budget_in_advertiser_currency": 1595.69,
                        "budget_in_impressions": 474397,
                        "daily_target_in_advertiser_currency": 7814.66,
                        "daily_target_in_impressions": 542673,
                        "campaign_flight_id": 136905,
                    },
                    {
                        "allocation_type": ttd_workflows.AllocationType.FIXED,
                        "budget_in_advertiser_currency": 3145.56,
                        "budget_in_impressions": 465009,
                        "daily_target_in_advertiser_currency": 8108.2,
                        "daily_target_in_impressions": 109630,
                        "campaign_flight_id": 186465,
                    },
                    {
                        "allocation_type": ttd_workflows.AllocationType.FIXED,
                        "budget_in_advertiser_currency": 2666.4,
                        "budget_in_impressions": 593663,
                        "daily_target_in_advertiser_currency": 2585.24,
                        "daily_target_in_impressions": 42750,
                        "campaign_flight_id": 597076,
                    },
                ],
            },
        })

        # Handle response
        print(res)

asyncio.run(main())
```
<!-- End SDK Example Usage [usage] -->

<!-- Start Authentication [security] -->
## Authentication

### Per-Client Security Schemes

This SDK supports the following security scheme globally:

| Name       | Type   | Scheme  | Environment Variable |
| ---------- | ------ | ------- | -------------------- |
| `ttd_auth` | apiKey | API key | `WORKFLOWS_TTD_AUTH` |

To authenticate with the API the `ttd_auth` parameter must be set when initializing the SDK client instance. For example:
```python
import os
import ttd_workflows
from ttd_workflows import Workflows


with Workflows(
    ttd_auth=os.getenv("WORKFLOWS_TTD_AUTH", ""),
) as workflows:

    res = workflows.ad_group.post_adgroup(request={
        "name": "<value>",
        "is_enabled": True,
        "description": "whose countess instead helplessly honestly unblinking hence opposite",
        "programmatic_guaranteed_private_contract_id": "<id>",
        "channel": ttd_workflows.AdGroupChannel.NATIVE,
        "funnel_location": ttd_workflows.AdGroupFunnelLocation.NONE,
        "budget": {
            "allocation_type": ttd_workflows.AllocationType.FIXED,
            "budget_in_advertiser_currency": 1255.27,
            "budget_in_impressions": 469226,
            "daily_target_in_advertiser_currency": 7461.36,
            "daily_target_in_impressions": 790907,
        },
        "base_bid_cpm_in_advertiser_currency": 310.16,
        "max_bid_cpm_in_advertiser_currency": 2360.6,
        "audience_targeting": {
            "audience_id": "<id>",
            "audience_accelerator_exclusions_enabled": False,
            "audience_booster_enabled": False,
            "audience_excluder_enabled": True,
            "audience_predictor_enabled": False,
            "cross_device_vendor_list_for_audience": [
                614673,
                684382,
            ],
            "recency_exclusion_window_in_minutes": 262820,
            "target_trackable_users_enabled": True,
            "use_mc_id_as_primary": True,
        },
        "roi_goal": {
            "maximize_reach": False,
            "maximize_ltv_incremental_reach": False,
            "cpc_in_advertiser_currency": 3537.6,
            "ctr_in_percent": 6333.79,
            "nielsen_otp_in_percent": 8443.6,
            "cpa_in_advertiser_currency": 8183.4,
            "return_on_ad_spend_percent": 9749.47,
            "vcr_in_percent": 5244.57,
            "viewability_in_percent": 1797.09,
            "vcpm_in_advertiser_currency": 9777.89,
            "cpcv_in_advertiser_currency": 4506.52,
            "miaozhen_otp_in_percent": 5639.62,
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
        "campaign_id": "<id>",
        "advanced_settings": {
            "koa_optimization_settings": {
                "are_future_koa_features_enabled": True,
                "predictive_clearing_enabled": True,
            },
            "comscore_settings": {
                "is_enabled": True,
                "population_id": 133150,
                "demographic_member_ids": [
                    199046,
                ],
                "mobile_demographic_member_ids": [
                    964861,
                    667844,
                ],
            },
            "contract_targeting": {
                "allow_open_market_bidding_when_targeting_contracts": True,
            },
            "dimensional_bidding_auto_optimization_settings": [
                [
                    ttd_workflows.DimensionalBiddingDimensions.HAS_VIDEO_COMPLETION_RATE_SCORE_RANGE,
                    ttd_workflows.DimensionalBiddingDimensions.HAS_FULL_REFERRER_URL,
                ],
                [],
                [
                    ttd_workflows.DimensionalBiddingDimensions.HAS_SELLER_ID,
                ],
            ],
            "is_use_clicks_as_conversions_enabled": True,
            "is_use_secondary_conversions_enabled": True,
            "nielsen_tracking_attributes": {
                "enhanced_reporting_option": ttd_workflows.EnhancedNielsenReportingOptions.NONE,
                "gender": ttd_workflows.TargetingGender.FEMALE,
                "start_age": ttd_workflows.TargetingStartAge.SIXTY_FIVE,
                "end_age": ttd_workflows.TargetingEndAge.TWENTY_NINE,
                "countries": [
                    "<value>",
                ],
            },
            "new_frequency_configs": [
                {
                    "counter_name": "<value>",
                    "frequency_cap": 746348,
                    "frequency_goal": 510683,
                    "reset_interval_in_minutes": 129092,
                },
                {
                    "counter_name": "<value>",
                    "frequency_cap": 755997,
                    "frequency_goal": 198769,
                    "reset_interval_in_minutes": 168827,
                },
            ],
            "flights": [
                {
                    "allocation_type": ttd_workflows.AllocationType.FIXED,
                    "budget_in_advertiser_currency": 1595.69,
                    "budget_in_impressions": 474397,
                    "daily_target_in_advertiser_currency": 7814.66,
                    "daily_target_in_impressions": 542673,
                    "campaign_flight_id": 136905,
                },
                {
                    "allocation_type": ttd_workflows.AllocationType.FIXED,
                    "budget_in_advertiser_currency": 3145.56,
                    "budget_in_impressions": 465009,
                    "daily_target_in_advertiser_currency": 8108.2,
                    "daily_target_in_impressions": 109630,
                    "campaign_flight_id": 186465,
                },
                {
                    "allocation_type": ttd_workflows.AllocationType.FIXED,
                    "budget_in_advertiser_currency": 2666.4,
                    "budget_in_impressions": 593663,
                    "daily_target_in_advertiser_currency": 2585.24,
                    "daily_target_in_impressions": 42750,
                    "campaign_flight_id": 597076,
                },
            ],
        },
    })

    # Handle response
    print(res)

```
<!-- End Authentication [security] -->

<!-- Start Available Resources and Operations [operations] -->
## Available Resources and Operations

<details open>
<summary>Available methods</summary>

### [ad_group](https://github.com/thetradedesk/ttd-workflows-python/blob/master/docs/sdks/adgroup/README.md)

* [post_adgroup](https://github.com/thetradedesk/ttd-workflows-python/blob/master/docs/sdks/adgroup/README.md#post_adgroup)
* [patch_adgroup](https://github.com/thetradedesk/ttd-workflows-python/blob/master/docs/sdks/adgroup/README.md#patch_adgroup)

### [campaign](https://github.com/thetradedesk/ttd-workflows-python/blob/master/docs/sdks/campaign/README.md)

* [create](https://github.com/thetradedesk/ttd-workflows-python/blob/master/docs/sdks/campaign/README.md#create) - Create a new campaign with required fields
* [post_campaign_bulk](https://github.com/thetradedesk/ttd-workflows-python/blob/master/docs/sdks/campaign/README.md#post_campaign_bulk) - Create a list of campaigns with required fields. `ValidationOnly` value should be the same for all campaigns.
* [post_campaign_archive](https://github.com/thetradedesk/ttd-workflows-python/blob/master/docs/sdks/campaign/README.md#post_campaign_archive) - Archive a list of campaigns
* [get_version](https://github.com/thetradedesk/ttd-workflows-python/blob/master/docs/sdks/campaign/README.md#get_version) - GET a campaign's version

### [graphql](https://github.com/thetradedesk/ttd-workflows-python/blob/master/docs/sdks/graphql/README.md)

* [execute](https://github.com/thetradedesk/ttd-workflows-python/blob/master/docs/sdks/graphql/README.md#execute) - An endpoint that executes valid GraphQL queries.


</details>
<!-- End Available Resources and Operations [operations] -->

<!-- Start Retries [retries] -->
## Retries

Some of the endpoints in this SDK support retries. If you use the SDK without any configuration, it will fall back to the default retry strategy provided by the API. However, the default retry strategy can be overridden on a per-operation basis, or across the entire SDK.

To change the default retry strategy for a single API call, simply provide a `RetryConfig` object to the call:
```python
import os
import ttd_workflows
from ttd_workflows import Workflows
from ttd_workflows.utils import BackoffStrategy, RetryConfig


with Workflows(
    ttd_auth=os.getenv("WORKFLOWS_TTD_AUTH", ""),
) as workflows:

    res = workflows.ad_group.post_adgroup(request={
        "name": "<value>",
        "is_enabled": True,
        "description": "whose countess instead helplessly honestly unblinking hence opposite",
        "programmatic_guaranteed_private_contract_id": "<id>",
        "channel": ttd_workflows.AdGroupChannel.NATIVE,
        "funnel_location": ttd_workflows.AdGroupFunnelLocation.NONE,
        "budget": {
            "allocation_type": ttd_workflows.AllocationType.FIXED,
            "budget_in_advertiser_currency": 1255.27,
            "budget_in_impressions": 469226,
            "daily_target_in_advertiser_currency": 7461.36,
            "daily_target_in_impressions": 790907,
        },
        "base_bid_cpm_in_advertiser_currency": 310.16,
        "max_bid_cpm_in_advertiser_currency": 2360.6,
        "audience_targeting": {
            "audience_id": "<id>",
            "audience_accelerator_exclusions_enabled": False,
            "audience_booster_enabled": False,
            "audience_excluder_enabled": True,
            "audience_predictor_enabled": False,
            "cross_device_vendor_list_for_audience": [
                614673,
                684382,
            ],
            "recency_exclusion_window_in_minutes": 262820,
            "target_trackable_users_enabled": True,
            "use_mc_id_as_primary": True,
        },
        "roi_goal": {
            "maximize_reach": False,
            "maximize_ltv_incremental_reach": False,
            "cpc_in_advertiser_currency": 3537.6,
            "ctr_in_percent": 6333.79,
            "nielsen_otp_in_percent": 8443.6,
            "cpa_in_advertiser_currency": 8183.4,
            "return_on_ad_spend_percent": 9749.47,
            "vcr_in_percent": 5244.57,
            "viewability_in_percent": 1797.09,
            "vcpm_in_advertiser_currency": 9777.89,
            "cpcv_in_advertiser_currency": 4506.52,
            "miaozhen_otp_in_percent": 5639.62,
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
        "campaign_id": "<id>",
        "advanced_settings": {
            "koa_optimization_settings": {
                "are_future_koa_features_enabled": True,
                "predictive_clearing_enabled": True,
            },
            "comscore_settings": {
                "is_enabled": True,
                "population_id": 133150,
                "demographic_member_ids": [
                    199046,
                ],
                "mobile_demographic_member_ids": [
                    964861,
                    667844,
                ],
            },
            "contract_targeting": {
                "allow_open_market_bidding_when_targeting_contracts": True,
            },
            "dimensional_bidding_auto_optimization_settings": [
                [
                    ttd_workflows.DimensionalBiddingDimensions.HAS_VIDEO_COMPLETION_RATE_SCORE_RANGE,
                    ttd_workflows.DimensionalBiddingDimensions.HAS_FULL_REFERRER_URL,
                ],
                [],
                [
                    ttd_workflows.DimensionalBiddingDimensions.HAS_SELLER_ID,
                ],
            ],
            "is_use_clicks_as_conversions_enabled": True,
            "is_use_secondary_conversions_enabled": True,
            "nielsen_tracking_attributes": {
                "enhanced_reporting_option": ttd_workflows.EnhancedNielsenReportingOptions.NONE,
                "gender": ttd_workflows.TargetingGender.FEMALE,
                "start_age": ttd_workflows.TargetingStartAge.SIXTY_FIVE,
                "end_age": ttd_workflows.TargetingEndAge.TWENTY_NINE,
                "countries": [
                    "<value>",
                ],
            },
            "new_frequency_configs": [
                {
                    "counter_name": "<value>",
                    "frequency_cap": 746348,
                    "frequency_goal": 510683,
                    "reset_interval_in_minutes": 129092,
                },
                {
                    "counter_name": "<value>",
                    "frequency_cap": 755997,
                    "frequency_goal": 198769,
                    "reset_interval_in_minutes": 168827,
                },
            ],
            "flights": [
                {
                    "allocation_type": ttd_workflows.AllocationType.FIXED,
                    "budget_in_advertiser_currency": 1595.69,
                    "budget_in_impressions": 474397,
                    "daily_target_in_advertiser_currency": 7814.66,
                    "daily_target_in_impressions": 542673,
                    "campaign_flight_id": 136905,
                },
                {
                    "allocation_type": ttd_workflows.AllocationType.FIXED,
                    "budget_in_advertiser_currency": 3145.56,
                    "budget_in_impressions": 465009,
                    "daily_target_in_advertiser_currency": 8108.2,
                    "daily_target_in_impressions": 109630,
                    "campaign_flight_id": 186465,
                },
                {
                    "allocation_type": ttd_workflows.AllocationType.FIXED,
                    "budget_in_advertiser_currency": 2666.4,
                    "budget_in_impressions": 593663,
                    "daily_target_in_advertiser_currency": 2585.24,
                    "daily_target_in_impressions": 42750,
                    "campaign_flight_id": 597076,
                },
            ],
        },
    },
        RetryConfig("backoff", BackoffStrategy(1, 50, 1.1, 100), False))

    # Handle response
    print(res)

```

If you'd like to override the default retry strategy for all operations that support retries, you can use the `retry_config` optional parameter when initializing the SDK:
```python
import os
import ttd_workflows
from ttd_workflows import Workflows
from ttd_workflows.utils import BackoffStrategy, RetryConfig


with Workflows(
    retry_config=RetryConfig("backoff", BackoffStrategy(1, 50, 1.1, 100), False),
    ttd_auth=os.getenv("WORKFLOWS_TTD_AUTH", ""),
) as workflows:

    res = workflows.ad_group.post_adgroup(request={
        "name": "<value>",
        "is_enabled": True,
        "description": "whose countess instead helplessly honestly unblinking hence opposite",
        "programmatic_guaranteed_private_contract_id": "<id>",
        "channel": ttd_workflows.AdGroupChannel.NATIVE,
        "funnel_location": ttd_workflows.AdGroupFunnelLocation.NONE,
        "budget": {
            "allocation_type": ttd_workflows.AllocationType.FIXED,
            "budget_in_advertiser_currency": 1255.27,
            "budget_in_impressions": 469226,
            "daily_target_in_advertiser_currency": 7461.36,
            "daily_target_in_impressions": 790907,
        },
        "base_bid_cpm_in_advertiser_currency": 310.16,
        "max_bid_cpm_in_advertiser_currency": 2360.6,
        "audience_targeting": {
            "audience_id": "<id>",
            "audience_accelerator_exclusions_enabled": False,
            "audience_booster_enabled": False,
            "audience_excluder_enabled": True,
            "audience_predictor_enabled": False,
            "cross_device_vendor_list_for_audience": [
                614673,
                684382,
            ],
            "recency_exclusion_window_in_minutes": 262820,
            "target_trackable_users_enabled": True,
            "use_mc_id_as_primary": True,
        },
        "roi_goal": {
            "maximize_reach": False,
            "maximize_ltv_incremental_reach": False,
            "cpc_in_advertiser_currency": 3537.6,
            "ctr_in_percent": 6333.79,
            "nielsen_otp_in_percent": 8443.6,
            "cpa_in_advertiser_currency": 8183.4,
            "return_on_ad_spend_percent": 9749.47,
            "vcr_in_percent": 5244.57,
            "viewability_in_percent": 1797.09,
            "vcpm_in_advertiser_currency": 9777.89,
            "cpcv_in_advertiser_currency": 4506.52,
            "miaozhen_otp_in_percent": 5639.62,
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
        "campaign_id": "<id>",
        "advanced_settings": {
            "koa_optimization_settings": {
                "are_future_koa_features_enabled": True,
                "predictive_clearing_enabled": True,
            },
            "comscore_settings": {
                "is_enabled": True,
                "population_id": 133150,
                "demographic_member_ids": [
                    199046,
                ],
                "mobile_demographic_member_ids": [
                    964861,
                    667844,
                ],
            },
            "contract_targeting": {
                "allow_open_market_bidding_when_targeting_contracts": True,
            },
            "dimensional_bidding_auto_optimization_settings": [
                [
                    ttd_workflows.DimensionalBiddingDimensions.HAS_VIDEO_COMPLETION_RATE_SCORE_RANGE,
                    ttd_workflows.DimensionalBiddingDimensions.HAS_FULL_REFERRER_URL,
                ],
                [],
                [
                    ttd_workflows.DimensionalBiddingDimensions.HAS_SELLER_ID,
                ],
            ],
            "is_use_clicks_as_conversions_enabled": True,
            "is_use_secondary_conversions_enabled": True,
            "nielsen_tracking_attributes": {
                "enhanced_reporting_option": ttd_workflows.EnhancedNielsenReportingOptions.NONE,
                "gender": ttd_workflows.TargetingGender.FEMALE,
                "start_age": ttd_workflows.TargetingStartAge.SIXTY_FIVE,
                "end_age": ttd_workflows.TargetingEndAge.TWENTY_NINE,
                "countries": [
                    "<value>",
                ],
            },
            "new_frequency_configs": [
                {
                    "counter_name": "<value>",
                    "frequency_cap": 746348,
                    "frequency_goal": 510683,
                    "reset_interval_in_minutes": 129092,
                },
                {
                    "counter_name": "<value>",
                    "frequency_cap": 755997,
                    "frequency_goal": 198769,
                    "reset_interval_in_minutes": 168827,
                },
            ],
            "flights": [
                {
                    "allocation_type": ttd_workflows.AllocationType.FIXED,
                    "budget_in_advertiser_currency": 1595.69,
                    "budget_in_impressions": 474397,
                    "daily_target_in_advertiser_currency": 7814.66,
                    "daily_target_in_impressions": 542673,
                    "campaign_flight_id": 136905,
                },
                {
                    "allocation_type": ttd_workflows.AllocationType.FIXED,
                    "budget_in_advertiser_currency": 3145.56,
                    "budget_in_impressions": 465009,
                    "daily_target_in_advertiser_currency": 8108.2,
                    "daily_target_in_impressions": 109630,
                    "campaign_flight_id": 186465,
                },
                {
                    "allocation_type": ttd_workflows.AllocationType.FIXED,
                    "budget_in_advertiser_currency": 2666.4,
                    "budget_in_impressions": 593663,
                    "daily_target_in_advertiser_currency": 2585.24,
                    "daily_target_in_impressions": 42750,
                    "campaign_flight_id": 597076,
                },
            ],
        },
    })

    # Handle response
    print(res)

```
<!-- End Retries [retries] -->

<!-- Start Error Handling [errors] -->
## Error Handling

Handling errors in this SDK should largely match your expectations. All operations return a response object or raise an exception.

By default, an API error will raise a models.APIError exception, which has the following properties:

| Property        | Type             | Description           |
|-----------------|------------------|-----------------------|
| `.status_code`  | *int*            | The HTTP status code  |
| `.message`      | *str*            | The error message     |
| `.raw_response` | *httpx.Response* | The raw HTTP response |
| `.body`         | *str*            | The response content  |

When custom error responses are specified for an operation, the SDK may also raise their associated exceptions. You can refer to respective *Errors* tables in SDK docs for more details on possible exception types for each operation. For example, the `post_adgroup_async` method may raise the following exceptions:

| Error Type                 | Status Code | Content Type     |
| -------------------------- | ----------- | ---------------- |
| models.ProblemDetailsError | 400         | application/json |
| models.APIError            | 4XX, 5XX    | \*/\*            |

### Example

```python
import os
import ttd_workflows
from ttd_workflows import Workflows, models


with Workflows(
    ttd_auth=os.getenv("WORKFLOWS_TTD_AUTH", ""),
) as workflows:
    res = None
    try:

        res = workflows.ad_group.post_adgroup(request={
            "name": "<value>",
            "is_enabled": True,
            "description": "whose countess instead helplessly honestly unblinking hence opposite",
            "programmatic_guaranteed_private_contract_id": "<id>",
            "channel": ttd_workflows.AdGroupChannel.NATIVE,
            "funnel_location": ttd_workflows.AdGroupFunnelLocation.NONE,
            "budget": {
                "allocation_type": ttd_workflows.AllocationType.FIXED,
                "budget_in_advertiser_currency": 1255.27,
                "budget_in_impressions": 469226,
                "daily_target_in_advertiser_currency": 7461.36,
                "daily_target_in_impressions": 790907,
            },
            "base_bid_cpm_in_advertiser_currency": 310.16,
            "max_bid_cpm_in_advertiser_currency": 2360.6,
            "audience_targeting": {
                "audience_id": "<id>",
                "audience_accelerator_exclusions_enabled": False,
                "audience_booster_enabled": False,
                "audience_excluder_enabled": True,
                "audience_predictor_enabled": False,
                "cross_device_vendor_list_for_audience": [
                    614673,
                    684382,
                ],
                "recency_exclusion_window_in_minutes": 262820,
                "target_trackable_users_enabled": True,
                "use_mc_id_as_primary": True,
            },
            "roi_goal": {
                "maximize_reach": False,
                "maximize_ltv_incremental_reach": False,
                "cpc_in_advertiser_currency": 3537.6,
                "ctr_in_percent": 6333.79,
                "nielsen_otp_in_percent": 8443.6,
                "cpa_in_advertiser_currency": 8183.4,
                "return_on_ad_spend_percent": 9749.47,
                "vcr_in_percent": 5244.57,
                "viewability_in_percent": 1797.09,
                "vcpm_in_advertiser_currency": 9777.89,
                "cpcv_in_advertiser_currency": 4506.52,
                "miaozhen_otp_in_percent": 5639.62,
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
            "campaign_id": "<id>",
            "advanced_settings": {
                "koa_optimization_settings": {
                    "are_future_koa_features_enabled": True,
                    "predictive_clearing_enabled": True,
                },
                "comscore_settings": {
                    "is_enabled": True,
                    "population_id": 133150,
                    "demographic_member_ids": [
                        199046,
                    ],
                    "mobile_demographic_member_ids": [
                        964861,
                        667844,
                    ],
                },
                "contract_targeting": {
                    "allow_open_market_bidding_when_targeting_contracts": True,
                },
                "dimensional_bidding_auto_optimization_settings": [
                    [
                        ttd_workflows.DimensionalBiddingDimensions.HAS_VIDEO_COMPLETION_RATE_SCORE_RANGE,
                        ttd_workflows.DimensionalBiddingDimensions.HAS_FULL_REFERRER_URL,
                    ],
                    [],
                    [
                        ttd_workflows.DimensionalBiddingDimensions.HAS_SELLER_ID,
                    ],
                ],
                "is_use_clicks_as_conversions_enabled": True,
                "is_use_secondary_conversions_enabled": True,
                "nielsen_tracking_attributes": {
                    "enhanced_reporting_option": ttd_workflows.EnhancedNielsenReportingOptions.NONE,
                    "gender": ttd_workflows.TargetingGender.FEMALE,
                    "start_age": ttd_workflows.TargetingStartAge.SIXTY_FIVE,
                    "end_age": ttd_workflows.TargetingEndAge.TWENTY_NINE,
                    "countries": [
                        "<value>",
                    ],
                },
                "new_frequency_configs": [
                    {
                        "counter_name": "<value>",
                        "frequency_cap": 746348,
                        "frequency_goal": 510683,
                        "reset_interval_in_minutes": 129092,
                    },
                    {
                        "counter_name": "<value>",
                        "frequency_cap": 755997,
                        "frequency_goal": 198769,
                        "reset_interval_in_minutes": 168827,
                    },
                ],
                "flights": [
                    {
                        "allocation_type": ttd_workflows.AllocationType.FIXED,
                        "budget_in_advertiser_currency": 1595.69,
                        "budget_in_impressions": 474397,
                        "daily_target_in_advertiser_currency": 7814.66,
                        "daily_target_in_impressions": 542673,
                        "campaign_flight_id": 136905,
                    },
                    {
                        "allocation_type": ttd_workflows.AllocationType.FIXED,
                        "budget_in_advertiser_currency": 3145.56,
                        "budget_in_impressions": 465009,
                        "daily_target_in_advertiser_currency": 8108.2,
                        "daily_target_in_impressions": 109630,
                        "campaign_flight_id": 186465,
                    },
                    {
                        "allocation_type": ttd_workflows.AllocationType.FIXED,
                        "budget_in_advertiser_currency": 2666.4,
                        "budget_in_impressions": 593663,
                        "daily_target_in_advertiser_currency": 2585.24,
                        "daily_target_in_impressions": 42750,
                        "campaign_flight_id": 597076,
                    },
                ],
            },
        })

        # Handle response
        print(res)

    except models.ProblemDetailsError as e:
        # handle e.data: models.ProblemDetailsErrorData
        raise(e)
    except models.APIError as e:
        # handle exception
        raise(e)
```
<!-- End Error Handling [errors] -->

<!-- Start Server Selection [server] -->
## Server Selection

### Override Server URL Per-Client

The default server can be overridden globally by passing a URL to the `server_url: str` optional parameter when initializing the SDK client instance. For example:
```python
import os
import ttd_workflows
from ttd_workflows import Workflows


with Workflows(
    server_url="https://api.thetradedesk.com/workflows",
    ttd_auth=os.getenv("WORKFLOWS_TTD_AUTH", ""),
) as workflows:

    res = workflows.ad_group.post_adgroup(request={
        "name": "<value>",
        "is_enabled": True,
        "description": "whose countess instead helplessly honestly unblinking hence opposite",
        "programmatic_guaranteed_private_contract_id": "<id>",
        "channel": ttd_workflows.AdGroupChannel.NATIVE,
        "funnel_location": ttd_workflows.AdGroupFunnelLocation.NONE,
        "budget": {
            "allocation_type": ttd_workflows.AllocationType.FIXED,
            "budget_in_advertiser_currency": 1255.27,
            "budget_in_impressions": 469226,
            "daily_target_in_advertiser_currency": 7461.36,
            "daily_target_in_impressions": 790907,
        },
        "base_bid_cpm_in_advertiser_currency": 310.16,
        "max_bid_cpm_in_advertiser_currency": 2360.6,
        "audience_targeting": {
            "audience_id": "<id>",
            "audience_accelerator_exclusions_enabled": False,
            "audience_booster_enabled": False,
            "audience_excluder_enabled": True,
            "audience_predictor_enabled": False,
            "cross_device_vendor_list_for_audience": [
                614673,
                684382,
            ],
            "recency_exclusion_window_in_minutes": 262820,
            "target_trackable_users_enabled": True,
            "use_mc_id_as_primary": True,
        },
        "roi_goal": {
            "maximize_reach": False,
            "maximize_ltv_incremental_reach": False,
            "cpc_in_advertiser_currency": 3537.6,
            "ctr_in_percent": 6333.79,
            "nielsen_otp_in_percent": 8443.6,
            "cpa_in_advertiser_currency": 8183.4,
            "return_on_ad_spend_percent": 9749.47,
            "vcr_in_percent": 5244.57,
            "viewability_in_percent": 1797.09,
            "vcpm_in_advertiser_currency": 9777.89,
            "cpcv_in_advertiser_currency": 4506.52,
            "miaozhen_otp_in_percent": 5639.62,
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
        "campaign_id": "<id>",
        "advanced_settings": {
            "koa_optimization_settings": {
                "are_future_koa_features_enabled": True,
                "predictive_clearing_enabled": True,
            },
            "comscore_settings": {
                "is_enabled": True,
                "population_id": 133150,
                "demographic_member_ids": [
                    199046,
                ],
                "mobile_demographic_member_ids": [
                    964861,
                    667844,
                ],
            },
            "contract_targeting": {
                "allow_open_market_bidding_when_targeting_contracts": True,
            },
            "dimensional_bidding_auto_optimization_settings": [
                [
                    ttd_workflows.DimensionalBiddingDimensions.HAS_VIDEO_COMPLETION_RATE_SCORE_RANGE,
                    ttd_workflows.DimensionalBiddingDimensions.HAS_FULL_REFERRER_URL,
                ],
                [],
                [
                    ttd_workflows.DimensionalBiddingDimensions.HAS_SELLER_ID,
                ],
            ],
            "is_use_clicks_as_conversions_enabled": True,
            "is_use_secondary_conversions_enabled": True,
            "nielsen_tracking_attributes": {
                "enhanced_reporting_option": ttd_workflows.EnhancedNielsenReportingOptions.NONE,
                "gender": ttd_workflows.TargetingGender.FEMALE,
                "start_age": ttd_workflows.TargetingStartAge.SIXTY_FIVE,
                "end_age": ttd_workflows.TargetingEndAge.TWENTY_NINE,
                "countries": [
                    "<value>",
                ],
            },
            "new_frequency_configs": [
                {
                    "counter_name": "<value>",
                    "frequency_cap": 746348,
                    "frequency_goal": 510683,
                    "reset_interval_in_minutes": 129092,
                },
                {
                    "counter_name": "<value>",
                    "frequency_cap": 755997,
                    "frequency_goal": 198769,
                    "reset_interval_in_minutes": 168827,
                },
            ],
            "flights": [
                {
                    "allocation_type": ttd_workflows.AllocationType.FIXED,
                    "budget_in_advertiser_currency": 1595.69,
                    "budget_in_impressions": 474397,
                    "daily_target_in_advertiser_currency": 7814.66,
                    "daily_target_in_impressions": 542673,
                    "campaign_flight_id": 136905,
                },
                {
                    "allocation_type": ttd_workflows.AllocationType.FIXED,
                    "budget_in_advertiser_currency": 3145.56,
                    "budget_in_impressions": 465009,
                    "daily_target_in_advertiser_currency": 8108.2,
                    "daily_target_in_impressions": 109630,
                    "campaign_flight_id": 186465,
                },
                {
                    "allocation_type": ttd_workflows.AllocationType.FIXED,
                    "budget_in_advertiser_currency": 2666.4,
                    "budget_in_impressions": 593663,
                    "daily_target_in_advertiser_currency": 2585.24,
                    "daily_target_in_impressions": 42750,
                    "campaign_flight_id": 597076,
                },
            ],
        },
    })

    # Handle response
    print(res)

```
<!-- End Server Selection [server] -->

<!-- Start Custom HTTP Client [http-client] -->
## Custom HTTP Client

The Python SDK makes API calls using the [httpx](https://www.python-httpx.org/) HTTP library.  In order to provide a convenient way to configure timeouts, cookies, proxies, custom headers, and other low-level configuration, you can initialize the SDK client with your own HTTP client instance.
Depending on whether you are using the sync or async version of the SDK, you can pass an instance of `HttpClient` or `AsyncHttpClient` respectively, which are Protocol's ensuring that the client has the necessary methods to make API calls.
This allows you to wrap the client with your own custom logic, such as adding custom headers, logging, or error handling, or you can just pass an instance of `httpx.Client` or `httpx.AsyncClient` directly.

For example, you could specify a header for every request that this sdk makes as follows:
```python
from ttd_workflows import Workflows
import httpx

http_client = httpx.Client(headers={"x-custom-header": "someValue"})
s = Workflows(client=http_client)
```

or you could wrap the client with your own custom logic:
```python
from ttd_workflows import Workflows
from ttd_workflows.httpclient import AsyncHttpClient
import httpx

class CustomClient(AsyncHttpClient):
    client: AsyncHttpClient

    def __init__(self, client: AsyncHttpClient):
        self.client = client

    async def send(
        self,
        request: httpx.Request,
        *,
        stream: bool = False,
        auth: Union[
            httpx._types.AuthTypes, httpx._client.UseClientDefault, None
        ] = httpx.USE_CLIENT_DEFAULT,
        follow_redirects: Union[
            bool, httpx._client.UseClientDefault
        ] = httpx.USE_CLIENT_DEFAULT,
    ) -> httpx.Response:
        request.headers["Client-Level-Header"] = "added by client"

        return await self.client.send(
            request, stream=stream, auth=auth, follow_redirects=follow_redirects
        )

    def build_request(
        self,
        method: str,
        url: httpx._types.URLTypes,
        *,
        content: Optional[httpx._types.RequestContent] = None,
        data: Optional[httpx._types.RequestData] = None,
        files: Optional[httpx._types.RequestFiles] = None,
        json: Optional[Any] = None,
        params: Optional[httpx._types.QueryParamTypes] = None,
        headers: Optional[httpx._types.HeaderTypes] = None,
        cookies: Optional[httpx._types.CookieTypes] = None,
        timeout: Union[
            httpx._types.TimeoutTypes, httpx._client.UseClientDefault
        ] = httpx.USE_CLIENT_DEFAULT,
        extensions: Optional[httpx._types.RequestExtensions] = None,
    ) -> httpx.Request:
        return self.client.build_request(
            method,
            url,
            content=content,
            data=data,
            files=files,
            json=json,
            params=params,
            headers=headers,
            cookies=cookies,
            timeout=timeout,
            extensions=extensions,
        )

s = Workflows(async_client=CustomClient(httpx.AsyncClient()))
```
<!-- End Custom HTTP Client [http-client] -->

<!-- Start Resource Management [resource-management] -->
## Resource Management

The `Workflows` class implements the context manager protocol and registers a finalizer function to close the underlying sync and async HTTPX clients it uses under the hood. This will close HTTP connections, release memory and free up other resources held by the SDK. In short-lived Python programs and notebooks that make a few SDK method calls, resource management may not be a concern. However, in longer-lived programs, it is beneficial to create a single SDK instance via a [context manager][context-manager] and reuse it across the application.

[context-manager]: https://docs.python.org/3/reference/datamodel.html#context-managers

```python
import os
from ttd_workflows import Workflows
def main():

    with Workflows(
        ttd_auth=os.getenv("WORKFLOWS_TTD_AUTH", ""),
    ) as workflows:
        # Rest of application here...


# Or when using async:
async def amain():

    async with Workflows(
        ttd_auth=os.getenv("WORKFLOWS_TTD_AUTH", ""),
    ) as workflows:
        # Rest of application here...
```
<!-- End Resource Management [resource-management] -->

<!-- Start Debugging [debug] -->
## Debugging

You can setup your SDK to emit debug logs for SDK requests and responses.

You can pass your own logger class directly into your SDK.
```python
from ttd_workflows import Workflows
import logging

logging.basicConfig(level=logging.DEBUG)
s = Workflows(debug_logger=logging.getLogger("ttd_workflows"))
```

You can also enable a default debug logger by setting an environment variable `WORKFLOWS_DEBUG` to true.
<!-- End Debugging [debug] -->

<!-- Placeholder for Future Speakeasy SDK Sections -->
