# SeedSDK
(*seed*)

## Overview

### Available Operations

* [create](#create) - Create a new seed with required fields

## create

Create a new seed with required fields

### Example Usage

```python
import os
from ttd_workflows import Workflows


with Workflows(
    ttd_auth=os.getenv("WORKFLOWS_TTD_AUTH", ""),
) as workflows:

    res = workflows.seed.create(request={
        "advertiser_id": "<id>",
        "seed_name": "<value>",
        "is_default": True,
        "targeting_data": {
            "first_party_data_inclusion_ids": [
                417458,
                134365,
            ],
            "retail_data_inclusion": [
                {
                    "third_party_data_id": 796474,
                    "third_party_data_brand_id": "<id>",
                },
            ],
            "third_party_data_inclusion": [
                {
                    "third_party_data_id": 86,
                    "third_party_data_brand_id": "<id>",
                },
                {
                    "third_party_data_id": 169727,
                    "third_party_data_brand_id": "<id>",
                },
                {
                    "third_party_data_id": 89964,
                    "third_party_data_brand_id": "<id>",
                },
            ],
            "contextual_inclusion": {
                "keyphrases": [
                    "<value>",
                    "<value>",
                    "<value>",
                ],
                "urls": [
                    "<value>",
                    "<value>",
                    "<value>",
                ],
            },
            "country_filter_ids": [
                "<value>",
                "<value>",
            ],
        },
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [models.SeedCreationInput](../../models/seedcreationinput.md)       | :heavy_check_mark:                                                  | The request object to use for the request.                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.Seed](../../models/seed.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.ProblemDetailsError | 400                        | application/json           |
| models.APIError            | 4XX, 5XX                   | \*/\*                      |