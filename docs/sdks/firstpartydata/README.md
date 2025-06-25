# FirstPartyData
(*first_party_data*)

## Overview

### Available Operations

* [post_typebasedjob_firstpartydata](#post_typebasedjob_firstpartydata) - Submit a type-based job for first-party data retrieval for an advertiser

## post_typebasedjob_firstpartydata

When a first-party data query is submitted, a job ID is returned.
This job ID can be used to poll for the job's status using the associated operation under "Job Status".

### Example Usage

```python
import os
from ttd_workflows import Workflows


with Workflows(
    ttd_auth=os.getenv("WORKFLOWS_TTD_AUTH", ""),
) as workflows:

    res = workflows.first_party_data.post_typebasedjob_firstpartydata(request={
        "advertiser_id": "<id>",
        "name_filter": "<value>",
        "query_shape": None,
        "callback_input": {
            "callback_url": "https://ashamed-traffic.info",
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
| `request`                                                           | [models.FirstPartyDataInput](../../models/firstpartydatainput.md)   | :heavy_check_mark:                                                  | The request object to use for the request.                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.TypeBasedJobSubmitResponse](../../models/typebasedjobsubmitresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.ProblemDetailsError | 400, 401, 403, 404         | application/json           |
| models.APIError            | 4XX, 5XX                   | \*/\*                      |