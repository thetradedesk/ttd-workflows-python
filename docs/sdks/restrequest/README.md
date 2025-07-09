# RESTRequest
(*rest_request*)

## Overview

### Available Operations

* [submit_rest_request](#submit_rest_request) - Submit a valid REST request

## submit_rest_request

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

    res = workflows.rest_request.submit_rest_request(request={
        "method_type": ttd_workflows.RestAPIMethodType.GET,
        "endpoint": "<value>",
        "data_body": "<value>",
    })

    assert res.object is not None

    # Handle response
    print(res.object)

```

### Parameters

| Parameter                                                                   | Type                                                                        | Required                                                                    | Description                                                                 |
| --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- |
| `request`                                                                   | [models.CallRestAPIWorkflowInput](../../models/callrestapiworkflowinput.md) | :heavy_check_mark:                                                          | The request object to use for the request.                                  |
| `retries`                                                                   | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)            | :heavy_minus_sign:                                                          | Configuration to override the default retry behavior of the client.         |

### Response

**[models.SubmitRestRequestResponse](../../models/submitrestrequestresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.ProblemDetailsError | 400, 401, 403, 404         | application/json           |
| models.APIError            | 4XX, 5XX                   | \*/\*                      |