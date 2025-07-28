# JobStatus
(*job_status*)

## Overview

### Available Operations

* [get_graph_ql_query_job_status](#get_graph_ql_query_job_status) - Get the status of a previously submitted GraphQL query job.
* [get_job_status](#get_job_status) - Get the status of a previously submitted job

## get_graph_ql_query_job_status

Use this operation to get a previously submitted GraphQL query job's status and completion percentage.
Once a job is complete, this operation will return the URL from which to download the job results.

### Example Usage

<!-- UsageSnippet language="python" operationID="getGraphQlQueryJobStatus" method="get" path="/graphqlqueryjob/{id}" -->
```python
import os
from ttd_workflows import Workflows


with Workflows(
    ttd_auth=os.getenv("WORKFLOWS_TTD_AUTH", ""),
) as workflows:

    res = workflows.job_status.get_graph_ql_query_job_status(id="<id>")

    assert res.graph_ql_query_job_retrieval_response is not None

    # Handle response
    print(res.graph_ql_query_job_retrieval_response)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GetGraphQlQueryJobStatusResponse](../../models/getgraphqlqueryjobstatusresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.ProblemDetailsError | 400, 401, 403, 404         | application/json           |
| models.APIError            | 4XX, 5XX                   | \*/\*                      |

## get_job_status

Use this operation to get a previously submitted job's status and completion percentage.
Once a job is complete, this operation will return the URL from which to download the job results.
            
Job results expire after 24 hours, at which point you will need to submit a new job.

### Example Usage

<!-- UsageSnippet language="python" operationID="getJobStatus" method="get" path="/standardjob/{id}/status" -->
```python
import os
from ttd_workflows import Workflows


with Workflows(
    ttd_auth=os.getenv("WORKFLOWS_TTD_AUTH", ""),
) as workflows:

    res = workflows.job_status.get_job_status(id=412651)

    assert res.standard_job_status_response is not None

    # Handle response
    print(res.standard_job_status_response)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *int*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GetJobStatusResponse](../../models/getjobstatusresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.ProblemDetailsError | 400, 401, 403, 404         | application/json           |
| models.APIError            | 4XX, 5XX                   | \*/\*                      |