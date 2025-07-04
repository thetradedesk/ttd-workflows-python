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
from ttd_workflows import TtdWorkflows
from ttd_workflows.models import components


with TtdWorkflows(
    ttd_auth=os.getenv("WORKFLOWS_TTD_AUTH", ""),
) as tw_client:

    res = tw_client.rest_request.submit_rest_request(request={
        "method_type": components.RestAPIMethodType.GET,
        "endpoint": "<value>",
        "data_body": "<value>",
    })

    assert res.object is not None

    # Handle response
    print(res.object)

```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [components.CallRestAPIWorkflowInput](../../models/components/callrestapiworkflowinput.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |
| `retries`                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                           | :heavy_minus_sign:                                                                         | Configuration to override the default retry behavior of the client.                        |

### Response

**[operations.SubmitRestRequestResponse](../../models/operations/submitrestrequestresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.ProblemDetailsError | 400, 401, 403, 404         | application/json           |
| errors.APIError            | 4XX, 5XX                   | \*/\*                      |