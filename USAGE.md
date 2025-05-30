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
        "validate_input_only": True,
    })

    assert res is not None

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

        res = await workflows.ad_groups.create_async(request={
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
            "validate_input_only": True,
        })

        assert res is not None

        # Handle response
        print(res)

asyncio.run(main())
```
<!-- End SDK Example Usage [usage] -->