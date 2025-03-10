# CampaignCreationInput

Schema with required fields for creating a new campaign


## Fields

| Field                                                                                | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `advertiser_id`                                                                      | *str*                                                                                | :heavy_check_mark:                                                                   | The platform ID of the advertiser that owns this Campaign.                           |
| `campaign_name`                                                                      | *str*                                                                                | :heavy_check_mark:                                                                   | The name of the Campaign.                                                            |
| `primary_channel`                                                                    | [models.CampaignChannel](../models/campaignchannel.md)                               | :heavy_check_mark:                                                                   | N/A                                                                                  |
| `primary_goal`                                                                       | [models.CampaignCreateROIGoalInput](../models/campaigncreateroigoalinput.md)         | :heavy_check_mark:                                                                   | N/A                                                                                  |
| `campaign_flights`                                                                   | List[[models.CampaignFlightCreationInput](../models/campaignflightcreationinput.md)] | :heavy_check_mark:                                                                   | The List of flights associated with the Campaign.                                    |