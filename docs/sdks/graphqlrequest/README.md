# GraphQLRequest
(*graph_ql_request*)

## Overview

### Available Operations

* [submit_graph_ql_request](#submit_graph_ql_request) - Submit a valid GraphQL query or mutation
* [submit_graph_ql_query_job](#submit_graph_ql_query_job) - Submit a valid bulk GraphQL query

## submit_graph_ql_request

This generic operation can be used to execute any valid GraphQL request.
To explore the available GraphQL operations, see the [GraphQL Schema Explorer](https://partner.thetradedesk.com/v3/portal/api/graphql-schema).

### Example Usage

```python
import os
from ttd_workflows import Workflows


with Workflows(
    ttd_auth=os.getenv("WORKFLOWS_TTD_AUTH", ""),
) as workflows:

    res = workflows.graph_ql_request.submit_graph_ql_request(request={
        "request": "<value>",
        "variables": {},
    })

    assert res.object is not None

    # Handle response
    print(res.object)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [models.GraphQLRequestInput](../../models/graphqlrequestinput.md)   | :heavy_check_mark:                                                  | The request object to use for the request.                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.SubmitGraphQlRequestResponse](../../models/submitgraphqlrequestresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.ProblemDetailsError | 400, 401, 403, 404         | application/json           |
| models.APIError            | 4XX, 5XX                   | \*/\*                      |

## submit_graph_ql_query_job

This generic operation can be used to execute any valid bulk GraphQL query.
For information on bulk GraphQL query syntax, see [GraphQL API Bulk Operations](https://partner.thetradedesk.com/v3/portal/api/doc/GqlBulkOperations).

### Example Usage

```python
import os
from ttd_workflows import Workflows


with Workflows(
    ttd_auth=os.getenv("WORKFLOWS_TTD_AUTH", ""),
) as workflows:

    res = workflows.graph_ql_request.submit_graph_ql_query_job(request={
        "query": "<value>",
        "callback_input": {
            "callback_url": "https://wilted-cork.net/",
            "callback_headers": [
                {
                    "key": "<key>",
                    "value": "<value>",
                },
            ],
        },
    })

    assert res.graph_ql_query_job_response is not None

    # Handle response
    print(res.graph_ql_query_job_response)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [models.GraphQlQueryJobInput](../../models/graphqlqueryjobinput.md) | :heavy_check_mark:                                                  | The request object to use for the request.                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.SubmitGraphQlQueryJobResponse](../../models/submitgraphqlqueryjobresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.ProblemDetailsError | 400, 401, 403, 404         | application/json           |
| models.APIError            | 4XX, 5XX                   | \*/\*                      |