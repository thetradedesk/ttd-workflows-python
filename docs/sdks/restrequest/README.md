# RESTRequest
(*rest_request*)

## Overview

### Available Operations

* [post_restrequest](#post_restrequest) - Submit a valid REST request

## post_restrequest

This generic operation can be used to execute any valid REST request.
To explore the available REST operations, see the [REST API Reference](https://partner.thetradedesk.com/v3/portal/api/doc/ApiReferencePlatform).

### Example Usage

```python
import os
import ttd_workflows
from ttd_workflows import Workflows


with Workflows(
    ttd_auth=os.getenv("WORKFLOWS_TTD_AUTH", ""),
) as workflows:

    res = workflows.rest_request.post_restrequest(request={
        "method_type": ttd_workflows.PubAPIMethodType.POST,
        "endpoint": "<value>",
        "data_body": "<value>",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                 | Type                                                                      | Required                                                                  | Description                                                               |
| ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| `request`                                                                 | [models.CallPubAPIWorkflowInput](../../models/callpubapiworkflowinput.md) | :heavy_check_mark:                                                        | The request object to use for the request.                                |
| `retries`                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)          | :heavy_minus_sign:                                                        | Configuration to override the default retry behavior of the client.       |

### Response

**[models.PostRestrequestResponse](../../models/postrestrequestresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.ProblemDetailsError | 400, 401, 403, 404         | application/json           |
| models.APIError            | 4XX, 5XX                   | \*/\*                      |