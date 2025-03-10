# SeedCreationInput

Required fields for creating a new seed


## Fields

| Field                                                                | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `advertiser_id`                                                      | *str*                                                                | :heavy_check_mark:                                                   | The platform ID of the advertiser that owns this Seed.               |
| `seed_name`                                                          | *str*                                                                | :heavy_check_mark:                                                   | The name of the Seed.                                                |
| `is_default`                                                         | *bool*                                                               | :heavy_check_mark:                                                   | Whether this is the default seed for this advertiser                 |
| `targeting_data`                                                     | [models.SeedTargetingDataInput](../models/seedtargetingdatainput.md) | :heavy_check_mark:                                                   | N/A                                                                  |