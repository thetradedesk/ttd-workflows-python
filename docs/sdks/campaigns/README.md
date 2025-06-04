# Campaigns
(*campaigns*)

## Overview

### Available Operations

* [update](#update) - Update an existing campaign with specified fields
* [bulk_create](#bulk_create) - Create a list of campaigns with required fields. `ValidateInputOnly` value should be the same for all campaigns.
* [bulk_update](#bulk_update) - Update a list of existing campaigns with specified fields. `ValidateInputOnly` value should be the same for all campaigns.
* [archive](#archive) - Archive a list of campaigns

## update

Update an existing campaign with specified fields

### Example Usage

```python
import os
import ttd_workflows
from ttd_workflows import Workflows
from ttd_workflows.utils import parse_datetime


with Workflows(
    ttd_auth=os.getenv("WORKFLOWS_TTD_AUTH", ""),
) as workflows:

    res = workflows.campaigns.update(request={
        "primary_input": {
            "description": "until notwithstanding bump",
            "time_zone": None,
            "custom_cpa_click_weight": 6995,
            "custom_cpa_viewthrough_weight": 8563.38,
            "custom_cpa_type": ttd_workflows.CustomCPAType.DISABLED,
            "impressions_only_budgeting_cpm": 8246.96,
            "budget": {
                "pacing_mode": ttd_workflows.CampaignPacingMode.PACE_EVENLY,
                "budget_in_advertiser_currency": 8712.02,
                "budget_in_impressions": None,
                "daily_target_in_advertiser_currency": 8897.46,
                "daily_target_in_impressions": 665232,
            },
            "end_date_in_utc": None,
            "seed_id": "<id>",
            "campaign_conversion_reporting_columns": [
                {
                    "tracking_tag_id": "<id>",
                    "include_in_custom_cpa": True,
                    "reporting_column_id": 97349,
                    "roas_config": {
                        "include_in_custom_roas": False,
                        "custom_roas_weight": 4101.84,
                        "custom_roas_click_weight": None,
                        "custom_roas_viewthrough_weight": 4368.63,
                    },
                    "weight": 7340.95,
                    "cross_device_attribution_model_id": "<id>",
                },
                {
                    "tracking_tag_id": "<id>",
                    "include_in_custom_cpa": True,
                    "reporting_column_id": 97349,
                    "roas_config": {
                        "include_in_custom_roas": False,
                        "custom_roas_weight": 4101.84,
                        "custom_roas_click_weight": None,
                        "custom_roas_viewthrough_weight": 4368.63,
                    },
                    "weight": 7340.95,
                    "cross_device_attribution_model_id": "<id>",
                },
                {
                    "tracking_tag_id": "<id>",
                    "include_in_custom_cpa": True,
                    "reporting_column_id": 97349,
                    "roas_config": {
                        "include_in_custom_roas": False,
                        "custom_roas_weight": 4101.84,
                        "custom_roas_click_weight": None,
                        "custom_roas_viewthrough_weight": 4368.63,
                    },
                    "weight": 7340.95,
                    "cross_device_attribution_model_id": "<id>",
                },
            ],
            "id": "<id>",
            "name": "<value>",
            "primary_channel": ttd_workflows.CampaignChannelType.NONE,
            "primary_goal": {
                "maximize_reach": False,
                "maximize_ltv_incremental_reach": True,
                "cpc_in_advertiser_currency": 8699.49,
                "ctr_in_percent": 8949.6,
                "nielsen_otp_in_percent": 37.27,
                "cpa_in_advertiser_currency": 3521.28,
                "return_on_ad_spend_percent": 7256.13,
                "vcr_in_percent": 5452.85,
                "viewability_in_percent": 737.27,
                "vcpm_in_advertiser_currency": 1743.53,
                "cpcv_in_advertiser_currency": None,
                "miaozhen_otp_in_percent": 5666.12,
            },
            "start_date_in_utc": parse_datetime("2023-03-15T19:37:35.952Z"),
        },
        "advanced_input": {
            "flights": [
                {
                    "start_date_inclusive_utc": parse_datetime("2023-06-20T19:40:02.162Z"),
                    "end_date_exclusive_utc": parse_datetime("2025-01-24T04:52:37.846Z"),
                    "budget_in_advertiser_currency": 8764.81,
                    "budget_in_impressions": 472441,
                    "daily_target_in_advertiser_currency": 5399.55,
                    "daily_target_in_impressions": 808445,
                },
                {
                    "start_date_inclusive_utc": parse_datetime("2023-06-20T19:40:02.162Z"),
                    "end_date_exclusive_utc": parse_datetime("2025-01-24T04:52:37.846Z"),
                    "budget_in_advertiser_currency": 8764.81,
                    "budget_in_impressions": 472441,
                    "daily_target_in_advertiser_currency": 5399.55,
                    "daily_target_in_impressions": 808445,
                },
            ],
            "purchase_order_number": "<value>",
        },
        "validate_input_only": None,
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                     | Type                                                                                                          | Required                                                                                                      | Description                                                                                                   |
| ------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                     | [models.CampaignUpdateWorkflowInputWithValidation](../../models/campaignupdateworkflowinputwithvalidation.md) | :heavy_check_mark:                                                                                            | The request object to use for the request.                                                                    |
| `retries`                                                                                                     | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                              | :heavy_minus_sign:                                                                                            | Configuration to override the default retry behavior of the client.                                           |

### Response

**[models.CampaignPayload](../../models/campaignpayload.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.ProblemDetailsError | 400                        | application/json           |
| models.APIError            | 4XX, 5XX                   | \*/\*                      |

## bulk_create

Create a list of campaigns with required fields. `ValidateInputOnly` value should be the same for all campaigns.

### Example Usage

```python
import os
from ttd_workflows import Workflows


with Workflows(
    ttd_auth=os.getenv("WORKFLOWS_TTD_AUTH", ""),
) as workflows:

    res = workflows.campaigns.bulk_create(request={
        "input": None,
        "validate_input_only": True,
        "callback_input": {
            "callback_url": "https://dental-divine.org/",
            "callback_headers": {
                "key": "<value>",
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

**[models.BulkJobSubmitResponse](../../models/bulkjobsubmitresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.ProblemDetailsError | 400, 403                   | application/json           |
| models.APIError            | 4XX, 5XX                   | \*/\*                      |

## bulk_update

Update a list of existing campaigns with specified fields. `ValidateInputOnly` value should be the same for all campaigns.

### Example Usage

```python
import os
import ttd_workflows
from ttd_workflows import Workflows
from ttd_workflows.utils import parse_datetime


with Workflows(
    ttd_auth=os.getenv("WORKFLOWS_TTD_AUTH", ""),
) as workflows:

    res = workflows.campaigns.bulk_update(request={
        "input": [
            {
                "primary_input": {
                    "description": "make innocently gerbil",
                    "time_zone": "America/Halifax",
                    "custom_cpa_click_weight": 90.53,
                    "custom_cpa_viewthrough_weight": 6332.3,
                    "custom_cpa_type": ttd_workflows.CustomCPAType.DISABLED,
                    "impressions_only_budgeting_cpm": None,
                    "budget": {
                        "pacing_mode": ttd_workflows.CampaignPacingMode.PACE_TO_DAILY_CAP,
                        "budget_in_advertiser_currency": 7811.09,
                        "budget_in_impressions": None,
                        "daily_target_in_advertiser_currency": 3493.9,
                        "daily_target_in_impressions": 530411,
                    },
                    "end_date_in_utc": parse_datetime("2024-04-14T22:55:04.136Z"),
                    "seed_id": "<id>",
                    "campaign_conversion_reporting_columns": [
                        {
                            "tracking_tag_id": "<id>",
                            "include_in_custom_cpa": False,
                            "reporting_column_id": 75289,
                            "roas_config": {
                                "include_in_custom_roas": True,
                                "custom_roas_weight": 8299.16,
                                "custom_roas_click_weight": None,
                                "custom_roas_viewthrough_weight": 764.33,
                            },
                            "weight": 9258.39,
                            "cross_device_attribution_model_id": "<id>",
                        },
                    ],
                    "id": "<id>",
                    "name": "<value>",
                    "primary_channel": ttd_workflows.CampaignChannelType.DOOH,
                    "primary_goal": {
                        "maximize_reach": True,
                        "maximize_ltv_incremental_reach": False,
                        "cpc_in_advertiser_currency": 6613.91,
                        "ctr_in_percent": None,
                        "nielsen_otp_in_percent": 8409.91,
                        "cpa_in_advertiser_currency": 5081.39,
                        "return_on_ad_spend_percent": 8381.93,
                        "vcr_in_percent": 940.02,
                        "viewability_in_percent": 6474.82,
                        "vcpm_in_advertiser_currency": 8867.76,
                        "cpcv_in_advertiser_currency": 9393.86,
                        "miaozhen_otp_in_percent": 218.76,
                    },
                    "start_date_in_utc": parse_datetime("2024-01-25T12:04:17.661Z"),
                },
                "advanced_input": {
                    "flights": None,
                    "purchase_order_number": "<value>",
                },
            },
        ],
        "validate_input_only": False,
        "callback_input": {
            "callback_url": "https://grizzled-riser.com/",
            "callback_headers": {
                "key": "<value>",
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

**[models.BulkJobSubmitResponse](../../models/bulkjobsubmitresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.ProblemDetailsError | 400, 403                   | application/json           |
| models.APIError            | 4XX, 5XX                   | \*/\*                      |

## archive

Archive a list of campaigns

### Example Usage

```python
import os
from ttd_workflows import Workflows


with Workflows(
    ttd_auth=os.getenv("WORKFLOWS_TTD_AUTH", ""),
) as workflows:

    res = workflows.campaigns.archive(force_archive=False, request_body=[
        "<value 1>",
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