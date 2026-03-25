# BulkJobStatus

## Example Usage

```python
from ttd_workflows.models import BulkJobStatus

value = BulkJobStatus.QUEUED
```


## Values

| Name              | Value             |
| ----------------- | ----------------- |
| `QUEUED`          | Queued            |
| `IN_PROGRESS`     | InProgress        |
| `PARTIAL_SUCCESS` | PartialSuccess    |
| `FAILURE`         | Failure           |
| `SUCCESS`         | Success           |
| `CANCELLED`       | Cancelled         |