<!-- Start SDK Example Usage [usage] -->
```python
# Synchronous Example
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
                "enhanced_reporting_option": ttd_workflows.EnhancedNielsenReportingOptions.SITE,
                "gender": ttd_workflows.TargetingGender.MALE,
                "start_age": ttd_workflows.TargetingStartAge.TWENTY_FIVE,
                "end_age": ttd_workflows.TargetingEndAge.SEVENTEEN,
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

</br>

The same SDK client can also be used to make asynchronous requests by importing asyncio.
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

        res = await workflows.ad_groups.create_async(request={
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
                    "enhanced_reporting_option": ttd_workflows.EnhancedNielsenReportingOptions.SITE,
                    "gender": ttd_workflows.TargetingGender.MALE,
                    "start_age": ttd_workflows.TargetingStartAge.TWENTY_FIVE,
                    "end_age": ttd_workflows.TargetingEndAge.SEVENTEEN,
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

asyncio.run(main())
```
<!-- End SDK Example Usage [usage] -->