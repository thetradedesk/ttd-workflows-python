# Campaign
(*campaign*)

## Overview

### Available Operations

* [create](#create) - Create a new campaign with required fields
* [get_version](#get_version) - GET a campaign's version

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

| Parameter                                                                         | Type                                                                              | Required                                                                          | Description                                                                       |
| --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- |
| `request`                                                                         | [models.CampaignCreateWorkflowInput](../../models/campaigncreateworkflowinput.md) | :heavy_check_mark:                                                                | The request object to use for the request.                                        |
| `retries`                                                                         | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                  | :heavy_minus_sign:                                                                | Configuration to override the default retry behavior of the client.               |

### Response

**[models.CampaignPayload](../../models/campaignpayload.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.ProblemDetailsError | 400, 403                   | application/json           |
| models.APIError            | 4XX, 5XX                   | \*/\*                      |

## get_version

GET a campaign's version

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