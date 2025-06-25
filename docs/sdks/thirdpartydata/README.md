# ThirdPartyData
(*third_party_data*)

## Overview

### Available Operations

* [post_typebasedjob_thirdpartydata](#post_typebasedjob_thirdpartydata) - Submit a type-based job for third-party data retrieval for an advertiser

## post_typebasedjob_thirdpartydata

When a third-party data query is submitted, a job ID is returned.
This job ID can be used to poll for the job's status using the associated operation under "Job Status".

### Example Usage

```python
import os
from ttd_workflows import Workflows


with Workflows(
    ttd_auth=os.getenv("WORKFLOWS_TTD_AUTH", ""),
) as workflows:

    res = workflows.third_party_data.post_typebasedjob_thirdpartydata(request={
        "partner_id": "<id>",
        "query_shape": "<value>",
        "callback_input": {
            "callback_url": "https://colorful-utilization.com/",
            "callback_headers": {
                "key": "<value>",
                "key1": "<value>",
            },
        },
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [models.ThirdPartyDataInput](../../models/thirdpartydatainput.md)   | :heavy_check_mark:                                                  | The request object to use for the request.                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.TypeBasedJobSubmitResponse](../../models/typebasedjobsubmitresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.ProblemDetailsError | 400, 401, 403, 404         | application/json           |
| models.APIError            | 4XX, 5XX                   | \*/\*                      |