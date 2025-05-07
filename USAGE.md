<!-- Start SDK Example Usage [usage] -->
```python
# Synchronous Example
import os
from ttd_workflows import Workflows


with Workflows(
    ttd_auth=os.getenv("WORKFLOWS_TTD_AUTH", ""),
) as workflows:

    res = workflows.demo.get_demo()

    # Handle response
    print(res)
```

</br>

The same SDK client can also be used to make asychronous requests by importing asyncio.
```python
# Asynchronous Example
import asyncio
import os
from ttd_workflows import Workflows

async def main():

    async with Workflows(
        ttd_auth=os.getenv("WORKFLOWS_TTD_AUTH", ""),
    ) as workflows:

        res = await workflows.demo.get_demo_async()

        # Handle response
        print(res)

asyncio.run(main())
```
<!-- End SDK Example Usage [usage] -->