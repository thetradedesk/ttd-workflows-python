# CampaignWorkflowCampaignConversionReportingColumnInput


## Fields

| Field                                                              | Type                                                               | Required                                                           | Description                                                        |
| ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ |
| `tracking_tag_id`                                                  | *str*                                                              | :heavy_check_mark:                                                 | N/A                                                                |
| `include_in_custom_cpa`                                            | *bool*                                                             | :heavy_check_mark:                                                 | N/A                                                                |
| `reporting_column_id`                                              | *int*                                                              | :heavy_check_mark:                                                 | N/A                                                                |
| `roas_config`                                                      | [Optional[models.CustomROASConfig]](../models/customroasconfig.md) | :heavy_minus_sign:                                                 | N/A                                                                |
| `weight`                                                           | *OptionalNullable[float]*                                          | :heavy_minus_sign:                                                 | N/A                                                                |
| `cross_device_attribution_model_id`                                | *OptionalNullable[str]*                                            | :heavy_minus_sign:                                                 | N/A                                                                |