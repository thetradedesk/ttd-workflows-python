# Dmp
(*dmp*)

## Overview

### Available Operations

* [get_first_party_data_job](#get_first_party_data_job) - Submit a job for first-party data retrieval for an advertiser
* [get_third_party_data_job](#get_third_party_data_job) - Submit a job for third-party data retrieval for a partner

## get_first_party_data_job

When a first-party data query is submitted, a job ID is returned.
This job ID can be used to poll for the job's status using the associated operation under "Job Status".

### Example Usage

```python
import os
from ttd_workflows import Workflows


with Workflows(
    ttd_auth=os.getenv("WORKFLOWS_TTD_AUTH", ""),
) as workflows:

    res = workflows.dmp.get_first_party_data_job(request={
        "advertiser_id": "<id>",
        "name_filter": "<value>",
        "query_shape": "<value>",
        "callback_input": {
            "callback_url": "https://difficult-pocket-watch.com",
            "callback_headers": {
                "key": "<value>",
                "key1": "<value>",
                "key2": "<value>",
            },
        },
    })

    assert res.standard_job_submit_response is not None

    # Handle response
    print(res.standard_job_submit_response)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [models.FirstPartyDataInput](../../models/firstpartydatainput.md)   | :heavy_check_mark:                                                  | The request object to use for the request.                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GetFirstPartyDataJobResponse](../../models/getfirstpartydatajobresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.ProblemDetailsError | 400, 401, 403, 404         | application/json           |
| models.APIError            | 4XX, 5XX                   | \*/\*                      |

## get_third_party_data_job

When a third-party data query is submitted, a job ID is returned.
This job ID can be used to poll for the job's status, and when complete, the results download link,
using the associated operation under "Job Status".

### Example Usage

```python
import os
from ttd_workflows import Workflows


with Workflows(
    ttd_auth=os.getenv("WORKFLOWS_TTD_AUTH", ""),
) as workflows:

    res = workflows.dmp.get_third_party_data_job(request={
        "partner_id": "<id>",
        "query_shape": "<value>",
        "callback_input": {
            "callback_url": "https://extroverted-intent.net",
            "callback_headers": {
                "key": "<value>",
                "key1": "<value>",
            },
        },
    })

    assert res.standard_job_submit_response is not None

    # Handle response
    print(res.standard_job_submit_response)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [models.ThirdPartyDataInput](../../models/thirdpartydatainput.md)   | :heavy_check_mark:                                                  | The request object to use for the request.                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GetThirdPartyDataJobResponse](../../models/getthirdpartydatajobresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.ProblemDetailsError | 400, 401, 403, 404         | application/json           |
| models.APIError            | 4XX, 5XX                   | \*/\*                      |