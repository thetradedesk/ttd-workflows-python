# Campaigns
(*campaigns*)

## Overview

### Available Operations

* [update](#update) - Update a campaign with specified fields
* [archive](#archive) - Archive multiple campaigns

## update

Only the fields provided in the request payload will be updated.

### Example Usage

<!-- UsageSnippet language="python" operationID="updateCampaign" method="patch" path="/campaign" -->
```python
import os
import ttd_workflows
from ttd_workflows import Workflows
from ttd_workflows.utils import parse_datetime


with Workflows(
    ttd_auth=os.getenv("WORKFLOWS_TTD_AUTH", ""),
) as workflows:

    res = workflows.campaigns.update(request=ttd_workflows.CampaignUpdateWorkflowInputWithValidation(
        id="<id>",
        primary_input=ttd_workflows.CampaignUpdateWorkflowPrimaryInput(
            description="yahoo whether frail but into form sway neck notwithstanding",
            campaign_group_id=760468,
            time_zone="Asia/Amman",
            custom_cpa_click_weight=1380.93,
            custom_cpa_viewthrough_weight=3991.98,
            custom_cpa_type=ttd_workflows.CustomCPAType.CLICK_VIEWTHROUGH_WEIGHTING,
            custom_roas_type=ttd_workflows.CustomROASType.DISABLED,
            impressions_only_budgeting_cpm=126.57,
            budget=ttd_workflows.CampaignWorkflowBudgetInput(
                pacing_mode=ttd_workflows.CampaignPacingMode.PACE_AS_SOON_AS_POSSIBLE,
                budget_in_advertiser_currency=6974.82,
                budget_in_impressions=834352,
                daily_target_in_advertiser_currency=8583.49,
                daily_target_in_impressions=746941,
            ),
            end_date_in_utc=parse_datetime("2024-07-09T17:14:23.542Z"),
            seed_id="<id>",
            campaign_conversion_reporting_columns=[
                ttd_workflows.CampaignWorkflowCampaignConversionReportingColumnInput(
                    tracking_tag_id="<id>",
                    include_in_custom_cpa=False,
                    reporting_column_id=716444,
                    roas_config=ttd_workflows.CustomROASConfig(
                        include_in_custom_roas=True,
                        custom_roas_weight=8307.9,
                        custom_roas_click_weight=129.65,
                        custom_roas_viewthrough_weight=2890.82,
                    ),
                    weight=5187.48,
                    cross_device_attribution_model_id=None,
                ),
            ],
            is_managed_by_ttd=False,
            secondary_goal=ttd_workflows.CampaignWorkflowROIGoalInput(
                maximize_reach=True,
                maximize_ltv_incremental_reach=False,
                cpc_in_advertiser_currency=1165.14,
                ctr_in_percent=5157.73,
                nielsen_otp_in_percent=3855.93,
                cpa_in_advertiser_currency=5164.28,
                return_on_ad_spend_percent=8554.35,
                vcr_in_percent=9569.97,
                viewability_in_percent=9650.33,
                vcpm_in_advertiser_currency=5268.69,
                cpcv_in_advertiser_currency=7216.52,
                miaozhen_otp_in_percent=6966.26,
                iqvia_audience_quality_index=True,
                crossix_audience_quality_index=True,
                iqvia_audience_quality_index_and_cost_per_target=True,
                crossix_cost_per_target=True,
            ),
            tertiary_goal=ttd_workflows.CampaignWorkflowROIGoalInput(
                maximize_reach=True,
                maximize_ltv_incremental_reach=True,
                cpc_in_advertiser_currency=5149.5,
                ctr_in_percent=5602.97,
                nielsen_otp_in_percent=3514.56,
                cpa_in_advertiser_currency=1.97,
                return_on_ad_spend_percent=3177.79,
                vcr_in_percent=5564.63,
                viewability_in_percent=472.11,
                vcpm_in_advertiser_currency=4614.14,
                cpcv_in_advertiser_currency=8553.51,
                miaozhen_otp_in_percent=5511.72,
                iqvia_audience_quality_index=False,
                crossix_audience_quality_index=False,
                iqvia_audience_quality_index_and_cost_per_target=None,
                crossix_cost_per_target=False,
            ),
            name="<value>",
            primary_channel=ttd_workflows.CampaignChannelType.DISPLAY,
            primary_goal=ttd_workflows.CampaignWorkflowROIGoalInput(
                maximize_reach=False,
                maximize_ltv_incremental_reach=True,
                cpc_in_advertiser_currency=8835.54,
                ctr_in_percent=4975.78,
                nielsen_otp_in_percent=6033.78,
                cpa_in_advertiser_currency=None,
                return_on_ad_spend_percent=5696.08,
                vcr_in_percent=8315.31,
                viewability_in_percent=1059.68,
                vcpm_in_advertiser_currency=4588.07,
                cpcv_in_advertiser_currency=2202.71,
                miaozhen_otp_in_percent=2682.12,
                iqvia_audience_quality_index=False,
                crossix_audience_quality_index=True,
                iqvia_audience_quality_index_and_cost_per_target=True,
                crossix_cost_per_target=True,
            ),
            start_date_in_utc=parse_datetime("2024-02-29T10:31:50.069Z"),
        ),
        advanced_input=ttd_workflows.CampaignUpdateWorkflowAdvancedInput(
            flights=[
                ttd_workflows.CampaignWorkflowFlightInput(
                    start_date_inclusive_utc=parse_datetime("2025-11-09T04:11:39.432Z"),
                    end_date_exclusive_utc=parse_datetime("2025-09-10T20:38:51.701Z"),
                    budget_in_advertiser_currency=6534.57,
                    budget_in_impressions=865481,
                    daily_target_in_advertiser_currency=1033.72,
                    daily_target_in_impressions=None,
                ),
            ],
            purchase_order_number="<value>",
        ),
        validate_input_only=True,
    ))

    assert res.campaign_payload is not None

    # Handle response
    print(res.campaign_payload)

```

### Parameters

| Parameter                                                                                                     | Type                                                                                                          | Required                                                                                                      | Description                                                                                                   |
| ------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                     | [models.CampaignUpdateWorkflowInputWithValidation](../../models/campaignupdateworkflowinputwithvalidation.md) | :heavy_check_mark:                                                                                            | The request object to use for the request.                                                                    |
| `retries`                                                                                                     | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                              | :heavy_minus_sign:                                                                                            | Configuration to override the default retry behavior of the client.                                           |

### Response

**[models.UpdateCampaignResponse](../../models/updatecampaignresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.ProblemDetailsError | 400                        | application/json           |
| models.APIError            | 4XX, 5XX                   | \*/\*                      |

## archive

**NOTE**: Once archived, campaigns cannot be un-archived.

### Example Usage

<!-- UsageSnippet language="python" operationID="archiveCampaigns" method="post" path="/campaign/archive" -->
```python
import os
from ttd_workflows import Workflows


with Workflows(
    ttd_auth=os.getenv("WORKFLOWS_TTD_AUTH", ""),
) as workflows:

    res = workflows.campaigns.archive(force_archive=False, request_body=[
        "<value 1>",
        "<value 2>",
        "<value 3>",
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

**[models.ArchiveCampaignsResponse](../../models/archivecampaignsresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.ProblemDetailsError | 400, 403                   | application/json           |
| models.APIError            | 4XX, 5XX                   | \*/\*                      |