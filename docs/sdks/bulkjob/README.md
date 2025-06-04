# BulkJob
(*bulk_job*)

## Overview

### Available Operations

* [post_bulkjob_thirdpartydata](#post_bulkjob_thirdpartydata) - Submits a query for Third Party Data to Hydra

## post_bulkjob_thirdpartydata

Submits a query for Third Party Data to Hydra

### Example Usage

```python
import os
from ttd_workflows import Workflows


with Workflows(
    ttd_auth=os.getenv("WORKFLOWS_TTD_AUTH", ""),
) as workflows:

    res = workflows.bulk_job.post_bulkjob_thirdpartydata(request={
        "partner_id": "<id>",
        "query_shape": "<value>",
        "callback_input": {
            "callback_url": "https://impolite-coal.name/",
            "callback_headers": {
                "key": "<value>",
                "key1": "<value>",
                "key2": "<value>",
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

**[models.BulkJobSubmitResponse](../../models/bulkjobsubmitresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.ProblemDetailsError | 400, 401, 403, 404         | application/json           |
| models.APIError            | 4XX, 5XX                   | \*/\*                      |