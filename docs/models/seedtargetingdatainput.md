# SeedTargetingDataInput


## Fields

| Field                                                                    | Type                                                                     | Required                                                                 | Description                                                              |
| ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ |
| `first_party_data_inclusion_ids`                                         | List[*int*]                                                              | :heavy_minus_sign:                                                       | These are the AdvertiserTargetingDataIds for first party data.           |
| `retail_data_inclusion`                                                  | List[[models.ThirdPartyDataInput](../models/thirdpartydatainput.md)]     | :heavy_minus_sign:                                                       | RetailDataInclusion                                                      |
| `third_party_data_inclusion`                                             | List[[models.ThirdPartyDataInput](../models/thirdpartydatainput.md)]     | :heavy_minus_sign:                                                       | ThirdPartyDataInclusion                                                  |
| `contextual_inclusion`                                                   | [Optional[models.ContextualDataInput]](../models/contextualdatainput.md) | :heavy_minus_sign:                                                       | N/A                                                                      |
| `country_filter_ids`                                                     | List[*str*]                                                              | :heavy_minus_sign:                                                       | CountryFilterIds                                                         |